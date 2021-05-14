/*
    whatabook
    Ricardo Guillen Vergara
    5/1/2021
    WhatABook database creation with tables and inserting of data into tables
*/

-- create whatabook database and show all databases
CREATE DATABASE whatabook;
SHOW DATABASES;


-- drop test user if exists 
DROP USER IF EXISTS 'whatabook_user'@'localhost';

-- create whatabook_user and grant them all privileges to the whatabook database 
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

-- grant all privileges to the whatabook database to user whatabook_user on localhost 
GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

-- drop contstraints if they exist
ALTER TABLE wishlist DROP FOREIGN KEY fk_book;
ALTER TABLE wishlist DROP FOREIGN KEY fk_user;

-- drop tables if they exist
-- drop wishlist table first or the FK constraints may not allow you to drop book and user tables
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS user;

/*
    Create table(s)
*/
CREATE TABLE store (
    store_id    INT             NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);

CREATE TABLE book (
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    author      VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    PRIMARY KEY(book_id)
);

CREATE TABLE user (
    user_id         INT         NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75) NOT NULL,
    last_name       VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id) 
);

CREATE TABLE wishlist (
    wishlist_id     INT         NOT NULL    AUTO_INCREMENT,
    user_id         INT         NOT NULL,
    book_id         INT         NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_Id)
);

/*
    insert store records 
*/
INSERT INTO store(locale)
    VALUES('1313 Harbor Blvd, Anaheim, CA 92802');

/*
    insert book records 
*/
INSERT INTO book(book_name, author, details)
    VALUES('Cien Anos De Soledad', 'Gabriel Garcia Marquez', 'Version in Spanish');

INSERT INTO book(book_name, author, details)
    VALUES('A Hundred Years of Solitude', 'Gabriel Garcia Marquez', 'Version in English');

INSERT INTO book(book_name, author, details)
    VALUES("Maradona: The Autobiography of Soccer's Greatest and Most Controversial Star", 'Diego Armando Maradona', 'Paperback version and afterword by Mark Weinstein');

INSERT INTO book(book_name, author, details)
    VALUES('Pele: The Autobiography', 'Pele', 'Paperback version - English Version');

INSERT INTO book(book_name, author, details)
    VALUES('Harry Potter and the Order of the Phoenix', 'J.K Rowling', 'Hardcover-Unabridged, January 1, 2003 - UK Version');

INSERT INTO book(book_name, author, details)
    VALUES('Puppet Planet', 'Rita Turvey', 'A coworker wrote this book-buy it if you can please');

INSERT INTO book(book_name, author, details)
    VALUES('Siddhartha', 'Hermann Hesse','World Classics Unabridged');

INSERT INTO book(book_name, author, details)
    VALUES('The Alchemist, 25th Anniversary: A Fable About Following Your Dream', 'Paulo Coelho', 'Paperback-Deckle Edge, April 15, 2014');

INSERT INTO book(book_name, author, details)
    VALUES('Dragon Ball, Vol. 1', 'Akira Toriyama', 'Paperback - March 1, 2003');

/*
    insert user records
*/ 
INSERT INTO user(first_name, last_name) 
    VALUES('kakaroto', 'Goku');

INSERT INTO user(first_name, last_name)
    VALUES('Vegeta', 'Prince');

INSERT INTO user(first_name, last_name)
    VALUES('Seya', 'Saint');

/*
    insert wishlist records 
*/
INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE last_name = 'Goku'), 
        (SELECT book_id FROM book WHERE book_name = 'Harry Potter and the Order of the Phoenix')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Vegeta'),
        (SELECT book_id FROM book WHERE book_name = 'Cien Anos De Soledad')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Seya'),
        (SELECT book_id FROM book WHERE author = 'Rita Turvey')
    );
