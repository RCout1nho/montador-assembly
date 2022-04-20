# Documentação

## Autor

José Ricardo Sampaio Coutinho II

## Sobre o Trabalho

Este trabalho consiste no desenvolvimento de um programa que emula a última etapa de um compilador para nosso computador de 8bits. Consiste em um **montador** que converte **assembly** em **binário**.

Este trabalho foi desenvolvido no contexto da disciplina de Organização de Computadores, ministrada pelo professor Juan Collona em 2022.

## Como executar

Para executar o programa, rode o seguinte comando no seu terminal:

```bash
python3 src/main.py nome_arquivo_entrada nome_arquivo_saida
```

`nome_arquivo_entrada` representa o nome do arquivo assembly que será compilado.

`nome_arquivo_saida` representa o nome do arquivo onde serão escritas as instruções em código hexadecimal no formato de interpretação da memória RAM do logisim.

## Sobre o arquivo assembly

### Registradores suportados

- R0
- R1
- R2
- R3

### Operações suportadas

### **Operações básicas**

| Operador | Operandos | Exemplo      |
| -------- | --------- | -------      |
| ADD      | Ra,Rb     | ADD R1,R2    |
| SHR      | Ra,Rb     | SHR R1,R2    |
| SHL      | Ra,Rb     | SHL R1,R2    |
| NOT      | Ra,Rb     | NOT R1,R2    |
| OR       | Ra,Rb     | OR R1,R2     |
| XOR      | Ra,Rb     | XOR R1,R2    |
| CMP      | Ra,Rb     | CMP R1,R2    |
| LD       | Ra,Rb     | LD R1,R2     |
| ST       | Ra,Rb     | ST R1,R2     |
| DATA     | Ra,Addr   | DATA R1,0x61 |
| JMP      | Label     | JMP loop     |
| CLF      |           | CLF          |

### **Jumps condicionais**

| Operador | Operandos | Exemplo    |
| -------- | --------- | ---------- |
| JZ       | Label     | JZ loop    |
| JE       | Label     | JE loop    |
| JEZ      | Label     | JEZ loop   |
| JA       | Label     | JA loop    |
| JAZ      | Label     | JAZ loop   |
| JAE      | Label     | JAE loop   |
| JAEZ     | Label     | JAEZ loop  |
| JC       | Label     | JC loop    |
| JCZ      | Label     | JCZ loop   |
| JCE      | Label     | JCE loop   |
| JCEZ     | Label     | JCEZ loop  |
| JCA      | Label     | JCA loop   |
| JCAZ     | Label     | JCAZ loop  |
| JCAE     | Label     | JCAE loop  |
| JCAEZ    | Label     | JCAEZ loop |

### **Operações de I/O**

| Operador | Operandos | Exemplo    |
| -------- | --------- | ---------- |
| IN       | tipo,Rb   | data,R0    |
| IN       | tipo,Rb   | addr,R1    |
| OUT      | tipo,Rb   | data,R2    |
| OUT      | tipo,Rb   | addr,R3    |

### **Observações**

Para montar uma linha de instrução, atente aos seguintes requisitos:

- Todo **operador** deve estar em **upper case**, da mesma forma que está escrito nas tabelas acima. Por exemplo: `ADD` é um operador válido, mas `add` não.

- Todo **registrador** deve estar em **upper case**, da mesma forma que está especificada anteriormete. Por exemplo: `R0` é um operador válido, mas `r0` não.

- O comentários devem sempre vir após "#". Por exemplo:`DATA R0,0x61 # comentário` ou apenas `# comentário` se for uma linha apenas com o comentário.

- Na instrução `DATA`, é possível passar como `addr` valores em **hexadecimal** ou em **decimal** positivos ou negativos, o próprio programa se encarrega de fazer as conversões necessárias. Para representar valores hexadecimais, use o prefixo "0x", por exemplo: `DATA R0,0x61`. Para representar valor decimais, basta o número, por exemplo: `DATA R0,15` ou `DATA R0,-5`.