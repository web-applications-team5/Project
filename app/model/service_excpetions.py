
from __future__ import absolute_import
from flask_sqlalchemy import Model


class ServiceException:

    def __init__(self, message=None, code=None, details=None):
        self.message = message
        self.code = code
        self.details = details