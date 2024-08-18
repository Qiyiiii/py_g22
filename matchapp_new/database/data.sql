PRAGMA foreign_keys = ON;
-- Preload Users
INSERT INTO User (name, email, gender, location, age)
VALUES ('Qiyi', 'qiyi@rotman.com', "Male", "40202", 18);

INSERT INTO User (name, email, gender, location, age)
VALUES ('Olivia', 'oliv@rotman.com',"Female", "40202", 18);

INSERT INTO User (name, email, gender, location, age)
VALUES ('Scott', 'scott@rotman.com',"Male", "40202", 18);

INSERT INTO User (name, email, gender, location, age)
VALUES ('Bella', 'bella@rotman.com', "Female", "40202",18);

INSERT INTO User (name, email, gender, location, age)
VALUES ('Jiwon', 'jiwon@rotman.com', "Female", "40202",18);


-- Preload Actions
INSERT INTO Actions (uid1, uid2, like)
VALUES (
    (SELECT uid FROM User WHERE name = 'Qiyi'),
    (SELECT uid FROM User WHERE name = 'Olivia'),
    TRUE
);

INSERT INTO Actions (uid1, uid2, like)
VALUES (
    (SELECT uid FROM User WHERE name = 'Olivia'),
    (SELECT uid FROM User WHERE name = 'Qiyi'),
    TRUE
);

INSERT INTO Actions (uid1, uid2, like)
VALUES (
    (SELECT uid FROM User WHERE name = 'Qiyi'),
    (SELECT uid FROM User WHERE name = 'Scott'),
    TRUE
);

INSERT INTO Actions (uid1, uid2, like)
VALUES (
    (SELECT uid FROM User WHERE name = 'Scott'),
    (SELECT uid FROM User WHERE name = 'Qiyi'),
    TRUE
);
INSERT INTO Actions (uid1, uid2, like)
VALUES (
    (SELECT uid FROM User WHERE name = 'Qiyi'),
    (SELECT uid FROM User WHERE name = 'Bella'),
    TRUE
);

INSERT INTO Actions (uid1, uid2, like)
VALUES (
    (SELECT uid FROM User WHERE name = 'Bella'),
    (SELECT uid FROM User WHERE name = 'Qiyi'),
    TRUE
);


INSERT INTO Actions (uid1, uid2, like)
VALUES (
    (SELECT uid FROM User WHERE name = 'Qiyi'),
    (SELECT uid FROM User WHERE name = 'Jiwon'),
    TRUE
);
INSERT INTO Actions (uid1, uid2, like)
VALUES (
    (SELECT uid FROM User WHERE name = 'Jiwon'),
    (SELECT uid FROM User WHERE name = 'Qiyi'),
    TRUE
);

-- interest for Qiyi
INSERT INTO Interest (uid, interest) VALUES ((SELECT uid FROM User WHERE name = 'Qiyi'), 'Action & Adventure');
INSERT INTO Interest (uid, interest) VALUES ((SELECT uid FROM User WHERE name = 'Qiyi'), 'Lifestyle & Entertainment');




