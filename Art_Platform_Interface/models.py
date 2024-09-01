from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

db = SQLAlchemy()

class User(UserMixin, db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(50), nullable=False)  # Artist/Buyer

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    # Define relationships
    artist = db.relationship('Artist', uselist=False, back_populates='user')
    reviews = db.relationship('Review', back_populates='buyer')
    orders = db.relationship('Order', back_populates='buyer')

class Artist(db.Model):
    __tablename__ = 'artist'
    artist_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), primary_key=True)
    biography = db.Column(db.Text)
    portfolio_url = db.Column(db.String(200))

    # Define relationship
    user = db.relationship('User', back_populates='artist')
    artworks = db.relationship('Artwork', back_populates='artist')

class Artwork(db.Model):
    __tablename__ = 'artwork'
    artwork_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)
    availability = db.Column(db.String(50), nullable=False, default='Available')
    medium = db.Column(db.String(100))
    style = db.Column(db.String(100))
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.artist_id'))

    # Define relationship
    artist = db.relationship('Artist', back_populates='artworks')
    reviews = db.relationship('Review', back_populates='artwork')
    order_items = db.relationship('OrderItem', back_populates='artwork')

class Order(db.Model):
    __tablename__ = 'order'
    order_id = db.Column(db.Integer, primary_key=True)
    order_date = db.Column(db.DateTime, default=datetime.utcnow)
    total_amount = db.Column(db.Float, nullable=False)
    buyer_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    status = db.Column(db.String(50), nullable=False, default='Pending')

    # Define relationship
    buyer = db.relationship('User', back_populates='orders')
    order_items = db.relationship('OrderItem', back_populates='order')

class OrderItem(db.Model):
    __tablename__ = 'orderitem'
    order_item_id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.order_id'))
    artwork_id = db.Column(db.Integer, db.ForeignKey('artwork.artwork_id'))
    quantity = db.Column(db.Integer, nullable=False)

    # Define relationships
    order = db.relationship('Order', back_populates='order_items')
    artwork = db.relationship('Artwork', back_populates='order_items')

class Review(db.Model):
    __tablename__ = 'review'
    review_id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text, nullable=False)
    buyer_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    artwork_id = db.Column(db.Integer, db.ForeignKey('artwork.artwork_id'))

    # Define relationships
    buyer = db.relationship('User', back_populates='reviews')
    artwork = db.relationship('Artwork', back_populates='reviews')
