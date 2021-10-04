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



plantuml_jar = sys.argv[1]
print("PlantUML jar: " + plantuml_jar)

shutil.rmtree("diagrams", ignore_errors=True)
os.mkdir("diagrams")


def process_file(source, md_name):
    print("Processing %s and generating %s" %(source, md_name))
    readme = open(source, 'r')
    lines = readme.readlines()


    diagram_number = 0
    diagram = False
    diagram_file = None

    out = open(md_name, "w")
    for line in lines:
        if line == "```\n" and diagram == True:
            print("Rendering diagram: %s" % (diagram_file.name))
            diagram_file.flush()
            diagram_file.close()
            proc = subprocess.Popen(["java", "-jar", plantuml_jar, diagram_file.name, "-tpng"], \
                                    stdout=subprocess.PIPE)
            proc.wait()

            out.write("\n>![Diagram](diagrams/" + md_name + "_" + str(diagram_number) + ".png)\n")
            diagram = False

        elif line.startswith("```puml"):
            print("Found diagram")
            diagram_number += 1
            name = ("diagrams/" + md_name + "_" + str( diagram_number) + ".puml")
            diagram_file = open(name, 'w')
            diagram = True
        elif diagram == True:
            diagram_file.write(line)
        else:
            out.write(line)

    out.close()
    readme.close()

for file in os.listdir("src"):
    if file.endswith(".md"):
        process_file(os.path.join("src", file), file)
