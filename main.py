from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
    {"id": 1, "name": "Raghav", "age": 25, "city": "Mumbai"},
    {"id": 2, "name": "Janaki", "age": 30, "city": "Bangalore"},
    {"id": 3, "name": "Bhajrang", "age": 40, "city": "Chennai"},
    {"id": 4, "name": "Mohan", "age": 50, "city": "london"},
    {"id": 5, "name": "Rudra", "age": 35, "city": "Freiburg"},
    # Additional user data can be added here
]


# GET request
@app.route('/api/users', methods=['GET'])
def get_users():
    filtered_users = users

    # Filtering capability

    # Checks the name and city input for filtering and raises and exception from server side (5xx) if there is any
    try:
        # Filter by name
        name = request.args.get('name')
        if name:
            filtered_users = [user for user in filtered_users if user['name'].lower() == name.lower()]
            if not filtered_users:
                return {'message': 'Name not found for user'}

        # Filter by city
        city = request.args.get('city')
        if city:
            filtered_users = [user for user in filtered_users if user['city'].lower() == city.lower()]
            if not filtered_users:
                return {'message': 'city not found for user'}

    except Exception as e:
        return {'message': str(e)}, 500

    # Filter by id - Gives an error message if the ID is invalid.
    # The response code is 4xx since it is a client side error
    try:
        id = request.args.get('id')
        if id:
            filtered_users = [user for user in filtered_users if user['id'] == int(id)]
            if not filtered_users:
                return {'message': 'ID not found for user'}

    except ValueError:
        return {'message': 'Invalid ID'}, 400

    # Gives an error message if the AGE input is invalid. The response code is 4xx since it is a client side error
    try:
        # Filter by age
        age = request.args.get('age')
        if age:
            filtered_users = [user for user in filtered_users if user['age'] == int(age)]
            if not filtered_users:
                return {'message': 'AGE not found for user'}

        # Filter by age greater than
        age_gr = request.args.get('age_gr')
        if age_gr:
            filtered_users = [user for user in filtered_users if user['age'] > int(age_gr)]

        # Filter by age less than
        age_less = request.args.get('age_less')
        if age_less:
            filtered_users = [user for user in filtered_users if user['age'] < int(age_less)]

        # Filter by age greater than or equal to
        age_greq = request.args.get('age_greq')
        if age_greq:
            filtered_users = [user for user in filtered_users if user['age'] >= int(age_greq)]

        # Filter by age less than or equal to
        age_lesseq = request.args.get('age_lesseq')
        if age_lesseq:
            filtered_users = [user for user in filtered_users if user['age'] <= int(age_lesseq)]

        # Filter by age range
        age_min = request.args.get('age_min')
        age_max = request.args.get('age_max')
        if age_min and age_max:
            filtered_users = [user for user in filtered_users if int(age_min) <= user['age'] <= int(age_max)]

    except ValueError:
        return {'message': 'Invalid age input'}, 400

    return jsonify(filtered_users)


# POST request
# Check if the data provided is valid or not. Returns error message if it is not valid
# Posts the  data, if the input data is valid
@app.route('/api/users', methods=['POST'])
def create_user():
    try:
        new_user = request.json
        if not new_user or 'name' not in new_user or 'age' not in new_user or 'city' not in new_user:
            return {'message': 'Invalid user data'}, 400
        new_user['id'] = len(users) + 1
        users.append(new_user)
        return jsonify(new_user), 201
    except Exception as e:
        return {'message': str(e)}, 500


# PUT(update) request
# Check if the data provided is valid or not. Returns error message if it is not valid
# Updates the  data  completely, if the input data is valid
@app.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    try:
        updated_user = request.json
        if not updated_user or 'name' not in updated_user or 'age' not in updated_user or 'city' not in updated_user:
            return {'message': 'Invalid user data'}, 400
        for user in users:
            if user['id'] == user_id:
                user.update(updated_user)
                return jsonify(user)
        return {'message': 'User not found'}, 404
    except Exception as e:
        return {'message': str(e)}, 500


# PATCH(partial update) request
# Check if the data provided is valid or not. Returns error message if it is not valid
# Updates the  data  partially, if the input data is valid
@app.route('/api/users/<int:user_id>', methods=['PATCH'])
def partial_update_user(user_id):
    try:
        updated_fields = request.json
        if not updated_fields:
            return {'message': 'Invalid update data'}, 400
        for user in users:
            if user['id'] == user_id:
                user.update(updated_fields)
                return jsonify(user)
        return {'message': 'User not found'}, 404
    except Exception as e:
        return {'message': str(e)}, 500


# DELETE request
# Check if the data provided is valid or not. Returns error message if it is not valid
# Deletes the requested users, if the input data is valid
@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        global users
        users = [user for user in users if user['id'] != user_id]
        return {'message': 'User deleted'}, 200
    except Exception as e:
        return {'message': str(e)}, 500


if __name__ == '__main__':
    app.run(debug=True)
