#!/usr/bin/python3
"""
Defines the entry point of command interpreter
"""
import cmd

from models.base_model import BaseModel
from models import storage
from models.user import User
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Creates command line interpreter for AirBnB console"""
    prompt = '(hbnb) '
    available_classes = ['BaseModel',
                         'User',
                         'Place',
                         'State',
                         'City',
                         'Amenity',
                         'Review'
                         ]

    def do_quit(self, arg):
        """Quit command to exit the program
        """
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
        if class_name not in self.available_classes:
            print("** class doesn't exist **")
            return

        '''
            Extra feature (Because of ALX checker):
            Incase of excess Arguments tell the user it is not required
            if len(args) > 1:
            print("Excess ClassName (Not Required)")
        '''
        new_instance = eval(class_name)()
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
        if class_name not in self.available_classes:
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
        if class_name not in self.available_classes:
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
        objs = storage.all()
        if len(args) > 0:
            class_name = args[0]
            if class_name not in self.available_classes:
                print("** class doesn't exist **")
            else:
                output = []
                for k, v in objs.items():
                    if class_name == v.__class__.__name__:
                        output.append(str(objs[k]))
                print(output)
        else:
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
        if len(args) == 1:
            print("** instance id missing **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return

        class_name = args[0]
        instance_id = args[1]
        attribute_name = args[2]
        attribute_value = args[3].replace('"', '')
        if class_name not in self.available_classes:
            print("** class doesn't exist **")
            return
        key = class_name + "." + instance_id

        if storage.all().get(key) is None:
            print("** no instance found **")
            return

        obj = storage.all()[key]
        if attribute_name in type(obj).__dict__:
            '''v_type contains the type of the previous value so that we
               can cast the new value into the required data type
               else if it is not in the dict, store it fresh with a string type
               You can change the data type to your later when you run update
               in the future, it would be stored as that data type
            '''
            value_type = type(obj.__class__.__dict__[attribute_name])
            setattr(obj, attribute_name, value_type(attribute_value))

        else:
            setattr(obj, attribute_name, attribute_value)

        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
