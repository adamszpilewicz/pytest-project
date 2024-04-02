# utils.py

def generate_insert_query(table, data):
    """
    Generates an SQL INSERT query string.

    Parameters:
    - table: String name of the table.
    - data: Dictionary of column names and their values to insert.

    Returns:
    - tuple: (query_string, values) where query_string is the SQL query and values is a list of values to insert.
    """
    columns = ', '.join(data.keys())
    # Correctly generate placeholders string
    placeholders = ', '.join('%s' for _ in data)  # Fixed here
    query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
    values = list(data.values())
    return query, values


def validate_email(email: str) -> bool:
    """
    Validates an email address.

    Parameters:
    - email: String, the email address to validate.

    Returns:
    - bool: True if the email is valid, False otherwise.
    """
    import re
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    proper = re.match(pattern, email) is not None
    if not proper:
        raise ValueError("Invalid email address")
    return proper
