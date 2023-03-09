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
        args = arg.split()
        if len(arg) == 0:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in ['BaseModel']:
            print("** class doesn't exist **")
            return

        '''
            Extra feature (Because of ALX checker):
            Incase of excess Arguments tell the user it is not required
            if len(args) > 1:
            print("Excess ClassName (Not Required)")
        '''
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
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = class_name + "." + instance_id
        obj = storage.all().get(key)
        if obj is None:
            print("** No instance found **")
            return
        print(obj)

    def do_destroy(self, arg):
        """
        Delete an instance based on the className and Id,
        and update JSON storage file
        Usage: <destroy ClassName Id>
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
        if storage.all().get(key) is None:
            print("** no instance found **")
            return
        else:
            """Modify the abstract storage and save the modified version
            to the JSON file
            """
            del storage.all()[key]
            storage.save()

    def do_all(self, arg):
        """
        Print all string repr of all instances based or not
        on the class name

        Usage: <all classname> or <all>
        """
        args = arg.split()
        classes = ['BaseModel']
        if len(args) > 0:
            class_name = args[0]
            if class_name not in classes:
                print("** class doesn't exist **")
                return
            else:
                objs = storage.all()
        else:
            objs = storage.all()
        print([str(objs[obj]) for obj in objs])

    def do_update(self, arg):
        """Updates an instance based on the class name and id
        by adding or updating attribute. Saves change to JSON file.

        Usage: update <class name> <id> <attribute name> "<attribute value>"

        Only one attribute can be updated at a time.
        Attribute value is casted to attribute type
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
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = class_name + "." + instance_id
        if storage.all().get(key) is None:
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        elif len(args) == 3:
            print("** value missing **")
            return
        else:
            obj = storage.all()[key]
            if args[2] in type(obj).__dict__:
                v_type = type(obj.__class__.__dict__[args[2]])
                setattr(obj, args[2], v_type(args[3]))
            else:
                setattr(obj, args[2], args[3])
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
