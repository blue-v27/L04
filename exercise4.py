import os


ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "")


def check_admin(password):
    """true if the password is the admin password"""
    admin_pw = os.environ.get("ADMIN_PASSWORD", ADMIN_PASSWORD)
    return admin_pw != "" and password == admin_pw


def find_user(db, username):
    """The user's row, or None if the username does not exist"""
    return db.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()