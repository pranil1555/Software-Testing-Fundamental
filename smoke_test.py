#verify critical routes smoke testing

from app import login
def test_smoke_login():
    assert login ("admin","Password123")["status"]=="success"