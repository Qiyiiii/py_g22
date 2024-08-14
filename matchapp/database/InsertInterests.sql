--DELETE FROM interest;
-- Mia (email: mmd158@yahoo.com)
INSERT INTO interest (uid, interest)
SELECT uid, 'Reality TV' FROM user WHERE email = 'mmd158@yahoo.com'
UNION ALL
SELECT uid, 'Comedy' FROM user WHERE email = 'mmd158@yahoo.com'
UNION ALL
SELECT uid, 'Drama' FROM user WHERE email = 'mmd158@yahoo.com';

-- Sophia (email: sophia1999@gmail.com)
INSERT INTO interest (uid, interest)
SELECT uid, 'Science Fiction & Fantasy' FROM user WHERE email = 'sophia1999@gmail.com'
UNION ALL
SELECT uid, 'Action & Adventure' FROM user WHERE email = 'sophia1999@gmail.com'
UNION ALL
SELECT uid, 'Documentary' FROM user WHERE email = 'sophia1999@gmail.com'
UNION ALL
SELECT uid, 'Thriller & Crime' FROM user WHERE email = 'sophia1999@gmail.com';

-- Beth (email: b_beth22@hotmail.com)
INSERT INTO interest (uid, interest)
SELECT uid, 'Thriller & Crime' FROM user WHERE email = 'b_beth22@hotmail.com'
UNION ALL
SELECT uid, 'Horror & Supernatural' FROM user WHERE email = 'b_beth22@hotmail.com'
UNION ALL
SELECT uid, 'Adventure' FROM user WHERE email = 'b_beth22@hotmail.com';

-- Ava (email: ava28@gmail.com)
INSERT INTO interest (uid, interest)
SELECT uid, 'Comedy' FROM user WHERE email = 'ava28@gmail.com'
UNION ALL
SELECT uid, 'Lifestyle & Entertainment' FROM user WHERE email = 'ava28@gmail.com'
UNION ALL
SELECT uid, 'Documentary' FROM user WHERE email = 'ava28@gmail.com'
UNION ALL
SELECT uid, 'Reality TV' FROM user WHERE email = 'ava28@gmail.com'
UNION ALL
SELECT uid, 'Action & Adventure' FROM user WHERE email = 'ava28@gmail.com';

-- Emily (email: e_emily25@yahoo.com)
INSERT INTO interest (uid, interest)
SELECT uid, 'Action & Adventure' FROM user WHERE email = 'e_emily25@yahoo.com'
UNION ALL
SELECT uid, 'Lifestyle & Entertainment' FROM user WHERE email = 'e_emily25@yahoo.com'
UNION ALL
SELECT uid, 'Science Fiction & Fantasy' FROM user WHERE email = 'e_emily25@yahoo.com'
UNION ALL
SELECT uid, 'Comedy' FROM user WHERE email = 'e_emily25@yahoo.com'
UNION ALL
SELECT uid, 'Thriller & Crime' FROM user WHERE email = 'e_emily25@yahoo.com';

-- Isabella (email: i_isabella24@gmail.com)
INSERT INTO interest (uid, interest)
SELECT uid, 'Historical & Period Drama' FROM user WHERE email = 'i_isabella24@gmail.com'
UNION ALL
SELECT uid, 'Lifestyle & Entertainment' FROM user WHERE email = 'i_isabella24@gmail.com'
UNION ALL
SELECT uid, 'Thriller & Crime' FROM user WHERE email = 'i_isabella24@gmail.com';

-- Charlotte (email: c_charlotte26@hotmail.com)
INSERT INTO interest (uid, interest)
SELECT uid, 'Documentary' FROM user WHERE email = 'c_charlotte26@hotmail.com'
UNION ALL
SELECT uid, 'Lifestyle & Entertainment' FROM user WHERE email = 'c_charlotte26@hotmail.com'
UNION ALL
SELECT uid, 'Reality TV' FROM user WHERE email = 'c_charlotte26@hotmail.com'
UNION ALL
SELECT uid, 'Thriller & Crime' FROM user WHERE email = 'c_charlotte26@hotmail.com'
UNION ALL
SELECT uid, 'Comedy' FROM user WHERE email = 'c_charlotte26@hotmail.com'
UNION ALL
SELECT uid, 'Adventure' FROM user WHERE email = 'c_charlotte26@hotmail.com';

-- Liam (email: l_iam29@gmail.com)
INSERT INTO interest (uid, interest)
SELECT uid, 'Science Fiction & Fantasy' FROM user WHERE email = 'l_iam29@gmail.com'
UNION ALL
SELECT uid, 'Adventure' FROM user WHERE email = 'l_iam29@gmail.com'
UNION ALL
SELECT uid, 'Lifestyle & Entertainment' FROM user WHERE email = 'l_iam29@gmail.com';

