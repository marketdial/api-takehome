#!/usr/bin/env python3
import csv
import os
import unittest
import copy

import challenges

CLIENT_NAME = "tc_topps"

SKU = '48052'

EXPECT = [{"name": SKU, "price": "15.99", "quantity_sold": 54}]
DB_CLIENT = {"client_collection": {CLIENT_NAME: {"items_sold": EXPECT}}}
REPORT_FILENAME = "/tmp/TC_Finance_Report.csv"


class TestBadCodeChallenge(unittest.TestCase):

    def test_send_report(self):

        if os.path.exists(REPORT_FILENAME):
            os.remove(REPORT_FILENAME)

        self.assertTrue(challenges.send_report(copy.deepcopy(DB_CLIENT), rejects=False))

        with open(REPORT_FILENAME, newline="") as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                self.assertEqual(row["name"], "TC Tuggers")
                self.assertEqual(row["price"], "15.99")
                self.assertEqual(row["quantity_sold"], "54")

        if os.path.exists(REPORT_FILENAME):
            os.remove(REPORT_FILENAME)
