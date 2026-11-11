## Rol
Actúa como desarrollador/a con experiencia en Python 3.14, FastAPI, Jinja2 y pytest.

## Objetivo
Implementa la mejora para que `GET /api/unidades`, sin parámetros, devuelva los tipos de medida y sus unidades. La página principal también debe consultar este endpoint y usar sus datos para llenar las listas de unidades de origen y destino según el tipo elegido.

## Contexto
Este proyecto es un conversor de unidades con FastAPI, plantillas Jinja2 y datos en memoria. Revisa `AGENTS.md` y sigue la estructura existente: rutas en `app/main.py`, datos/lógica en `app/servicios.py` y página en `app/templates/index.html`. La mejora debe conservar la conversión existente.

## Restricciones
- Añade una prueba en `tests/test_mejora.py` que compruebe que `GET /api/unidades` responde con el código 200 y el JSON exacto del ejemplo.
- No modifiques ni borres `tests/test_aceptacion.py` ni la prueba de aceptación existente en `test/test_aceptacion.py`.
- No uses base de datos ni archivos para guardar datos; conserva los datos en memoria.
- No añadas dependencias: utiliza solo las incluidas en `requirements.txt`.
- Mantén la página principal funcional y haz que use `/api/unidades` para cargar las unidades disponibles por tipo.

## Formato de salida
Antes de modificar archivos, presenta un plan breve que enumere cada archivo que crearás o modificarás, usando su ruta absoluta completa. En este proyecto, por ejemplo: `C:\Users\Juan Esper\Documents\practica-prompts\mini-app-b\app\main.py`. Espera mi aprobación explícita antes de continuar; no edites archivos antes de recibirla. Al terminar, resume los cambios y los comandos de validación ejecutados.

## Ejemplo
Petición:
```http
GET /api/unidades
```

Respuesta esperada:
```json
{
  "temperatura": ["C", "F", "K"],
  "longitud": ["mm", "cm", "m", "km"],
  "masa": ["g", "kg", "lb"]
}
```

## Criterio de éxito
La prueba nueva y las pruebas existentes deben pasar, y Ruff no debe reportar errores: ejecuta `python -m pytest -v` y `ruff check .`. Si la validación falla, realiza como máximo tres intentos en total de corregir y volver a ejecutar los comandos; si siguen fallando tras el tercer intento, detente e informa claramente el fallo.
