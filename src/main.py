instructions = {
  "ADD": "1000",
  "SHR": "1001",
  "SHL": "1010",
  "NOT": "1011",
  "OR": "1101",
  "XOR": "1110",
  "CMP": "1111",
  "LD": "0000",
  "ST": "0001",
  "DATA": "0010",
  "JMP": "0100",
  "CLF": "0110"
}

file = open('src/in/assembly.txt', 'r')

lines = file.readlines()
quantity_of_lines = len(lines)

for i in range(quantity_of_lines):
  cur_line = lines[i]
  
  # Verify if is a comment
  if(cur_line[0] == '#' or cur_line[0] == '\n'):
    continue
  
  words = cur_line.split()
  if(words[0] in instructions.keys()):
    # É uma instrição
    print("Binary code:", instructions[words[0]])
  
  
  