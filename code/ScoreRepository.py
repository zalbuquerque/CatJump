import sqlite3
from code.decorators import log_action


class ScoreRepository:
    def __init__(self, db_name='travessia.db'):
        self.db_name = db_name
        self.create_table()

    def connect(self):
        return sqlite3.connect(self.db_name)

    def create_table(self):
        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS scores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                mode TEXT NOT NULL,
                level INTEGER NOT NULL,
                time_left INTEGER NOT NULL
            )
        """)

        conn.commit()
        conn.close()

    @log_action
    def save_score(self, mode, level, time_left):
        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO scores (mode, level, time_left) VALUES (?, ?, ?)",
            (mode, level, time_left)
        )

        conn.commit()
        conn.close()

    def get_top_scores(self, limit=5):
        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT mode, level, time_left
            FROM scores
            ORDER BY level DESC, time_left DESC
            LIMIT ?
        """, (limit,))

        rows = cursor.fetchall()
        conn.close()
        return rows