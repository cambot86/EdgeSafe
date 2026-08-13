# test_edgesafe.py
"""
Tests for EdgeSafe module.
"""

import unittest
from edgesafe import EdgeSafe

class TestEdgeSafe(unittest.TestCase):
    """Test cases for EdgeSafe class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = EdgeSafe()
        self.assertIsInstance(instance, EdgeSafe)
        
    def test_run_method(self):
        """Test the run method."""
        instance = EdgeSafe()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
