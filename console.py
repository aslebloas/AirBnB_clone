#!/usr/bin/python3


import cmd, sys, os, json
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """comand line prompt for air bnb"""

    def do_update(self, line):
        """Updates an instance by add ing or updating an attribute"""
        Models = ["BaseModel"]
        """ Need add More once More models exist"""
        args = line.split(' ')
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in Models:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            dic = storage.all()
            flag = 1
            for k, v in dic:
                key = k.split('.')
                if key[1] == args[2]:
                    flag = 0
                    if len(args) == 2:
                        print("** attribute name missing **")
                    elif len(args) == 3:
                        print("** value missing **")
                    else:
                        """ actual update"""
                        v[args[2]] = args[3]
                        v.save()
                if flag == 1:
                    print("** no instance found **")

    def do_show(self, line):
        """Shows a given Model"""
        models = ['BaseModel']
        """ Need Work once more models made"""
        if len(line) == 0:
            print("** class name missing **")
        else:
            args = line.split(' ')
            if args[0] in models:
                if len(args) < 2:
                    print("** instance id missing **")
                else:
                    dic = storage.all()
                    ins_id = args[0] + '.' + args[1]
                    if ins_id in dic:
                        st = ('[' + args[0] + '] (' + args[1] + ') ' +
                              str(dic[ins_id]))
                        print(st)
                    else:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_all(self, line):
        """Prints All Insteses of Spacific Model Type"""
        models = ["BaseModel"]
        """Add More Once more Models added"""
        if line in models:
            dic = storage.all()
            lst = []
            for k in dic.keys():
                key = k.split('.')
                if line == key[0]:
                    """ Needs work once mode models added"""
                    st = ('[' + line + '] (' + str(dic[k]['id']) + ') '
                          + str(dic[k]))
                    lst += [st]
            print(lst)
        else:
            print("** class doesn't exist **")

    def do_destroy(self, line):
        """Deletes a Spacific Object"""
        Models = ["BaseModel"]
        """Add Mode Once More Models added"""
        args = line.split(' ')
        if len(line) == 0:
            print("** class name missing **")
        elif args[0] not in Models:
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

    def do_create(self, line):
        """Creates a new Model"""
        if line == "BaseModel":
            new = BaseModel()
            print(new.id)
            new.save()
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
