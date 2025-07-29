from pathlib import Path
import shutil


def copyFileMultipleTimes(filePath: str, count: int, startIndex: int = 1) -> int:
    src = Path(filePath).expanduser().resolve()
    if not src.is_file():
        raise FileNotFoundError(f"원본 파일을 찾을 수 없습니다: {src}")

    if count <= 0:
        raise ValueError("count 값은 1 이상이어야 합니다.")

    folder = src.parent
    ext = src.suffix.lower()
    copied = 0

    for num in range(startIndex, startIndex + count):
        dst = folder / f"{num}{ext}"
        if dst.exists():
            raise FileExistsError(f"이미 존재하는 파일입니다: {dst}")
        shutil.copy2(src, dst)
        copied += 1

    return copied

copyFileMultipleTimes(r"D:\Machine Learning\mnist_invert\NaN\0.png", 7000)
