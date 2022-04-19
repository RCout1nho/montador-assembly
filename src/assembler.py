operators_ra_rb = {
    "ADD": "1000",
    "SHR": "1001",
    "SHL": "1010",
    "NOT": "1011",
    "OR": "1101",
    "XOR": "1110",
    "CMP": "1111",
    "LD": "0000",
    "ST": "0001",
}

operators_rb_addr = {
    "DATA": "0010",
}

operators_addr = {
    "JMP": "01000000",
    "JC": "01011000",
    "JA": "01010100",
    "JE": "01010010",
    "JZ": "01010001",
}

operators_nothing = {
    "CLF": "01100000"
}

registers = {
    "R0": "00",
    "R1": "01",
    "R2": "10",
    "R3": "11"
}


class Assembly:
    __hex_code = []
    __labels = {}

    # constructor
    def __init__(self, lines):
        # setting labels lines
        self.__set_labels__(lines)

        # reading code
        for line in lines:
            if(line[0] == '#' or line[0] == '\n'):
                continue
            hex_code = self.__get_hex_code__(line)
            if(hex_code):
                self.__hex_code.extend(hex_code)

    # @returns `hex_code`
    # `hex_code` is a list with all hexadecimal codes
    def get_hex_code(self):
        return self.__hex_code

    # @returns void
    # this function calculates the labels lines
    # Mandatorily should be runned before __get_hex_code__
    def __set_labels__(self, lines):
        cont = 0
        for line in lines:
            if(line[0] == '#' or line[0] == '\n'):
                continue
            words = line.split()
            operator = words[0]

            op_category, op_code = self.__get_operator_data__(operator)
            if(op_category == 'RB_ADDR' or op_category == 'ADDR'):
                cont += 2
            elif(op_category != 'LABEL'):
                cont += 1
            if(op_category == 'LABEL'):
                self.__labels[operator[:-1]] = cont

    # @returns `operator_category`, `operator_bin_code`
    # `operator_category` should be one of this: ['RA_RB', 'RA_ADDR', 'ADDR', 'NOTHING']
    # `operator_bin_code` should be a 4-bit binary code

    def __get_operator_data__(self, operator):
        if(operator in operators_ra_rb.keys()):
            return 'RA_RB', operators_ra_rb[operator]
        if(operator in operators_rb_addr.keys()):
            return 'RB_ADDR', operators_rb_addr[operator]
        if(operator in operators_addr.keys()):
            return 'ADDR', operators_addr[operator]
        if(operator in operators_nothing.keys()):
            return 'NOTHING', operators_nothing[operator]
        if(operator[-1] == ':'):
            return 'LABEL', None
        raise Exception('Operando inválido')

    # @returns `register_code`
    # `register_code` is the register binary code
    def __get_register_code__(self, register):
        if(register not in registers.keys()):
            raise Exception('Registrador inválido')
        return registers[register]

    # @returns `label_line`
    # `label_line` is the line where is the label
    def __get_label_line__(self, label):
        return self.__labels[label]

    # @returns `hex_code`
    def __get_hex_code__(self, line):
        words = line.split()

        if(len(words) == 1):
            operator = words[0]
        else:
            operator, operands = words[0], words[1]

        op_category, op_code = self.__get_operator_data__(operator)

        if(op_category == "RA_RB"):
            ra, rb = operands.split(',')

            bin_code = op_code + \
                self.__get_register_code__(ra) + self.__get_register_code__(rb)

            hex_code = f'{int(bin_code,2):X}'
            return [hex_code.zfill(2)]

        if(op_category == "RB_ADDR"):
            rb, addr = operands.split(',')

            addr_base = 10
            if(addr[0:2] == "0x"):
                addr_base = 16

            bin_code = op_code + "00" +\
                self.__get_register_code__(
                    rb) + format(int(addr, addr_base), 'b').zfill(8)

            hex_code = f'{int(bin_code,2):X}'
            return [hex_code[0:2], hex_code[2:]]

        if(op_category == 'ADDR'):
            jump_to = operands
            bin_code = op_code + \
                format(self.__get_label_line__(jump_to), 'b').zfill(8)
            hex_code = f'{int(bin_code,2):X}'
            return [hex_code[0:2], hex_code[2:].zfill(2)]

        if(op_category == 'NOTHING'):
            bin_code = op_code
            hex_code = f'{int(bin_code,2):X}'
            return [hex_code]