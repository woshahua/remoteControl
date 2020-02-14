import os

# get all the environment variable of current system
def run(**args):
    print ("[*] in environment module.")
    return str(os.environ)