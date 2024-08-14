--DELETE FROM actions;

-- Insert actions where each female user likes between 0 and 5 males

-- Example for mmd158@yahoo.com (Female)
INSERT INTO actions (uid1, uid2, like)
SELECT
    (SELECT uid FROM user WHERE email = 'mmd158@yahoo.com'),
    (SELECT uid FROM user WHERE email = 'l_iam29@gmail.com'),
    1
UNION ALL
SELECT
    (SELECT uid FROM user WHERE email = 'mmd158@yahoo.com'),
    (SELECT uid FROM user WHERE email = 'n_noah22@hotmail.com'),
    1
UNION ALL
SELECT
    (SELECT uid FROM user WHERE email = 'mmd158@yahoo.com'),
    (SELECT uid FROM user WHERE email = 'e_ethan27@gmail.com'),
    1;

-- Example for sophia1999@gmail.com (Female)
INSERT INTO actions (uid1, uid2, like)
SELECT
    (SELECT uid FROM user WHERE email = 'sophia1999@gmail.com'),
    (SELECT uid FROM user WHERE email = 'o_oliver24@yahoo.com'),
    1
UNION ALL
SELECT
    (SELECT uid FROM user WHERE email = 'sophia1999@gmail.com'),
    (SELECT uid FROM user WHERE email = 'james26@gmail.com'),
    1;

-- Example for b_beth22@hotmail.com (Female)
INSERT INTO actions (uid1, uid2, like)
SELECT
    (SELECT uid FROM user WHERE email = 'b_beth22@hotmail.com'),
    (SELECT uid FROM user WHERE email = 'b_benjamin28@hotmail.com'),
    1
UNION ALL
SELECT
    (SELECT uid FROM user WHERE email = 'b_beth22@hotmail.com'),
    (SELECT uid FROM user WHERE email = 'l_lucas24@gmail.com'),
    1;

-- Example for ava28@gmail.com (Female)
INSERT INTO actions (uid1, uid2, like)
SELECT
    (SELECT uid FROM user WHERE email = 'ava28@gmail.com'),
    (SELECT uid FROM user WHERE email = 'ravi18@gmail.com'),
    1
UNION ALL
SELECT
    (SELECT uid FROM user WHERE email = 'ava28@gmail.com'),
    (SELECT uid FROM user WHERE email = 'kai21@gmail.com'),
    1;

-- Example for e_emily25@yahoo.com (Female)
INSERT INTO actions (uid1, uid2, like)
SELECT
    (SELECT uid FROM user WHERE email = 'e_emily25@yahoo.com'),
    (SELECT uid FROM user WHERE email = 'amir20@hotmail.com'),
    1
UNION ALL
SELECT
    (SELECT uid FROM user WHERE email = 'e_emily25@yahoo.com'),
    (SELECT uid FROM user WHERE email = 'dante23@gmail.com'),
    1
UNION ALL
SELECT
    (SELECT uid FROM user WHERE email = 'e_emily25@yahoo.com'),
    (SELECT uid FROM user WHERE email = 'luca22@gmail.com'),
    1;

-- Example for i_isabella24@gmail.com (Female)
INSERT INTO actions (uid1, uid2, like)
SELECT
    (SELECT uid FROM user WHERE email = 'i_isabella24@gmail.com'),
    (SELECT uid FROM user WHERE email = 'hassan19@yahoo.com'),
    1;

-- Example for c_charlotte26@hotmail.com (Female)
INSERT INTO actions (uid1, uid2, like)
SELECT
    (SELECT uid FROM user WHERE email = 'c_charlotte26@hotmail.com'),
    (SELECT uid FROM user WHERE email = 'javier25@hotmail.com'),
    1
UNION ALL
SELECT
    (SELECT uid FROM user WHERE email = 'c_charlotte26@hotmail.com'),
    (SELECT uid FROM user WHERE email = 'nico24@gmail.com'),
    1
