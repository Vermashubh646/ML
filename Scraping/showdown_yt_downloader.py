import subprocess
import json
import sys
import os

def run_yt_dlp_info(url):
    print("📥 Fetching format info...")

    result = subprocess.run(
        ['yt-dlp', '-j', url],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    if result.returncode != 0 or not result.stdout.strip():
        print("❌ Failed to fetch video info.")
        print("🧠 STDERR from yt-dlp:")
        print(result.stderr)
        sys.exit(1)

    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError:
        print("❌ Output was not valid JSON. Here’s what we got:")
        print(result.stdout[:300])
        sys.exit(1)

def get_best_audio(formats):
    audio_formats = [f for f in formats if f.get('acodec') != 'none' and f.get('vcodec') == 'none']
    audio_formats = sorted(audio_formats, key=lambda f: f.get('abr') or 0, reverse=True)
    return audio_formats[0] if audio_formats else None

def get_best_video(formats):
    video_formats = [f for f in formats if f.get('vcodec') != 'none' and f.get('acodec') == 'none']
    video_formats = sorted(video_formats, key=lambda f: (
        f.get('height', 0),
        f.get('fps', 0),
        f.get('tbr') or f.get('vbr') or 0
    ), reverse=True)
    return video_formats[0] if video_formats else None

def list_video_formats(formats):
    video_formats = [f for f in formats if f.get('vcodec') != 'none' and f.get('acodec') == 'none']
    for f in video_formats:
        print(f"ID: {f['format_id']} | Res: {f.get('resolution')} | FPS: {f.get('fps')} | TBR: {f.get('tbr')} | Ext: {f['ext']}")

def download_combined(video_id, audio_id, url, output='output.mp4'):
    subprocess.run([
        'yt-dlp',
        '-f', f"{video_id}+{audio_id}",
        url,
        '-o', output
    ])

def download_audio(audio_id, url, output='audio_only.m4a'):
    subprocess.run([
        'yt-dlp',
        '-f', audio_id,
        url,
        '-o', output
    ])

def main():
    url = input("🎯 Enter YouTube URL: ")
    mode = input("🔧 Mode (auto/audio/manual): ").strip().lower()
    output_dir = input("📂 Enter output directory (leave blank for current folder): ").strip()

    if not output_dir:
        output_dir = '.'

    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, '%(title)s.%(ext)s')

    print("📥 Fetching format info...")
    info = run_yt_dlp_info(url)
    formats = info['formats']

    best_audio = get_best_audio(formats)
    best_video = get_best_video(formats)

    if mode == 'auto':
        print(f"🎧 Best audio: {best_audio['format_id']} - {best_audio.get('abr')}kbps ({best_audio['ext']})")
        print(f"📹 Best video: {best_video['format_id']} - {best_video.get('resolution')} ({best_video['ext']})")
        download_combined(best_video['format_id'], best_audio['format_id'], url, output=output_path)

    elif mode == 'audio':
        print(f"🎧 Best audio-only: {best_audio['format_id']} - {best_audio.get('abr')}kbps ({best_audio['ext']})")
        download_audio(best_audio['format_id'], url, output=output_path)

    elif mode == 'manual':
        print("🎞️ Available video-only formats:")
        list_video_formats(formats)
        chosen_vid = input("✍️ Enter the format ID of your chosen video: ").strip()
        print(f"🔗 Merging video ({chosen_vid}) with best audio ({best_audio['format_id']})...")
        download_combined(chosen_vid, best_audio['format_id'], url, output=output_path)

    else:
        print("❌ Invalid mode. Please choose: auto, audio, or manual.")

if __name__ == '__main__':
    main()
