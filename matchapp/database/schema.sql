
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Interest;
DROP TABLE IF EXISTS Actions;
DROP TABLE IF EXISTS Coordinates;

CREATE TABLE IF NOT EXISTS User (
    uid INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(50) UNIQUE NOT NULL,
    gender VARCHAR(5) CHECK (gender IN ('Male', 'Female')),
    location VARCHAR(100) NOT NULL,
    age INTEGER CHECK (age >= 18),
    sim_weight INTEGER CHECK (sim_weight BETWEEN 1 AND 10),
    loc_weight INTEGER CHECK (loc_weight BETWEEN 1 AND 10),
    age_weight INTEGER CHECK (age_weight BETWEEN 1 AND 10)
);

CREATE TABLE IF NOT EXISTS Actions (
    uid1 INTEGER,
    uid2 INTEGER,
    like BOOLEAN NOT NULL,
    PRIMARY KEY (uid1, uid2),
    FOREIGN KEY (uid1) REFERENCES User(uid) ON DELETE CASCADE,
    FOREIGN KEY (uid2) REFERENCES User(uid) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Interest (
    uid INTEGER,
    interest VARCHAR(100) NOT NULL,
    PRIMARY KEY (uid, interest),
    FOREIGN KEY (uid) REFERENCES User(uid) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Coordinates (
    uid INTEGER,
    latitude REAL NOT NULL,
    longitude REAL NOT NULL,
    PRIMARY KEY (uid),
    FOREIGN KEY (uid) REFERENCES User(uid) ON DELETE CASCADE
);

