#!/usr/bin/python3
""" console that contains the entry point """

if __name__ == "__main__":
    # protects against execution when imported

    import cmd  # the library/ framework
    from models.base_model import BaseModel  # explicit import the base class
    import shlex  # need the split function to tokenize commands
    from models import storage  # we need the objects and data held in this

    class HBNBCommand(cmd.Cmd):
        """ The console for AirBnB,
        written by Peter Wu and Bryan Leung """

        prompt = "(hbtn) "  # the intranet's required prompt
        classes = {"BaseModel", "User", "State", "City",
                   "Amenity", "Place", "Review"}  # for tasks 8/ 9

        def do_quit(self, line):  # getting rid of parameters throws errors
            """Quit command to exit the program
            """
            exit()  # not sure if there is a desired return value

        def do_EOF(self, line):
            """ EOF calls on quit """
            do_quit()  # assuming EOF function does the same as do_quit

        def emptyline(self):
            """ do nothing """
            pass

        # The above is for Console 0.0.1
        # Below is for Console 0.1 or task 7 and onwards

        def do_create(self, line):
            """ creates new instance of BaseModel, saves to JSON file,
            and prints the ID """

            if len(line) < 1:  # if no arguments passed
                print("** class name missing **")
            elif line not in HBNBCommand.classes:
                print("** class doesn't exist **")  # if class doesn't exist
            else:
                new = eval(line)()  # execute the string argument into a shell
                print(new.id)  # prints the new id of the object we created
                new.save()  # serialize into JSON file

        def do_show(self, line):  # shows the class and id
            """ prints the string representation of an instance,
            based on the class name and id """

            classID = ""  # will store the input if >= 2 words
            if len(line) < 1:  # user just typed show into CLI
                print("** class name missing **")
                return
            tokenize = shlex.split(line)  # tokenize the input with split
            if tokenize[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")  # they typed a fake class
            elif len(tokenize) < 2:  # user typed a class with no ID
                print("** instance id missing **")
            else:  # we have 2 or more arguments now. should unit test this
                classID = tokenize[0] + "." + tokenize[1]
                # combines the 2 strings- class with the id
                if classID in storage.all().keys():
                    print(storage.all()[classID])  # prints the object!!
                # matching class and id is found in our storage, success!!!
                else:
                    print("** no instance found **")  # bad

    HBNBCommand().cmdloop()  # recursively loops back until exited or errors
