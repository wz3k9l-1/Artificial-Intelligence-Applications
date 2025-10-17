# main.py - FastAPI application
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from model_module import predict_iris

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "result": None})


@app.post("/", response_class=HTMLResponse)
async def predict(
        request: Request,
        sepal_length: float = Form(...),
        sepal_width: float = Form(...),
        petal_length: float = Form(...),
        petal_width: float = Form(...)
):
    result = predict_iris(sepal_length, sepal_width, petal_length, petal_width)
    return templates.TemplateResponse("index.html", {"request": request, "result": result})
