# test_daorough.py
"""
Tests for DaoRough module.
"""

import unittest
from daorough import DaoRough

class TestDaoRough(unittest.TestCase):
    """Test cases for DaoRough class."""

    def test_initialization(self):
        """Test class initialization."""
        instance = DaoRough()
        self.assertIsInstance(instance, DaoRough)

    def test_run_method(self):
        """Test the run method."""
        instance = DaoRough()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
