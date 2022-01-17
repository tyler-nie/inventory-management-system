import unittest
from flask_testing import TestCase
from app import create_app, db
from app.model import Item
import os
from flask import abort, url_for
from app.model import Item
from instance.config import SQLALCHEMY_DATABASE_URI_TEST

class TestBase(TestCase):

    def create_app(self):

        # passing the test configurations
        config_name = 'testing'
        app = create_app(config_name)
        app.config.update(SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI_TEST)
        return app

    def setUp(self):
        """
        Called before every test
        """
        db.create_all()

        # create test Item
        item = Item(name="Football", quantity=7, description="British football's")

         # save item to database
        db.session.add(item)
        db.session.commit()

    def tearDown(self):
        """
        Called after every test
        """

        db.session.remove()
        db.drop_all()

class TestModel(TestBase):

    def test_item_model(self):
        """
        Test number of records in Item
        """
        self.assertEqual(Item.query.count(), 1, "One item expected in the database")

class TestView(TestBase):

    def test_items_view(self):
        """
        Test that items inventory page is accessible
        """

        response = self.client.get(url_for('items.list_items'))
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()