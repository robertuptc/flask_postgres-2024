DROP TABLE IF EXISTS students;

CREATE TABLE students(
    id serial PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    age INT,
    grade CHAR(1)
);

-- Inserting info from CSV file to database
\COPY students FROM '/Users/robert/Documents/Software Engineer/week3/flask_postgres/data.csv' DELIMITER ',' CSV HEADER;
