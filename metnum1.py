import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from decimal import Decimal, ROUND_HALF_UP
# 1. DEFINISI FUNGSI
def f(x):
    return np.exp(x) - 5 * x**2

a = 0.0
b = 1.0
epsilon = 0.00001

data = []
# 2. FUNGSI PEMBULATAN
def format_6(nilai):
    return str(
        Decimal(str(nilai)).quantize(
            Decimal("0.000001"),
            rounding=ROUND_HALF_UP
        )
    )
# 3. PROSES BISECTION r = 0 SAMPAI 16
for r in range(17):

    c = (a + b) / 2

    fa = f(a)
    fc = f(c)
    fb = f(b)

    lebar_lama = abs(b - a)

    if fa * fc < 0:
        selang_baru = "[a, c]"
        a_baru = a
        b_baru = c

    elif fc * fb < 0:
        selang_baru = "[c, b]"
        a_baru = c
        b_baru = b

    else:
        selang_baru = "Akar ditemukan"
        a_baru = c
        b_baru = c

    lebar_baru = abs(b_baru - a_baru)

    data.append({
        "r": r,
        "a": a,
        "c": c,
        "b": b,
        "f(a)": fa,
        "f(c)": fc,
        "f(b)": fb,
        "Selang baru": selang_baru,
        "Lebarnya": lebar_baru
    })

    a = a_baru
    b = b_baru
# 4. MENAMPILKAN TABEL ITERASI
df = pd.DataFrame(data)

kolom_angka = [
    "a", "c", "b",
    "f(a)", "f(c)", "f(b)",
    "Lebarnya"
]

print("\nTABEL ITERASI METODE BISECTION")
print("=" * 125)

formatters = {
    kolom: format_6
    for kolom in kolom_angka
}

print(
    df.to_string(
        index=False,
        formatters=formatters
    )
)
# 5. HASIL AKHIR
akar = (a + b) / 2

print("\nHASIL AKHIR")
print("=" * 40)
print(f"Akar hampiran : {akar:.8f}")
print(f"Nilai f(x)    : {f(akar):.8f}")
print(f"Toleransi     : {epsilon}")
print(f"Jumlah baris  : {len(df)}")
print("Iterasi       : r = 0 sampai r = 16")
# 6. GRAFIK FUNGSI
x = np.linspace(0, 1, 1000)
y = f(x)

plt.figure(figsize=(12, 7))

plt.plot(
    x, y,
    linewidth=2,
    label=r"$f(x)=e^x-5x^2$"
)

plt.axhline(
    y=0,
    color="black",
    linewidth=1
)

plt.axvline(
    x=akar,
    linestyle="--",
    linewidth=1.5,
    label=f"Akar hampiran = {akar:.6f}"
)

plt.scatter(
    [akar],
    [f(akar)],
    color="red",
    s=70,
    zorder=5,
    label=f"({akar:.6f}, {f(akar):.6f})"
)

plt.scatter(
    df["c"],
    df["f(c)"],
    color="orange",
    s=25,
    label="Titik tengah iterasi",
    zorder=4
)

plt.title("Grafik Metode Bisection")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.xlim(0, 1)
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()
# 7. GRAFIK PENYUSUTAN INTERVAL
plt.figure(figsize=(10, 5))

plt.plot(
    df["r"],
    df["Lebarnya"],
    marker="o",
    linewidth=2,
    label="Lebar interval baru"
)

plt.axhline(
    epsilon,
    color="red",
    linestyle="--",
    label=f"Toleransi = {epsilon}"
)

plt.yscale("log")
plt.title("Penyusutan Lebar Interval")
plt.xlabel("Iterasi (r)")
plt.ylabel("Lebar interval")
plt.xticks(range(17))
plt.grid(True, which="both", alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()
# 8. TABEL VISUAL
fig, ax = plt.subplots(figsize=(16, 8))
ax.axis("off")

tabel_data = df.copy()

for kolom in kolom_angka:
    tabel_data[kolom] = tabel_data[kolom].map(format_6)

tabel_visual = ax.table(
    cellText=tabel_data.values,
    colLabels=tabel_data.columns,
    cellLoc="center",
    loc="center"
)

tabel_visual.auto_set_font_size(False)
tabel_visual.set_fontsize(8)
tabel_visual.scale(1, 1.5)

plt.title(
    "Tabel Lengkap Iterasi Bisection (r = 0 sampai 16)",
    pad=20
)

plt.tight_layout()
plt.show()
# 9. SIMPAN TABEL KE CSV
df.to_csv(
    "Tabel_Bisection_r0_sampai_r16.csv",
    index=False,
    float_format="%.10f"
)

print("\nTabel berhasil disimpan ke:")
print("Tabel_Bisection_r0_sampai_r16.csv")