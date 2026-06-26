from pathlib import Path
import pandas as pd

DATA_DIR = Path.home() / "My-co-Lab" / "data" / "environment"

files = sorted(DATA_DIR.glob("*_environment.csv"))

if not files:
    print("Nenhum ficheiro encontrado.")
    exit()

# Ler todos os CSV
df = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)

# Converter datas
df["datetime"] = pd.to_datetime(
    df["datetime"],
    format="%Y-%m-%d %H:%M:%S"
)

# Selecionar últimas 24 horas
last24 = df[df["datetime"] >= df["datetime"].max() - pd.Timedelta(hours=24)]

print("=" * 50)
print("MY-CO-LAB ENVIRONMENT REPORT")
print("=" * 50)

print(f"\nPeríodo analisado:")
print(f"{last24['datetime'].min()}  ->  {last24['datetime'].max()}")

print(f"\nNúmero de medições: {len(last24)}")

print("\nTemperatura")
print(f" Média : {last24['temperature_c'].mean():.1f} °C")
print(f" Mínima: {last24['temperature_c'].min()} °C")
print(f" Máxima: {last24['temperature_c'].max()} °C")

print("\nHumidade")
print(f" Média : {last24['humidity_percent'].mean():.1f} %")
print(f" Mínima: {last24['humidity_percent'].min()} %")
print(f" Máxima: {last24['humidity_percent'].max()} %")

print("\nConclusão:")

temp_var = last24["temperature_c"].max() - last24["temperature_c"].min()
hum_var = last24["humidity_percent"].max() - last24["humidity_percent"].min()

print(f" Variação temperatura: {temp_var:.1f} °C")
print(f" Variação humidade: {hum_var:.1f} %")

print("\n" + "=" * 50)