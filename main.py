# app.py
from db.postgresdb import PostgreSQL
from db.mysqldb import MySQLDatabase
from services.post_service import PostService
from services.user_service import UserService

# ---- POSTGRES DATABASE CONNECTION ----
dsn = "dbname=postgres user=postgres password=postgres host=localhost"

# Initialize the PostgreSQL connection.
db = PostgreSQL(dsn)

# Initialize UserService with the PostgreSQL database connection
user_service = UserService(db)

# Example: Register a new user using UserService
user_data = {
    "username": "john_doe",
    "email": "john@example.com"
}
try:
    user_service.register_user(user_data)
    print("User registered successfully with PostgreSQL.")
except ValueError as e:
    print(e)

# Initialize PostService with the PostgreSQL database connection
post_service = PostService(db)

# Example: Creating a new post using PostService
post_data = {
    "title": "Exploring PostgreSQL with Python",
    "content": "This post discusses how to use PostgreSQL with Python.",
    "user_id": 1  # Assuming a user with ID 1 exists
}
post_service.create_post(post_data)

# # Example: Retrieving a post by ID using PostService
# post_id = 2  # Assuming the post with ID 1 exists
# post = post_service.get_post(post_id)
# print(post)
#
# # Example: Updating a post using PostService
# update_data = {"title": "Updated Post Title", "content": "Updated content."}
# post_service.update_post(post_id, update_data)
#
# # Example: Deleting a post using PostService
# post_service.delete_post(post_id)


# --------------------------------------------

# ---- MYSQL DATABASE CONNECTION ----
# MySQL connection details
host = 'localhost'
user = 'user'  # Your MySQL username
password = 'userpass'  # Your MySQL password
database = 'user'  # Your MySQL database name

# Initialize the MySQL connection
db = MySQLDatabase(host, user, password, database)

# Initialize UserService with the MySQL database connection
user_service = UserService(db)

# Example: Register a new user using UserService
user_data = {
    "username": "john_doe",
    "email": "john@example.com"
}
try:
    user_service.register_user(user_data)
    print("User registered successfully with MySQL.")
except ValueError as e:
    print(e)


# Initialize PostService with the MySQL database connection
post_service = PostService(db)

# Example usage of PostService
# Creating a new post
post_data = {
    "title": "New Post Title",
    "content": "This is the content of the new post.",
    "user_id": 1  # Assuming the user with ID 1 exists
}
post_service.create_post(post_data)

# # Retrieving a post by ID
# post = post_service.get_post(2)  # Assuming the post with ID 1 exists
# print(post)
#
# # Updating a post
# update_data = {"title": "Updated Post Title"}
# post_service.update_post(1, update_data)  # Assuming the post with ID 1 exists
#
# # Deleting a post
# post_service.delete_post(1)  # Assuming the post with ID 1 exists
#
# #
# # --------------------------------------------
# # csv exporter
# csv_exporter = CSVExporter( db)
# query = "SELECT * FROM posts"
# data = csv_exporter.fetch_data(query)
# csv_exporter.save_to_csv(data, './posts_export.csv')