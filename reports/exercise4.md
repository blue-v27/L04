# Bug reports for exercise4.py

Line: 9
Problem: The function check_admin uses os.environ.get("ADMIN_PASSWORD", ADMIN_PASSWORD) which may lead to inconsistent behavior if ADMIN_PASSWORD is set in the environment but the default value is also non-empty.
Example: If ADMIN_PASSWORD is set to "secret" in environment, but the default value is also "secret", the function will still return True for password matching, but if the environment variable is empty, it will fall back to the default, which might not be intended.
Fix: Use a consistent source for the admin password, preferably just os.environ.get("ADMIN_PASSWORD") without fallback to the default variable.
