import os
import sqlite3 as sqlite
import random
import base64
from sqlalchemy import Column, Integer, String, Text, LargeBinary
import simplejson as json
from be.model.database import Base
from be.model.database import db_session

# class Book:
#     id: str
#     title: str
#     author: str
#     publisher: str
#     original_title: str
#     translator: str
#     pub_year: str
#     pages: int
#     price: int
#     binding: str
#     isbn: str
#     author_intro: str
#     book_intro: str
#     content: str
#     tags: [str]
#     pictures: [bytes]
#
#

class Book(Base):
    __tablename__ = 'book'
    __table_args__ = {'extend_existing': True}
    book_id = Column(Integer, primary_key=True)
    title = Column(Text, nullable=False)
    author = Column(Text)
    publisher = Column(Text)
    original_title = Column(Text)
    translator = Column(Text)
    pub_year = Column(Text)
    pages = Column(Integer)
    price= Column(Integer)
    currency_unit = Column(Text)
    binding = Column(Text)
    isbn = Column(Text)
    author_intro = Column(Text)
    book_intro = Column(Text)
    content = Column(Text)
    tags = Column(Text)


    def __init__(self,book_id=None,title=None,author=None,publisher=None,original_title=None,translator=None,pub_year=None,pages=None,price=None,currency_unit=None,binding=None,isbn=None,author_intro=None,book_intro=None,content=None,tags=None):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.publisher = publisher
        self.original_title = original_title
        self.translator = translator
        self.pub_year = pub_year
        self.pages = pages
        self.price = price
        self.currency_unit = currency_unit
        self.binding = binding
        self.isbn = isbn
        self.author_intro = author_intro
        self.book_intro = book_intro
        self.content = content
        self.tags = tags



    def __repr__(self):
        return '<book %r>' % (self.title)


class BookDB:
    def __init__(self, large: bool = False):

        parent_path = os.path.dirname(os.path.dirname(__file__))
        parent_path=parent_path[:-2]
        self.db_s = os.path.join(parent_path, "fe/data/book.db")
        self.db_l = os.path.join(parent_path, "fe/data/book_lx.db")
        if large:
            self.book_db = self.db_l
        else:
            self.book_db = self.db_s

    def get_book_count(self):

        conn = sqlite.connect(self.book_db)
        cursor = conn.execute(
            "SELECT count(id) FROM book")
        row = cursor.fetchone()
        return row[0]

    def get_book_info(self, start, size) -> [Book]:#得到爬虫爬到的db.book里的内容

        conn = sqlite.connect(self.book_db)
        cursor = conn.execute(
            "SELECT id, title, author, "
            "publisher, original_title, "
            "translator, pub_year, pages, "
            "price, currency_unit, binding, "
            "isbn, author_intro, book_intro, "
            "content, tags FROM book ORDER BY id "
            "LIMIT ? OFFSET ?", (size, start))
        for row in cursor:
            # book = Book()
            # book.id = row[0]
            # book.title = row[1]
            # book.author = row[2]
            # book.publisher = row[3]
            # book.original_title = row[4]
            # book.translator = row[5]
            # book.pub_year = row[6]
            # book.pages = row[7]
            # book.price = row[8]
            #
            # book.currency_unit = row[9]
            # book.binding = row[10]
            # book.isbn = row[11]
            # book.author_intro = row[12]
            # book.book_intro = row[13]
            # book.content = row[14]
            book_tag=[]
            tags = row[15]

            for tag in tags.split("\n"):
                if tag.strip() != "":
                    book_tag.append(tag)
                    # book.tags.append(tag)
            # for i in range(0, random.randint(0, 9)):
            #     if picture is not None:

            #         encode_str = base64.b64encode(picture).decode('utf-8')
            #         book_pic.append(encode_str)
                    # book.pictures.append(encode_str)
            book_tag=str(book_tag)#要转换成string类型
            book = Book(book_id=row[0], title=row[1], author=row[2], publisher=row[3], original_title=row[4],translator=row[5],pub_year=row[6], pages=row[7], price=row[8], currency_unit=row[9], binding=row[10],isbn=row[11],author_intro=row[12], book_intro=row[13], content=row[14],tags=book_tag)



            db_session.add(book)

        db_session.commit()


        # return books


# #
# if __name__ == '__main__':
#     bookdb = BookDB()
#     bookdb.get_book_info(0, bookdb.get_book_count())
