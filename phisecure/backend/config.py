# backend/config.py

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:my-secret-pw@172.18.8.82:3306/phisecure_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
