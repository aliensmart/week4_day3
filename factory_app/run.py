from app import ORM
from app import controller
from app import Worker
import os

DIR = os.path.dirname(__file__)
DBPATH = os.path.join(DIR, 'data', 'factory.db')
ORM.dbpath = DBPATH


controller.run()