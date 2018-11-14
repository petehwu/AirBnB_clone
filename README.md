OVERVIEW:
    -Make command interpreter to manage Airbnb objects


Future implementations:
    -Front end web dev, database storage, API


Goals:
    -Create parent class (BaseModel) that handles init, (de)serialization of instances
    -Translate data from |||||| Instance ←→ Dict ←→ JSON ←→ file
    -Create classes that inherit from BaseModel (User, State, City, Place, …)
    -Create file storage engine
    -UNITTESTS. For classes and storage engine


Command interpreter should be able to:
    -Create an object
    -Retrieve an object from a file, database, etc.
    -Compute the object
    -Update attributes on an object
    -Delete object


README OUTLINE:
    -Copy paste above
    -Add how to boot it and examples
    -Contributing Authors









Extra Trivia
How to create a Python package
https://docs.python.org/3.4/tutorial/modules.html#packages
A python file can be a module but if that file is in a folder, that colder is called a package. In python, packages are everywhere
In C we include, in python we import (from). 
Don’t forget the \_\_init\_\_.py file to make the folder into a module/ package
Use relative paths?????? 

How to create a command interpreter in Python using the cmd module
https://docs.python.org/3.4/library/cmd.html
Cmd is a class with lots of stuff
If you want a given stdin to be used, make sure to set the instance’s use\_rawinput attribute to False, otherwise stdin will be ignored.
Commands: cmdloop, onecmd, emptyline, default, completedefault, precmd, postcmd, preloop, postloop, prompt, indentchars, lastcmd, cmdqueue, intro, doc\_header, misc\_header, undoc\_header, ruler, use\_rawinput
Mainly useful for building custom shells and build an interactive program. 

What is Unit testing and how to implement it in a large project
https://docs.python.org/3.4/library/unittest.html#module-unittest
Checks for a specific response to a particular input.
Make tests before code. Fix code to get the right test outputs.
Many flags, many options, many assertions.
Can use skip test for newer code.
 Ask sumin for all the tests!!!!
Cheat sheet. https://www.pythonsheets.com/notes/python-tests.html

How to serialize and deserialize a Class
Can use Pickle
Resources Here

How to write and read a JSON file
Json dump to write. Json load to read. 
We need strings and dicts.
Use with. Please.
Loads takes string parameter and load takes file like object. read () returns a string object.

How to manage datetime
See time and calendar modules
2 types of date and time objects, naive and aware.
Aware is smart. Can do daylight savings and math. Aware is a specific moment in time and not interpreted. Aware has a time zone attribute (tzinfo).
Native is wtf. Up to program to tell it what it is. This is easy to understand and simple to work with.
https://docs.python.org/3.4/library/datetime.html 

What is an UUID
Universal Unique Identifier. https://docs.python.org/3.4/library/uuid.html
Generate random IDs. 128 bits. Generated on the basis of time. Advantage: general unique random. Can be used in cryptography and hashing. Useful when generating random addresses, documents, etc.
Uuid uses mac addresses and time.

What is \*args and how to use it
https://pythontips.com/2013/08/04/args-and-kwargs-in-python-explained/
Non keyword arguments given.

What is \*\*kwargs and how to use it
https://pythontips.com/2013/08/04/args-and-kwargs-in-python-explained/
Keywords given with the parameters

How to handle named arguments in a function
kwargs.

