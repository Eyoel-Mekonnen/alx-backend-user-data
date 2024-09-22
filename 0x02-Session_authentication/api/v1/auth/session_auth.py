#!/usr/bin/env python3
"""Session Auth class."""
from api.v1.auth.auth import Auth
from uuid import uuid4


class SessionAuth(Auth):
    """Class session Auth."""

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Create a unique session id to append session id by user."""
        if user_id is None:
            return None
        if type(user_id) != str:
            return None
        session_id = str(uuid4())
        SessionAuth.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Return User ID based on session_id."""
        if sesion_id is None:
            return None
        if type(session_id) != str:
            return None
        user_id = SessionAuth[session_id]
        return user_id
