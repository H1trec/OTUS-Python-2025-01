"""
Домашнее задание №5
Первое веб-приложение

- в модуле `app` создайте базовое FastAPI приложение
- создайте обычные представления
  - создайте index view `/`
  - добавьте страницу `/about/`, добавьте туда текст, информацию о сайте и разработчике
  - создайте базовый шаблон (используйте https://getbootstrap.com/docs/5.0/getting-started/introduction/#starter-template)
  - в базовый шаблон подключите статику Bootstrap 5 (подключите стили), примените стили Bootstrap
  - в базовый шаблон добавьте навигационную панель `nav` (https://getbootstrap.com/docs/5.0/components/navbar/)
  - в навигационную панель добавьте ссылки на главную страницу `/` и на страницу `/about/` при помощи `url_for`
  - добавьте новые зависимости в файл `requirements.txt` в корне проекта
    (лучше вручную, но можно командой `pip freeze > requirements.txt`, тогда обязательно проверьте, что туда попало, и удалите лишнее)
- создайте api представления:
  - создайте api router, укажите префикс `/api`
  - добавьте вложенный роутер для вашей сущности (если не можете придумать тип сущности, рассмотрите варианты: товар, книга, автомобиль)
  - добавьте представление для чтения списка сущностей
  - добавьте представление для чтения сущности
  - добавьте представление для создания сущности
"""
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

# Инициализация приложения
app = FastAPI()

# Подключение статических файлов (Bootstrap CSS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Настройка шаблонов
templates = Jinja2Templates(directory="templates")

# Модель для товаров
class Item(BaseModel):
    id: int
    name: str
    description: str

# Пример данных
items = [
    {"id": 1, "name": "Book", "description": "Книга по FastAPI"},
    {"id": 2, "name": "Pen", "description": "Ручка для заметок"},
]

# API роутер
api_router = FastAPI(prefix="/api")

@api_router.get("/items/", tags=["Items"])
async def read_items():
    return items

@api_router.get("/items/{item_id}", tags=["Items"])
async def read_item(item_id: int):
    for item in items:
        if item["id"] == item_id:
            return item
    return {"error": "Item not found"}

@api_router.post("/items/", tags=["Items"])
async def create_item(item: Item):
    new_item = item.dict()
    items.append(new_item)
    return new_item

# HTML роутер
@app.get("/", response_class=HTMLResponse, tags=["HTML"])
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/about/", response_class=HTMLResponse, tags=["HTML"])
async def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})