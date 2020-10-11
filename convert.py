import os
import argparse

# Argument parser
parser = argparse.ArgumentParser("Convert md to html")
parser.add_argument("-m", "--md")
parser.add_argument("-s", "--site")
args = parser.parse_args()


result = [os.path.join(dp, f) for dp, dn, filenames in os.walk(args.md) for f in filenames if os.path.splitext(f)[1] == '.md']
print(result)


newFiles = []
for f in os.listdir(args.md):
    #if os.isdir(f)

    print(f)
