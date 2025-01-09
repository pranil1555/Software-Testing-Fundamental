def login(username, password):
    if username == "admin" and password == "Password123":
        return {"status": "success", "user_id": 1}
    return {"status": "failure"}

def dashboard(user_id):
    if user_id == 1:
        return "Welcome, Admin"
    return "Access Denied"
