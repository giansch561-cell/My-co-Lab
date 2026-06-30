from pathlib import Path
import sys
import pandas as pd

DATA_DIR = Path.home() / "My-co-Lab" / "data" / "environment"

if len(sys.argv) < 2:
    print("Uso: python3 analysis/compare.py YYYY-MM-DD YYYY-MM-DD ...")
    exit(1)

rows = []

for day in sys.argv[1:]:
    file_path = DATA_DIR / f"{day}_environment.csv"

    if not file_path.exists():
        print(f"Aviso: ficheiro não encontrado: {file_path}")
        continue

    df = pd.read_csv(file_path)

    rows.append({
        "day": day,
        "measurements": len(df),
        "temp_mean": df["temperature_c"].mean(),
        "temp_min": df["temperature_c"].min(),
        "temp_max": df["temperature_c"].max(),
        "hum_mean": df["humidity_percent"].mean(),
        "hum_min": df["humidity_percent"].min(),
        "hum_max": df["humidity_percent"].max(),
        "temp_var": df["temperature_c"].max() - df["temperature_c"].min(),
        "hum_var": df["humidity_percent"].max() - df["humidity_percent"].min(),
    })

if not rows:
    print("Nenhum dado válido encontrado.")
    exit(1)

result = pd.DataFrame(rows)

print("=" * 100)
print("MY-CO-LAB EXPERIMENT COMPARISON")
print("=" * 100)

print(
    result.to_string(
        index=False,
        formatters={
            "temp_mean": "{:.1f}".format,
            "hum_mean": "{:.1f}".format,
            "temp_var": "{:.1f}".format,
            "hum_var": "{:.1f}".format,
        }
    )
)

print("=" * 100)
