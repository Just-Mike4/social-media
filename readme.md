# Social Media API
## Summary
This is an API for social networking application built using Django Rest Framework.

### Functionalities
1. User Management: Login and signup functionality with email and password, with email case insensitivity and no OTP verification required.
2. Search Users: Search users by email or name, with pagination up to 10 records per page.
3. Friend Requests: Send, accept, and reject friend requests, with a limit of 3 requests per minute.
4. Friendship Management: List friends and pending friend requests.

## Usage
1. **Clone the Repository:**
    ```bash
    git clone https://github.com/Just-Mike4/social-media.git
    ```

2. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Server:**
    - For Windows:
        ```bash
        python manage.py runserver
        ```
    - For macOS:
        ```bash
        python3 manage.py runserver
        ```

## API Documentation
### API Endpoint for Seamless Interaction
Explore and interact with the application through the API, providing easy access to various functionalities.
- **Register User Endpoint:** `/api/auth/register` (Method: POST)
- **User Login Endpoint:** `/api/auth/login` (Method: POST)
- **User Search Endpoint:**  `/api/user-search/`
- **Friend Request Endpoint:**  `/api/friendrequests/`
- **Friends List Endpoint:**  `/api/friends/`
- **Refresh Token Endpoint:**  `/api/auth/refresh/`

The API documentation is available at the following endpoints:

- **Register User:**
    - Endpoint: `/api/auth/register`
    - Method: `POST`
    - Request Body:
        ```json
        {
            "username": "",
            "email": "",
            "password1": "",
            "password2": ""
        }
        ```

    - Response Body: 
    ``` json
        {
            "refresh": "",
            "access": "",
            "user": {
                "username": "",
                "email": ""
            }
        }
    ```

- **User Login:**
    - Endpoint: `/api/auth/login`
    - Method: `POST`
    - Request Body:
        ```json
        {
            "username": "",
            "password": ""
        }
        ```
    - Response Body: 
    ``` json
        {
            "refresh": "",
            "access": "",
            "user": {
                "username": "",
                "email": ""
            }
        }
    ```
