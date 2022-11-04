from os import listdir
from os.path import isfile, join

from demo import runDemo

PATH = 'video/'

files = list()

for file in listdir(PATH):
    if isfile(join(PATH, file)):
        if '.MOV' in file:
            file_path = PATH + file
            files.append(file_path)

for file in files:
    print(f"Running file '{file}'")
    runDemo(file)
    