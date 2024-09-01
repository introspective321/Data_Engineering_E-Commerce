from flask import Flask, render_template, redirect, url_for, flash, request, abort
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, current_user, login_required, logout_user
from models import db, User, Artist, Artwork, Order, OrderItem, Review
from forms import LoginForm, RegisterForm, ArtworkForm
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config.from_object('config.Config')
db.init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    if current_user.is_authenticated:
        if current_user.role == 'Artist':
            return redirect(url_for('artist_dashboard'))
        return redirect(url_for('browse_artwork'))
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, email=form.email.data, role=form.role.data)
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        if new_user.role == 'Artist':
            new_artist = Artist(artist_id=new_user.id)  # Adjusted to match User model
            db.session.add(new_artist)
            db.session.commit()
        flash('Registration successful!')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

from forms import LoginForm, RegisterForm, ArtworkForm

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():  # No extra arguments should be passed here
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Login successful!')
            if user.role == 'Artist':
                return redirect(url_for('artist_dashboard'))
            return redirect(url_for('browse_artwork'))
        flash('Invalid email or password.')
    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully.')
    return redirect(url_for('login'))

@app.route('/artist/dashboard')
@login_required
def artist_dashboard():
    if current_user.role != 'Artist':
        return redirect(url_for('browse_artwork'))
    artworks = Artwork.query.filter_by(artist_id=current_user.id).all()  # Adjusted to match User model
    return render_template('artist_dashboard.html', artworks=artworks)

@app.route('/artist/add_artwork', methods=['GET', 'POST'])
@login_required
def add_artwork():
    if current_user.role != 'Artist':
        return redirect(url_for('browse_artwork'))
    form = ArtworkForm()
    if form.validate_on_submit():
        file = request.files.get('image')
        if not file or file.filename == '':
            flash('No selected file.')
            return redirect(request.url)
        filename = secure_filename(file.filename)
        if not filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            flash('Invalid file type.')
            return redirect(request.url)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        new_art = Artwork(
            title=form.title.data,
            description=form.description.data,
            price=form.price.data,
            medium=form.medium.data,
            style=form.style.data,
            artist_id=current_user.id,  # Adjusted to match User model
            image_url=filename
        )
        db.session.add(new_art)
        db.session.commit()
        flash('Artwork added successfully!')
        return redirect(url_for('artist_dashboard'))
    return render_template('add_artwork.html', form=form)

@app.route('/artworks')
def browse_artwork():
    artworks = Artwork.query.filter_by(availability='Available').all()
    return render_template('browse_artwork.html', artworks=artworks)

@app.route('/artwork/<int:artwork_id>', methods=['GET', 'POST'])
def view_artwork(artwork_id):
    artwork = Artwork.query.get_or_404(artwork_id)
    if request.method == 'POST' and current_user.is_authenticated:
        rating = request.form.get('rating')
        comment = request.form.get('comment')
        review = Review(
            rating=rating,
            comment=comment,
            buyer_id=current_user.id,  # Adjusted to match User model
            artwork_id=artwork_id
        )
        db.session.add(review)
        db.session.commit()
        flash('Review submitted successfully!')
        return redirect(url_for('view_artwork', artwork_id=artwork_id))
    return render_template('view_artwork.html', artwork=artwork)

@app.route('/artwork/<int:artwork_id>/reviews')
def view_reviews(artwork_id):
    artwork = Artwork.query.get_or_404(artwork_id)
    reviews = Review.query.filter_by(artwork_id=artwork_id).all()
    return render_template('view_reviews.html', artwork=artwork, reviews=reviews)

@app.route('/artist_profile')
@login_required
def artist_profile():
    if current_user.role != 'Artist':
        abort(403)
    artist = Artist.query.get_or_404(current_user.id)  # Adjusted to match User model
    return render_template('artist_profile.html', artist=artist)

if __name__ == '__main__':
    app.run(debug=True)
