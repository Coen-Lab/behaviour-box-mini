from pathlib import Path
import subprocess


def count_frames(video_path):
    command = [
        "ffprobe",
        "-v", "error",
        "-count_frames",
        "-select_streams", "v:0",
        "-show_entries", "stream=nb_read_frames",
        "-of", "default=nokey=1:noprint_wrappers=1",
        str(video_path),
    ]

    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
        check=True,
    )

    return int(result.stdout.strip())


def convert_to_h264(input_path, output_path, crf=18):
    input_path = Path(input_path)
    output_path = Path(output_path)

    input_frames = count_frames(input_path)

    command = [
        "ffmpeg",
        "-hide_banner",
        "-n",
        "-i", str(input_path),
        "-map", "0:v:0",
        "-c:v", "libx264",
        "-preset", "medium",
        "-crf", str(crf),
        "-pix_fmt", "yuv420p",
        "-fps_mode", "passthrough",
        "-movflags", "+faststart",
        str(output_path),
    ]

    subprocess.run(command, check=True)

    output_frames = count_frames(output_path)

    if input_frames != output_frames:
        raise RuntimeError(
            f"Frame mismatch: input={input_frames}, "
            f"output={output_frames}"
        )

    print(f"Conversion complete: {output_path}")
    print(f"Frame count: {output_frames}")


def main():
    input_video = Path(
        r"C:\Users\Jenkin\OneDrive - University College London\Desktop\work\sub-M01231\ses-06_date-2026-07-17T14-23-44\VideoData_Camera.avi"
    )

    output_video = Path(
        r"C:\Users\Jenkin\OneDrive - University College London\Desktop\work\sub-M01231\ses-06_date-2026-07-17T14-23-44\VideoData_Camera_h264.mp4"
    )

    convert_to_h264(
        input_path=input_video,
        output_path=output_video,
        crf=18,
    )


if __name__ == "__main__":
    main()