#!/usr/bin/env python3
"""Auth Template."""
from flask import request
from typing import List, TypeVar


class Auth:
    """Class that contain the template for auth."""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Handle requirement of auth."""
        if path is None or excluded_paths is None:
            return True
        if path[len(path) - 1] != '/':
            path = path + '/'
        if path in excluded_paths:
            return False
        else:
            return True

    def authorization_header(self, request=None) -> str:
        """Handle authorization of header."""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Handle current user."""
        return None
