#!/usr/bin/python3
""" Unittets BaseModel class """

import unittest
import pep8
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ Test class """

    def test_class(self):
        """ Tests the instance of a class """
        self.assertTrue(isinstance(BaseModel(), BaseModel))

    def test_docstring(self):
        """Test doc strings"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_style_base(self):
        """Test pep8"""
        style = pep8.StyleGuide()
        m = style.check_files(["models/base_model.py"])
        self.assertEqual(m.total_errors, 0, "fix pep8")

    def test_str(self):
        """test that the str method has the correct output"""
        inst = BaseModel()
        string = "[BaseModel] ({}) {}".format(inst.id, inst.__dict__)
        self.assertEqual(string, str(inst))


if __name__ == "__main__":
    unittest.main()
