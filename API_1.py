from fastapi import FastAPI
from enum import Enum
from typing import Optional
app = FastAPI()

BOOKS = {
    'book_1' : {'title' : 'Title One', 'author': 'Aythor One'},
    'book_2' : {'title' : 'Title Two', 'author': 'Aythor Two'},
    'book_3' : {'title' : 'Title Three', 'author': 'Aythor Three'},
    'book_4' : {'title' : 'Title Four', 'author': 'Aythor Four'},
    'book_5' : {'title' : 'Title Five', 'author': 'Aythor Five'}
}

class DirectionName(str, Enum):
    north = "North"
    south = "South"
    east = "East"
    west = "West"

@app.get("/")
async def reall_all_books(skip_book: Optional[str] = None):
    if skip_book:
        new_books = BOOKS.copy()
        del new_books[skip_book]
        return new_books
    return BOOKS

@app.get("/{book_name}")
async def read_book(book_name: str):
    return BOOKS[book_name]



@app.get("/directions/{direction_name}")
async def get_direction(direction_name: DirectionName):
    if direction_name == direction_name.north:
        return  {"Direction" : direction_name, "sub": "Up"}
    if direction_name == direction_name.south:
        return  {"Direction" : direction_name, "sub": "Down"}
    if direction_name == direction_name.west:
        return  {"Direction" : direction_name, "sub": "Left"}
    #if direction_name == direction_name.east:
        return  {"Direction" : direction_name, "sub": "Right"}



@app.get("/books/mybook")
async def read_favorite_book():
    return {"book_title": "My favorite book"}


@app.get("/books/{book_id}")
async def read_book(book_id : int):
    return {"book_title" : book_id}

@app.post("/")
async  def create_book(book_title, book_author):
    current_book_id = 0

    if len(BOOKS) > 0:
        for book in BOOKS:
            x = int(book.split('_')[-1])
            if x > current_book_id:
                current_book_id = x

    BOOKS[f'book_{current_book_id+1}']= {'title': book_title, 'author': book_author}
    return BOOKS[f'book_{current_book_id+1}']

@app.put("/{book_name}")
async def update_book(book_name: str, book_title: str, book_author:str ):
    book_information = {'title' : book_title, 'author' : book_author}
    BOOKS[book_name] = book_information
    return book_information

@app.delete("/{book_name}")
async  def delete_book(book_name):
    del BOOKS [book_name]
    return f'Book {book_name} deleted.'




@app.get("/assignment/")
async def read_book_assignment(book_name:str):
    return BOOKS[book_name]

@app.delete("/assignment/")
async def delete_book_assignemnt(book_name: str):
    del BOOKS[book_name]
    return BOOKS
