-- cek citus tables
SELECT *
FROM citus_tables;

-- create table user
CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    username VARCHAR NOT NULL,
    password VARCHAR NOT NULL,
    created_at TIMESTAMP DEFAULT NOW() NOT NULL,
    updated_at TIMESTAMP DEFAULT NULL
);

-- create table categories
CREATE TABLE categories(
    id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    created_at TIMESTAMP DEFAULT NOW() NOT NULL,
    updated_at TIMESTAMP DEFAULT NULL
);

-- create table posts
CREATE TABLE posts(
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    category_id INT NOT NULL,
    title VARCHAR NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT NOW() NOT NULL,
    updated_at TIMESTAMP DEFAULT NULL
);

-- create table comments
CREATE TABLE comments(
    id SERIAL PRIMARY KEY,
    post_id INT NOT NULL,
    user_id INT NOT NULL,
    category_id INT NOT NULL,
    content VARCHAR NOT NULL,
    created_at TIMESTAMP DEFAULT NOW() NOT NULL,
    updated_at TIMESTAMP DEFAULT NULL
);

-- insert data table users
INSERT INTO users (username, password)
VALUES ('ikap', 'Ika12345'),
    ('bopu', 'Bopu09870'),
    ('chell', 'chel0102'),
    ('virli', 'vliloi0'),
    ('taki', 'taki123');

-- insert data table categories
INSERT INTO categories (name)
VALUES ('sport'),
    ('food'),
    ('drink'),
    ('holiday'),
    ('nature');

-- insert data table posts
INSERT INTO posts (user_id, category_id, title, content)
VALUES (1, 1, 'Cokelat', 'Hunting cokelat di hari libur'),
    (
        2,
        1,
        'Bermain Bulu Tangkis',
        'Bermain bulu tangkis di hari sabtu'
    ),
    (
        3,
        5,
        'Mendaki Gunung',
        'Di libur semester ini aku mendaki gunung rinjani bersama komunitas yang aku ikuti'
    ),
    (
        4,
        4,
        'Family Time Moments',
        'Aku sedang berlibur bersama keluarga hari ini'
    ),
    (
        5,
        3,
        'Es Teh',
        'Minuman favorit ku itu es teh manis'
    ),
    (
        2,
        2,
        'Bakpia dan Bolu',
        'Besok aku mau beli bakpia sama bolu siliwangi di stasiun untuk oleh-oleh pulane ke rumah'
    ),
    (
        5,
        1,
        'Pertandingan Bola',
        'Aku menonton pertandingan timnas di GBK'
    );

-- insert data table comments
INSERT INTO comments (post_id, user_id, content)
VALUES (8, 5, 'WAH aku juga suka coklat'),
(10, 1, 'Info gabung komunitas kak'),
(8, 2, 'aku juga sukaaaa'),
(14, 3, 'aku juga nonton, yu bareng'),
(14, 1, 'Info tiket'),
(14, 4, 'info tiket22');