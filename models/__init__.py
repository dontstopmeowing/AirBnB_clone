#!/usr/bin/python3
"""
initialize the models package
"""

from models.engine.file_storage import Filestorage

storage = Filestorage()
storage.reload()
