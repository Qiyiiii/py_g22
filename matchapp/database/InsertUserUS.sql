-- Insert entries if they don't already exist
INSERT INTO user (name, email, gender, location, age)
SELECT 'Mia', 'mmd158@yahoo.com', 'Female', '10001', 22
WHERE NOT EXISTS (SELECT 1 FROM user WHERE email = 'mmd158@yahoo.com');

INSERT INTO user (name, email, gender, location, age)
SELECT 'Sophia', 'sophia1999@gmail.com', 'Female', '10002', 25
WHERE NOT EXISTS (SELECT 1 FROM user WHERE email = 'sophia1999@gmail.com');

INSERT INTO user (name, email, gender, location, age)
SELECT 'Beth', 'b_beth22@hotmail.com', 'Female', '10003', 22
WHERE NOT EXISTS (SELECT 1 FROM user WHERE email = 'b_beth22@hotmail.com');

INSERT INTO user (name, email, gender, location, age)
SELECT 'Ava', 'ava28@gmail.com', 'Female', '10004', 28
WHERE NOT EXISTS (SELECT 1 FROM user WHERE email = 'ava28@gmail.com');

INSERT INTO user (name, email, gender, location, age)
SELECT 'Emily', 'e_emily25@yahoo.com', 'Female', '10005', 25
WHERE NOT EXISTS (SELECT 1 FROM user WHERE email = 'e_emily25@yahoo.com');

INSERT INTO user (name, email, gender, location, age)
SELECT 'Isabella', 'i_isabella24@gmail.com', 'Female', '10006', 24
WHERE NOT EXISTS (SELECT 1 FROM user WHERE email = 'i_isabella24@gmail.com');

INSERT INTO user (name, email, gender, location, age)
SELECT 'Charlotte', 'c_charlotte26@hotmail.com', 'Female', '10007', 26
WHERE NOT EXISTS (SELECT 1 FROM user WHERE email = 'c_charlotte26@hotmail.com');

INSERT INTO user (name, email, gender, location, age)
SELECT 'Liam', 'l_iam29@gmail.com', 'Male', '10008', 29
WHERE NOT EXISTS (SELECT 1 FROM user WHERE email = 'l_iam29@gmail.com');

INSERT INTO user (name, email, gender, location, age)
SELECT 'Noah', 'n_noah22@hotmail.com', 'Male', '10009', 22
WHERE NOT EXISTS (SELECT 1 FROM user WHERE email = 'n_noah22@hotmail.com');

INSERT INTO user (name, email, gender, location, age)
SELECT 'Ethan', 'e_ethan27@gmail.com', 'Male', '10010', 27
WHERE NOT EXISTS (SELECT 1 FROM user WHERE email = 'e_ethan27@gmail.com');

INSERT INTO user (name, email, gender, location, age)
SELECT 'Oliver', 'o_oliver24@yahoo.com', 'Male', '10011', 24
WHERE NOT EXISTS (SELECT 1 FROM user WHERE email = 'o_oliver24@yahoo.com');

INSERT INTO user (name, email, gender, location, age)
SELECT 'James', 'james26@gmail.com', 'Male', '10012', 26
WHERE NOT EXISTS (SELECT 1 FROM user WHERE email = 'james26@gmail.com');

INSERT INTO user (name, email, gender, location, age)
SELECT 'Benjamin', 'b_benjamin28@hotmail.com', 'Male', '10013', 28
WHERE NOT EXISTS (SELECT 1 FROM user WHERE email = 'b_benjamin28@hotmail.com');

INSERT INTO user (name, email, gender, location, age)
SELECT 'Lucas', 'l_lucas24@gmail.com', 'Male', '10014', 24
WHERE NOT EXISTS (SELECT 1 FROM user WHERE email = 'l_lucas24@gmail.com');

INSERT INTO user (name, email, gender, location, age)
SELECT 'Ravi', 'ravi18@gmail.com', 'Male', '10015', 18
WHERE NOT EXISTS (SELECT 1 FROM user WHERE email = 'ravi18@gmail.com');

INSERT INTO user (name, email, gender, location, age)
SELECT 'Kai', 'kai21@gmail.com', 'Male', '10016', 21
WHERE NOT EXISTS (SELECT 1 FROM user WHERE email = 'kai21@gmail.com');

INSERT INTO user (name, email, gender, location, age)
SELECT 'Amir', 'amir20@hotmail.com', 'Male', '10017', 20
WHERE NOT EXISTS (SELECT 1 FROM user WHERE email = 'amir20@hotmail.com');

INSERT INTO user (name, email, gender, location, age)
SELECT 'Dante', 'dante23@gmail.com', 'Male', '10018', 23
WHERE NOT EXISTS (SELECT 1 FROM user WHERE email = 'dante23@gmail.com');

INSERT INTO user (name, email, gender, location, age)
SELECT 'Luca', 'luca22@gmail.com', 'Male', '10019', 22
WHERE NOT EXISTS (SELECT 1 FROM user WHERE email = 'luca22@gmail.com');

INSERT INTO user (name, email, gender, location, age)
SELECT 'Hassan', 'hassan19@yahoo.com', 'Male', '10020', 19
WHERE NOT EXISTS (SELECT 1 FROM user WHERE email = 'hassan19@yahoo.com');

INSERT INTO user (name, email, gender, location, age)
SELECT 'Javier', 'javier25@hotmail.com', 'Male', '10021', 25
WHERE NOT EXISTS (SELECT 1 FROM user WHERE email = 'javier25@hotmail.com');

INSERT INTO user (name, email, gender, location, age)
SELECT 'Nico', 'nico24@gmail.com', 'Male', '10022', 24
WHERE NOT EXISTS (SELECT 1 FROM user WHERE email = 'nico24@gmail.com');

INSERT INTO user (name, email, gender, location, age)
SELECT 'Arjun', 'arjun20@gmail.com', 'Male', '10023', 20
WHERE NOT EXISTS (SELECT 1 FROM user WHERE email = 'arjun20@gmail.com');

INSERT INTO user (name, email, gender, location, age)
SELECT 'Ibrahim', 'ibrahim18@hotmail.com', 'Male', '10024', 18
WHERE NOT EXISTS (SELECT 1 FROM user WHERE email = 'ibrahim18@hotmail.com');
