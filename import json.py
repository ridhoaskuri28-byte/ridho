import json
import pandas as pd

# Buka file JSON
with open("RIDHO ASYKURI_V3925015.Json.JSON", "r") as f:
    data = json.load(f)

# Contoh: ubah bagian video jadi tabel
df_video = pd.DataFrame(data["video"])
print("Tabel Video:")
print(df_video)

# Contoh: ubah bagian audio jadi tabel
df_audio = pd.DataFrame(data["audio"])
print("\nTabel Audio:")
print(df_audio)

# Contoh: ubah bagian foto jadi tabel
df_foto = pd.DataFrame(data["foto"])
print("\nTabel Foto:")
print(df_foto)

# Contoh: ubah bagian gps jadi tabel
df_gps = pd.DataFrame(data["gps"])
print("\nTabel GPS:")
print(df_gps)

# Simpan ke Excel biar lebih rapi
with pd.ExcelWriter("output_tabel.xlsx") as writer:
    df_video.to_excel(writer, sheet_name="Video", index=False)
    df_audio.to_excel(writer, sheet_name="Audio", index=False)
    df_foto.to_excel(writer, sheet_name="Foto", index=False)
    df_gps.to_excel(writer, sheet_name="GPS", index=False)

print("\nSemua tabel sudah disimpan ke output_tabel.xlsx")
