from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine,inspect
from faker import Faker
from random import randrange,choice
from datetime import timedelta, datetime
import os
from models import Reader, Book,Base
from werkzeug.exceptions import NotFound



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Создаем движок базы данных
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], pool_pre_ping=True)

# Создаем фабрику сессий
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_or_404(model, identifier):
    session = SessionLocal()
    obj = session.query(model).get(identifier)
    if obj is None:
        raise NotFound(description=f"{model.__name__} with id={identifier} was not found")
    return obj

# Функция для проверки наличия таблиц и их создания при необходимости
def initialize_database():
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    print("Проверяем наличие таблиц...")
    # Проверяем наличие таблиц
    required_tables = {'readers', 'books'}
    missing_tables = required_tables - set(tables)

    if missing_tables:
        # Если таблицы отсутствуют, создаем их
        print(f"Создаются недостающие таблицы: {missing_tables}")
        Base.metadata.create_all(bind=engine)

        # Генерируем тестовые данные и вставляем их
        fake = Faker(locale='ru_RU')
        session = SessionLocal()

        # Генерируем читателей
        readers = []
        for _ in range(10):
            reader = Reader(
                FIO=fake.name(),
                DateBirth=fake.date_between(start_date='-60y', end_date='-18y')
            )
            session.add(reader)
            readers.append(reader)
        session.commit()

        # Генерируем книги, выбрав случайного читателя
        for _ in range(50):
            book = Book(
                ReaderID=choice(readers).id,  # случайный выбор читателя
                Title=fake.sentence(nb_words=randrange(3, 6)),  # случайное название книги
                Author=fake.name(),  # случайный автор
                DateStart=fake.date_between(start_date='-1y', end_date='today')  # случайная дата выдачи
            )
            session.add(book)
        session.commit()
        session.close()
    else:
        print("Все необходимые таблицы уже существуют.")

if __name__ == '__main__':
    # Выполняем инициализацию базы данных при запуске главного процесса
    initialize_database()

    # Запускаем приложение
    app.run(host='0.0.0.0', port=5000, debug=False)

if __name__ != "gunicorn":
    # Запускаем инициализацию базы данных только в мастере (не в воркерах)
    initialize_database()

# Отображение списка читателей
@app.route('/readers')
def readers_list():
    session = SessionLocal()
    readers = session.query(Reader).all()
    session.close()
    return render_template('readers.html', readers=readers)
# Отображение всех книг
@app.route('/books/all')
def all_books():
    session = SessionLocal()
    books = session.query(Book).all()
    session.close()
    return render_template('all_books.html', books=books)

# Добавление нового читателя
@app.route('/add_reader', methods=['GET', 'POST'])
def add_reader():
    session = SessionLocal()
    if request.method == 'POST':
        fio = request.form['fio']
        birth_date = request.form['birth_date']
        reader = Reader(FIO=fio, DateBirth=datetime.strptime(birth_date, '%Y-%m-%d').date())
        session.add(reader)
        session.commit()
        session.close()
        return redirect(url_for('readers_list'))
    return render_template('add_reader.html')

# МДобавление новой книги
@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    session = SessionLocal()
    if request.method == 'POST':
        reader_id = int(request.form['reader_id'])
        title = request.form['title']
        author = request.form['author']
        start_date = request.form['start_date']
        book = Book(
            ReaderID=reader_id,
            Title=title,
            Author=author,
            DateStart=datetime.strptime(start_date, '%Y-%m-%d').date()
        )
        session.add(book)
        session.commit()
        session.close()
        return redirect(url_for('show_books', reader_id=reader_id))
    else:
        # Получаем всех читателей для выпадающего списка
        readers = session.query(Reader).all()
        session.close()
        return render_template('add_book.html', readers=readers)
# Начальная страница
@app.route('/')
def index():
    session = SessionLocal()
    readers = session.query(Reader).all()
    session.close()
    return render_template('index.html', readers=readers)

# Получение списка книг, взятых читателем
@app.route('/books/<int:reader_id>')
def show_books(reader_id):
    session = SessionLocal()
    reader = get_or_404(Reader, reader_id)
    session.close()
    return render_template('books.html', reader=reader)


if __name__ == '__main__':
    initialize_database()
    app.run(host='0.0.0.0', port=5000, debug=False)