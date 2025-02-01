from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import db_init
from query_handler import handle_query

app = FastAPI()

# Initialize templates & database
templates = Jinja2Templates(directory="templates")
db_init.init_db()

class UserQuery(BaseModel):
    query: str

@app.get("/")
async def get_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/query")
def process_query(user_query: UserQuery):
    return handle_query(user_query.query.lower())
