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
- **Refresh Token Endpoint:**  `/api/auth/refresh` (Method: POST)
- **User Search Endpoint:**  `/api/user-search` (Method: GET)
- **Friends List Endpoint:**  `/api/friends` (Method: GET)
- **Friend Request Endpoint:**  `/api/friendrequests` (Methods: GET, POST, PATCH)




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

- **Refresh Token:**
    - Endpoint: `/api/auth/refresh`
    - Method: `POST`
    - Request Body:
        ```json
        {
            "refresh": "",
        }
        ```

    - Response Body: 
    ```json
        {
            "access": "",
        }
        ```
- **User Search:**
    - Endpoint: `/api/friends`
    - Method: `GET`
    - Request Query Params:
        ```json
        {
            "search": "" 
        }
        ```

    - Response Body:
        ``` json
            [
        {
            "username": "friend1",
            "email": "friend1@gmail.com"
        },
        {
            "username": "friend2",
            "email": "friend2@gmail.com"
        }
            ]
        ```

        
- **Friends List:**
    - Endpoint: `/api/friends`
    - Method: `GET`
    - Response Body:
        ``` json
            [
        {
            "username": "friend1",
            "email": "friend1@gmail.com"
        },
        {
            "username": "friend2",
            "email": "friend2@gmail.com"
        }
            ]
        ```

- **Friend Request:**
    - Endpoint: `/api/friendrequests`
    - Method: `GET`
    - Response Body:
        ``` json
            [
                {
                    "id": "",
                    "from_user": {
                        "username": "",
                        "email": ""
                    },
                    "to_user": {
                        "username": "",
                        "email": ""
                    },
                    "status": "accepted",
                    "timestamp": ""
                }
            ]
        ```


    - Endpoint: `/api/friendrequests`
    - Method: `POST`
    - Request Body:
        ```json
        {
            "to_username": "",
        }
        ```

    - Response Body:
    
        ``` json
            {
                "id": "",
                "from_user": {
                    "username": "",
                    "email": ""
                },
                "to_user": {
                    "username": "",
                    "email": ""
                },
                "status": "pending",
                "timestamp": ""
            }
        ```


    - Endpoint: `/api/friendrequests/<friend_request_id>`
    - Method: `PATCH`
    - Request Body:
        ```json
        {
            "action": "",
        }
        ```
    - Response Body:
        ``` json
            {
                "id": "",
                "from_user": {
                    "username": "",
                    "email": ""
                },
                "to_user": {
                    "username": "",
                    "email": ""
                },
                "status": "accepted",
                "timestamp": ""
            }
        ```

