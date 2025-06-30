import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy import inspect
from models import Base, User, Post, engine
from jsonplaceholder_requests import get_users, get_posts

# Заводим фабрику сессий
Session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def load_and_save_users(session, users_data):
    """Загрузка и сохранение пользователей."""
    users = []
    for user in users_data:
        filtered_user = {
            "id": user["id"],
            "name": user["name"],
            "username": user["username"],
            "email": user["email"]
        }
        users.append(User(**filtered_user))
    session.add_all(users)
    await session.commit()

async def load_and_save_posts(session, posts_data):
    """Загрузка и сохранение постов в правильном порядке."""
    posts = []
    for post in posts_data:
        filtered_post = {
            "user_id": post["userId"],
            "id": post["id"],
            "title": post["title"],
            "body": post["body"]
        }
        posts.append(Post(**filtered_post))

    # Вставляем посты в правильном порядке
    session.add_all(posts)
    await session.commit()

async def check_tables_exist(engine):
    """Проверка наличия таблиц в базе данных."""
    async with engine.begin() as connection:
        def sync_get_table_names(connection):
            ins = inspect(connection)
            return ins.get_table_names()

        existing_tables = await connection.run_sync(sync_get_table_names)
        expected_tables = ["users", "posts"]
        missing_tables = [table for table in expected_tables if table not in existing_tables]
        return len(missing_tables) > 0

async def async_main():
    # Проверяем наличие таблиц
    should_create_tables = await check_tables_exist(engine)

    if should_create_tables:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    # Начинаем загрузку данных
    async with Session() as session:
        # Параллельно получаем данные пользователей и постов
        users_data, posts_data = await asyncio.gather(get_users(), get_posts())

        # Сначала сохраняем пользователей
        await load_and_save_users(session, users_data)

        # Затем сохраняем посты в правильном порядке
        await load_and_save_posts(session, posts_data)

def main():
    asyncio.run(async_main())

if __name__ == "__main__":
    main()
