def função_a():
    return ...

def função_b():
    return função_a()
def função_c():
    return função_b()

def função_d():
    return função_c()


breakpoint()
função_d()
print('Fim!')

'''
where -> muito bom pra analisar oq foi feito pra chegar onde vc ta do shell
    tipo uma lista dos steps onde vc entrou
    
Python é uma linguagem interpretada baseada em pilhas. Exemplo:
    Qnd uma funçao chama outra funçao, o python cria um novo nivel na pilha.
Esse estrutura é chamada de Frame.
'''