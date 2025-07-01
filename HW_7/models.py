from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.types import Integer, String, Date
from sqlalchemy import ForeignKey

class Base(DeclarativeBase):
    pass

class Reader(Base):
    __tablename__ = 'readers'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    FIO: Mapped[str] = mapped_column(String(500), nullable=False)
    DateBirth: Mapped[Date] = mapped_column(Date, nullable=False)
    books: Mapped[list["Book"]] = relationship(back_populates="reader")

class Book(Base):
    __tablename__ = 'books'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    ReaderID: Mapped[int] = mapped_column(ForeignKey('readers.id'), nullable=False)
    Title: Mapped[str] = mapped_column(String(500), nullable=False)
    Author: Mapped[str] = mapped_column(String(500), nullable=False)
    DateStart: Mapped[Date] = mapped_column(Date, nullable=False)
    reader: Mapped["Reader"] = relationship(back_populates="books")
