from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#Create a flask application
app = Flask(__name__)

#Database configurations to connect to phisecure database on mysql
app.config['SQLALCHEMY_DATABASE_URI'] = (
    'mysql+pymysql://root:my-secret-pw@172.18.8.82:3306/phisecure_db'
)

#Initialize SQlAlchemy
db = SQLAlchemy(app)


# Create a function to test the connection
def test_connection():
    ###Function that checks the connection to the phisecure database on the VM machine. ###
    try:
        with app.app_context():
            db.engine.connect()
            print("Database connection successful")
    except Exception as e:
        print(f"Error connecting to the database: {e}")

if __name__ == '__main__':
    test_connection()

