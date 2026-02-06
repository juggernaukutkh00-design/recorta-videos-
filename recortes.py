import subprocess
from pathlib import Path
from tqdm import tqdm
import os

VIDEO_EXT = {".mp4", ".mkv", ".avi", ".mov", ".webm", ".flv"}


def get_duration(file_path: Path) -> float:
    cmd = [
        "ffprobe",
        "-v", "error",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        str(file_path)
    ]
    return float(subprocess.check_output(cmd).decode().strip())


def trim_to_folder(input_file: Path, out_dir: Path, seconds: float):
    duration = get_duration(input_file)
    new_duration = max(duration - seconds, 0)

    # precisión decimal
    t = f"{new_duration:.3f}"

    temp_out = out_dir / (input_file.stem + ".tmp" + input_file.suffix)
    final_out = out_dir / input_file.name

    cmd = [
        "ffmpeg",
        "-y",
        "-i", str(input_file),
        "-t", t,
        "-c", "copy",
        str(temp_out)
    ]

    subprocess.run(cmd, check=True)
    os.replace(temp_out, final_out)


def main():
    src = Path("videoscompletos")
    dst = Path("videosincompletos")
    dst.mkdir(exist_ok=True)

    s = input("Segundos a recortar (ej 2.35): ").strip().replace(",", ".")
    seconds = float(s)

    videos = [f for f in src.iterdir()
              if f.is_file() and f.suffix.lower() in VIDEO_EXT]

    errores = []

    for video in tqdm(videos, desc="Recortando", unit="video"):
        try:
            trim_to_folder(video, dst, seconds)
        except Exception as e:
            errores.append((video.name, str(e)))

    print("\nTerminado")
    print("Procesados:", len(videos))
    print("Errores:", len(errores))

    for n, e in errores:
        print(" -", n, "→", e)


if __name__ == "__main__":
    main()
