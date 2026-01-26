"""
EX04 (Texto) · Listín telefónico en fichero

Vas a implementar un pequeño "CRUD" (Crear/Leer/Actualizar/Borrar) de contactos,
guardados en un fichero de texto.

Formato del fichero (una línea por contacto):
nombre,telefono

Ejemplo:
Ana,600123123
Luis,600000000

Para que el ejercicio sea más limpio, se proponen dos funciones "privadas":
- _load_phonebook(): lee el fichero y lo convierte en dict
- _save_phonebook(): guarda el dict en el fichero

Luego, las funciones públicas usan esas helpers:
- add_contact(): alta/actualización
- get_phone(): consulta
- remove_contact(): baja
"""

from __future__ import annotations

from pathlib import Path


def _load_phonebook(path: str | Path) -> dict[str, str]:
    """
    Carga el listín desde `path` y devuelve un diccionario {name: phone}.

    Reglas:
    - Si el fichero no existe, devuelve {} (NO es error).
    - Ignora líneas vacías.
    - Cada línea debe tener exactamente 2 partes separadas por coma:
      "nombre,telefono"
      Si alguna línea está mal formada, lanza ValueError.
    - Recorta espacios alrededor de nombre y teléfono con .strip().

    Consejo:
    - Usa `with open(..., encoding="utf-8") as f:`
    - Recorre línea a línea con `for line in f:`
    """
    phonebook = {}
    try:
        with open(path, "r", encoding="utf-8") as file:
            for linea in file:
                l1 = linea.strip()
                if not l1:
                    continue
                secc = l1.split(",")
                if len(secc) != 2:
                    raise ValueError("Línea mal formada")
                name, phone = secc
                phonebook[name.strip()] = phone.strip()
    except FileNotFoundError:
        pass
    return phonebook


def _save_phonebook(path: str | Path, phonebook: dict[str, str]) -> None:
    """
    Guarda el diccionario en `path` en formato "nombre,telefono", una línea por contacto.

    Reglas:
    - Sobrescribe el fichero (modo 'w').
    - Puedes guardar en cualquier orden.
    - Usa encoding="utf-8".
    """
    with open(path, "w", encoding="utf-8") as file:
        for name, phone in phonebook.items():
            file.write(f"{name},{phone}\n")


def add_contact(path: str | Path, name: str, phone: str) -> None:
    """
    Añade o actualiza un contacto (name -> phone) en el fichero.

    Reglas:
    - name y phone no pueden estar vacíos (tras strip). Si lo están, ValueError.
    - Si el contacto ya existe, se actualiza su teléfono.
    - Si no existe, se añade.

    Pista:
    - load -> modificar dict -> save
    """
    phonebook = _load_phonebook(path)
    if not name.strip() or not phone.strip():
        raise ValueError("El nombre y el teléfono no pueden estar vacíos")

    phonebook[name.strip()] = phone.strip()
    _save_phonebook(path, phonebook)

def get_phone(path: str | Path, name: str) -> str | None:
    """
    Devuelve el teléfono del contacto `name` o None si no existe.

    Reglas:
    - Si el fichero no existe, devuelve None (porque no hay contactos).
    - `name` se compara tras strip().
    """
    phonebook = _load_phonebook(path)
    return phonebook.get(name.strip(), None)


def remove_contact(path: str | Path, name: str) -> bool:
    """
    Elimina el contacto `name` si existe.

    Devuelve:
    - True si se eliminó
    - False si no existía

    Reglas:
    - Si el fichero no existe, devuelve False.
    - `name` se compara tras strip().

    Pista:
    - load -> borrar si existe -> save si cambió
    """
    phonebook = _load_phonebook(path)
    name = name.strip()
    if name in phonebook:
        del phonebook[name]
        _save_phonebook(path, phonebook)
        return True
    return False
    raise NotImplementedError("Implementa remove_contact(path, name)")