-- Noah (email: n_noah22@hotmail.com)
INSERT INTO interest (uid, interest)
SELECT uid, 'Comedy' FROM user WHERE email = 'n_noah22@hotmail.com'
UNION ALL
SELECT uid, 'Lifestyle & Entertainment' FROM user WHERE email = 'n_noah22@hotmail.com'
UNION ALL
SELECT uid, 'Horror & Supernatural' FROM user WHERE email = 'n_noah22@hotmail.com'
UNION ALL
SELECT uid, 'Documentary' FROM user WHERE email = 'n_noah22@hotmail.com'
UNION ALL
SELECT uid, 'Action & Adventure' FROM user WHERE email = 'n_noah22@hotmail.com'
UNION ALL
SELECT uid, 'Game Shows' FROM user WHERE email = 'n_noah22@hotmail.com'
UNION ALL
SELECT uid, 'Science Fiction & Fantasy' FROM user WHERE email = 'n_noah22@hotmail.com';

-- Ethan (email: e_ethan27@gmail.com)
INSERT INTO interest (uid, interest)
SELECT uid, 'Action & Adventure' FROM user WHERE email = 'e_ethan27@gmail.com'
UNION ALL
SELECT uid, 'Science Fiction & Fantasy' FROM user WHERE email = 'e_ethan27@gmail.com'
UNION ALL
SELECT uid, 'Thriller & Crime' FROM user WHERE email = 'e_ethan27@gmail.com'
UNION ALL
SELECT uid, 'Lifestyle & Entertainment' FROM user WHERE email = 'e_ethan27@gmail.com'
UNION ALL
SELECT uid, 'Superhero' FROM user WHERE email = 'e_ethan27@gmail.com';

-- Oliver (email: o_oliver24@yahoo.com)
INSERT INTO interest (uid, interest)
SELECT uid, 'Science Fiction & Fantasy' FROM user WHERE email = 'o_oliver24@yahoo.com'
UNION ALL
SELECT uid, 'Thriller & Crime' FROM user WHERE email = 'o_oliver24@yahoo.com'
UNION ALL
SELECT uid, 'Adventure' FROM user WHERE email = 'o_oliver24@yahoo.com'
UNION ALL
SELECT uid, 'Lifestyle & Entertainment' FROM user WHERE email = 'o_oliver24@yahoo.com';

-- James (email: james26@gmail.com)
INSERT INTO interest (uid, interest)
SELECT uid, 'Comedy' FROM user WHERE email = 'james26@gmail.com'
UNION ALL
SELECT uid, 'Historical & Period Drama' FROM user WHERE email = 'james26@gmail.com'
UNION ALL
SELECT uid, 'Documentary' FROM user WHERE email = 'james26@gmail.com'
UNION ALL
SELECT uid, 'Lifestyle & Entertainment' FROM user WHERE email = 'james26@gmail.com'
UNION ALL
SELECT uid, 'Science Fiction & Fantasy' FROM user WHERE email = 'james26@gmail.com'
UNION ALL
SELECT uid, 'Adventure' FROM user WHERE email = 'james26@gmail.com';

-- Benjamin (email: b_benjamin28@hotmail.com)
INSERT INTO interest (uid, interest)
SELECT uid, 'Comedy' FROM user WHERE email = 'b_benjamin28@hotmail.com'
UNION ALL
SELECT uid, 'Reality TV' FROM user WHERE email = 'b_benjamin28@hotmail.com'
UNION ALL
SELECT uid, 'Lifestyle & Entertainment' FROM user WHERE email = 'b_benjamin28@hotmail.com'
UNION ALL
SELECT uid, 'Superhero' FROM user WHERE email = 'b_benjamin28@hotmail.com'
UNION ALL
SELECT uid, 'Animated' FROM user WHERE email = 'b_benjamin28@hotmail.com';

-- Lucas (email: l_lucas24@gmail.com)
INSERT INTO interest (uid, interest)
SELECT uid, 'Science Fiction & Fantasy' FROM user WHERE email = 'l_lucas24@gmail.com'
UNION ALL
SELECT uid, 'Thriller & Crime' FROM user WHERE email = 'l_lucas24@gmail.com'
UNION ALL
SELECT uid, 'Documentary' FROM user WHERE email = 'l_lucas24@gmail.com'
UNION ALL
SELECT uid, 'Adventure' FROM user WHERE email = 'l_lucas24@gmail.com'
UNION ALL
SELECT uid, 'Horror & Supernatural' FROM user WHERE email = 'l_lucas24@gmail.com';

-- Ravi (email: ravi18@gmail.com)
INSERT INTO interest (uid, interest)
SELECT uid, 'Reality TV' FROM user WHERE email = 'ravi18@gmail.com'
UNION ALL
SELECT uid, 'Lifestyle & Entertainment' FROM user WHERE email = 'ravi18@gmail.com'
UNION ALL
SELECT uid, 'Comedy' FROM user WHERE email = 'ravi18@gmail.com'
UNION ALL
SELECT uid, 'Drama' FROM user WHERE email = 'ravi18@gmail.com'
UNION ALL
SELECT uid, 'Historical & Period Drama' FROM user WHERE email = 'ravi18@gmail.com'
UNION ALL
SELECT uid, 'Superhero' FROM user WHERE email = 'ravi18@gmail.com';

-- Kai (email: kai21@gmail.com)
INSERT INTO interest (uid, interest)
SELECT uid, 'Action & Adventure' FROM user WHERE email = 'kai21@gmail.com'
UNION ALL
SELECT uid, 'Science Fiction & Fantasy' FROM user WHERE email = 'kai21@gmail';

