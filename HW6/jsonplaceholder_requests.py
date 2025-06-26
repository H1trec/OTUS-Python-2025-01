import asyncio
from typing import List, Dict
import aiohttp

# Константы с ресурсами
USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def fetch_json(session: aiohttp.ClientSession, url: str) -> List[Dict]:
    """
    Базовая асинхронная функция для отправки GET-запроса и получения JSON-данных.

    :param session: объект ClientSession
    :param url: целевой URL
    :return: список объектов в виде словарей
    """
    async with session.get(url) as response:
        return await response.json()


async def get_users() -> List[Dict]:
    """
    Получение списка пользователей с сервера.

    :return: Список пользователей
    """
    async with aiohttp.ClientSession() as session:
        users_data = await fetch_json(session, USERS_DATA_URL)
        return users_data


async def get_posts() -> List[Dict]:
    """
    Получение списка постов с сервера.

    :return: Список постов
    """
    async with aiohttp.ClientSession() as session:
        posts_data = await fetch_json(session, POSTS_DATA_URL)
        return posts_data


if __name__ == "__main__":
    # Демонстрация работы модулей
    loop = asyncio.get_event_loop()
    users = loop.run_until_complete(get_users())
    print("Пользователи:", users[:2])

    posts = loop.run_until_complete(get_posts())
    print("Посты:", posts[:2])