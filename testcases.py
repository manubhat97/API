import unittest
import json
import sys
sys.path.append('main.py')  # Replace with the actual path to your code

from main import app

class AppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_users(self):
        response = self.app.get('/api/users')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 5)  # Assuming there are 5 initial users


    def test_filter_users_by_name(self):
        response = self.app.get('/api/users?name=Raghav')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['name'], 'Raghav')

    def test_filter_users_by_city(self):
        response = self.app.get('/api/users?city=Bangalore')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['city'], 'Bangalore')

    def test_filter_users_by_id(self):
        response = self.app.get('/api/users?id=3')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['id'], 3)

    def test_filter_users_by_age(self):
        response = self.app.get('/api/users?age=40')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['age'], 40)

    def test_filter_users_by_age_range(self):
        response = self.app.get('/api/users?age_min=30&age_max=50')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 4)

    def test_filter_users_by_invalid_age(self):
        response = self.app.get('/api/users?age=abc')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['message'], 'Invalid age input')

    def test_filter_users_by_age_range(self):
        response = self.app.get('/api/users?age_min=30&age_max=50')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 4)

        # Check if the filtered users are within the age range
        for user in data:
            self.assertGreaterEqual(user['age'], 30)
            self.assertLessEqual(user['age'], 50)

    def test_filter_users_by_age_range_empty_result(self):
        response = self.app.get('/api/users?age_min=60&age_max=70')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 0)

    def test_filter_users_by_age_range_invalid_min(self):
        response = self.app.get('/api/users?age_min=abc&age_max=50')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['message'], 'Invalid age input')

    def test_filter_users_by_age_range_invalid_max(self):
        response = self.app.get('/api/users?age_min=30&age_max=def')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['message'], 'Invalid age input')

    def test_filter_users_by_age_range_invalid_min_max(self):
        response = self.app.get('/api/users?age_min=abc&age_max=def')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['message'], 'Invalid age input')

    def test_create_user(self):
        new_user = {
            'name': 'John',
            'age': 35,
            'city': 'New York'
        }
        response = self.app.post('/api/users', json=new_user)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['name'], 'John')
        self.assertEqual(data['age'], 35)
        self.assertEqual(data['city'], 'New York')
        self.assertEqual(data['id'], 6)  # Assuming the new user ID is 6

    def test_update_user(self):
        updated_user = {
            'name': 'Janaki Devi',
            'age': 32,
            'city': 'Bangalore'
        }
        response = self.app.put('/api/users/2', json=updated_user)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['name'], 'Janaki Devi')
        self.assertEqual(data['age'], 32)
        self.assertEqual(data['city'], 'Bangalore')
        self.assertEqual(data['id'], 2)

    def test_partial_update_user(self):
        updated_fields = {
            'name': 'Mohan Sharma',
        }
        response = self.app.patch('/api/users/4', json=updated_fields)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['name'], 'Mohan Sharma')
        self.assertEqual(data['age'], 50)  # Age should not change
        self.assertEqual(data['city'], 'london')  # City should not change
        self.assertEqual(data['id'], 4)

    def test_delete_user(self):
        response = self.app.delete('/api/users/5')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'User deleted')

if __name__ == '__main__':
    unittest.main()
