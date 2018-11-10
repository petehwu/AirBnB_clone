#!/usr/bin/python3
""" console that contains the entry point """

if __name__ == "__main__":

    import cmd

    class HBNBCommand(cmd.Cmd):
        """ the console for teh air bnb """
        
        prompt = "(hbtn) "

        def do_quit(self, line):
            """Quit command to exit the program
            """
            exit()

        def do_EOF(self, line):
            """ EOF calls on quit """
            do_quit()

        def emptyline(self):
            """ do nothing """
            pass

    HBNBCommand().cmdloop()
