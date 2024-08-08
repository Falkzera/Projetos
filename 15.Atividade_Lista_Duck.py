
tarefa = []
lixeira = []

print('Comandos: listar, desfazer, refazer\n' 'Digite uma tarefa ou comando: ')

while True:

    execucao = input( ).strip().lower()
    
    if execucao == 'desfazer':

        try:
            lixeira.append(tarefa[-1])
            del tarefa[-1]
            print(tarefa)
        except  IndexError:
            print('Não há nada para desfazer')

    elif execucao == 'refazer':
        
        try: 
            refaz = lixeira[-1]
        except IndexError:
            print('Não há nada para refazer')   
        if refaz not in tarefa:
            tarefa.append(refaz)
            del lixeira[-1]
            print(tarefa)
        else:
            print('Já foi refeito')

        # pegar da lixeira e colocar de volta na lista

    elif execucao == 'sair':
        break

    else:
        tarefa.append(execucao)
        print(tarefa)