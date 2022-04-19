import assembler

file = open('src/in/assembly.txt', 'r')

lines = file.readlines()
instructions = assembler.Assembly(lines)

print(instructions.get_hex_code())
