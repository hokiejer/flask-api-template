# Tests for the system module

# Path: tests/test_system.py

import os
import unittest
from unittest.mock import patch
from system import system

class TestSystem(unittest.TestCase):
    """Tests for the system module."""

    def setUp(self):
        """Set up the tests."""
        system.System._env_vars = {}
        system.System._defaults = {}
        system.System._overrides = {}

    def test_declare(self):
        """Test declaring a variable."""
        system.System.declare('TEST', 'TEST_VAR')
        self.assertEqual(system.System._env_vars['TEST'], 'TEST_VAR')

    def test_undeclare(self):
        """Test undeclaring a variable."""
        system.System.declare('TEST', 'TEST_VAR')
        system.System.undeclare('TEST')
        self.assertNotIn('TEST', system.System._env_vars)

    def test_read_environment_variable(self):
        """Test reading an environment variable."""
        with patch.dict(os.environ, {'TEST_VAR': 'test'}):
            system.System.declare('TEST', 'TEST_VAR')
            self.assertEqual(system.System.read_environment_variable('TEST'), 'test')

    def test_read_environment_variable_not_defined(self):
        """Test reading an undefined environment variable."""
        with self.assertRaises(system.LabelNotDefinedError):
            system.System.read_environment_variable('TEST')

    def test_defined(self):
        """Test checking if a variable is defined."""
        system.System.declare('TEST', 'TEST_VAR')
        self.assertFalse(system.System.defined('TEST'))
        with patch.dict(os.environ, {'TEST_VAR': 'test'}):
            self.assertTrue(system.System.defined('TEST'))
        system.System._defaults['TEST'] = 'test'
        self.assertTrue(system.System.defined('TEST'))
        system.System._overrides['TEST'] = 'test'
        self.assertTrue(system.System.defined('TEST'))

    def test_getvar(self):
        """Test getting a variable."""
        system.System.declare('TEST', 'TEST_VAR', 'test')
        self.assertEqual(system.System.getvar('TEST'), 'test')
        system.System._overrides['TEST'] = 'test'
        self.assertEqual(system.System.getvar('TEST'), 'test')
        with patch.dict(os.environ, {'TEST_VAR': 'test'}):
            self.assertEqual(system.System.getvar('TEST'), 'test')

    def test_getvar_not_defined(self):
        """Test getting an undefined variable."""
        with self.assertRaises(system.VariableNotDefinedError):
            system.System.getvar('TEST')