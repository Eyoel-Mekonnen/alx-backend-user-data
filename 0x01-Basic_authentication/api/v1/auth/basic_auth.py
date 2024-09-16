#!/usr/bin/env python3
"""Class for basic Authentication."""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Class taht will implement basic auth."""

    def extract_base64_authorization_header(self, authorization: str) -> str:
        """Extraacts the base64 encoded."""
        if authorization is None:
            return None
        if type(authorization) != str:
            return None
        header_string = authorization.split()[0]
        if header_string != 'Basic':
            return None
        else:
            return authorization.split()[1]
