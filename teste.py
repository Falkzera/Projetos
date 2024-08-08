while True:
    try:
        number = int(input('Digite um número: ').strip())
        if number < 0:
            print('Digite apenas números positivos.')
            continue            
    except:
        print('Você não digitou um número.')
        continue


    fatorial = 1
    conta = 1

    while number >= fatorial:
        conta *= fatorial
    
        fatorial += 1
    print(f'O fatorial de {number} é {conta}')
    break
