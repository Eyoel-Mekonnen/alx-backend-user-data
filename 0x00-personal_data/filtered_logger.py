#!/usr/bin/env python3
"""Personal Data handled."""
from typing import List
import re


def filter_datum(fields: List[str], redaction:
                 str, message: str, separator: str) -> str:
    """Apply regex and replaces redaction value."""
    field_joined = "(" + "|".join(fields) + ")" + "="
    regex = "([^" + separator + "]+)"
    pattern = field_joined + regex
    redact = r"\1=" + redaction
    match = re.sub(pattern, redact, message)
    return match
