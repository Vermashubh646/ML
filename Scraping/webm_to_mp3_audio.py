import subprocess
import os
import sys

def webm_to_high_quality_mp3(input_file):
    if not os.path.exists(input_file):
        print(f"❌ File not found: {input_file}")
        return

    base, _ = os.path.splitext(input_file)
    output_file = base + ".mp3"

    command = [
        "ffmpeg",
        "-i", input_file,
        "-vn",
        "-codec:a", "libmp3lame",
        "-q:a", "0",
        "-y",
        output_file
    ]

    subprocess.run(command, check=True)
    print(f"✅ Saved as: {output_file}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <file.webm>")
    else:
        webm_to_high_quality_mp3(sys.argv[1])