import unittest
import os
import sys
import json
sys.path.append(os.getcwd())
from app import app
from app.config import app_config
from app.views import entries_list


class MyTestCase(unittest.TestCase):
    def create_app(self):
        """
        Create an instance of the app with the testing configuration
        """
        app.config.from_object(app_config["testing"])
        return app

    def setUp(self):
        self.client = app.test_client(self)

    def tearDown(self):
        """
        Drop the data structure data slicing
        """
        entries_list[:] = []

    def add_entry(self,id, title, content,date):
        """
        Function to create a request
        """
        return self.client.post(
            '/api/v1/entries',
            data=json.dumps(
                dict(
                    id=id,
                    title=title,
                    content=content,
                    date=date
                )
            ),
            content_type='application/json'
        )

    def get_entries(self):
        """
        function to return get
        """
        return self.client.get('/api/v1/entries')

    def get_single_entry(self,id ):
        """
        function to return get
        """
        return self.client.get('/api/v1/entries/%d'%id) #concatenting

    def update_single_entry(self, id,title,content,date):
        """
        function to return get
        """
        return self.client.put('/api/v1/entries/%d'%id,
                               data=json.dumps(
                                   dict(
                                       id=id,
                                       title=title,
                                       content=content,
                                       date=date
                                   )
                               ),
                               content_type='application/json'

                               )



