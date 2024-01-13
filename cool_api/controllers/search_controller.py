
from flask import Blueprint
from .search_service import add_books, search_books

searchData = Blueprint('searchData', __name__)

@searchData.route('/add-books', methods=['GET'])
def add_books_route():
    return add_books()

@searchData.route('/search-books', methods=['GET'])
def search_books_route():
    return search_books()