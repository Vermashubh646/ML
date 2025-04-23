import subprocess
import os

def check_spotdl_installed():
    try:
        subprocess.run(["spotdl", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except FileNotFoundError:
        return False

def download_spotify_audio(spotify_url, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created folder: {output_dir}")
    
    command = [
        "spotdl",
        spotify_url,
        "--output", os.path.join(output_dir, "{title} - {artist}")
    ]

    print("\nDownloading in highest quality (usually 320kbps MP3)...")
    subprocess.run(command)

if __name__ == '__main__':
    print("🎧 Spotify High-Quality Audio Downloader\n")

    if not check_spotdl_installed():
        print("❌ spotdl is not installed. Run 'pip install spotdl' and try again.")
        exit(1)

    spotify_url = input("🔗 Enter Spotify Track / Album / Playlist URL: ").strip()
    output_dir = input("📁 Enter output folder path: ").strip()

    download_spotify_audio(spotify_url, output_dir)
    print("\n✅ Download complete!")
