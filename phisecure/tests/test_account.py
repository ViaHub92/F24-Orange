import pytest
from backend.project.blueprints.account import list_users, get_user, create_user
from database.db_connection import create_app, db
"""
unittesting.py
Team Orange
Last Modified: 10/3/24
Unit testing for backend.
"""

def test_list_users():
    userlist = list_users()
    assert len(userlist) != 0, "Was not able to properly read list of users from database."
    print(userlist)
    return

def test_get_user():
    user1 = get_user("Dman92")
    user2 = get_user("FaultyUser")
    assert user1 != None and user2 != None, "Could not properly grab users from database."
    return

def test_create_user():
    return

def main():
    test_list_users()

if __name__ == "__main__":
    main()