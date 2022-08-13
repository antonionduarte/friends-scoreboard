DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS entry;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL,
  admin INTEGER NOT NULL
);

CREATE TABLE entry (
  id INTEGER,
  score INTEGER,
  user_id INTEGER,
  entry_date TIMESTAMP,
  PRIMARY KEY (id, user_id),
  FOREIGN KEY (user_id) REFERENCES user (id)
);

