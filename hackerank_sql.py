import mysql.connector
from datetime import datetime

def get_db_connection():
    return mysql.connector.connect(
        host="localhost", user="root", password="manigandan", database="test"
    )

def insert_submission(username, problem_slug, source_code, srclink):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = """
        INSERT INTO submissions (username, problem_slug, source_code, srclink, timestamp)
        VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(query, (username, problem_slug, source_code, srclink, datetime.now()))
    conn.commit()
    conn.close()