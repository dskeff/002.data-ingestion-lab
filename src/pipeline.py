import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

def run_pipeline():
    print("Iniciando pipeline...")

    input_path = BASE_DIR / "data/raw/transactions.csv"
    output_path = BASE_DIR / "data/processed/transactions_partitioned"

    df = pd.read_csv(input_path)

    df['data'] = pd.to_datetime(df['data'])
    df['ano'] = df['data'].dt.year
    df['mes'] = df['data'].dt.month

    df.to_parquet(
        output_path,
        partition_cols=['ano','mes'],
        index=False
    )

    print("Pipeline concluído com sucesso!")

if __name__ == "__main__":
    run_pipeline()