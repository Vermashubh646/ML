import os
import yt_dlp

def list_formats(video_url):
    ydl_opts = {
        'listformats': True
    }
    print("\nFetching available formats...\n")
    with yt_dlp.YoutubeDL({}) as ydl:
        info = ydl.extract_info(video_url, download=False)
        formats = info.get('formats', [])
        format_list = []
        for idx, f in enumerate(formats):
            # Only show formats with resolution or audio quality
            if f.get('vcodec') != 'none' or f.get('acodec') != 'none':
                format_list.append(f['format_id'])
                fmt_str = f"{len(format_list)}. Format ID: {f['format_id']} | Ext: {f['ext']} | "
                if f.get('resolution'):
                    fmt_str += f"Video: {f['resolution']}"
                elif f.get('abr'):
                    fmt_str += f"Audio: {f['abr']}kbps"
                fmt_str += f" | Note: {f.get('format_note', '')}"
                print(fmt_str)
    return format_list


def download_media(url, download_dir, is_playlist, is_audio, format_id):
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
        print(f"Created folder: {download_dir}")

    # Base options
    ydl_opts = {
        'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'),
        'ignoreerrors': True,
        'noplaylist': not is_playlist,
        'format': format_id
    }

    # If only audio is requested
    if is_audio:
        ydl_opts.update({
            'format': 'bestaudio',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        })
    else:
        # ✅ Combine selected video format with best available audio automatically
        ydl_opts['format'] = f"{format_id}+bestaudio/best"
        ydl_opts['postprocessors'] = [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',  # final output format
        }]

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


if __name__ == '__main__':
    url = input("Enter the YouTube video or playlist URL: ").strip()
    download_dir = input("Enter the folder path to save downloads: ").strip()

    is_playlist_input = input("Download as playlist? (y/n): ").strip().lower()
    is_playlist = is_playlist_input == 'y'

    is_audio_input = input("Download audio only? (y/n): ").strip().lower()
    is_audio = is_audio_input == 'y'

    format_id = None
    if not is_audio:
        available_formats = list_formats(url)
        print("\nSelect a format number from the list above:")
        try:
            choice = int(input("Enter the number corresponding to your desired quality: ").strip())
            format_id = available_formats[choice - 1]
        except (IndexError, ValueError):
            print("Invalid selection, using default best format...")
            format_id = 'bestvideo+bestaudio/best'

    download_media(url, download_dir, is_playlist, is_audio, format_id)
