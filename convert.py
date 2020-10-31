import os
import subprocess
import shutil
import argparse
import time
import re

# Argument parser
parser = argparse.ArgumentParser("Convert md to html")
parser.add_argument("-m", "--md")
parser.add_argument("-s", "--site")
args = parser.parse_args()

def modify_file(filepath):
    
    with open(filepath, 'r') as f:
        contents = f.read()
    
    if "image: " in contents:
        header = contents.split("image: ")[1].split("\n")[0]
        header_img = "![header_image](" + header[1:-1] + ")"
    else:
        header_img = ""

    
    new_contents = contents.split("---")[-1]
    #new_contents = re.sub("~~~bash", "~~~python", new_contents)
    #new_contents = re.sub("~~~c", "~~~python", new_contents)
    new_contents = re.sub("```shell", "```python", new_contents)

    new_contents = header_img + new_contents

    with open(filepath, 'w') as f:
        f.write(new_contents)

    return

def convert_file(filepath):
    title = filepath.split("/")[-1].split(".")[0]
    
    if "_posts" in filepath:
        title = " ".join(title.split("-")[3:])
    else:
        title = " ".join(title.split("-"))
    print(title)
    
    new_file = filepath[:-3] + ".html"
    open(new_file, 'a').close()

    with open(new_file, 'w') as f:
        o = subprocess.call(["markdown", "-h", "-t", title, "-s", "template.html", filepath], stdout=f)
        print(filepath)
    print("Done markdown conversion to html")
    return

result = [os.path.join(dp, f) for dp, dn, filenames in os.walk(args.md) for f in filenames if os.path.splitext(f)[1] == '.md']

print(result)

newFiles = []
for f in result:
    f1 = f.strip(args.md)
    print("Found {}".format(f1))
    
    d = "/".join(f1.split('/')[:-1])
    print(d)
    newdir = os.path.join(os.path.join(os.getcwd(), args.site), d)

    print("New DIR : {}".format(newdir))
    if not os.path.isdir(newdir):
        os.mkdir(newdir)
        print("Created directory {}".format(newdir))
    
    new_file = os.path.join(newdir,f.split("/")[-1])
    shutil.copyfile(f, new_file)
    print("Created {}".format(new_file))
    
    modify_file(new_file)
    convert_file(new_file)
    os.remove(new_file)

    print(f)
