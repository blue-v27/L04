import os
import sqlite3
import subprocess

import pytest

import exercise3
from exercise3 import *


# bug report 1
def percent(part, total):
    """part as a percentage of total. If total is 0, the result is 0"""
    return part / total * 100 if total != 0 else 0
