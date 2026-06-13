def get_user_by_name(name):
    # Use parameterized queries (simulated) to avoid SQL injection
    query = "SELECT * FROM users WHERE name = %s"
    params = (name,)
    print("Executing:", query, params)
    return None


def delete_all():
    # dangerous function
    sql = "DELETE FROM users"
    print("Executing:", sql)
    return True
