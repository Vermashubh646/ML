import os
import yt_dlp

def download_playlist(playlist_url, download_dir):
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
        print(f"Created folder: {download_dir}")

    ydl_opts = {
        'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'),
        'ignoreerrors': True,
        'noplaylist': False,
        'format': 'bestvideo[height=1080]+bestaudio/best[height=1080]',
        'merge_output_format': 'mp4',  # Ensure output is in mp4
        # 'ffmpeg_location': 'C:/path/to/ffmpeg/bin'  # Optional
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([playlist_url])
    except KeyboardInterrupt:
        print("\nDownload interrupted by user.")

if __name__ == '__main__':
    playlist_url = input("Enter the YouTube playlist URL: ").strip()
    download_dir = input("Enter the folder path where you want to save the playlist: ").strip()
    download_playlist(playlist_url, download_dir)
