-- Insert entries if they don't already exist
INSERT INTO user (name, email, gender, age, sim_weight, loc_weight, age_weight)
SELECT 'Mia', 'mmd158@yahoo.com', 'Female', 22, 10, 10, 5
WHERE NOT EXISTS (SELECT 1 FROM user WHERE email = 'mmd158@yahoo.com');

INSERT INTO user (name, email, gender, age, sim_weight, loc_weight, age_weight)
SELECT 'Sophia', 'sophia1999@gmail.com', 'Female', 25, 10, 10, 5
WHERE NOT EXISTS (SELECT 1 FROM user WHERE email = 'sophia1999@gmail.com');

INSERT INTO user (name, email, gender, age, sim_weight, loc_weight, age_weight)
SELECT 'Beth', 'b_beth22@hotmail.com', 'Female', 22, 10, 10, 5
WHERE NOT EXISTS (SELECT 1 FROM user WHERE email = 'b_beth22@hotmail.com');

INSERT INTO user (name, email, gender, age, sim_weight, loc_weight, age_weight)
SELECT 'Ava', 'ava28@gmail.com', 'Female', 28, 10, 10, 5
WHERE NOT EXISTS (SELECT 1 FROM user WHERE email = 'ava28@gmail.com');

INSERT INTO user (name, email, gender, age, sim_weight, loc_weight, age_weight)
SELECT 'Emily', 'e_emily25@yahoo.com', 'Female', 25, 10, 10, 5
WHERE NOT EXISTS (SELECT 1 FROM user WHERE email = 'e_emily25@yahoo.com');

INSERT INTO user (name, email, gender, age, sim_weight, loc_weight, age_weight)
SELECT 'Isabella', 'i_isabella24@gmail.com', 'Female', 24, 10, 10, 5
WHERE NOT EXISTS (SELECT 1 FROM user WHERE email = 'i_isabella24@gmail.com');

INSERT INTO user (name, email, gender, age, sim_weight, loc_weight, age_weight)
SELECT 'Charlotte', 'c_charlotte26@hotmail.com', 'Female', 26, 10, 10, 5
WHERE NOT EXISTS (SELECT 1 FROM user WHERE email = 'c_charlotte26@hotmail.com');

INSERT INTO user (name, email, gender, age, sim_weight, loc_weight, age_weight)
SELECT 'Liam', 'l_iam29@gmail.com', 'Male', 29, 10, 10, 5
WHERE NOT EXISTS (SELECT 1 FROM user WHERE email = 'l_iam29@gmail.com');

INSERT INTO user (name, email, gender, age, sim_weight, loc_weight, age_weight)
SELECT 'Noah', 'n_noah22@hotmail.com', 'Male', 22, 10, 10, 5
WHERE NOT EXISTS (SELECT 1 FROM user WHERE email = 'n_noah22@hotmail.com');

INSERT INTO user (name, email, gender, age, sim_weight, loc_weight, age_weight)
SELECT 'Ethan', 'e_ethan27@gmail.com', 'Male', 27, 10, 10, 5
WHERE NOT EXISTS (SELECT 1 FROM user WHERE email = 'e_ethan27@gmail.com');

INSERT INTO user (name, email, gender, age, sim_weight, loc_weight, age_weight)
SELECT 'Oliver', 'o_oliver24@yahoo.com', 'Male', 24, 10, 10, 5
WHERE NOT EXISTS (SELECT 1 FROM user WHERE email = 'o_oliver24@yahoo.com');

INSERT INTO user (name, email, gender, age, sim_weight, loc_weight, age_weight)
SELECT 'James', 'james26@gmail.com', 'Male', 26, 10, 10, 5
WHERE NOT EXISTS (SELECT 1 FROM user WHERE email = 'james26@gmail.com');

INSERT INTO user (name, email, gender, age, sim_weight, loc_weight, age_weight)
SELECT 'Benjamin', 'b_benjamin28@hotmail.com', 'Male', 28, 10, 10, 5
WHERE NOT EXISTS (SELECT 1 FROM user WHERE email = 'b_benjamin28@hotmail.com');

INSERT INTO user (name, email, gender, age, sim_weight, loc_weight, age_weight)
SELECT 'Lucas', 'l_lucas24@gmail.com', 'Male', 24, 10, 10, 5
WHERE NOT EXISTS (SELECT 1 FROM user WHERE email = 'l_lucas24@gmail.com');

INSERT INTO user (name, email, gender, age, sim_weight, loc_weight, age_weight)
SELECT 'Ravi', 'ravi18@gmail.com', 'Male', 18, 10, 10, 5
WHERE NOT EXISTS (SELECT 1 FROM user WHERE email = 'ravi18@gmail.com');

INSERT INTO user (name, email, gender, age, sim_weight, loc_weight, age_weight)
SELECT 'Kai', 'kai21@gmail.com', 'Male', 21, 10, 10, 5
WHERE NOT EXISTS (SELECT 1 FROM user WHERE email = 'kai21@gmail.com');

INSERT INTO user (name, email, gender, age, sim_weight, loc_weight, age_weight)
SELECT 'Amir', 'amir20@hotmail.com', 'Male', 20, 10, 10, 5
WHERE NOT EXISTS (SELECT 1 FROM user WHERE email = 'amir20@hotmail.com');

INSERT INTO user (name, email, gender, age, sim_weight, loc_weight, age_weight)
SELECT 'Dante', 'dante23@gmail.com', 'Male', 23, 10, 10, 5
WHERE NOT EXISTS (SELECT 1 FROM user WHERE email = 'dante23@gmail.com');

INSERT INTO user (name, email, gender, age, sim_weight, loc_weight, age_weight)
SELECT 'Luca', 'luca22@gmail.com', 'Male', 22, 10, 10, 5
WHERE NOT EXISTS (SELECT 1 FROM user WHERE email = 'luca22@gmail.com');

INSERT INTO user (name, email, gender, age, sim_weight, loc_weight, age_weight)
SELECT 'Hassan', 'hassan19@yahoo.com', 'Male', 19, 10, 10, 5
WHERE NOT EXISTS (SELECT 1 FROM user WHERE email = 'hassan19@yahoo.com');

INSERT INTO user (name, email, gender, age, sim_weight, loc_weight, age_weight)
SELECT 'Javier', 'javier25@hotmail.com', 'Male', 25, 10, 10, 5
WHERE NOT EXISTS (SELECT 1 FROM user WHERE email = 'javier25@hotmail.com');

INSERT INTO user (name, email, gender, age, sim_weight, loc_weight, age_weight)
SELECT 'Nico', 'nico24@gmail.com', 'Male', 24, 10, 10, 5
WHERE NOT EXISTS (SELECT 1 FROM user WHERE email = 'nico24@gmail.com');

INSERT INTO user (name, email, gender, age, sim_weight, loc_weight, age_weight)
SELECT 'Arjun', 'arjun20@gmail.com', 'Male', 20, 10, 10, 5
WHERE NOT EXISTS (SELECT 1 FROM user WHERE email = 'arjun20@gmail.com');

INSERT INTO user (name, email, gender, age, sim_weight, loc_weight, age_weight)
SELECT 'Ibrahim', 'ibrahim18@hotmail.com', 'Male', 18, 10, 10, 5
WHERE NOT EXISTS (SELECT 1 FROM user WHERE email = 'ibrahim18@hotmail.com');
