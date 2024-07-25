import random

def jogoAdivinhacao():
    numeroSecreto = random.randint(1, 100)
    tentativas = 10

    print("--- SEJA BEM-VINDO AO JOGO DA ADIVINHAÇÃO ---")
    print("\nEu escolhi um número aleatório de 1 a 100 para você tentar adivinhar.")
    print(f"Você tem {tentativas} tentativas para adivinhar.\n")

    for tentativa in range(1, tentativas + 1):
        palpite = int(input(f"Tentativa {tentativa}: "))
        
        if palpite < numeroSecreto:
            print("Muito baixo!")
        elif palpite > numeroSecreto:
            print("Muito alto!")
        else:
            print(f"Parabéns! Você acertou o número secreto {numeroSecreto} em {tentativa} tentativas!")
            break
    else:
        print(f"Desculpe, você não conseguiu adivinhar o número. O número correto era {numeroSecreto}.")

if __name__ == "__main__":
    jogoAdivinhacao()
