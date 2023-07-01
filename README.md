# Flask CRUD API

This repository contains a Flask-based API that enables basic CRUD operations using REST API endpoints. The API also provides various filtering capabilities to retrieve specific user data. The testing of the API can be performed using Postman.

## Installation

1. Clone the repository to your local machine.
2. Install the required dependencies by running the following command:


```shell
pip install -r requirements.txt
```
## Usage

### Starting the API

To start the Flask API, execute the following command:
```shell
python main.py
```
The API will start running on `http://localhost:5000`.

### Endpoints

#### GET /api/users

This endpoint retrieves a list of users based on the specified filtering parameters. The available filters include:

- `name`: Filter users by name (case-insensitive)
- `city`: Filter users by city (case-insensitive)
- `id`: Filter users by ID
- `age`: Filter users by exact age
- `age_gr`: Filter users by age greater than the specified value
- `age_less`: Filter users by age less than the specified value
- `age_greq`: Filter users by age greater than or equal to the specified value
- `age_lesseq`: Filter users by age less than or equal to the specified value
- `age_min` and `age_max`: Filter users by age within the specified range

Example usage:
```shell
GET /api/users?name=Raghav&city=Mumbai
 ```
#### POST /api/users

This endpoint allows the creation of a new user by sending a JSON object containing the user's `name`, `age`, and `city` in the request body. If successful, the newly created user will be returned in the response.

Example usage:
 ```shell
POST /api/users
Content-Type: application/json

{
  "name": "John Doe",
  "age": 30,
  "city": "New York"
}
```
#### PUT /api/users/{user_id}

This endpoint updates an existing user's information completely. Provide the `user_id` in the URL path and send a JSON object containing the updated user details in the request body, including the `name`, `age`, and `city`. If the user is found and the update is successful, the updated user information will be returned.

Example usage:
 ```shell
PUT /api/users/1
Content-Type: application/json

{
  "name": "Updated Name",
  "age": 35,
  "city": "Updated City"
}
```

#### PATCH /api/users/{user_id}

This endpoint allows partial updates to an existing user's information. Provide the `user_id` in the URL path and send a JSON object containing the fields to be updated in the request body. If the user is found and the update is successful, the updated user information will be returned.

Example usage:
 ```shell
PATCH /api/users/1
Content-Type: application/json

{
  "age": 40
}

```
#### DELETE /api/users/{user_id}

This endpoint deletes the specified user based on the provided `user_id` in the URL path. If the user is found and successfully deleted, a success message will be returned.

Example usage:
 ```shell
DELETE /api/users/1
```

## Test Cases

The project includes test cases to validate the functionality of the API. To run the test cases, execute the following command:

 ```shell
python test_api.py
```

## Contributions

Contributions to this project are welcome. If you encounter any issues or would like to suggest improvements, please create a new issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
