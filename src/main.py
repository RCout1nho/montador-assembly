import assembler


def generate_logisim_ram_code(codes):
    with open('out.txt', 'w') as writer:
        cont = 0
        writer.write('v3.0 hex words addressed\n')
        for i in range(16):
            hex_code = f'{cont:X}'
            if(i > 0):
                writer.write(f'\n{hex_code.zfill(2).lower()}: ')
            else:
                writer.write(f'{hex_code.zfill(2).lower()}: ')
            for j in range(16):
                if(j < 16):
                    if(len(codes) > j+cont):
                        writer.write(codes[j+cont]+" ")
                    else:
                        writer.write("00 ")
                else:
                    if(len(codes) > j+cont):
                        writer.write(codes[j+cont-1])
                    else:
                        writer.write("00")
            cont += 16


file = open('src/in/assembly.txt', 'r')

lines = file.readlines()
instructions = assembler.Assembly(lines)

# print(instructions.get_hex_code())
generate_logisim_ram_code(instructions.get_hex_code())
