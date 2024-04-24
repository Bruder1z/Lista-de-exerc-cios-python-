expr = str(input('DIGITE A EXPRESSÃO: '))
pilha = []
for símb in expr:
    if símb == '(':
        pilha.append('(')
    elif símb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len (pilha) == 0:
    print('SUA EXPRESSÃO ESTÁ VÁLIDA')
else:
    print("SUA EXPRESSÃO ESTÁ INVÁLIDA")