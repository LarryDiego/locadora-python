listaJogos = ["Hollow Knight", "Dark Souls"]

opcao = -1

while opcao != 5:
  print()
  print("--- LOCADORA LARRY ---")
  print("1) Quantidade de jogos disponíveis")
  print("2) Listar jogos disponíveis")
  print("3) Adicionar um novo jogo")
  print("4) Locar um jogo")
  print("5) Sair")
  print()

  quantidadeJogos = len(listaJogos)

  opcao = int(input("O que você deseja fazer? "))
  print() 

  if opcao == 1:    
    print("Quantidade de jogos disponíveis:", quantidadeJogos)

  elif opcao == 2:
    if quantidadeJogos >= 1:
      print("Lista de jogos:")
      for i in range(quantidadeJogos):
        numeroLista = i + 1
        print(f"{numeroLista}) {listaJogos[i]}")
    else:
      print("Nenhum jogo disponível.")
  
  elif opcao == 3:
    novoJogo = input("Digite o nome do jogo que deseja adicionar: ")
    listaJogos.append(novoJogo)
    print()
    print(f"{novoJogo} foi adicionado com sucesso a lista de jogos.")
  
  elif opcao == 4:
    print("Locar um jogo (Ainda por fazer).")
  
  elif opcao == 5:
    print("Obrigado por usar a nossa locadora.")

  else:
    print("Opção inválida, por favor digitar uma das opção disponíveis.")