from flask import Blueprint, request, jsonify, make_response
import json
from src import db


buyers = Blueprint('buyers', __name__)

# Get all buyers from the DB
@buyers.route('/buyers', methods=['GET'])
def get_buyers():
    cursor = db.get_db().cursor()
    cursor.execute('select * from buyers')
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
@buyers.route('/buyers/<buyer_id>', methods=['GET'])
def get_customer(buyer_id):
    cursor = db.get_db().cursor()
    cursor.execute('select * from buyers where buyer_id = {0}'.format(buyer_id))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# post a new buyer into the database
@buyers.route('/buyer', methods=['POST'])
def post_new_buyer():

    the_data = request.json

    first = the_data['buyer_first']
    last = the_data['buyer_last']
    email = the_data['buyer_email']
    phone = the_data['buyer_phone']
    street_number = the_data['buyer_street_number']
    address = the_data['buyer_address']
    suffix = the_data['buyer_suffix']
    city = the_data['buyer_city']
    state = the_data['buyer_state']
    postal = the_data['buyer_postal']
    country = the_data['buyer_country']
    
    #Constructing the query
    query = 'insert into buyers (b_first, b_last, b_email, b_phone, street_number, b_address, street_suffix, city, state, postal_code, country) values ("'
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

# update buyer email with particular buyer_id
@buyers.route('/buyers/<buyer_id>/email', methods=['PUT'])
def put_buyer_email(buyer_id):
    the_data = request.json

    cursor = db.get_db().cursor()
    cursor.execute('update buyers set s_email= {0} where buyer_id = {1}'.format(the_data['buyer_email'], buyer_id))
    db.get_db().commit()
    
    
    return 'Success!'

# delete a buyer from the database
@buyers.route('/buyers/<buyer_id>', methods=['DELETE'])
def delete_buyer(buyer_id):
    cursor = db.get_db().cursor()
    cursor.execute('delete from buyers where buyer_id = {0}'.format(buyer_id))
    db.get_db().commit()
    return 'Success!'