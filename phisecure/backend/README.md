# Phisecure API - Backend

## Setup

1. Navigate to backend directory

2. Activate virtual environment
    In bash terminal
    ```bash
    source venv/bin/activate
    ```
3. install the required dependencies
    ```bash
    pip install -r requirements.txt
    ```

## Run Flask

1. Make sure you are still in backend directory

2. Use run.py to start flask
    ```bash
    python run.py
    ```

## API Routes

Below is a list of the API routes available in the Phisecure backend:

### 1. Landing Page
   - **URL:** `/`
   - **Method:** GET
   - **Description:** Returns a welcome message and a list of available routes.

### 2. Create User
   - **URL:** `/create_user`
   - **Method:** POST
   - **Description:** Create a new user with the required details.
   - **Expected Input:** JSON object with `username`, `email`, `password_hash`, `first_name`, `last_name`.
   - **Response:** Success or error message.

### 3. Get User by Username
   - **URL:** `/get_user/<username>`
   - **Method:** GET
   - **Description:** Retrieve a user by their username.
   - **Response:** User information (`username`, `email`, `first_name`, `last_name`) or an error message if the user is not found.

### 4. List All Users
   - **URL:** `/list_users`
   - **Method:** GET
   - **Description:** Returns a list of all registered users.
   - **Response:** JSON array of user objects with `username`, `email`, `first_name`, and `last_name`.

## Examples

1. **Create User (POST Request):**
   ```bash
   curl -X POST http://localhost:5000/create_user \
   -H "Content-Type: application/json" \
   -d '{
       "username": "johndoe",
       "email": "johndoe@example.com",
       "password_hash": "securepassword123",
       "first_name": "John",
       "last_name": "Doe"
   }'