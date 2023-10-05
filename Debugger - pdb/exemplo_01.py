'''
Problema: linha 8 -> return (faltao o f)'{quem} está jantando {n} pratos de {c}'
mas o debugger ajuda a entender alem do traceback. Conseguimos assim verificar
quais partes apresentam problemas por meio dos breakpoint()
'''
def formatação(quem, n, c):
    return '{quem} está jantando {n} pratos de {c}'


nome = 'Gabriel'
quantidade_n = 2
comida = 'Lentilha'


#breakpoint()

formatado = formatação(nome, quantidade_n, comida)

#breakpoint()

# TESTE!
assert formatado == 'Gabriel está jantando 2 pratos de Lentilha'

'''
Comandos para usar no pdb.

n(ext) -> Avança o debugger para a proxima linha e a executa
s(tep) -> Entra no bloco, caso seja um bloco faz uma chama de funçao, exec
    de metodo e etc...
whatis -> Diz o tipo de algum objeto
c(cont(inue)) -> Avança o debugger ate o prox breakpoint
q(uit) / exit -> Sai do debugger
p -> printa algo no shell
vars() -> mostra as variaveis relacionadas ao escopo
locals -> o espoco local
where -> muito bom pra analisar oq foi feito pra chegar onde vc ta do shell
    tipo uma lista dos steps onde vc entrou
'''