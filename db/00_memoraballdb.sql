CREATE DATABASE MemoraBallDB;
USE MemoraBallDB;

-- table 1
CREATE TABLE Sellers (
  s_first varchar(50) NOT NULL,
  s_last varchar(50) NOT NULL,
  s_email varchar(100) NOT NULL UNIQUE,
  s_phone varchar(50) NOT NULL UNIQUE,
  street_number integer,
  s_address varchar(50),
  street_suffix varchar(25),
  city varchar(50),
  state varchar(25),
  postal_code varchar(25),
  country varchar(50),
  seller_id integer PRIMARY KEY AUTO_INCREMENT
);

-- table 2
CREATE TABLE Buyers (
    b_first varchar(50) NOT NULL,
    b_last varchar(50) NOT NULL,
    b_email varchar(100) NOT NULL UNIQUE,
    b_phone varchar(50) NOT NULL UNIQUE,
    street_number integer,
    b_address varchar(50),
    street_suffix varchar(25),
    city varchar(50),
    state varchar(25),
    postal_code varchar(25),
    country varchar(50),
    buyer_id integer PRIMARY KEY AUTO_INCREMENT
);

-- table 3
CREATE TABLE Shippers (
    shipper_name varchar(50) NOT NULL,
    email_address varchar(100) NOT NULL UNIQUE,
    phone_number varchar(50) NOT NULL UNIQUE,
    street_number integer,
    shipper_address varchar(50),
    street_suffix varchar(25),
    city varchar(50),
    state varchar(25),
    postal_code varchar(25),
    country varchar(50),
    shipper_id integer PRIMARY KEY AUTO_INCREMENT
);

-- table 4
CREATE TABLE Teams (
    team_name varchar(100),
    team_id integer PRIMARY KEY AUTO_INCREMENT
);

-- table 5
CREATE TABLE Products (
    product_name varchar(100),
    unit_price decimal(10,2),
    team_id integer,
    description varchar(200),
    product_id integer AUTO_INCREMENT,
    PRIMARY KEY (product_id),
    FOREIGN KEY (team_id)
                      REFERENCES Teams(team_id)
);

-- table 6
CREATE TABLE Orders (
    seller_id integer,
    buyer_id integer,
    order_date date,
    shipped_date date,
    product_id integer,
    order_id integer AUTO_INCREMENT,
    PRIMARY KEY (order_id),
    FOREIGN KEY (seller_id)
                    REFERENCES Sellers(seller_id),
    FOREIGN KEY (buyer_id)
                    REFERENCES Buyers(buyer_id),
    FOREIGN KEY (product_id)
                    REFERENCES Products(product_id)
);

-- table 7
CREATE TABLE Shipping (
    shipper_id integer,
    order_id integer,
    shipping_id integer AUTO_INCREMENT,
    PRIMARY KEY (shipping_id),
    FOREIGN KEY (shipper_id)
                      REFERENCES Shippers(shipper_id) ON DELETE RESTRICT,
    FOREIGN KEY (order_id)
                      REFERENCES Orders(order_id) ON DELETE RESTRICT
);

-- table 8
CREATE TABLE ReturnDetails (
  order_id integer,
  return_id integer AUTO_INCREMENT,
  PRIMARY KEY (return_id),
  FOREIGN KEY (order_id)
                      REFERENCES Orders(order_id) ON DELETE RESTRICT
);

-- table 9
CREATE TABLE Warehouse (
    w_phone varchar(50) NOT NULL UNIQUE,
    street_number varchar(25),
    w_address varchar(50),
    street_suffix varchar(25),
    city varchar(50),
    state varchar(25),
    postal_code varchar(25),
    country varchar(50),
    warehouse_id int AUTO_INCREMENT,
    PRIMARY KEY (warehouse_id)
);


-- table 10
CREATE TABLE Authenticators (
    authenticator_id integer,
    a_first varchar(50) NOT NULL,
    a_last varchar(50) NOT NULL,
    a_email varchar(100) NOT NULL UNIQUE,
    warehouse_id int AUTO_INCREMENT,
    PRIMARY KEY (authenticator_id),
    FOREIGN KEY (warehouse_id)
                            REFERENCES Warehouse(warehouse_id)
);

-- table 11
CREATE TABLE Verification_Documents (
    order_id integer,
    authenticator_id integer,
    verified BIT NOT NULL,
    verification_id integer AUTO_INCREMENT,
    PRIMARY KEY (verification_id),
    FOREIGN KEY (authenticator_id)
                            REFERENCES Authenticators(authenticator_id),
    FOREIGN KEY (order_id)
                            REFERENCES Orders(order_id)
);

-- table 12
CREATE TABLE Wishlist (
    product_id integer,
    buyer_id integer,
    FOREIGN KEY (buyer_id)
                      REFERENCES Buyers(buyer_id)
);
