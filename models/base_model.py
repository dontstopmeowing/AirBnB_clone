#!/usr/bin/python3
"""Creating a class base model"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """Base model class"""

    def __init__(self, *args, **kwargs):
        """Initialization of the base model"""

        if kwargs:
            self.__dict__ = kwargs
            if "created_at" in kwargs:
                self.created_at = self.__dict__["created_at"] = datetime.now()
            if "updated_at" in kwargs:
                self.updated_at = self.__dict__["updated_at"] = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """String representation of the class itself."""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """Updates the attribute 'updated_at' with current time."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a new dic with the class values."""
        self.__dict__["__clas__"] = __class__.__name__
        self.__dict__["created_at"] = self.created_at.isoformat()
        self.__dict__["updated_at"] = self.updated_at.isoformat()

        return self.__dict__
