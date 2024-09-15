#!/usr/bin/env python3
"""Encrypt password using bcrypt."""
import bcrypt


def hash_password(password: str) -> bytes:
    """Return encrypted bytes of password using bcrypt."""
    password = password.encode('utf-8')
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    return hashed
