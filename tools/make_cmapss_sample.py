from pathlib import Path
import pandas as pd

RAW_TRAIN = Path("data/raw/cmapss/FD001/train_FD001.txt")
OUT_SAMPLE = Path("sample-data/cmapss_fd001_train_sample.csv")

COLS = (
    ["unit", "cycle", "setting1", "setting2", "setting3"]
    + [f"s{i}" for i in range(1, 22)]
)

def main(n_rows: int = 200, random_state: int = 42) -> None:
    if not RAW_TRAIN.exists():
        raise FileNotFoundError(f"Missing raw file: {RAW_TRAIN}")

    df = pd.read_csv(RAW_TRAIN, sep=r"\s+", header=None)
    df.columns = COLS

    sample = df.sample(n=min(n_rows, len(df)), random_state=random_state)

    OUT_SAMPLE.parent.mkdir(parents=True, exist_ok=True)
    sample.to_csv(OUT_SAMPLE, index=False)
    print(f"Saved: {OUT_SAMPLE} | rows={len(sample)}")

if __name__ == "__main__":
    main()