#!/usr/bin/env python3
"""Class for basic Authentication."""
from api.v1.auth.auth import Auth
import binascii
import base64


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

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        """Decode base64 encoded authorization."""
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) != str:
            return None
        try:
            decoded = base64.b64decode(base64_authorization_header)
            decoded = decoded.decode('utf-8')
            return decoded
        except (binascii.Error, UnicodeDecodeError):
            return None

    def extract_user_credentials(self,
                                 decode_base64_authorization_header:
                                 str) -> (str, str):
        """Return Email and Password."""
        if decode_base64_authorization_header is None:
            return (None, None)
        if type(decode_base64_authorization_header) != str:
            return (None, None)
        if ':' not in decode_base64_authorization_header:
            return (None, None)
        username = decode_base64_authorization_header.split(':')[0]
        password = decode_base64_authorization_header.split(':')[1]
        return (username, password)
