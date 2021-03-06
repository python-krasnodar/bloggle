from flask_testing import TestCase

from app import app
from config import environments


class BaseTestCase(TestCase):
    def create_app(self):
        app.config.from_object(environments['test'])
        return app
