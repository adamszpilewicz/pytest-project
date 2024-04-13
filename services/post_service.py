# services/post_service.py
class PostService:
    def __init__(self, db):
        self.db = db

    def create_post(self, post_data):
        """
        Creates a new post.

        Parameters:
        - post_data: Dictionary containing post details ('title', 'content', 'user_id').
        """
        self.db.create('posts', post_data)
        print("Post created successfully.")

    def get_post(self, post_id):
        """
        Retrieves a post by its ID.

        Parameters:
        - post_id: Integer, the ID of the post to retrieve.

        Returns:
        - A dictionary containing post details if found, None otherwise.
        """
        query = "SELECT * FROM posts WHERE id = %s"
        result = self.db.read(query, (post_id,))
        return result[0] if result else None

    def update_post(self, post_id, update_data):
        """
        Updates an existing post.

        Parameters:
        - post_id: Integer, the ID of the post to update.
        - update_data: Dictionary containing the columns to update and their new values.
        """
        set_clause = ', '.join(f"{key} = %s" for key in update_data.keys())
        values = tuple(update_data.values())
        query = f"UPDATE posts SET {set_clause} WHERE id = %s"
        self.db.update(query, values + (post_id,))
        print("Post updated successfully.")

    def delete_post(self, post_id):
        """
        Deletes a post by its ID.

        Parameters:
        - post_id: Integer, the ID of the post to delete.
        """
        query = "DELETE FROM posts WHERE id = %s"
        self.db.delete(query, (post_id,))
        print("Post deleted successfully.")
