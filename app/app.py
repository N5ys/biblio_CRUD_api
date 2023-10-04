from flask import Flask
from models.book import Base
from routes.book_routes import book_routes
from routes.author_routes import author_routes
from routes.user_routes import user_routes
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)


DATABASE_URL = 'postgresql://postgres:p@$$w0rd@localhost:5432/biblio'
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()


app.register_blueprint(book_routes)
app.register_blueprint(author_routes)
app.register_blueprint(user_routes)

if __name__ == "__main__":
    app.run(debug=True)