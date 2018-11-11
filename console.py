#!/usr/bin/python3


import cmd, sys, os, json
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """comand line prompt for air bnb"""

    def do_show(self, line):
        """Shows a given Model"""
        models = ['BaseModel']
        if not line:
            print("** class name missing **")
        else:
            args = line.split(' ')
            if args[0] in models:
                if len(args) < 2:
                    print("** instance id missing **")
                elif os.path.exists('file.json'):
                    file_path = os.path.abspath("file.json")
                    with open(file_path, "r") as file:
                        dic = json.load(file)
                        ins_id = args[0] + '.' + args[1]
                        if ins_id in dic:
                            print(dic[ins_id])
                        else:
                            print("** no instance found **")
                else:
                    print("** no instance found no file**")
            else:
                print("** class doesn't exist **")

    def do_all(self, line):
        """Prints All Insteses of Spacific Model Type"""
        models = ["BaseModel"]
        if line in models:
            if os.path.exists('file.json'):
                file_path = os.path.abspath("file.json")
                with open(file_path, "r") as file:
                    """ INCORRECT FORMAT and Prints All!!!!!!!!!!!!!!!!!!!!"""
                    print("incorrect format")
                    print(file.read())
        else:
            print("** class doesn't exist **")

    def do_destroy(self, line):
        """Deletes a Spacific Object"""
        Models = ["BaseModel"]
        args = line.split(' ')
        if len(line) == 0:
            print("** class name missing **")
        elif args[1] not in Models:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            file_path = os.path.abspath("file.json")
            if os.path.exists('file.json'):
                with open(file_path, "r+") as file:
                    dic = json.loads(file):
                    inst = args[0] + '.' + args[1]
                    if inst in dic:
                        dic.pop(inst)
                        json.dump(dic, file)
                    else:
                        print("** no instance found **")

    def do_create(self, line):
        """Creates a new Model"""
        if line == "BaseModel":
            new = BaseModel()
            print(new.id)
        elif len(line) == 0:
            print("** class name missing **")
        else:
            print("** class doesn't exist **")

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """simply clicking enter goes to next line with prompt no other print"""
        if self.lastcmd:
            self.lastcmd = ""
            return self.onecmd(self.lastcmd)

    def do_quit(self, args):
        """Quit command to exit the program"""
        raise SystemExit

if __name__ == '__main__':
    prompt = HBNBCommand()
    prompt.prompt = '(HBNB) '
    prompt.cmdloop('')
