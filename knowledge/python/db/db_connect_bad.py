def get_db_connection():
    # TODO: Connect to production DB
    host = "localhost"
    user = "admin"
    password = "12345_secret_password" # HARDCODED PASSWORD!
    
    print(f"Connecting as {user} with pass {password}")
    return f"Connected to {host}"