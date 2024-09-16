#!/usr/bin/python3
""" Check response
"""

if __name__ == "__main__":
    from api.v1.auth.basic_auth import BasicAuth

    ba = BasicAuth()
    res = ba.user_object_from_credentials("email", None)
    if res is not None:
        print("user_object_from_credentials must return None if 'user_pwd' is None")
        exit(1)
    
    print("OK", end="")
