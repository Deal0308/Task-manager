--Create database table

CREATE TABLE task(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    summary VARCHAR(128),
    description TEXT,
    is_done BOOLEAN DEFAULT 0
);

--Generate some dummy data

INSERT INTO task(
    summary,
    description
) VALUES (
    "Create a task manager",
    "Create a task manager with SQLite and Lua"
),
(
    "do something",
    "do all the things"
),
(
    "Finish homework",
    "Finish homework before 11:59pm"
);

