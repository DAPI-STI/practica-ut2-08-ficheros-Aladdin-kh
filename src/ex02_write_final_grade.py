"""
EX02 (CSV) · Registrar calificaciones finales

Objetivo:
- Practicar escritura en ficheros en modo "append" (añadir al final).
- Guardar datos en un formato estándar: CSV (separado por comas).

En una app real esto sería el típico "registro" de resultados.
"""

from __future__ import annotations

from pathlib import Path


def write_final_grade(path: str | Path, name: str, average: float) -> None:
    """
    Añade una línea al fichero CSV en `path` con este formato:

    nombre,nota

    Ejemplo:
    Ana,7.5

    Reglas:
    - El fichero se crea si no existe.
    - Si ya existe, se añade una línea al final (NO se sobrescribe).
    - name no puede estar vacío tras strip(). Si lo está, ValueError.
    - average debe estar entre 0 y 10 (incluidos). Si no, ValueError.

    Nota:
    - No hace falta escribir cabecera para este ejercicio.
    """
    # Validaciones palabra y nota
    name = name.strip()
    if name == "":
        raise ValueError("El nombre no puede estar vacío")
    if not (0 <= average <= 10):
        raise ValueError("La nota debe estar entre 0 y 10")
    # Escritura en el fichero
    with open(path, "a", encoding="utf-8") as file:
        file.write(f"{name},{average}\n")
