## MemoraBall

Overview
MemoraBall is an online marketplace where sellers can sell their sports memorabilia to buyers. When a buyer makes a purchase from a seller, the listed product gets sent to the nearest MemoraBall warehouse, where an authenticator examines the product. It is the easiest way for collectors to profit off of their collection and passionate fans to get their hands on rare items without worrying about the legitimacy of the item.

3 Main Blueprints
Sellers (5 Routes):
1. get all sellers from the database
2. get details given a sellerID
3. post a new seller into the database
4. update the sellers email given a sellerID
5. delete a seller from the database 

Buyers (5 Routes):
1. get all buyers from the database
2. get details given a buyerID
3. post a new buyer
4. update buyer email given a buyerID
5. delete a buyer 

Products (8 Routes):
1. get all products from the database
2. get the top 50 products from the database
3. get the products based on team_id
4. get the product detail with particular productID
5. post a new product
6. update product price given productID
7. update product dscription given productID
8. delete a product from the database

3 Docker containers: 
1. A MySQL 8 container for obvious reasons
1. A Python Flask container to implement a REST API
1. A Local AppSmith Server

## How to setup and start the containers
**Important** - you need Docker Desktop installed

1. Clone this repository.  
1. Create a file named `db_root_password.txt` in the `secrets/` folder and put inside of it the root password for MySQL. 
1. Create a file named `db_password.txt` in the `secrets/` folder and put inside of it the password you want to use for the a non-root user named webapp. 
1. In a terminal or command prompt, navigate to the folder with the `docker-compose.yml` file.  
1. Build the images with `docker compose build`
1. Start the containers with `docker compose up`.  To run in detached mode, run `docker compose up -d`. 


LINK TO VIDEO: https://youtu.be/XLe2FVxuctE 

