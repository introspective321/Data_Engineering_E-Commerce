import os
class Config:
    SECRET_KEY = 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:DataE*99@localhost/art_ecommerce'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'static/images')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # Max file size 16MB
