from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def check_db_connection():
    try:
        # check connection
        db.session.execute('SELECT 1')
    except Exception as e:
        raise Exception(f"Database connection error: {str(e)}")

