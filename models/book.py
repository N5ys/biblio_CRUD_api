from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    year = Column(Integer)
    author_id = Column(Integer, ForeignKey('authors.id'))
    genre = Column(String)
    is_read = Column(Boolean)
    rating = Column(Float)

    author = relationship("Author", back_populates="books")