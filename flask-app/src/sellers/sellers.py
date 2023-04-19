from flask import Blueprint, request, jsonify, make_response
import json
from src import db


sellers = Blueprint('sellers', __name__)

# Get all sellers from the DB
@sellers.route('/sellers', methods=['GET'])
def get_sellers():
    cursor = db.get_db().cursor()
    cursor.execute('select * from sellers')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get customer detail for customer with particular userID
@sellers.route('/sellers/<seller_ID>', methods=['GET'])
def get_customer(userID):
    cursor = db.get_db().cursor()
    cursor.execute('select * from sellers where id = {0}'.format(userID))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# post a new seller into the database
@sellers.route('/seller', methods=['POST'])
def post_new_seller():

    the_data = request.json

    first = the_data['seller_first']
    last = the_data['seller_last']
    email = the_data['seller_email']
    phone = the_data['seller_phone']
    street_number = the_data['seller_street_number']
    address = the_data['seller_address']
    suffix = the_data['seller_suffix']
    city = the_data['seller_city']
    state = the_data['seller_state']
    postal = the_data['seller_postal']
    country = the_data['seller_country']
    
    #Constructing the query
    query = 'insert into sellers (s_first, s_last, s_email, s_phone, street_number, s_address, street_suffix, city, state, postal_code, country) values ("'
    query += first + '","'
    query += last + '","'
    query += email + '","'
    query += phone + '",'
    query += str(street_number) + ',"'
    query += address + '","'
    query += suffix + '","'
    query += city + '","'
    query += state + '","'
    query += postal + '","'
    query += country + '")'

    # executing and committing the insert statement
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    return 'Success!'

# update seller email with particular seller_id
@sellers.route('/sellers/<seller_id>/email', methods=['PUT'])
def put_seller_email(seller_id):
    the_data = request.json

    cursor = db.get_db().cursor()
    cursor.execute('update sellers set s_email= {0} where seller_id = {1}'.format(the_data['seller_email'], seller_id))
    db.get_db().commit()
    
    
    return 'Success!'

# delete a seller from the database
@sellers.route('/sellers/<seller_id>', methods=['DELETE'])
def delete_seller(seller_id):
    cursor = db.get_db().cursor()
    cursor.execute('delete from sellers where seller_id = {0}'.format(seller_id))
    db.get_db().commit()
    return 'Success!'