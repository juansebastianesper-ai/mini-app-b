## Rol
Actúa como desarrollador backend con experiencia en FastAPI, Jinja2 y pruebas con
pytest.
## Objetivo
Construir la mini-aplicación web  Conversor de unidades con estos requisitos:
1. GET / muestra un formulario para elegir el tipo de medida, el valor y las unidades
de origen y de destino, y muestra el resultado sin recargar la página.
2. GET /api/convertir recibe los parámetros tipo, valor, de y a, y devuelve
{"resultado": número}, redondeado a 4 decimales.
3. Tipos y unidades: temperatura (C, F, K), longitud (mm, cm, m, km) y masa (g, kg,
lb).
4. Si el tipo o una unidad no son válidos, o si las unidades no corresponden al tipo,
responde con el código 400 y un mensaje en el campo detail.
## Contexto
Lee AGENTS.md. El contrato de la API está en tests/test_aceptacion.py: las rutas, los
nombres de los campos y los códigos de estado deben coincidir con esas pruebas.
## Restricciones
- Usa solo las dependencias de requirements.txt.
- Define las rutas en app/main.py y la lógica en app/servicios.py, sin importar
FastAPI en servicios.
- Guarda los datos en memoria, sin base de datos ni archivos.
- No modifiques tests/test_aceptacion.py.
- La página usa HTML, CSS y JavaScript sin librerías externas.
## Formato de salida
Antes de escribir código, muestra el plan con las rutas completas de los archivos que
vas a crear y espera mi aprobación. Al terminar, resume en una línea qué hace cada
archivo.
## Ejemplo
GET /api/convertir?tipo=temperatura&valor=100&de=C&a=F devuelve:
{"resultado": 212.0}
GET /api/convertir?tipo=masa&valor=1&de=kg&a=lb devuelve:
{"resultado": 2.2046}
## Criterio de éxito
python -m pytest -v pasa todas las pruebas y ruff check . no reporta errores. Si
después de 3 intentos las pruebas no pasan, detente y explica el problema.