import mysql.connector
from mysql.connector import Error
from config import Config

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host=Config.MYSQL_HOST,
            user=Config.MYSQL_USER,
            password=Config.MYSQL_PASSWORD,
            database=Config.MYSQL_DB
        )
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

def init_db():
    """Initializes the database via schema.sql script."""
    # Connect without DB first to create it if not exists
    try:
        conn = mysql.connector.connect(
            host=Config.MYSQL_HOST,
            user=Config.MYSQL_USER,
            password=Config.MYSQL_PASSWORD
        )
        cursor = conn.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {Config.MYSQL_DB}")
        conn.close()
        
        # Now connect to the DB and run schema
        conn = get_db_connection()
        if conn:
            cursor = conn.cursor()
            with open('schema.sql', 'r') as f:
                # Split commands by semicolon for execution
                schema = f.read()
                commands = schema.split(';')
                for command in commands:
                    if command.strip():
                        cursor.execute(command)
            conn.commit()
            cursor.close()
            conn.close()
            print("Database initialized successfully.")
    except Error as e:
        print(f"Failed to initialize database: {e}")
