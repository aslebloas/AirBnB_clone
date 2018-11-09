#!/usr/bin/python3


import cmd, sys


class HBNBCommand(cmd.Cmd):
    """comand line prompt for air bnb"""

    def do_EOF(self, line):
        """quits program"""
        return True

    def help_EOF(self):
        """help line for eof"""
        print("EOF command to exit the program")

    def emptyline(self):
        """simply clicking enter goes to next line with prompt no other print"""
        if self.lastcmd:
            self.lastcmd = ""
            return self.onecmd(self.lastcmd)

    def do_quit(self, args):
        """quits program"""
        raise SystemExit

    def help_quit(self):
        print("Quit command to exit the program")

if __name__ == '__main__':
    prompt = HBNBCommand()
    prompt.prompt = '(HBNB)'
    prompt.cmdloop('')
