#!/usr/env/python

import os

folder = ""

for file in os.listdir(folder):
    if file.endswith(".jfif"):
        print("Changing this one: " + file)
        old_name = os.path.join(folder, file)
        new_name = old_name[:-5]+".jpg"
        print("New name is this: " + new_name)
        os.rename(old_name, new_name)
