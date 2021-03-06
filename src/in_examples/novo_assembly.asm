DATA R1,0x50      # 21 50  inicio dos valores

leitura: # dec=2 hex = 2
DATA R2,0x01      # 22 01 contador 
DATA R0,0x64      # 20 64 endereco do teclado
OUT addr,R0  # 7c
IN data,R3      # 73    le o teclado

XOR R0,R0       # e0
CMP R0,R3       # f3    compara se ainda tem coisa pra ler 
JE imprimir          # 52 15 se o carecter lido == 0 (não exiSTe caracter)

ADD R2,R1       # 89   valor_inicial+=1

# complemento de 2 do numero 20
DATA R0,0x20      # 20 20
NOT R0,R0       # b0
ADD R2,R0       # 88

ADD R0,R3       # 83  subtrai 20 de R3

ST R1,R3        # 17
JMP leitura     # 40 02


imprimir: # dec=21 hex=15
DATA R0,0x61      # 20 61
OUT addr,R0  # 7c

XOR R3,R3       # ef

LD R1,R2        # 06

CMP R2,R3       # fb     compara para saber se ja leu todos os valores
JE fim          # 52 28

OUT data,R2     # 7a

XOR R0,R0       # e0
DATA R0,0x1       # 20 01

# complemento de 2 do número 1
DATA R2,0x1       # 22 01
NOT R2,R2       # ba
ADD R0,R2       # 82

ADD R2,R1       # 89 subtrai 1

JMP imprimir    # 40 15

fim: # dec=40 hex=28
JMP fim         # 40 28
