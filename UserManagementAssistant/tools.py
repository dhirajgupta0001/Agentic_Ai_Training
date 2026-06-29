from langchain.tools import tool

users_db: dict[int, dict] = {}
next_id = 1

def new_id() -> int:
    global next_id
    id = next_id
    next_id += 1
    return id

@tool
def create_user(name: str, email: str, age: int) -> str:
    """
    Create a new user and store them in the database.
    Use when the user wants to add / register / create a new person.
    Returns the new user's ID.
    """
    user_id = new_id()
    users_db[user_id] = {"id": user_id, "name": name, "email": email, "age": age}
    return f"User created! ID={user_id}, name={name}, email={email}, age={age}"

@tool
def get_user(user_id: int) -> str:
    """
    Retrieve a single user by their numeric ID.
    Use when the user asks to fetch, find, show, or look up a specific person.
    """
    user = users_db.get(user_id)
    if not user:
        return f"No user found with ID={user_id}"
    return str(user)

@tool
def update_user(user_id: int, name: str = "", email: str = "", age: int = 0) -> str:
    """
    Update an existing user's details. Only fields with non-empty / non-zero
    values will be changed. Use when the user wants to edit, modify, or change
    someone's information.
    """
    user = users_db.get(user_id)
    if not user:
        return f"No user found with ID={user_id}"
    if name:
        user["name"] = name
    if email:
        user["email"] = email
    if age:
        user["age"] = age
    return f"User {user_id} updated: {user}"


@tool
def delete_user(user_id: int) -> str:
    """
    Permanently delete a user from the database by their ID.
    Use when the user wants to remove, delete, or unregister a person.
    """
    if user_id not in users_db:
        return f"No user found with ID={user_id}"
    removed = users_db.pop(user_id)
    return f"Deleted user: {removed}"


@tool
def list_users(dummy: str = "") -> str:
    """
    Return a list of ALL users currently in the database.
    Use when the user asks to see everyone, show all users, or list users.
    The 'dummy' parameter is unused — just pass an empty string.
    """
    if not users_db:
        return "No users in the database yet."
    return "\n".join(str(u) for u in users_db.values())


@tool
def search_users(keyword: str) -> str:
    """
    Search users by a keyword that matches their name or email (case-insensitive).
    Use when the user wants to find someone but doesn't know the exact ID.
    """
    kw = keyword.lower()
    results = [
        u for u in users_db.values()
        if kw in u["name"].lower() or kw in u["email"].lower()
    ]
    if not results:
        return f"No users matched '{keyword}'"
    return "\n".join(str(u) for u in results)
