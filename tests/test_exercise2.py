import os
import sqlite3
import subprocess

import pytest

import exercise2
from exercise2 import *


# bug report 1
def clamp(x, low, high):
    """x, limited to the range from low to high"""
    return max(low, min(x, low))
