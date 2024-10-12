import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()


def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )''')


# в задании написано ||description(описание) - тест||. Решил, что тут опечатка и на самом деле тут "теКст"

initiate_db()

'''Перед запуском бота пополните вашу таблицу Products 4 или более записями для последующего вывода в чате Telegram-бота'''


# Для наполнения таблицы
# for i in range(1, 5):
#     cursor.execute('INSERT INTO  Products(title, description, price) VALUES (?, ?, ?)',
#                    (f'Product{i}', f'Описание{i}', i * 100,))


def get_all_products():
    cursor.execute('SELECT * FROM Products')
    all_products = cursor.fetchall()
    return all_products


cursor.execute('SELECT COUNT(*) FROM Products')
count_str = cursor.fetchone()[0]

connection.commit()
# connection.close()
