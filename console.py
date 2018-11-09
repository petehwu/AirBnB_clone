#!/usr/bin/python3
""" console that contains the entry point """

if __name__ == "__main__":

    import cmd

    class HBNBCommand(cmd.Cmd):
        """ the console for teh air bnb """
        
        prompt = "(hbtn)"

        def do_quit(self):
            """ the quit command """
            "Quit command to exit the program"
            return True

        def do_help(self):
            """ the help command """
            pass

        def do_EOF(self):
            """ EOF calls on quit """
            do_quit()

        def emptyline(self):
            """ do nothing """
            pass
