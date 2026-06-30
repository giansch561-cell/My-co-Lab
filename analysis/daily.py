from pathlib import Path
from datetime import datetime

import pandas as pd

DATA_DIR = Path.home() / "My-co-Lab" / "data" / "environment"
REPORT_DIR = Path.home() / "My-co-Lab" / "analysis" / "reports"


def main():
    today = datetime.now().strftime("%Y-%m-%d")
    csv_file = DATA_DIR / f"{today}_environment.csv"

    if not csv_file.exists():
        print(f"ERROR: CSV file not found: {csv_file}")
        return

    REPORT_DIR.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(csv_file)

    if df.empty:
        print("ERROR: CSV file is empty")
        return

    report_file = REPORT_DIR / f"{today}_daily_report.txt"

    temperature = df["temperature_c"]
    humidity = df["humidity_percent"]

    with open(report_file, "w") as report:
        report.write(f"My-co-Lab Daily Report\n")
        report.write(f"Date: {today}\n")
        report.write("=" * 40 + "\n\n")

        report.write(f"Records: {len(df)}\n\n")

        report.write("Temperature\n")
        report.write(f"  Min : {temperature.min()} °C\n")
        report.write(f"  Max : {temperature.max()} °C\n")
        report.write(f"  Avg : {temperature.mean():.2f} °C\n\n")

        report.write("Humidity\n")
        report.write(f"  Min : {humidity.min()} %\n")
        report.write(f"  Max : {humidity.max()} %\n")
        report.write(f"  Avg : {humidity.mean():.2f} %\n")

    print(f"Report created: {report_file}")


if __name__ == "__main__":
    main()
