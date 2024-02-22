from api.v1.auth.auth import Auth
import base64
from typing import TypeVar


class BasicAuth(Auth):
    """
    Basic Auth class
    """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """
        extract_base64_authorization_header function
        """
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        if authorization_header[0:6] != 'Basic ':
            return None
        return authorization_header[6:]
    
    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """
        Decode a Base64 string
        """
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) is not str:
            return None
        try:
            base64_bytes = base64_authorization_header.encode("utf-8")
            sample_string_bytes = base64.b64decode(base64_bytes)
            sample_string = sample_string_bytes.decode("utf-8")
            return sample_string
        except Exception:
            return None
