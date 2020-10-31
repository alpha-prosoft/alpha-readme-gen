# Render PlantUML diagram in readme

Place README.md in src/ directory and add gen.sh file containing folowing code in root fo your repo: 
```bash
#!/usr/bin/env bash
python3 <(curl -s -L https://git.io/JTHXw)
```

Put our PlantUML diagrams in README file: 

```puml
@startuml
Class01 <|-- Class02
Class03 *-- Class04
Class05 o-- Class06
Class07 .. Class08
Class09 -- Class10
@enduml
```

You can use InteliJ plugin and it will render diagram four you during development. 

Then run: 

```
./gen.sh
```

It will analyze your `src/README.md` file and genearete `README.md` in root of the project. 
