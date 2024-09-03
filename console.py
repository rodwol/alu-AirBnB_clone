#!/usr/bin/python3
"""
This file serves as the entry point for the command interpreter,
allowing the user to interact with the app through CLI

"""


import cmd
import sys
import re
import shlex
import json
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class AluBnBCommand(cmd.Cmd):
    """ created a class
    """
    # class definition
    prompt = ">"
    
    """ command methods """
    def do_create(self, arg):
    # create a new instance
    if not arg:
        print("** class name missing **")
        return

    try:
        obj = eval(arg)() # create an instance
        obj.save() # save the instance to storage
        print(obj.id)
    except NameError:
        print("** class doesn't exist **")

    def do_show(self, arg):
    # show instance based on class name and ID
    args = arg.split()
    if len(args) == 0:
        print("** class name missing **")
        return
    if not self.validate_class_name(args[0]):
        print("** class doesn't exist **")
        return
    if len(args) == 1:
        print("** instance id missing **")
        return

    key = f"{args[0]}.{args[1]}"
    if key not in storage.all():
        print("** no instance found **")
    else:
        print(storage.all()[key])

    def do_destroy(self, arg):
    # to delete an instance based on class name and ID
    args = arg.split()
    if len(args) == 0:
        print("** class name missing **")
        return
    if not self.validate_class_name(args[0]):
        print("** class doesn't exist **")
        return
    if len(args) == 1:
        print("** instance id missing **")
        return

    key = f"{args[0]}.{args[1]}"
    if key not in storage.all():
        print("** no instance **")
    else:
        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
    # show all instances
    args = self.parse_args(arg)
    if len(args) == 0:
        objects = storage.all().values()
    elif self.validate_class_name(args[0]):
        objects = [obj for obj in storage.all().values() if type(obj).__name__ == arg]
    else:
        print("** class doesn't exist **")
        return

    print([str(obj) for obj in objects])

    def do_update(self, arg):
    # update an instance's attributes
    args = shlex.split(arg)
    if len(args) == 0:
        print("** class name missing **")
        return
    if not self.validate_class_name(args[0]):
        return
    if len(args) == 1:
        print("** instance id missing **")
        return

    key = f"{args[0]}.{args[1]}"
    if key not in storage.all():
        print("** no instance found **")
        return
    if len(args) == 2:
        print("** attribute name missing **")
        return
    if len(args) == 3:
        print("** value missing **")
        return

    obj = storage.all()[key]
    setattr(obj, args[2], args[3])
    obj.save()

    """ helper methods(with parsing and validating commands)
    """
    def parse_args(self, arg):
    # parse command arguments
    return shlex.split(arg)

    def validate_class_name(self, class_name):
    # validate if class name is correct
    if class_name not in storage.classes():
        print("** class doesn't exist **")
        return False
    return True

    """ default methods(handles unrecognized commands)"""
    def default(self, line):
    # handle unrecognized commands
    pass

    def do_EOF(self, line):
    print()
    return True

    def do_quit(self, arg):
    return True

    def emptyline(self):
    pass

if __name__ == '__main__':
    AluBnBCommand().cmdloop()
