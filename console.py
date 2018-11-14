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

    def default(self, line):
        """ the default function use model_type.function(args)"""
        if len(line) != 0:
            """formats the line for later use"""
            arg = line.split('.')
            typ = arg[0]
            if len(arg) != 1:
                args = arg[1].split('(')
                if len(args) != 1:
                    args[1] = args[1][:-1]
                    """checks the function type to call or do"""
                    if args[0] == 'all':
                        self.do_all(typ)
                    elif args[0] == 'show':
                        self.do_show(typ + ' ' + args[1])
                    elif args[0] == 'destroy':
                        self.do_destroy(typ + ' ' + args[1])
                    elif args[0] == 'update':
                        argss = args[1].split(',', 1)
                        if len(argss) > 1:
                            if argss[1][1] == '{':
                                """ Use of update with dictionary"""
                                dic = storage.all()
                                key = typ + '.' + argss[0]
                                obj = dic[key]
                                dicc = obj.to_dict()
                                """ formating dictionary str for use"""
                                argss[1] = argss[1][2:-1]
                                key_val = argss[1].split(', ')
                                for i in key_val:
                                    """ updateing object dictionary"""
                                    k_v = i.split(': ')
                                    dicc[k_v[0][1:-1]] = k_v[1][1:-1]
                                """ making new Model with updated dictionary"""
                                if typ == "BaseModel":
                                    new = BaseModel(**dicc)
                                elif typ == "User":
                                    new = User(**dicc)
                                elif typ == "State":
                                    new = State(**dicc)
                                elif typ == "City":
                                    new = City(**dicc)
                                elif typ == "Amenity":
                                    new = Amenity(**dicc)
                                elif typ == "Place":
                                    new = Place(**dicc)
                                elif typ == "Review":
                                    new = Review(**dicc)
                                """replace old obj with new one"""
                                new.save()
                            else:
                                """update without dictionary"""
                                argss[1] = argss[1][1:]
                                if len(argss) > 2:
                                    argss[2] = argss[2][1:]
                                    self.do_update(typ + ' ' + argss[0] +
                                                   ' ' + argss[1] + ' ' +
                                                   argss[2])
                                else:
                                    self.do_update(typ + ' ' + argss[0] + ' ' +
                                                   argss[1])
                        else:
                            """update without dictionary"""
                            self.do_update(typ + ' ' + argss[0])
                    elif args[0] == 'count':
                        dic = storage.all()
                        count = 0
                        for k in dic.keys():
                            key = k.split('.')
                            if key[0] == typ:
                                count += 1
                        print(count)
                    else:
                        """errors"""
                        print('*** Unknown syntax: ' + line)
                else:
                    print('*** Unknown syntax: ' + line)
            else:
                print('*** Unknown syntax: ' + line)

    def do_update(self, line):
        """Updates an instance by add ing or updating an attribute
        Args:
            line: line argument
        """

        args = line.split(' ', maxsplit=3)
        if len(line) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.models:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            dic = storage.all().copy()
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
                    else:
                        dictionary[args[2]] = str(string)
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
        Args:
            line: command line
        """

        if len(line) == 0:
            print("** class name missing **")
        else:
            args = line.split(' ')
            if args[0] in HBNBCommand.models:
                if len(args) < 2:
                    print("** instance id missing **")
                else:
                    dic = storage.all().copy()
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
        """Prints All Instances of Specific Model Type
        Args:
            line: command line
        """
        if len(line) == 0:
            dic = storage.all().copy()
            lst = []
            for k in dic.keys():
                lst.append(str(dic[k]))
            print(lst)
        elif line in HBNBCommand.models:
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
        flag = 0
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
            flag = 1
        else:
            print("** class doesn't exist **")
            flag = 1
        if flag == 0:
            new.save()
            print(new.id)

    def help_create(self):
        print("Creates a new Model\n")

    def help_create(self):
        print("Creates a new Model\n")

    def do_EOF(self, line):
        """EOF command to exit the program
        """
        return True

    def help_EOF(self):
        print("EOF command to exit the program\n")

    def emptyline(self):
        """simply clicking enter goes to next line
        with prompt no other print
        """
        pass

    def postloop(self):
        print()

    def do_quit(self, args):
        """Quit command to exit the program
        """
        return True

    def help_quit(self):
        print("Quit command to exit the program\n")

if __name__ == '__main__':
    prompt = HBNBCommand()
    prompt.prompt = '(hbnb) '
    prompt.cmdloop('')