UNION ALL
SELECT
    (SELECT uid FROM user WHERE email = 'c_charlotte26@hotmail.com'),
    (SELECT uid FROM user WHERE email = 'arjun20@gmail.com'),
    1;

-- Insert actions where each male user likes between 0 and 2 females

-- Example for l_iam29@gmail.com (Male)
INSERT INTO actions (uid1, uid2, like)
SELECT
    (SELECT uid FROM user WHERE email = 'l_iam29@gmail.com'),
    (SELECT uid FROM user WHERE email = 'mmd158@yahoo.com'),
    1
UNION ALL
SELECT
    (SELECT uid FROM user WHERE email = 'l_iam29@gmail.com'),
    (SELECT uid FROM user WHERE email = 'e_emily25@yahoo.com'),
    1;

-- Example for n_noah22@hotmail.com (Male)
INSERT INTO actions (uid1, uid2, like)
SELECT
    (SELECT uid FROM user WHERE email = 'n_noah22@hotmail.com'),
    (SELECT uid FROM user WHERE email = 'sophia1999@gmail.com'),
    1;

-- Example for e_ethan27@gmail.com (Male)
INSERT INTO actions (uid1, uid2, like)
SELECT
    (SELECT uid FROM user WHERE email = 'e_ethan27@gmail.com'),
    (SELECT uid FROM user WHERE email = 'ava28@gmail.com'),
    1;

-- Example for o_oliver24@yahoo.com (Male)
INSERT INTO actions (uid1, uid2, like)
SELECT
    (SELECT uid FROM user WHERE email = 'o_oliver24@yahoo.com'),
    (SELECT uid FROM user WHERE email = 'b_beth22@hotmail.com'),
    1;

-- Example for james26@gmail.com (Male)
INSERT INTO actions (uid1, uid2, like)
SELECT
    (SELECT uid FROM user WHERE email = 'james26@gmail.com'),
    (SELECT uid FROM user WHERE email = 'i_isabella24@gmail.com'),
    1
UNION ALL
SELECT
    (SELECT uid FROM user WHERE email = 'james26@gmail.com'),
    (SELECT uid FROM user WHERE email = 'c_charlotte26@hotmail.com'),
    1;

-- Example for b_benjamin28@hotmail.com (Male)
INSERT INTO actions (uid1, uid2, like)
SELECT
    (SELECT uid FROM user WHERE email = 'b_benjamin28@hotmail.com'),
    (SELECT uid FROM user WHERE email = 'mmd158@yahoo.com'),
    1;

-- Example for l_lucas24@gmail.com (Male)
INSERT INTO actions (uid1, uid2, like)
SELECT
    (SELECT uid FROM user WHERE email = 'l_lucas24@gmail.com'),
    (SELECT uid FROM user WHERE email = 'ava28@gmail.com'),
    1
UNION ALL
SELECT
    (SELECT uid FROM user WHERE email = 'l_lucas24@gmail.com'),
    (SELECT uid FROM user WHERE email = 'i_isabella24@gmail.com'),
    1;

-- Example for ravi18@gmail.com (Male)
INSERT INTO actions (uid1, uid2, like)
SELECT
    (SELECT uid FROM user WHERE email = 'ravi18@gmail.com'),
    (SELECT uid FROM user WHERE email = 'e_emily25@yahoo.com'),
    1;

-- Example for kai21@gmail.com (Male)
INSERT INTO actions (uid1, uid2, like)
SELECT
    (SELECT uid FROM user WHERE email = 'kai21@gmail.com'),
    (SELECT uid FROM user WHERE email = 'b_beth22@hotmail.com'),
    1;

-- Example for amir20@gmail.com (Male)
INSERT INTO actions (uid1, uid2, like)
SELECT
    (SELECT uid FROM user WHERE email = 'amir20@gmail.com'),
    (SELECT uid FROM user WHERE email = 'sophia1999@gmail.com'),
    1;

