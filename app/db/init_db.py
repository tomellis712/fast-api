from app.db.session import create_db_and_tables

if __name__ == "__main__":
    create_db_and_tables()
    print("Database initialized.")
