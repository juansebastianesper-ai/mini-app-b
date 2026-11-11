from pathlib import Path

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app import servicios

app = FastAPI()
templates = Jinja2Templates(directory=str(Path(__file__).resolve().parent / "templates"))


@app.get("/", response_class=HTMLResponse)
def pagina_principal(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"tipos": servicios.UNIDADES_POR_TIPO},
    )


@app.get("/api/convertir")
def convertir(tipo: str, valor: float, de: str, a: str) -> dict[str, float]:
    try:
        resultado = servicios.convertir(tipo, valor, de, a)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error)) from error

    return {"resultado": resultado}
