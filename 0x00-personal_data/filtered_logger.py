#!/usr/bin/env python3
"""Personal Data handled."""
from typing import List
import re
import logging
import os
import mysql.connector

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction:
                 str, message: str, separator: str) -> str:
    """Apply regex and replaces redaction value."""
    field_joined = "(" + "|".join(fields) + ")" + "="
    regex = "([^" + separator + "]+)"
    pattern = field_joined + regex
    redact = r"\1=" + redaction
    match = re.sub(pattern, redact, message)
    return match


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class."""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Intialize the constructor."""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Filter the log received to remove sensitive data."""
        result = filter_datum(self.fields, RedactingFormatter.REDACTION,
                              record.msg, RedactingFormatter.SEPARATOR)
        record.msg = result
        formatted_message = super(RedactingFormatter, self).format(record)
        return formatted_message


def get_logger() -> logging.Logger:
    """Create Logger return logging.Logger Object."""
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False
    """Because my Redacting is also a formatter."""
    formatter = RedactingFormatter(PII_FIELDS)
    streamhandler = logging.StreamHandler()
    streamhandler.setFormatter(formatter)
    logger.addHandler(streamhandler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """Return a connector to the database."""
    print("User:", os.getenv('PERSONAL_DATA_DB_USERNAME'))
    print("Password:", os.getenv('PERSONAL_DATA_DB_PASSWORD'))
    print("Host:", os.getenv('PERSONAL_DATA_DB_HOST'))
    print("Database:", os.getenv('PERSONAL_DATA_DB_NAME'))
    db_config = {
            'user': os.getenv('PERSONAL_DATA_DB_USERNAME'),
            'password': os.getenv('PERSONAL_DATA_DB_PASSWORD'),
            'host': os.getenv('PERSONAL_DATA_DB_HOST'),
            'database': os.getenv('PERSONAL_DATA_DB_NAME')
    }
    database_connection = mysql.connector.connect(**db_config)
    return database_connection
