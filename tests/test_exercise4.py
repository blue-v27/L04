import os
import sqlite3
import subprocess

import pytest

import exercise4
from exercise4 import *


# bug report 1
admin_pw = os.environ.get("ADMIN_PASSWORD", ADMIN_PASSWORD)
