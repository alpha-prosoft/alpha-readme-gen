#!/usr/bin/env bash
plant_uml=$(mktemp)
curl $plant_uml -k -s -L https://github.com/alpha-prosoft/alpha-readme-gen/raw/master/plantuml.jar
python3 <(curl -s -L https://raw.githubusercontent.com/alpha-prosoft/alpha-readme-gen/master/plant-uml-render.py) $plant_uml
