#!/usr/bin/python3
"""This file contains the Holberton console class!"""

import models
import cmd


class HBNBCommand(cmd.Cmd):
    """ HBNH console """
    prompt = '(hbnb)'

    def do_author(self, line):
        """Program written by Carlos Galeano."""
        return True

    def emptyline(self):
        """Overwrites an emptyline."""
        pass

    def do_EOF(self, arg):
        """Quickly logs out of the terminal."""
        return True

    def do_quit(self, arg):
        """Quit command is used to exit the program."""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
