import sys
import assembler
import logisim

# get args
filename_in = sys.argv[1]
filename_out = sys.argv[2]

# open and read files
file = open(filename_in, 'r')
lines = file.readlines()

# instance of Assembly class
instructions = assembler.Assembly(lines)

# generate logisim RAM code file
logisim.generate_logisim_ram_code(instructions.get_hex_code(), filename_out)
