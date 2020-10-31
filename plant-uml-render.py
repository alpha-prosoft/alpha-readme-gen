#!/usr/bin/env python3

import tempfile
import subprocess
import base64
import os
import shutil
import os.path

source = 'src/README.md'
if not os.path.isfile(source):
    print("No %s file found" % (source))
    exit 1

readme = open(source, 'r')
lines = readme.readlines()

count = 0
# Strips the newline character

block = ""
diagram = False
diagram_number = 0

diagram_file = None

out = open("README.md", "w")
shutil.rmtree("diagrams")
os.mkdir("diagrams")

for line in lines:
    if line == "```\n" and diagram == True:
        print("Diagram end: %s" % (diagram_file.name))
        diagram_file.flush()
        diagram_file.close()
        proc = subprocess.Popen(["java", "-jar", "plantuml.jar", diagram_file.name], \
                                stdout=subprocess.PIPE)
        proc.wait()

        out.write("\n>![Diagram](diagrams/" + str(diagram_number) + ".png)")
        diagram = False;

    elif line.startswith("```puml"):
        print("Diagram start")
        diagram_number += 1
        name = ("diagrams/" + str(diagram_number) + ".puml")
        diagram_file = open(name, 'w')
        diagram = True;
    elif diagram == True:
        print("Writing")
        diagram_file.write(line)
    else:
        out.write(line)

out.close()
readme.close()

