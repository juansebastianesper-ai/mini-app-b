UNIDADES_POR_TIPO = {
    "temperatura": ("C", "F", "K"),
    "longitud": ("mm", "cm", "m", "km"),
    "masa": ("g", "kg", "lb"),
}


def obtener_unidades() -> dict[str, list[str]]:
    return {tipo: list(unidades) for tipo, unidades in UNIDADES_POR_TIPO.items()}


_FACTORES_LONGITUD = {"mm": 0.001, "cm": 0.01, "m": 1.0, "km": 1000.0}
_FACTORES_MASA = {"g": 0.001, "kg": 1.0, "lb": 0.45359237}


def _a_celsius(valor: float, unidad: str) -> float:
    if unidad == "C":
        return valor
    if unidad == "F":
        return (valor - 32) * 5 / 9
    return valor - 273.15


def _desde_celsius(valor: float, unidad: str) -> float:
    if unidad == "C":
        return valor
    if unidad == "F":
        return valor * 9 / 5 + 32
    return valor + 273.15


def convertir(tipo: str, valor: float, de: str, a: str) -> float:
    unidades = UNIDADES_POR_TIPO.get(tipo)
    if unidades is None:
        raise ValueError(f"Tipo de medida no válido: {tipo}")
    if de not in unidades or a not in unidades:
        raise ValueError(
            f"Las unidades {de} y {a} no son válidas para el tipo {tipo}"
        )

    if tipo == "temperatura":
        resultado = _desde_celsius(_a_celsius(valor, de), a)
    elif tipo == "longitud":
        resultado = valor * _FACTORES_LONGITUD[de] / _FACTORES_LONGITUD[a]
    else:
        resultado = valor * _FACTORES_MASA[de] / _FACTORES_MASA[a]

    return round(resultado, 4)
