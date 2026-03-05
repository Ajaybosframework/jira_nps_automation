import sqlite3

def log_email(sprint_id, email, status):

    conn = sqlite3.connect("database/email_logs.db")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS email_logs (
        sprint_id INTEGER,
        email TEXT,
        status TEXT
    )
    """)

    cursor.execute(
        "INSERT INTO email_logs VALUES (?, ?, ?)",
        (sprint_id, email, status)
    )

    conn.commit()
    conn.close()