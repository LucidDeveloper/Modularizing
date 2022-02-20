'''@ author
Gianni M. Javier
'''

# Import paretn into child

import parent

# Notice that all of the code from parent.py
# executed when ran the file after importing
# This means that every print statement and variable
# instantiation is still happening upon import

print(locals())
# Sees what variables are availale at any given space
# and see what variables are available in current 
# namespace

# We see a dictionary containing the key value pairs
# from the keys name, doc, package, loader, 
# spec, annotations, builtins, file,
# cached, and parent.

# The object that prints will be a dictionary where 
# the variable names are keys and the objects they
# reference are the values. Understanding namespace 
# will help you understand the next portion, where 
# we will use namespace to control the functionality
# that is imported with our document.
