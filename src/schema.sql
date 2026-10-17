CREATE TABLE IF NOT EXISTS task_manager (
    id INTEGER PRIMARY KEY,
    task TEXT NOT NULL,
    status Text not NULL DEFAULT 'Pending',
    dates TEXT DEFAULT CURRENT_TIMESTAMP
);

-- import sqlite3

-- with sqlite3.connect("Task.db") as connection:
--     cursor = connection.cursor()
--     cursor.execute("""
--         CREATE TABLE IF NOT EXISTS task_manager (
--             id INTEGER PRIMARY KEY ,
--             task TEXT NOT NULL,
--             status Text Not null,
--             dates TEXT DEFAULT CURRENT_TIMESTAMP
--         ) if you want to try without schema
--     """)
