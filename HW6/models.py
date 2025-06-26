import os
import asyncpg
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.orm.decl_api import declared_attr
from config import settings


#  Строка подключения к PostgreSQL
PG_CONN_URI = settings.get_db_url()

print(PG_CONN_URI)

engine = create_async_engine(url=PG_CONN_URI)

# Определяем класс для наследования моделей
class Base(DeclarativeBase):
    pass

# Класс Session для асинхронных операций
#session_factory = AsyncSession(engine, expire_on_commit=False)
Session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

# Пользовательская модель
class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False)
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)

    # Связь с Post
    posts: Mapped[list["Post"]] = relationship(back_populates="user")

# Постовая модель
class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    title: Mapped[str] = mapped_column(nullable=False)
    body: Mapped[str] = mapped_column(nullable=False)

    # Обратная ссылка на User
    user: Mapped["User"] = relationship(back_populates="posts")