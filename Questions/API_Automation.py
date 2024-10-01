import requests
import time
import json

class TestApi:
    def __init__(self, url):
        self.url = url

    # Function to check if the API response is successful
    def test_able_to_fetch_api(self):
        response = requests.get(self.url)
        print(f"Response Status Code: {response.status_code}")
        assert response.status_code == 200, f"Failed to fetch details, status code: {response.status_code}"
        return response

    # Function to check if API response time is within the expected limit
    def test_check_api_response_time(self, expected_time=100):
        start_time = time.time()
        response = requests.get(self.url)
        end_time = time.time()
        response_time_ms = (end_time - start_time) * 1000  # Convert to milliseconds
        print(f"Response Time: {response_time_ms:.2f} ms")
        assert response_time_ms < expected_time, f"API response time is too high: {response_time_ms:.2f} ms"
        return response_time_ms

    # Polling function to repeatedly list users every 'poll_interval' seconds
    def poll_users_list(self, poll_interval=100):
        while True:
            response = self.test_able_to_fetch_api()
            if response.status_code == 200:
                users_data = response.json()
                self.list_email_addresses(users_data)
            time.sleep(poll_interval)

    # Function to list email addresses from the user database
    def list_email_addresses(self, response_data):
        users = response_data.get("data", [])
        emails = [user['email'] for user in users]
        print("Email Addresses in User Database:")
        for email in emails:
            print(email)

# URL to check the users list
url = "https://reqres.in/api/users"

# Instantiate the class
test_api = TestApi(url)

# Run tests
test_api.test_able_to_fetch_api()  # Check if API response is successful
test_api.test_check_api_response_time()  # Check if response time is below 100 ms

# Poll the API every 100 seconds and list email addresses
# Uncomment the line below to run the polling function
# test_api.poll_users_list(poll_interval=100)