-- Example for dante23@gmail.com (Male)
INSERT INTO actions (uid1, uid2, like)
SELECT
    (SELECT uid FROM user WHERE email = 'dante23@gmail.com'),
    (SELECT uid FROM user WHERE email = 'c_charlotte26@hotmail.com'),
    1;

-- Example for luca22@gmail.com (Male)
INSERT INTO actions (uid1, uid2, like)
SELECT
    (SELECT uid FROM user WHERE email = 'luca22@gmail.com'),
    (SELECT uid FROM user WHERE email = 'b_beth22@hotmail.com'),
    1;

-- Example for hassan19@yahoo.com (Male)
INSERT INTO actions (uid1, uid2, like)
SELECT
    (SELECT uid FROM user WHERE email = 'hassan19@yahoo.com'),
    (SELECT uid FROM user WHERE email = 'e_emily25@yahoo.com'),
    1;

-- Example for javier25@hotmail.com (Male)
INSERT INTO actions (uid1, uid2, like)
SELECT
    (SELECT uid FROM user WHERE email = 'javier25@hotmail.com'),
    (SELECT uid FROM user WHERE email = 'ava28@gmail.com'),
    1;

-- Example for nico24@gmail.com (Male)
INSERT INTO actions (uid1, uid2, like)
SELECT
    (SELECT uid FROM user WHERE email = 'nico24@gmail.com'),
    (SELECT uid FROM user WHERE email = 'i_isabella24@gmail.com'),
    1;

-- Insert dislikes where each female user dislikes between 0 and 2 males they haven't liked

-- Example for mmd158@yahoo.com (Female)
INSERT INTO actions (uid1, uid2, like)
SELECT
    (SELECT uid FROM user WHERE email = 'mmd158@yahoo.com'),
    (SELECT uid FROM user WHERE email = 'ravi18@gmail.com'),
    0
UNION ALL
SELECT
    (SELECT uid FROM user WHERE email = 'mmd158@yahoo.com'),
    (SELECT uid FROM user WHERE email = 'kai21@gmail.com'),
    0;

-- Example for sophia1999@gmail.com (Female)
INSERT INTO actions (uid1, uid2, like)
SELECT
    (SELECT uid FROM user WHERE email = 'sophia1999@gmail.com'),
    (SELECT uid FROM user WHERE email = 'b_benjamin28@hotmail.com'),
    0
UNION ALL
SELECT
    (SELECT uid FROM user WHERE email = 'sophia1999@gmail.com'),
    (SELECT uid FROM user WHERE email = 'l_lucas24@gmail.com'),
    0;

-- Example for b_beth22@hotmail.com (Female)
INSERT INTO actions (uid1, uid2, like)
SELECT
    (SELECT uid FROM user WHERE email = 'b_beth22@hotmail.com'),
    (SELECT uid FROM user WHERE email = 'javier25@hotmail.com'),
    0;

-- Example for ava28@gmail.com (Female)
INSERT INTO actions (uid1, uid2, like)
SELECT
    (SELECT uid FROM user WHERE email = 'ava28@gmail.com'),
    (SELECT uid FROM user WHERE email = 'luca22@gmail.com'),
    0
UNION ALL
SELECT
    (SELECT uid FROM user WHERE email = 'ava28@gmail.com'),
    (SELECT uid FROM user WHERE email = 'hassan19@yahoo.com'),
    0;

-- Example for i_isabella24@gmail.com (Female)
INSERT INTO actions (uid1, uid2, like)
SELECT
    (SELECT uid FROM user WHERE email = 'i_isabella24@gmail.com'),
    (SELECT uid FROM user WHERE email = 'l_iam29@gmail.com'),
    0;

-- Example for c_charlotte26@hotmail.com (Female)
INSERT INTO actions (uid1, uid2, like)
SELECT
    (SELECT uid FROM user WHERE email = 'c_charlotte26@hotmail.com'),
    (SELECT uid FROM user WHERE email = 'e_ethan27@gmail.com'),
    0
UNION ALL
SELECT
    (SELECT uid FROM user WHERE email = 'c_charlotte26@hotmail.com'),
    (SELECT uid FROM user WHERE email = 'n_noah22@hotmail.com'),
    0;

