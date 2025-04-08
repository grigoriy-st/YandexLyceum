import unittest
import json
from 
from data.jobs import Jobs

class JobAPITestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = 