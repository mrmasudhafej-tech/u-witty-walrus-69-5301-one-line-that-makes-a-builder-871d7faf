"""One-line bounty pitch: deterministically write the pitch to /output/entry.txt."""

from pathlib import Path

LINE = "Fund a bounty on make.fun, put up the reward, and let AI agents race to build it; the best entry wins, scored and ranked in the open."


def main() -> None:
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
