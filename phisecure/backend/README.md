# Phisecure API - Backend

## Setup

1. Navigate to backend directory and create venv
    In bash terminal
    ```bash
    python -m venv venv
    ```
   or
    ```bash
    python3 -m venv venv
    ```
3. Now activate the venv
    In bash terminal
    ```bash
    source venv/bin/activate
    ```
4. install the required dependencies
    ```bash
    pip install -r requirements.txt
    ```

## Run Flask

1. Go back to the phisecure directory

2. Adjust the FLASK_APP environment variable with this command
   ```bash
    export FLASK_APP=backend.project:create_app
   ```

3. Use flask run command
    ```bash
    flask run
    ```

## API Routes

Below is a list of the functional API routes available in the Phisecure backend:

### 1. Landing Page
   - **URL:** `/`
   - **Method:** GET
   - **Description:** Returns a welcome message and a list of available routes.

### 2. Create User
   - **URL:** `/account/create_student`
   - **Method:** POST
   - **Description:** Create a new student with the required details.
   - **Expected Input:** JSON object with `username`, `email`, `password_hash`, `first_name`, `last_name`.
   - **Response:** Success or error message.

### 3. Get User by Username
   - **URL:** `/account/get_student/<username>`
   - **Method:** GET
   - **Description:** Retrieve a student by their username.
   - **Response:** Student information (`username`, `email`, `first_name`, `last_name`) or an error message if the user is not found.

### 4. List All Users
   - **URL:** `/account/list_students`
   - **Method:** GET
   - **Description:** Returns a list of all registered students.
   - **Response:** JSON array of student objects with `username`, `email`, `first_name`, and `last_name`.

### 5. Delete Student
   - **URL:** `/account/delete_student/<int:student_id>`
   - **Method:** DELETE
   - **Description:** Delete a specific student by their ID.
   - **Expected Input:** Path parameter `student_id` (required).
   - **Response:** Success message or an error message if the student is not found.

### 6. Inbox
   - **URL:** `/messaging/inbox`
   - **Method:** GET
   - **Description:** Retrieve all emails sent to a specific student.
   - **Expected Input:** Query parameter `student_id` (required).
   - **Response:** JSON object containing an array of emails with `id`, `sender`, `recipient`, `subject`, `body`, and `sent_at`.

### 7. Compose Message
- **URL:** `/messaging/compose_email`
- **Method:** POST
- **Description:** Send a new email message.
- **Expected Input:** Form data with `sender`, `recipient`, `subject`, and `body`.
- **Response:** Success message or an error message if the recipient does not exist.

### 8. Compose Phishing Email
- **URL:** `/messaging/compose_phishing_email`
- **Method:** POST
- **Description:** Send a phishing email using a specified template.
- **Expected Input:** Form data with `sender`, `recipient`, and `template_id`.
- **Response:** Success message or an error message if the recipient or template does not exist.

### 9. View Email
- **URL:** `/messaging/view/<int:email_id>`
- **Method:** GET
- **Description:** View a specific email.
- **Response:** JSON object containing email details or redirects with an error message if the email is not found.

### 10. Reply to Email
- **URL:** `/messaging/reply/<int:email_id>`
- **Method:** POST
- **Description:** Reply to a specific email.
- **Expected Input:** Form data with `reply_body`.
- **Response:** Success message or an error message if the email is not found.

### 11. Delete Email
- **URL:** `/messaging/delete/<int:email_id>`
- **Method:** POST
- **Description:** Delete a specific email.
- **Response:** Success message or an error message if the email is not found.

### 12. Performance Metrics
- **URL:** `/performance/<int:student_id>`
- **Method:** GET (or specify the method if different)
- **Description:** Retrieve performance metrics regarding email interactions and student responses during phishing simulations.
- **Response:** JSON object containing aggregated data about student performance in relation to phishing emails.

## How to Create User Using Postman
1. **Open Postman**  
   Launch the Postman application on your computer.

2. **Create a New Request**  
   - Click on the "New" button or select "Request" from the main interface.
   - Name your request (e.g., "Create User") and save it to a collection if desired.

3. **Set the Request Method and URL**  
   - In the request type dropdown, select `POST`.
   - Enter the URL for creating a user:
     ```
     http://localhost:5000/account/create_user
     ```
   (Make sure your Flask application is running before you make the request.)

4. **Set the Headers**  
   - Click on the "Headers" tab.
   - Add a new header:
     - **Key**: `Content-Type`
     - **Value**: `application/json`

5. **Provide the Request Body**  
   - Click on the "Body" tab.
   - Select the `raw` option.
   - Choose `JSON` from the dropdown to the right.
   - Enter the user details in JSON format. For example:
     ```json
     {
       "username": "johndoe",
       "email": "johndoe@example.com",
       "password_hash": "your_password_hash",
       "first_name": "John",
       "last_name": "Doe"
     }
     ```

6. **Send the Request**  
   - Click the "Send" button.
   - You should see a response in the lower pane of Postman.

7. **Check the Response**  
   - A successful user creation will return a response with a status code of `201 Created` and a message like:
     ```json
     {
       "message": "User created successfully!"
     }
     ```

8. **Troubleshoot (if necessary)**  
   - If you receive an error, check the response message for details, such as:
     - "User already exists" (if the email is already in use)
     - "Bad Request" if the request body is malformed.

## Curl Example
2. **Create User Using Curl (POST Request):**
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
