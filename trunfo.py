# Import
import random
import json
from os import system, name


# Função para lima a tela a cada execução
def limpa_tela():

  # Windows
  if name == 'nt':
    _ = system('cls')

  # Mac ou Linux
  else:
    _ = system('clear')

# Função para exibir a carta do ADVERSARIO
def exibir_carta_adversario(carta_adversario):

    # Abrir o arquivo JSON com os dicionarios contendo os animais e seus atributos
    with open ('animais.json', 'r', encoding = 'utf-8') as lista_animais:
        animais = json.load(lista_animais)
        margem_carta = '--------------------'
        print(f'\n{margem_carta}\nA carta do seu Adversário é:\n|  {carta_adversario["nome"]}')
        for atributo, valor in carta_adversario["atributos"].items():
            print(f"| {atributo}: {valor}")
        print(margem_carta)
        print('\n')

# Função para exibir a carta do USUARIO
def exibir_carta_usuario(carta_usuario):

    # Abrir o arquivo JSON com os dicionarios contendo os animais e seus atributos
    with open ('animais.json', 'r', encoding = 'utf-8') as lista_animais:
        animais = json.load(lista_animais)
        margem_carta = '--------------------'
        print(margem_carta)
        print(f'|  {carta_usuario["nome"]}')
        for atributo, valor in carta_usuario["atributos"].items():
          print(f"|{atributo}: {valor}")
        print(margem_carta)
        print('\n')

# Função
def game():

  limpa_tela()

    # Abrir o arquivo JSON com a lista de animais
  with open ('animais.json', 'r', encoding = 'utf-8') as lista_animais:
    animais = json.load(lista_animais)

  print('Olá, vamos jogar super trunfo.\n')
  print('Ganhe 5 rodadas para vencer o jogo.')
  print('Você receberá uma carta aleatoria, boa sorte.\n')
  
  acertos = 0
  game_over = False

  while not game_over:

      # Escolher cartas novas a cada rodada
      carta_adversario = random.choice(animais)
      carta_usuario = random.choice(animais)  

      while True:
        try:
          exibir_carta_usuario(carta_usuario)
          escolha = int(input('escolha qual atributo comparar:\n 1 - Força\n 2 - Velocidade\n 3 - Inteligência\n'))
          
          # Comparando a força dos dois animais
          if escolha == 1:
            print('\nVocê escolheu Força.')
            exibir_carta_adversario(carta_adversario)
            if carta_usuario["atributos"]["forca"] > carta_adversario["atributos"]["forca"]:
              print(f"{carta_usuario['nome']} é mais forte que {carta_adversario['nome']}.")
              acertos += 1
              print(f'\nParabêns!\nVocê ganhou até agora {acertos} rodadas.')
              break

            elif carta_usuario["atributos"]["forca"] == carta_adversario["atributos"]["forca"]:
              print(f'A força da {carta_usuario["nome"]} e a {carta_adversario["nome"]}, como foi empate, você não pontua e será escolhida outra carta para você.')
              break

            else:
              print(f"{carta_adversario['nome']} é mais forte que {carta_usuario['nome']}.")
              print(f'\nQue pena, você perdeu com {acertos} rodadas ganhas.')
              game_over = True
              break

          # Comparando a velocidade dos dois animais
          elif escolha == 2:
            print('\nVocê escolheu Velocidade.')
            exibir_carta_adversario(carta_adversario)
            if carta_usuario["atributos"]["velocidade"] > carta_adversario["atributos"]["velocidade"]:
              print(f"{carta_usuario['nome']} é mais veloz que {carta_adversario['nome']}.")
              acertos += 1
              print(f'\nParabêns!\nVocê ganhou até agora {acertos} rodadas')
              break

            elif carta_usuario["atributos"]["velocidade"] == carta_adversario["atributos"]["velocidade"]:
              print(f'A velocidade da {carta_usuario["nome"]} e a {carta_adversario["nome"]}, como foi empate, você não pontua e será escolhida outra carta para você.')
              break

            else:
              print(f"{carta_adversario['nome']} é mais veloz que {carta_usuario['nome']}.")
              print(f'\nQue pena, você perdeu com {acertos} rodadas ganhas.')
              game_over = True
              break

          # Comparando a inteligencia dos dois animais
          elif escolha == 3:
            print('\nVocê escolheu Inteligência.')
            exibir_carta_adversario(carta_adversario)
            if carta_usuario["atributos"]["inteligencia"] > carta_adversario["atributos"]["inteligencia"]:
              print(f"{carta_usuario['nome']} é mais inteligente que {carta_adversario['nome']}.")
              acertos += 1
              print(f'\nParabêns!\nVocê ganhou até agora {acertos} rodadas')
              break

            elif carta_usuario["atributos"]["inteligencia"] == carta_adversario["atributos"]["inteligencia"]:
              print(f'A inteligencia da {carta_usuario["nome"]} e a {carta_adversario["nome"]}, como foi empate, você não pontua e será escolhida outra carta para você.')
              break

            else:
              print(f"{carta_adversario['nome']} é mais inteligente que {carta_usuario['nome']}.")
              print(f'\nQue pena, você perdeu com {acertos} rodadas ganhas.')
              game_over = True
              break

          else:
            print('Escolha inválida. Por favor, escolha 1, 2 ou 3.')
            continue

        except ValueError:
          print('Escolha invalida! Por favor, insira um numero inteiro.')

      if acertos >= 5:
        print('Parabêns você venceu o jogo!')
        game_over = True

      elif game_over:
        print('Fim de jogo, reinicie e tente novamente.')


# Bloco main
if __name__ == '__main__':
  game()
  print('\nObrigado por ter Jogado\n')