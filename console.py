#!/usr/bin/python3
"""
Defines the entry point of command interpreter
"""

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Creates command line interpreter for AirBnB console"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """CTRL+D function to abruptly but cleanly terminate program"""
        print("")
        return True

    def emptyline(self):
        """Do nothing when an empty line + ENTER is pressed"""
        pass

    def do_create(self, arg):
        """
        Usage: <create classname>
        Creates new instance of BaseModel. Saves it and prints id
        """
        if len(arg) == 0:
            print("** class name missing **")
            return

        class_name = arg.split()[0]
        if class_name not in ['BaseModel']:
            print("** class doesn't exist **")
            return

        new_instance = BaseModel()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """
        Usage: <show classname id>
        Prints the string representation of an instance based on
        class name and id
        """
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in ['BaseModel']:
            print("** class doesn't exist **")
            return

        if len(args) == 1:
            print("** instance id is missing **")
            return

        instance_id = args[1]
        key = class_name + "." + instance_id
        obj = storage.all().get(key)
        if obj is None:
            print("** No instance found **")
            return
        print(obj)



if __name__ == '__main__':
    HBNBCommand().cmdloop()