-- Insert dislikes where each male user dislikes between 0 and 2 females they haven't liked

-- Example for l_iam29@gmail.com (Male)
INSERT INTO actions (uid1, uid2, like)
SELECT
    (SELECT uid FROM user WHERE email = 'l_iam29@gmail.com'),
    (SELECT uid FROM user WHERE email = 'b_beth22@hotmail.com'),
    0
UNION ALL
SELECT
    (SELECT uid FROM user WHERE email = 'l_iam29@gmail.com'),
    (SELECT uid FROM user WHERE email = 'i_isabella24@gmail.com'),
    0;

-- Example for n_noah22@hotmail.com (Male)
INSERT INTO actions (uid1, uid2, like)
SELECT
    (SELECT uid FROM user WHERE email = 'n_noah22@hotmail.com'),
    (SELECT uid FROM user WHERE email = 'mmd158@yahoo.com'),
    0;

-- Example for e_ethan27@gmail.com (Male)
INSERT INTO actions (uid1, uid2, like)
SELECT
    (SELECT uid FROM user WHERE email = 'e_ethan27@gmail.com'),
    (SELECT uid FROM user WHERE email = 'sophia1999@gmail.com'),
    0;



-- Example for james26@gmail.com (Male)
INSERT INTO actions (uid1, uid2, like)
SELECT
    (SELECT uid FROM user WHERE email = 'james26@gmail.com'),
    (SELECT uid FROM user WHERE email = 'e_emily25@yahoo.com'),
    0;

-- Example for b_benjamin28@hotmail.com (Male)
INSERT INTO actions (uid1, uid2, like)
SELECT
    (SELECT uid FROM user WHERE email = 'b_benjamin28@hotmail.com'),
    (SELECT uid FROM user WHERE email = 'ava28@gmail.com'),
    0;

-- Example for l_lucas24@gmail.com (Male)
INSERT INTO actions (uid1, uid2, like)
SELECT
    (SELECT uid FROM user WHERE email = 'l_lucas24@gmail.com'),
    (SELECT uid FROM user WHERE email = 'mmd158@yahoo.com'),
    0;

-- Example for ravi18@gmail.com (Male)
INSERT INTO actions (uid1, uid2, like)
SELECT
    (SELECT uid FROM user WHERE email = 'ravi18@gmail.com'),
    (SELECT uid FROM user WHERE email = 'sophia1999@gmail.com'),
    0;

-- Example for kai21@gmail.com (Male)
INSERT INTO actions (uid1, uid2, like)
SELECT
    (SELECT uid FROM user WHERE email = 'kai21@gmail.com'),
    (SELECT uid FROM user WHERE email = 'e_emily25@yahoo.com'),
    0;

-- Example for amir20@gmail.com (Male)
INSERT INTO actions (uid1, uid2, like)
SELECT
    (SELECT uid FROM user WHERE email = 'amir20@gmail.com'),
    (SELECT uid FROM user WHERE email = 'b_beth22@hotmail.com'),
    0;

-- Example for dante23@gmail.com (Male)
INSERT INTO actions (uid1, uid2, like)
SELECT
    (SELECT uid FROM user WHERE email = 'dante23@gmail.com'),
    (SELECT uid FROM user WHERE email = 'i_isabella24@gmail.com'),
    0;

-- Example for luca22@gmail.com (Male)
INSERT INTO actions (uid1, uid2, like)
SELECT
    (SELECT uid FROM user WHERE email = 'luca22@gmail.com'),
    (SELECT uid FROM user WHERE email = 'c_charlotte26@hotmail.com'),
    0;

-- Example for hassan19@yahoo.com (Male)
INSERT INTO actions (uid1, uid2, like)
SELECT
    (SELECT uid FROM user WHERE email = 'hassan19@yahoo.com'),
    (SELECT uid FROM user WHERE email = 'sophia1999@gmail.com'),
    0;
