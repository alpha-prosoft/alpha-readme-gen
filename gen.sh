#!/usr/bin/env bash
plant_uml="$(mktemp).jar"
curl -o $plant_uml -k -s -L https://raw.githubusercontent.com/alpha-prosoft/alpha-readme-gen/master/plantuml.jar
python3 <(curl -s -L https://raw.githubusercontent.com/alpha-prosoft/alpha-readme-gen/master/plant-uml-render.py) $plant_uml
