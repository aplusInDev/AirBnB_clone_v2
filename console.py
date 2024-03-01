#!/usr/bin/python3
"""This module contains the entry point of the command interpreter"""

from models import *
import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""
    prompt = "(hbnb) "
    classes_list = ["BaseModel", "User", "State", "City", "Amenity", "Place",
                    "Review"]

    def do_help(self, arg):
        """Help command"""
        return super().do_help(arg)

    def do_EOF(self, line):
        '''end of file command to exit the program'''
        print()
        return True

    def do_quit(self, line):
        '''Quit command to exit the program
        '''
        return True

    def emptyline(self):
        """Empty line"""
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel"""

        if not line:
            print("** class name missing **")
            return

        arg_list = line.split()
        class_name = arg_list[0]
        if class_name not in HBNBCommand.classes_list:
            print("** class doesn't exist **")
            return
        new_instance = eval(class_name)()
        if len(arg_list) > 1:
            for param in arg_list[1:]:
                if "=" not in param:
                    return
                key = param.split("=")[0]
                value = param.split("=")[1]
                if value.startswith('"') and value.endswith('"'):
                    value = value[1:-1]
                try:
                    if 'id' not in key:
                        value = eval(value)
                    if type(value) is str:
                        value = value.replace("_", " ")
                except NameError:
                    pass
                setattr(new_instance, key, value)
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class
        name and id"""
        if not arg:
            print("** class name missing **")
        else:
            arg_list = arg.split()
            if arg_list[0] not in HBNBCommand.classes_list:
                print("** class doesn't exist **")
            elif len(arg_list) == 1:
                print("** instance id missing **")
            else:
                try:
                    all_objs = storage.all()
                    key = arg_list[0] + "." + arg_list[1]
                    if key in all_objs:
                        print(all_objs[key])
                    else:
                        print("** no instance found **")
                except ImportError:
                    print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file)"""
        if not arg:
            print("** class name missing **")
        else:
            arg_list = arg.split()
            if arg_list[0] not in HBNBCommand.classes_list:
                print("** class doesn't exist **")
            elif len(arg_list) == 1:
                print("** instance id missing **")
            else:
                try:
                    all_objs = storage.all()
                    key = arg_list[0] + "." + arg_list[1]
                    if key in all_objs:
                        del all_objs[key]
                        storage.save()
                    else:
                        print("** no instance found **")
                except ImportError:
                    print("** class doesn't exist **")

    def do_all(self, arg):
        """ Prints all string representation of all instances based
        """

        if arg and arg not in HBNBCommand.classes_list:
            print("** class doesn't exist **")
            return
        elif arg:
            try:
                class_name = eval(arg)
                all_objs = storage.all(class_name)
            except Exception:
                print("error")
        else:
            all_objs = storage.all()
        for value in all_objs.values():
            print(value)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file)"""
        if not arg:
            print("** class name missing **")
        else:
            arg_list = arg.split()
            if arg_list[0] not in HBNBCommand.classes_list:
                print("** class doesn't exist **")
            elif len(arg_list) == 1:
                print("** instance id missing **")
            else:
                try:
                    all_objs = storage.all()
                    key = arg_list[0] + "." + arg_list[1]
                    if key not in all_objs:
                        print("** no instance found **")
                    elif len(arg_list) == 2:
                        print("** attribute name missing **")
                    elif len(arg_list) == 3:
                        print("** value missing **")
                    else:
                        setattr(all_objs[key], arg_list[2],
                                " ".join(arg_list[3:]))
                        all_objs[key].save()
                except ImportError:
                    print("** class doesn't exist **")

    def do_count(self, arg):
        """Counts instances of a class"""
        try:
            all_objs = storage.all()
            count = 0
            for key in all_objs.keys():
                if arg in key:
                    count += 1
            print(count)
        except ImportError:
            print("** class doesn't exist **")

    def default(self, line):
        """ Default method """
        if ('.' in line and '(' in line and ')' in line):
            args = line.split('(')[1]
            args = args.split(')')[0]
            args = args.split(',')
            args = " ".join(args)
            line = line.replace('(', '.(')
            line = line.split('.')
            if len(line) > 1:
                if line[1] == "all":
                    self.do_all(line[0])
                elif line[1] == "count":
                    self.do_count(line[0])
                elif line[1] == "show":
                    self.do_show(line[0] + " " + args)
                elif line[1] == "destroy":
                    self.do_destroy(line[0] + " " + args)
                elif line[1] == "update":
                    self.do_update(line[0] + " " + args)
                else:
                    print("*** Unknown syntax: {}".format(line[1]))


if __name__ == "__main__":
    HBNBCommand().cmdloop()
