# backend/config.py

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:my-secret-pw@172.18.8.82:3306/phisecure_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestConfig(Config):
    """
    Configuration for Flask testing.
    
    This class overrides config settings for testing purposes. 
    It uses an in-memory SQLITE database to ensure
    that tests do not affect dev database

    Args:
        Config (class): The base configuration with common settings for testing. 
        TestConfig inherits from `Config` and changes specific settings for tests.

    """
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # Use SQLite in-memory for tests
    TESTING = True