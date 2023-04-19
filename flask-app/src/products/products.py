from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db


products = Blueprint('products', __name__)

# Get all the products from the database
@products.route('/products', methods=['GET'])
def get_products():
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of products
    cursor.execute('SELECT product_name, unit_price, team_id, description, product_id FROM products')

    # grab the column headers from the returned data
    column_headers = [x[0] for x in cursor.description]

    # create an empty dictionary object to use in 
    # putting column headers together with data
    json_data = []

    # fetch all the data from the cursor
    theData = cursor.fetchall()

    # for each of the rows, zip the data elements together with
    # the column headers. 
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)

# get the top 50 products from the database
@products.route('/mostExpensive', methods=['GET'])
def get_most_pop_products():
    cursor = db.get_db().cursor()
    query = '''
        SELECT product_name, unit_price, team_id, description, product_id
        FROM products
        ORDER BY unit_price DESC
        LIMIT 50
    '''
    cursor.execute(query)
       # grab the column headers from the returned data
    column_headers = [x[0] for x in cursor.description]

    # create an empty dictionary object to use in 
    # putting column headers together with data
    json_data = []

    # fetch all the data from the cursor
    theData = cursor.fetchall()

    # for each of the rows, zip the data elements together with
    # the column headers. 
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)

# get the products based on team_id from the database
@products.route('/products/<team_id>', methods=['GET'])
def get_team_products(team_id):
    cursor = db.get_db().cursor()
    cursor.execute('select * from products where team_id = {0}'.format(team_id))
       # grab the column headers from the returned data
    column_headers = [x[0] for x in cursor.description]

    # create an empty dictionary object to use in 
    # putting column headers together with data
    json_data = []

    # fetch all the data from the cursor
    theData = cursor.fetchall()

    # for each of the rows, zip the data elements together with
    # the column headers. 
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)

# get product detail with particular product_id
@products.route('/products/<product_id>', methods=['GET'])
def get_product(product_id):
    cursor = db.get_db().cursor()
    cursor.execute('select * from products where product_id = {0}'.format(product_id))
    column_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# post a new product into the database
@products.route('/product', methods=['POST'])
def post_new_product():

    the_data = request.json
    current_app.logger.info(the_data)

    name = the_data['product_name']
    price = the_data['product_price']
    team = the_data['product_team']
    description = the_data['product_description']
    
    #Constructing the query
    query = 'insert into products (product_name, unit_price, team_id, description) values ("'
    query += name + '",'
    query += str(price) + ','
    query += str(team) + ',"'
    query += description + '")'
    current_app.logger.info(query)

    # executing and committing the insert statement
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    return 'Success!'

# update product price with particular product_id
@products.route('/products/<product_id>/price', methods=['PUT'])
def put_product_price(product_id):
    the_data = request.json

    cursor = db.get_db().cursor()
    cursor.execute('update products set unit_price = {0} where product_id = {1}'.format(the_data['product_price'], product_id))
    db.get_db().commit()
    
    
    return 'Success!'


# update product descrition with particular product_id
@products.route('/products/<product_id>/description', methods=['PUT'])
def put_product_description(product_id):
    the_data = request.json

    cursor = db.get_db().cursor()
    cursor.execute('update products set description = "{0}" where product_id = {1}'.format(the_data['product_description'], product_id))
    db.get_db().commit()
    
    
    return 'Success!'


# delete a product from the database
@products.route('/products/<product_id>', methods=['DELETE'])
def delete_product(product_id):
    cursor = db.get_db().cursor()
    cursor.execute('delete from products where product_id = {0}'.format(product_id))
    column_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

