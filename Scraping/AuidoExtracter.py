import os
import subprocess

def extract_audio():
    print("🎵 Extract Audio from Video using FFmpeg")

    video_path = input("Enter the full path to the video file: ").strip()

    if not os.path.isfile(video_path):
        print("❌ The specified video file does not exist.")
        return

    print("\nChoose output audio format:")
    print("1. MP3")
    print("2. WAV")
    print("3. AAC")
    print("4. OGG")
    format_choice = input("Enter your choice (1-4): ").strip()

    format_map = {
        '1': 'mp3',
        '2': 'wav',
        '3': 'aac',
        '4': 'ogg'
    }

    audio_format = format_map.get(format_choice)
    if not audio_format:
        print("❌ Invalid choice.")
        return

    # Create output directory if not exists
    output_dir = r"D:\extractedAudio"
    os.makedirs(output_dir, exist_ok=True)

    # Generate default output filename based on input video
    base_name = os.path.splitext(os.path.basename(video_path))[0]
    output_filename = f"{base_name}_audio.{audio_format}"
    output_path = os.path.join(output_dir, output_filename)

    try:
        command = [
            'ffmpeg',
            '-i', video_path,
            '-vn',                # No video
            '-ab', '192k',        # Audio bitrate
            '-ar', '44100',       # Audio sample rate
            '-y',                 # Overwrite without asking
            output_path
        ]
        subprocess.run(command, check=True)
        print(f"\n✅ Audio extracted successfully: {output_path}")
    except subprocess.CalledProcessError:
        print("❌ Something went wrong during audio extraction.")

if __name__ == '__main__':
    extract_audio()
