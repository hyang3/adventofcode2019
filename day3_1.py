f = open("input3.txt", "r")
wires = f.read.split("\n")

space = [[0 for i in range(2000)] for j in range(2000)]

for wire in wires:
    commands = wire.split(",") 
    for command in commands: 
