#!/usr/bin/python3
"""Module for the console"""
import cmd
import json
import os
import sys
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    """comand line prompt for air bnb
    """
    models = ["BaseModel", "User", "State", "City", "Amenity", "Place",
              "Review"]
    str_atts = ["name", "state_id", "city_id", "user_id", "description",
                "place_id", "user_id", "text", "email", "password",
                "first_name", "last_name"]
    int_atts = ["number_rooms", "number_bathrooms", "max_guest",
                "price_by_night"]
    float_atts = ["latitude", "longitude"]

    def do_update(self, line):
        """Updates an instance by add ing or updating an attribute
        """
        """
        Args:
            line: line argument
        """

        """ Need add More once More models exist"""
        args = line.split(' ')
        if len(line) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.models:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            dic = storage.all()
            key = args[0] + '.' + args[1]
            if key in dic:
                if len(args) == 2:
                    print("** attribute name missing **")
                elif len(args) == 3:
                    print("** value missing **")
                else:
                    """ actual update"""
                    dictionary = dic[key].to_dict()
                    string = args[3][1:-1]
                    if args[2] in HBNBCommand.str_atts:
                        dictionary[args[2]] = str(string)
                    elif args[2] in HBNBCommand.int_atts:
                        dictionary[args[2]] = int(string)
                    elif args[2] in HBNBCommand.float_atts:
                        dictionary[args[2]] = float(string)
                    elif args[2] == "amenity_ids":
                        dictionary[args[2]] = list(string)
                    """ change once mode models exist"""
                    if args[0] == "BaseModel":
                        new = BaseModel(**dictionary)
                    elif args[0] == "User":
                        new = User(**dictionary)
                    elif args[0] == "State":
                        new = State(**dictionary)
                    elif args[0] == "City":
                        new = City(**dictionary)
                    elif args[0] == "Amenity":
                        new = Amenity(**dictionary)
                    elif args[0] == "Place":
                        new = Place(**dictionary)
                    elif args[0] == "Review":
                        new = Review(**dictionary)
                    new.save()
            else:
                print("** no instance found **")

    def help_update(self):
        print("Updates an instance by add ing or updating an attribute\n")

    def do_show(self, line):
        """Shows a given Model
        """
        """
        Args:
            line: command line
        """
        """ Need Work once more models made"""
        if len(line) == 0:
            print("** class name missing **")
        else:
            args = line.split(' ')
            if args[0] in HBNBCommand.models:
                if len(args) < 2:
                    print("** instance id missing **")
                else:
                    dic = storage.all()
                    ins_id = args[0] + '.' + args[1]
                    if ins_id in dic:
                        print(dic[ins_id])
                    else:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def help_show(self):
        print("Shows a given Model\n")

    def do_all(self, line):
        """Prints All Insteses of Spacific Model Type
        """
        """
        Args:
            line: command line
        """
        """Add More Once more Models added"""
        if len(line) == 0:
            dic = {}
            dic = storage.all().copy()
            lst = []
            for k in dic.keys():
                lst.append(str(dic[k]))
            print(lst)
        elif line in HBNBCommand.models:
            dic = {}
            dic = storage.all().copy()
            lst = []
            for k in dic.keys():
                args = k.split('.')
                if line == args[0]:
                    lst.append(str(dic[k]))
            print(lst)
        else:
            print("** class doesn't exist **")

    def help_all(self):
        print("Prints All Insteses of Spacific Model Type\n")

    def do_destroy(self, line):
        """Deletes a Spacific Object
        """
        """
        Args:
            line: Command line
        """
        """Add Mode Once More Models added"""
        args = line.split(' ')
        if len(line) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.models:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            dic = storage.all()
            inst = args[0] + '.' + args[1]
            if inst in dic:
                dic.pop(inst)
                storage.save()
            else:
                print("** no instance found **")

    def help_destroy(self):
        print("Deletes a Spacific Object\n")

    def do_create(self, line):
        """Creates a new Model
        """
        """
        Args:
            line: command line
        """
        if line == "BaseModel":
            new = BaseModel()
        elif line == "User":
            new = User()
        elif line == "State":
            new = State()
        elif line == "City":
            new = City()
        elif line == "Amenity":
            new = Amenity()
        elif line == "Place":
            new = Place()
        elif line == "Review":
            new = Review()
        elif len(line) == 0:
            print("** class name missing **")
        else:
            print("** class doesn't exist **")
        new.save()
        print(new.id)

    def help_create(self):
        print("Creates a new Model\n")

    def do_EOF(self, line):
        """EOF command to exit the program
        """
        return SystemExit

    def help_EOF(self):
        print("EOF command to exit the program\n")

    def emptyline(self):
        """simply clicking enter goes to next line
        with prompt no other print
        """
        if self.lastcmd:
            self.lastcmd = ""
            return self.onecmd(self.lastcmd)

    def do_quit(self, args):
        """Quit command to exit the program
        """
        raise SystemExit

    def help_quit(self):
        print("Quit command to exit the program\n")

if __name__ == '__main__':
    prompt = HBNBCommand()
    prompt.prompt = '(HBNB) '
    prompt.cmdloop('')
