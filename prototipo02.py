while True:
    # Exibindo o menu inicial
    print("Menu Inicial:")
    print("1. Problemas Mecânicos")
    print("2. Problemas Elétricos")
    print("3. Requisitar Guincho")
    print("4. Sair")
    
    # Solicitando a escolha do usuário
    opcao_inicial = input("Selecione uma opção: ")
    
    # Verificando a opção escolhida no menu inicial
    match opcao_inicial:
        case "1":
            while True:
                # Exibindo o menu de problemas mecânicos
                print("\nMenu Problemas Mecânicos:")
                print("1. Verificar motor")
                print("2. Verificar freios")
                print("3. Verificar suspensão")
                print("4. Voltar ao menu inicial")
                
                # Solicitando a escolha do usuário
                opcao_mecanica = input("Selecione uma opção que se encaixe no seu problema: ")
                
                # Verificando a opção escolhida no menu de problemas mecânicos
                match opcao_mecanica:
                    case "1":
                        print("Motor verificado!")
                    case "2":
                        print("Freios verificados!")
                    case "3":
                        print("Suspenção verificada!")
                    case "4":
                        break
                    case _:
                        print("Opção inválida. Por favor, selecione uma opção válida.")
        
        case "2":
            while True:
                # Exibindo o menu de problemas elétricos
                print("\nMenu Problemas Elétricos:")
                print("1. Verificar bateria")
                print("2. Verificar fusíveis")
                print("3. Verificar alternador")
                print("4. Voltar ao menu inicial")
                
                # Solicitando a escolha do usuário
                opcao_eletrica = input("Selecione uma opção que se encaixe no seu problema: ")
                
                # Verificando a opção escolhida no menu de problemas elétricos
                match opcao_eletrica:
                    case "1":
                        print("Bateria verificada!")
                    case "2":
                        print("Fusiveis verificados!")
                    case "3":
                        print("Alternador verificado!")
                    case "4":
                        break
                    case _:
                        print("Opção inválida. Por favor, selecione uma opção válida.")
        
        case "3":
            # Exibindo o menu para chamar um guincho
            localizacao = input(print("Por favor, Insira o local no qual você se encontra:")) 
            print("Obrigado! Estamos enviando um guincho para", localizacao)

        case "4":
            print("Saindo.")
            break
        
        case _:
            print("Opção inválida. Por favor, selecione uma opção válida.")