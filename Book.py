import sqlite3


class Book:
    def __init__(self, title: str, year: int, author: str):
        self.title = title
        self.year = year
        self.author = author
    id: int