#permits to find a specific file that contains a certain word. To use in case there are different files with the same name

import os

result = []

def find_files(filename, search_path, word):
    global result

    for root, dirs, files in os.walk(search_path):
      if filename in files:
         result.append(os.path.join(root, filename))
    print(result)


    a = 0
    c = []

    for file in result:
        with open(file,"r") as fp:
            lines = fp.readlines()
        for row in lines:
            if word in row:
                b = a +1
                c.append(b)
                
            if word in row:
                print("word found in\n", file)
                break
    
    print("numbers of file found containing the word:",sum(c))

find_files("ofApp.cpp","/Users/leonardobasso/", "visualizer")

print("numbers of files with the same name:", len(result))