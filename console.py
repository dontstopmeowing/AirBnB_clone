#!/usr/bin/python3
"""This file contains the Holberton console class!"""

import models
from models.state import State
from models.review import Review
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.base_model import BaseModel
from models.user import User
import cmd
import shlex
from models.base_model import BaseModel
from models.user import User
classes = {
    "Amenity": Amenity,
    "BaseModel": BaseModel,
    "City": City,
    "Place": Place,
    "Review": Review,
    "State": State,
    "User": User
}


class HBNBCommand(cmd.Cmd):
    """ HBNH console """
    prompt = '(hbnb) '

    def default(self, args):
        """ Default methods """

        methods = ["all", "show", "destroy", "update", "count"]
        className = args.split(".", 1)
        if len(className) < 2:
            print("** Unknown syntax:", args)
            return
        if className[0] not in classes:
            print("** class doesn't exist **")
            return
        MethodName = className[1].split("(", 1)
        if MethodName[0] not in methods or len(MethodName) < 2:
            print("** Unknown syntax:", args)
            return
        MethodName[1] = MethodName[1].strip()
        if len(MethodName[1]) < 1 or MethodName[1][-1] != ')':
            print("** Unknown syntax:", args)
            return
        args = MethodName[1][:-1]
        if MethodName[0] == "show":
            return self.do_show(className[0] + " " + args)
        elif MethodName[0] == "all":
            return self.do_all(className[0])
        elif MethodName[0] == "destroy":
            return self.do_destroy(className[0] + " " + args)
        elif MethodName[0] == "count":
            return self.do_count(className[0])

    def do_author(self, args):
        """Program written by Carlos Galeano."""

        return True

    def emptyline(self):
        """Overwrites an emptyline."""

        pass

    def do_EOF(self, args):
        """Quickly logs out of the terminal."""

        return True

    def do_quit(self, args):
        """Quit command is used to exit the program."""

        return True

    def do_create(self, args):
        """ Creates an instance of a defined class."""

        if args:
            if args in classes:
                class_to_ins = classes.get(args)
                new_inst = class_to_ins()
                new_inst.save()
                print(new_inst.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_count(self, args):
        """Counts the number of created instances"""
        args = args.split()

        if len(args) < 1:
            print("** class name missing **")
            return
        count = 0
        objects = models.storage.all()
        for key in objects:
            if objects[key].__class__.__name__ == args[0]:
                count += 1
        print(count)

    def do_show(self, args):
        """
            Prints the string representation of
            an instance based on the class name and id.
        """

        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        else:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id."""

        args = args.split()
        if len(args) < 1:
            print("** class name missing **")
        else:
            if args[0] in classes:
                if len(args) < 2:
                    print("** instance id missing **")
                else:
                    try:
                        del models.storage.all()[args[0] + "." + args[1]]
                        models.storage.save()
                    except:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_all(self, args):
        """
            Prints all string representation of
            all instances based or not on the class name
        """

        args = args.split()
        dictionary = models.storage.all()
        my_list = []
        if len(args) < 1:
            for value in dictionary.keys():
                obj = dictionary[value]
                my_list.append("{}".format(obj))
            print(my_list)
        else:
            if args[0] in classes:
                for id_obj in dictionary.keys():
                    if args[0] in id_obj:
                        obj = dictionary[id_obj]
                        my_list.append("{}".format(obj))
                print(my_list)
            else:
                print("** class doesn't exist **")

    def do_update(self, args):
        """
            Updates an instance based on the class name and
            id by adding or updating attribute.
        """

        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj = models.storage.find_object(args[1])
        if obj:
            if len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                setattr(obj, args[2], args[3])
                models.storage.save()
        else:
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
