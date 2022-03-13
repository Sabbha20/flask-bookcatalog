from app.catalog import main
from app.catalog.models import Book, Publication
from flask import render_template, flash, request, redirect, url_for
from flask_login import login_required
from app import db
from app.catalog.forms import EditBookForm, CreateBookForm


@main.route('/')
def book_list():
    books = Book.query.all()
    pub = Publication.query.all()
    return render_template('home.html', books=books, pub=pub)


@main.route('/publisher/<publisher_id>')
def publisher_display(publisher_id):
    publisher = Publication.query.filter_by(id=publisher_id)[0]
    pub_books = Book.query.filter_by(pub_id=publisher_id)
    return render_template('publisher.html', publisher=publisher, pub_books=pub_books)


@main.route('/book/delete/<book_id>', methods=['GET', 'POST'])
@login_required
def delete_book(book_id):
    book = Book.query.get(book_id)
    if request.method == 'POST':
        db.session.delete(book)
        db.session.commit()
        flash('Book Deleted - ' + book.title)
        return redirect(url_for('main.book_list'))
    return render_template('delete_book.html', book=book, book_id=book_id)


@main.route('/book/edit/<book_id>', methods=['GET', 'POST'])
@login_required
def edit_book(book_id):
    book = Book.query.get(book_id)
    form = EditBookForm(obj=book)
    if form.validate_on_submit():
        book.title = form.title.data
        book.book_format = form.book_format.data
        book.num_pages = form.num_pages.data
        db.session.add(book)
        db.session.commit()
        flash('Book updated Successfully')
        return redirect(url_for('main.book_list'))
    return render_template('edit_book.html', form=form, fun='Edit/Update')


@main.route('/create/book/<pub_id>', methods=['GET', 'POST'])
@login_required
def create_book(pub_id):
    form = CreateBookForm()
    form.pub_id.data = pub_id
    if form.validate_on_submit():
        book = Book(title=form.title.data, author=form.author.data, avg_rating=form.avg_rating.data, book_format=form.book_format.data, image=form.img_url.data, num_pages=form.num_pages.data, pub_id=form.pub_id.data)
        db.session.add(book)
        db.session.commit()
        flash('Book Created Successfully')
        return redirect(url_for('main.publisher_display', publisher_id=pub_id))
    return render_template('edit_book.html', form=form, pub_id=pub_id, fun='Create')
