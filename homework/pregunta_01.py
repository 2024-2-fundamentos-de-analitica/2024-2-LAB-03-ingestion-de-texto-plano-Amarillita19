import pandas as pd
import re

def pregunta_01():
    # Leer todas las líneas del archivo
    with open("files/input/clusters_report.txt", encoding="utf-8") as f:
        lines = f.readlines()

    # Unir líneas en un solo texto y normalizar espacios
    raw_text = " ".join(line.strip() for line in lines)
    raw_text = re.sub(r"\s{2,}", " ", raw_text)  # Reemplazar múltiples espacios con uno solo

    # Leer datos con pandas
    df = pd.read_fwf("files/input/clusters_report.txt", skiprows=4, header=None)

    # Renombrar columnas manualmente
    df.columns = ["cluster", "cantidad_de_palabras_clave", "porcentaje_de_palabras_clave", "palabras_clave"]

    # Limpiar la columna de palabras clave
    df["palabras_clave"] = df["palabras_clave"].apply(lambda x: re.sub(r"\s+", " ", x.strip()).replace(" ", ", "))

    return df

# Ejecutar la función y mostrar los primeros registros
print(pregunta_01().head())
