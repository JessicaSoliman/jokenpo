def jogar_jokenpo():
    opcoes = ["pedra", "papel", "tesoura"]
    joagdor1 = input("Escolha pedra, papel ou tesoura: ").lower()
    joagdor2 = input("Escolha pedra, papel ou tesoura: ").lower()

    if jogador1 not in opcoes or jogador2 not in opcoes:
        print("Jogada inválida! Tente novamente.")
        return
    
    print(f"\nJogador 1 escolheu: {jogador1}")
    print(f"Jogador 2 escolheu: {jogador2}")

    if jogador1 == jogador2:
        print("Empate!")
    elif (jogador1 == "pedra" and jogador2 == "tesoura") or \
         (jogador1 == "papel" and jogador2 == "pedra") or \
         (jogador1 == "tesoura" and jogador2 == "papel"):
        print("Jogador 1 venceu!")
    else:
        print("Jogador 2 venceu!")