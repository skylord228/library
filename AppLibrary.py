from IRepository import IRepository
from Book import Book
from SQLLibrary import SQLLibrary
from fpdf import FPDF
import sqlite3

class AppLibrary(IRepository):
    def __init__(self):
        self.Repository = SQLLibrary()
        self.con = self.Repository.con
        self.cur = self.Repository.cur
    
    def Add(self, book: Book):
        data = (book.title, book.year, book.author)
        self.cur.execute("INSERT INTO books(title, year, author) VALUES(?,?,?)", data)
        self.con.commit()

    def RemoveAt(self, id: int):
        try:
            self.cur.execute("DELETE FROM books where id = ?", (id,))
            self.con.commit()
            
        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)

    def GetAt(self, id: int):
        self.cur.execute("SELECT title, year, author FROM books where id = ?", (id,))
        row = self.cur.fetchone()
        if row is None:
            return None
        else:
            book1 = Book(row[0],row[1],row[2])
            book1.id = id
            return book1

    def GetAll(self):
        self.cur.execute("SELECT title, year, author, id FROM books")
        row = self.cur.fetchall()
        if row is None:
            return None
        else:
            book_list = [Book(row[i][0],row[i][1],row[i][2]) for i in range(len(row))]
            for i in range(len(book_list)): book_list[i].id=row[i][3]
            return book_list

    def PrintBook(self, book: Book):
        print(str(book.id) + " " + book.title + " " + str(book.year) + " " + book.author)

    def FindBy(self, word: str):
        book_list = self.GetAll()
        for val in book_list:
            if word in val.title or word in str(val.year) or word in val.author:
                self.PrintBook(val)
                continue
    
    def Update(self):
        try:
            id = input("Type book id (back to go back): ")
            title_inpt: str = input("Type book title (back to not add): ")
            if title_inpt == "back":
                return
            year_input: int = input("Type book year (back to not add): ")
            if year_input == "back":
                return
            author_input: str = input("Type book author (back to not add): ")
            if author_input == "back":
                return
            

            #self.cur.execute("UPDATE books SET title = ?, year = ?, author = ? WHERE id = ?", (title_inpt, year_input, author_input, id))
            sql_update_query = """Update books set title = ?, year = ?, author = ? where id = ?"""
            data = (title_inpt, year_input, author_input, id)
            self.cur.execute(sql_update_query, data)
            self.con.commit()

        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)
            
        

    #деструктор
    def __del__(self):
        self.cur.close()
        self.con.close()




book = Book("MyBook",1984,"Alexander Ivanov Ivanovich")
lib = AppLibrary()
while True:
    inpt = input("Type one of the ecommands: add, remove, getbyid, getall, find, savepdf, exit: ")

    if inpt == "add":
        title_inpt: str = input("Type book title (back to not add): ")
        if title_inpt == "back":
            continue
        year_input: int = input("Type book year (back to not add): ")
        if year_input == "back":
            continue
        author_input: str = input("Type book author (back to not add): ")
        if author_input == "back":
            continue
        newbook = Book(
            title_inpt,
            year_input,
            author_input
        )
        lib.Add(newbook)

    elif inpt == "update":
        lib.Update()

    elif inpt == "remove":
        lib.RemoveAt(input("Type book id: "))
        
    elif inpt == "getbyid":
        newbook = lib.GetAt(input("Type book id: "))
        if newbook is None:
            print("The element does not exist")
        else:
            lib.PrintBook(newbook)
        
    elif inpt == "getall":
        book_list = lib.GetAll()
        if book_list is None:
            print("No elements in DB")
        else:
            for val in book_list:
                lib.PrintBook(val)

    elif inpt == "find":
        lib.FindBy(input("Enter keyword: "))

    elif inpt == "savepdf":
        spacing = 1
        book_list = lib.GetAll()
        pdf = FPDF()
        pdf.set_font("Arial", size=12)
        pdf.add_page()
        col_width = pdf.w / 3.4
        row_height = pdf.font_size
        for row in book_list:
            pdf.cell(col_width, row_height*spacing, txt=row.title, border=1)
            pdf.cell(col_width, row_height*spacing, txt=str(row.year), border=1)
            pdf.cell(col_width, row_height*spacing, txt=row.author, border=1)
            pdf.ln(row_height*spacing)
            
        pdf.output("DBtable.pdf")

    elif inpt == "exit":
        break
