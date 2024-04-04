from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import database

app = FastAPI()

templates = Jinja2Templates(directory="templates/main")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    cur = database.conn()
    database.create_table(cur)
    tasks = database.view_tasks(cur)
    print(tasks)
    return templates.TemplateResponse(
        request=request, name="index.html", context={"tasks": tasks}
    )


@app.post("/", response_class=HTMLResponse)
async def post_index(request: Request, form1: str):
    cur = database.conn()
    database.create_table(cur)
    tasks = database.view_tasks(cur)
    return templates.TemplateResponse(
        request=request, name="index.html", context={"tasks": tasks}
    )
