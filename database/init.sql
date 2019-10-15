CREATE DATABASE fibbonaci;
use fibbonaci;

CREATE TABLE fibbonaci_numbers (
    number_id INT,
    title VARCHAR(255) NOT NULL
);

INSERT INTO fibbonaci_numbers
  (number_id, title)
VALUES
  ('1', 'blue'),
  ('2', 'yellow');