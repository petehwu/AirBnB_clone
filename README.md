# AirBnB Clone Part 1 by Peter Wu and Bryan Leung

## OVERVIEW:
    This repo contains the basis of our AirBnB project.
    We made a command line interface(CLI) to manage and manipulate Airbnb-like objects. Such objects are Users, Places, Places, Reviews, Amenities, etc. And Python is the language used so every one of our data points are their own classes, which are objects or dicts that stores attributes and info.

## How to run this Repo:

    * git clone this repo  
    * cd into that directory and type "./console.py", you should be prompted with "(hbnb) " and that is our command line interpreter that we made.
    * type "quit" or "ctrl/cmd + c" or "ctrl/cmd + d" to quit.
    
## Examples
If you installed correctly, typing ./consoly.py in the command should give you this following prompt.
    
    (hbnb)

Here we can type all which should display the file.json. If there is no file, an empty list is printed.

    (hbnb) all
    []
    (hbnb) create BaseModel
    f10f6866-410c-4299-a280-b4092478c6dd
    (hbnb) all
    ["[BaseModel] (f10f6866-410c-4299-a280-b4092478c6dd) {'id': 'f10f6866-410c-4299-a280-b4092478c6dd', 'created_at': datetime.datetime(2018, 11, 15, 5, 1, 18, 87626), 'updated_at': datetime.datetime(2018, 11, 15, 5, 1, 18, 87670)}"]


There are many other functions with a required amount of arguments, here are some with their output if there was no file.json. Keep in mind your id and values returned back will vary and will not match exactly:
    
    (hbnb) create User
    170fd5df-bca7-40b1-80b6-d6f6344e789e
    (hbnb) show User 170fd5df-bca7-40b1-80b6-d6f6344e789e
    [User] (170fd5df-bca7-40b1-80b6-d6f6344e789e) {'created_at': datetime.datetime(2018, 11, 15, 5, 5, 15, 663720), 'id': '170fd5df-bca7-40b1-80b6-d6f6344e789e', 'updated_at': datetime.datetime(2018, 11, 15, 5, 5, 15, 663778)}
    (hbnb) update User 170fd5df-bca7-40b1-80b6-d6f6344e789e diablo "Immortal"
    (hbnb) 
    (hbnb) show User
    ** instance id missing **
    (hbnb) show User 170fd5df-bca7-40b1-80b6-d6f6344e789e
    [User] (170fd5df-bca7-40b1-80b6-d6f6344e789e) {'id': '170fd5df-bca7-40b1-80b6-d6f6344e789e', 'diablo': 'Immortal', 'updated_at': datetime.datetime(2018, 11, 15, 5, 5, 15, 663778), 'created_at': datetime.datetime(2018, 11, 15, 5, 5, 15, 663720)}
    (hbnb) destroy User 170fd5df-bca7-40b1-80b6-d6f6344e789e
    (hbnb) show User 170fd5df-bca7-40b1-80b6-d6f6344e789e
    ** no instance found **
    
So if an invalid number or value of arguments is entered, the console will report back. Some error string examples include "** class name missing \*\*", "\*\* class doesn't exist \*\*", and "\*\* attribute name missing \*\*".
    
Our currently implemented classes are BaseModel, User, State, City, Amenity, Place, and Review.  
Extra methods are "<class name>.all()", "<class name>.count()", "<class name>.show(<id>)", "<class name>.destroy(<id>)", "<class name>.update(<id>, <attribute name>, <attribute value>)", and "<class name>.update(<id>, <dictionary representation>)".
    
Each class has their own unit tests and they are still unfinished. There will be more included tests.  


#### TLDR Goals:  
The goals of this repo were to create a base model (BaseModel)
    * Create parent class (BaseModel) that handles initialization and (de)serialization of instances
    * Translate data from |||||| Instance ←→ Dict ←→ JSON ←→ file
    * Create classes that inherit from BaseModel (User, State, City, Place, …)
    * Create file storage engine
    * UNITTESTS. For classes and storage engine


Command interpreter should be able to:
    * Create an object
    * Retrieve an object from a file, database, etc.
    * Compute the object
    * Update attributes on an object
    * Delete object


#### Other Contributors
    Thank you to all other students from our cohort. We worked together on many problems and unittests. 

#### Future implementations:
    We will add the Front end client side where the user can look up each location marker, which we assume would store data that is relevant to the consumer. Languages used will be the web dev trifecta, at minimum.
    We will also include database storage to hold all the information and data about each venue or listing. We will use some version of SQL to query the database and fetch data.
    We will integrate APIs with the project. Some examples can be Google Maps API for location and relevant info. Another great API is FourSquare and that has a great venue API that a user can use to look up nearby venues which can help them decide on their location of stay.



### Extra Trivia
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

