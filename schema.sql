CREATE TABLE IF NOT EXISTS task_manager (
    id INTEGER PRIMARY KEY,
    task TEXT NOT NULL,
    status text not NULL DEFAULT 'Pending',
    dates TEXT DEFAULT CURRENT_TIMESTAMP
);