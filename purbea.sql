CREATE DATABASE djangodb CHARACTER SET utf8mb4;
CREATE USER rootandres@localhost IDENTIFIED BY 'root';
GRANT ALL PRIVILEGES ON djangodb.* TO rootandres@localhost;
FLUSH PRIVILEGES;