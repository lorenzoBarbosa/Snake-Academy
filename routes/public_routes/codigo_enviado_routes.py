from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.params import Form
from fastapi.responses import RedirectResponse

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/codigo_enviado")
async def get_codigo_enviado(request: Request):
    response = templates.TemplateResponse("publico/codigo_enviado.html", {"request": request})
    return response

@router.post("/codigo_enviado")
async def post_codigo_enviado(request: Request, email: str = Form(...)):
    response = templates.TemplateResponse(
        "publico/codigo_enviado.html",
        {"request": request, "email": email}
    )
    return response
