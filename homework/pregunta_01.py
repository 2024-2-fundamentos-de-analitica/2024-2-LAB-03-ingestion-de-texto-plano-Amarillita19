import pandas as pd
import re

def pregunta_01():
    with open("files/input/clusters_report.txt", encoding="utf-8") as f:
        lines = f.readlines()

    # Encontrar la línea donde realmente empiezan los datos
    start_idx = 4  # Saltamos las 4 primeras líneas del archivo, que contienen encabezados
    data_lines = lines[start_idx:]

    # Unir líneas y limpiar espacios adicionales
    cleaned_lines = []
    current_line = ""

    for line in data_lines:
        if re.match(r"\s*\d+\s+\d+\s+\d+\.\d+", line):  # Nueva fila detectada (empieza con números)
            if current_line:
                cleaned_lines.append(current_line)
            current_line = line.strip()
        else:
            current_line += " " + line.strip()  # Concatenar las palabras clave en una sola línea

    if current_line:
        cleaned_lines.append(current_line)

    # Leer el archivo con pandas
    df = pd.read_fwf(
        filepath_or_buffer="files/input/clusters_report.txt",
        widths=[10, 30, 30, 100],  # Ajusta estos valores según el archivo
        skiprows=4,
        header=None
    )

    # Renombrar columnas
    df.columns = ["cluster", "cantidad_de_palabras_clave", "porcentaje_de_palabras_clave", "palabras_clave"]

    # Limpiar la columna de palabras clave evitando errores con NaN
    df["palabras_clave"] = df["palabras_clave"].astype(str).apply(
        lambda x: re.sub(r"\s+", " ", x.strip()).replace(" ", ", ") if x != "nan" else ""
    )

    return df

# Ejecutar la función y mostrar los primeros registros
print(pregunta_01().head())
