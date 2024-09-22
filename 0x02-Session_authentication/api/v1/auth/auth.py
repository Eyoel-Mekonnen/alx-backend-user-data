#!/usr/bin/env python3
"""Auth Template."""
from flask import request
from typing import List, TypeVar
import os


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
        if request is None:
            return None
        authorization = request.headers.get('Authorization', None)
        if authorization:
            return authorization
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Handle current user."""
        return None

    def session_cookie(self, request=None) -> str:
        """Retrives cookie value from request from name on ENV."""
        if request is None:
            return None
        cookie_Name = os.getenv('SESSION_NAME')
        cookie_Value = request.cookies.get(cookie_Name)
        return cookie_Value
