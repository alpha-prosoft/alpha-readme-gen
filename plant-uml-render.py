#!/usr/bin/env python3
import urllib.request

import tempfile
import subprocess
import base64
import os
import shutil
import os.path
import sys

from urllib.request import urlopen


source = 'resource/README.md'
if not os.path.isfile(source):
    print("No %s file found" % (source))
    sys.exit(1)

plantuml_jar = sys.argv[1]
print("PlantUML jar: " + plantuml_jar)

readme = open(source, 'r')
lines = readme.readlines()

count = 0
# Strips the newline character

block = ""
diagram = False
diagram_number = 0

diagram_file = None

out = open("README.md", "w")
shutil.rmtree("diagrams", ignore_errors=True)
os.mkdir("diagrams")

for line in lines:
    if line == "```\n" and diagram == True:
        print("Renderng diagram: %s" % (diagram_file.name))
        diagram_file.flush()
        diagram_file.close()
        proc = subprocess.Popen(["java", "-jar", plantuml_jar, diagram_file.name, "-tsvg"], \
                                stdout=subprocess.PIPE)
        proc.wait()

        out.write("\n>![Diagram](diagrams/" + str(diagram_number) + ".svg)")
        diagram = False

    elif line.startswith("```puml"):
        print("Found diagram")
        diagram_number += 1
        name = ("diagrams/" + str(diagram_number) + ".puml")
        diagram_file = open(name, 'w')
        diagram = True
    elif diagram == True:
        diagram_file.write(line)
    else:
        out.write(line)

out.close()
readme.close()
