CREATE DATABASE MemoraBallDB;
USE MemoraBallDB;

CREATE TABLE Sellers (
  first_name varchar(50) NOT NULL,
  last_name varchar(50) NOT NULL,
  email_address varchar(100) NOT NULL UNIQUE,
  phone_number varchar(50) NOT NULL UNIQUE,
  unit_number varchar(25),
  street_number varchar(25),
  address_name varchar(50),
  city varchar(50),
  state varchar(25),
  postal_code varchar(25),
  country varchar(50),
  seller_id integer,
  PRIMARY KEY (seller_id)
);

CREATE TABLE Buyers (
    first_name varchar(50) NOT NULL,
    last_name varchar(50) NOT NULL,
    email_address varchar(100) NOT NULL UNIQUE,
    phone_number varchar(50) NOT NULL UNIQUE,
    unit_number varchar(25),
    street_number varchar(25),
    address_name varchar(50),
    city varchar(50),
    state varchar(25),
    postal_code varchar(25),
    country varchar(50),
    buyer_id integer,
    PRIMARY KEY (buyer_id)
);

CREATE TABLE Shippers (
    first_name varchar(50) NOT NULL,
    last_name varchar(50) NOT NULL,
    email_address varchar(100) NOT NULL UNIQUE,
    phone_number varchar(50) NOT NULL UNIQUE,
    unit_number varchar(25),
    street_number varchar(25),
    address_name varchar(50),
    city varchar(50),
    state varchar(25),
    postal_code varchar(25),
    country varchar(50),
    shipper_id integer,
    PRIMARY KEY (shipper_id)
);

CREATE TABLE Teams (
    name varchar(100),
    team_id integer,
    PRIMARY KEY (team_id)
);

CREATE TABLE Products (
    name varchar(100),
    unit_price decimal(10,2),
    team_id integer,
    product_id integer,
    description varchar(200),
    sport_team varchar(100),
    PRIMARY KEY (product_id),
    FOREIGN KEY (team_id)
                      REFERENCES Teams(team_id)
);

CREATE TABLE Orders (
    seller_id integer,
    buyer_id integer,
    order_id integer,
    order_date datetime,
    shipped_date datetime,
    PRIMARY KEY (order_id),
    FOREIGN KEY (seller_id)
                    REFERENCES Sellers(seller_id),
    FOREIGN KEY (buyer_id)
                    REFERENCES Buyers(buyer_id)
);

CREATE TABLE OrderDetails (
    product_id integer,
    order_id integer,
    unit_price decimal(10,2),
    FOREIGN KEY (product_id)
                          REFERENCES Products(product_id),
    FOREIGN KEY (order_id)
                          REFERENCES Orders(order_id)
);

CREATE TABLE Shipping (
    shipper_id integer,
    order_id integer,
    shipping_id integer,
    PRIMARY KEY (shipping_id),
    FOREIGN KEY (shipper_id)
                      REFERENCES Shippers(shipper_id) ON DELETE RESTRICT,
    FOREIGN KEY (order_id)
                      REFERENCES Orders(order_id) ON DELETE RESTRICT
);

CREATE TABLE ReturnDetails (
  order_id integer,
  return_id integer,
  product_id integer,
  PRIMARY KEY (return_id),
  FOREIGN KEY (order_id)
                      REFERENCES Orders(order_id) ON DELETE RESTRICT,
  FOREIGN KEY(product_id)
                      REFERENCES Products(product_id) ON DELETE RESTRICT
);

CREATE TABLE Warehouse (
    name varchar(100) NOT NULL,
    phone_number varchar(50) NOT NULL UNIQUE,
    unit_number varchar(25),
    street_number varchar(25),
    address_name varchar(50),
    city varchar(50),
    state varchar(25),
    postal_code varchar(25),
    country varchar(50),
    warehouse_id int,
    PRIMARY KEY (warehouse_id)
);

CREATE TABLE Authenticators (
    authenticator_id integer,
    first_name varchar(50) NOT NULL,
    last_name varchar(50) NOT NULL,
    email_address varchar(100) NOT NULL UNIQUE,
    warehouse_id int,
    PRIMARY KEY (authenticator_id),
    FOREIGN KEY (warehouse_id)
                            REFERENCES Warehouse(warehouse_id)
);

CREATE TABLE Verification_Documents (
    order_id integer,
    authenticator_id integer,
    product_id integer,
    verification_id integer,
    verified BIT NOT NULL,
    PRIMARY KEY (verification_id),
    FOREIGN KEY (authenticator_id)
                            REFERENCES Authenticators(authenticator_id),
    FOREIGN KEY (order_id)
                            REFERENCES Orders(order_id)
);

CREATE TABLE Wishlist (
    product_name varchar(100),
    product_id integer,
    FOREIGN KEY (product_id)
                      REFERENCES Products(product_id)
);