import os


# list all the files in current directory
def run(**args):
    print ("[*] in dirlister module")
    files = os.listdir(".")

    return str(files)