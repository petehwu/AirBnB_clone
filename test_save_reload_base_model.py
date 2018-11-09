#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new object --")
print(1)

my_model = BaseModel()
print(2)

my_model.name = "Holberton"
print(3)

my_model.my_number = 89
print(4)

my_model.save()
print(5)

print(my_model)
