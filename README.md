# Library Management System API

This project is a Flask-based API for managing a library system. It supports CRUD operations for both books and members, along with optional search and pagination functionality for books.

## Table of Contents
- [How to Run the Project](#how-to-run-the-project)
- [Design Choices](#design-choices)
- [Assumptions and Limitations](#assumptions-and-limitations)
- [Endpoints Overview](#endpoints-overview)

---

## How to Run the Project

### Prerequisites
1. Python 3.8 or higher installed on your system.
2. Flask module installed. You can install it using pip:
   ```bash
   pip install flask
   ```

### Steps to Run
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Run the Flask application:
   ```bash
   python app.py
   ```

3. The application will start running at `http://127.0.0.1:5000`. Use tools like Postman or cURL to interact with the endpoints.

---

## Design Choices

1. **In-memory Storage:**
   - For simplicity and to adhere to the "no third-party libraries" constraint, books and members are stored in Python lists. This avoids dependency on external databases.

2. **RESTful API Design:**
   - Separate routes for `GET`, `POST`, `PUT`, and `DELETE` operations ensure clarity and modularity.

3. **Pagination and Filtering:**
   - Pagination and search filters are implemented for the `GET /books` endpoint to enhance scalability and usability.

4. **Error Handling:**
   - Basic error responses for cases like invalid IDs or missing resources ensure better user feedback.

5. **Scalability:**
   - The modular structure allows for easy migration to a database in the future if needed.

---

## Assumptions and Limitations

### Assumptions:
1. The `title` and `author` fields in books and the `name` and `email` fields in members are mandatory for creation.
2. IDs are auto-generated and unique within their respective categories (books or members).
3. Search filters are case-insensitive.

### Limitations:
1. **In-memory storage**:
   - Data will be lost once the application stops. For production, a database (e.g., SQLite, PostgreSQL) is recommended.
2. **Authentication:**
   - No authentication or user roles are implemented.
3. **Concurrency Issues:**
   - The in-memory data structure isn't thread-safe.

---

## Endpoints Overview

### Book Endpoints
1. **Get All Books:**
   - `GET /books`
   - Query Parameters:
     - `title`: Filter by book title (optional).
     - `author`: Filter by book author (optional).
     - `page`: Page number for pagination (optional, default=1).
     - `per_page`: Number of books per page (optional, default=5).

2. **Add a Book:**
   - `POST /books`
   - Request Body:
     ```json
     {
       "title": "Book Title",
       "author": "Author Name",
       "year": 2024,
       "genre": "Fiction"
     }
     ```

3. **Update a Book:**
   - `PUT /books/<book_id>`
   - Request Body:
     ```json
     {
       "title": "Updated Title",
       "author": "Updated Author"
     }
     ```

4. **Delete a Book:**
   - `DELETE /books/<book_id>`

### Member Endpoints
1. **Get All Members:**
   - `GET /members`

2. **Add a Member:**
   - `POST /members`
   - Request Body:
     ```json
     {
       "name": "Member Name",
       "email": "member@example.com"
     }
     ```

3. **Update a Member:**
   - `PUT /members/<member_id>`
   - Request Body:
     ```json
     {
       "name": "Updated Name",
       "email": "updated@example.com"
     }
     ```

4. **Delete a Member:**
   - `DELETE /members/<member_id>`

---

Feel free to contribute to the repository or suggest improvements!

