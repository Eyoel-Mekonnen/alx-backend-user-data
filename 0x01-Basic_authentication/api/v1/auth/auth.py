#!/usr/bin/env python3
"""Auth Template."""
from flask import request
from typing import List, TypeVar


class Auth:
    """Class that contain the template for auth."""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Handle requirement of auth."""
        return False

    def authorization_header(self, request=None) -> str:
        """Handle authorization of header."""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Handle current user."""
        return None
