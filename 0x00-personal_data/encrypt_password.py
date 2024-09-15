#!/usr/bin/env python3
"""Encrypt password using bcrypt."""
import bcrypt


def hash_password(password: str) -> bytes:
    """Return encrypted bytes of password using bcrypt."""
    password = password.encode('utf-8')
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    return hashed

def is_valid(hash_password: bytes, password: str) -> bool:
    """Validate encrypted pasword."""
    if bcrypt.checkpw(password.encode('utf-8'), hash_password):
        return True
    else:
        return False
