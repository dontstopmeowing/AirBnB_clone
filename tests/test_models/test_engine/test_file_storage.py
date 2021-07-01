#!/usr/bin/python3
""" Unittets BaseModel class """

import unittest
import pep8
import models
from models.engine.file_storage import Filestorage


class TestBaseModel(unittest.TestCase):
    """ Test class """

    def test_class(self):
        """ Tests the instance of a class """
        self.assertTrue(isinstance(Filestorage(), Filestorage))

    def test_docstring(self):
        """Test doc strings"""
        self.assertIsNotNone(Filestorage.__doc__)
        self.assertIsNotNone(Filestorage.all.__doc__)
        self.assertIsNotNone(Filestorage.new.__doc__)
        self.assertIsNotNone(Filestorage.save.__doc__)
        self.assertIsNotNone(Filestorage.reload.__doc__)

    def test_style_base(self):
        """Test pep8"""
        style = pep8.StyleGuide()
        m = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(m.total_errors, 0, "fix pep8")

    def test_shebang(self):
        with open("models/engine/file_storage.py", mode='r') as _file:
            Shebang = _file.read()
            line = Shebang.splitlines()
            self.assertEqual(line[0], '#!/usr/bin/python3')


if __name__ == "__main__":
    unittest.main()
