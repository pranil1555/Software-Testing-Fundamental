from app import login, dashboard

def test_integration_login_dashboard():
    # Test valid login
    login_result = login("admin", "Password123")
    assert login_result["status"] == "success"

    # Test dashboard access
    user_id = login_result["user_id"]
    dashboard_message = dashboard(user_id)
    assert dashboard_message == "Welcome, Admin"
