from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


# ==========================================
# Configuração
# ==========================================

DATA_DIR = Path.home() / "My-co-Lab" / "data" / "environment"
REPORT_DIR = Path.home() / "My-co-Lab" / "analysis" / "reports"

REPORT_DIR.mkdir(parents=True, exist_ok=True)


# ==========================================
# Ler todos os ficheiros CSV
# ==========================================

files = sorted(DATA_DIR.glob("*_environment.csv"))

if not files:
    print("Nenhum ficheiro encontrado.")
    exit()

df = pd.concat(
    [pd.read_csv(file) for file in files],
    ignore_index=True
)

# Converter datas
df["datetime"] = pd.to_datetime(
    df["datetime"],
    format="%Y-%m-%d %H:%M:%S"
)

# ==========================================
# Últimas 24 horas
# ==========================================

last24 = df[
    df["datetime"] >=
    df["datetime"].max() - pd.Timedelta(hours=24)
]

# ==========================================
# Estatísticas
# ==========================================

print("=" * 60)
print("MY-CO-LAB ENVIRONMENT REPORT")
print("=" * 60)

print()
print("Período analisado")
print(last24["datetime"].min())
print("até")
print(last24["datetime"].max())

print()

print(f"Número de medições : {len(last24)}")

print()

print("TEMPERATURA")
print(f"Média   : {last24['temperature_c'].mean():.1f} °C")
print(f"Mínima  : {last24['temperature_c'].min()} °C")
print(f"Máxima  : {last24['temperature_c'].max()} °C")

print()

print("HUMIDADE")
print(f"Média   : {last24['humidity_percent'].mean():.1f} %")
print(f"Mínima  : {last24['humidity_percent'].min()} %")
print(f"Máxima  : {last24['humidity_percent'].max()} %")

print()

temp_var = (
    last24["temperature_c"].max()
    - last24["temperature_c"].min()
)

hum_var = (
    last24["humidity_percent"].max()
    - last24["humidity_percent"].min()
)

print("VARIAÇÃO")

print(f"Temperatura : {temp_var:.1f} °C")
print(f"Humidade    : {hum_var:.1f} %")

print()

print("=" * 60)

# ==========================================
# Gráfico
# ==========================================

plt.figure(figsize=(14,6))

plt.plot(
    last24["datetime"],
    last24["temperature_c"],
    linewidth=2,
    label="Temperatura (°C)"
)

plt.plot(
    last24["datetime"],
    last24["humidity_percent"],
    linewidth=2,
    label="Humidade (%)"
)

plt.title("My-co-Lab - Últimas 24 Horas")

plt.xlabel("Hora")

plt.ylabel("Valor")

plt.grid(True)

plt.legend()

plt.tight_layout()

plt.savefig(
    REPORT_DIR / "last24h.png",
    dpi=200
)

plt.show()

print()
print("Gráfico guardado em:")
print(REPORT_DIR / "last24h.png")