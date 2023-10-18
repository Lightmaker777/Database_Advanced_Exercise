-- Create the database
CREATE DATABASE clients_db;

-- Use the database
USE clients_db;

-- Create the clients table
CREATE TABLE clients (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL
);

-- Create the products table
CREATE TABLE products (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  price DECIMAL(10,2) NOT NULL
);

-- Insert some data into the clients table
INSERT INTO clients (name) VALUES
  ('Alice'),
  ('Bob'),
  ('Carol');

-- Insert some data into the products table
INSERT INTO products (name, price) VALUES
  ('Product 1', 100.00),
  ('Product 2', 200.00),
  ('Product 3', 300.00);