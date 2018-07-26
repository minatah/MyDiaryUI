import unittest
from tests import MyTestCase
import json
class Tests_Requests(MyTestCase):

    def test_entry_submission_successfully(self):
        """Tests when the entries  are submitted successfully"""
        with self.client:
            response = self.add_entry(1,"My First Python code","hahaha it was too intresting to develop.","2/08/2012")
            """getting the response  from data"""
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            self.assertEqual(data.get('message'), "Created an entry successfully.")

    def test_get_all_entries(self):
        """Tests when all entries are retrieved successfully"""
        with self.client:
            response = self.get_entries()
            self.assertEqual(response.status_code, 200)

    def test_entry_duplicates(self):
        """Tests when the entries  are duplicated"""
        with self.client:
            response = self.add_entry(1,"My First Python code","hahaha it was too intresting to develop.","2/08/2012")
            res = self.add_entry(1, "My First Python code", "hahaha it was too intresting to develop.",
                                      "2/08/2012")
            """getting the response  from data"""
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            self.assertEqual(data.get('message'), "Created an entry successfully.")

            """for duplicates"""
            new_data = json.loads(res.data.decode())
            self.assertEqual(res.status_code, 409)

    def test_get_single_entry(self):
        """Tests when an entry is retrieved successfully"""
        with self.client:
            """first add an entry"""
            res = self.add_entry(1, "My First Python code", "hahaha it was too intresting to develop.",
                                      "2/08/2012")
            data = json.loads(res.data.decode())
            self.assertEqual(res.status_code, 201)

            """get a single entry """
            response = self.get_single_entry(1)
            self.assertEqual(response.status_code, 200)

    def test_update_single_entry(self):
        """Tests when an entry is updated successfully"""
        with self.client:
            """first add an entry"""
            res = self.add_entry(1, "My First Python code", "hahaha it was too intresting to develop.",
                                      "2/08/2012")
            data = json.loads(res.data.decode())
            self.assertEqual(res.status_code, 201)

            """update a single entry """
            response = self.update_single_entry(1,"new title", "cool","3/3/2010")
            self.assertEqual(response.status_code, 200)





