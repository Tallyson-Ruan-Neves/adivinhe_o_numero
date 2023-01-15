simounao = 'sim'.upper()
while simounao != 'NÃO' and simounao == 'SIM':
  import random
  tent = 0
  comput = random.randint(0, 10)
  print(
    ' Eu sou seu computador...Estou pensando em um número...tente adivinhar!!!'
  )
  jogador = int(input('Qual é seu palpite? '))
  tent += 1
  while comput != jogador:
    if jogador < comput:
      print('mais...')
    if jogador > comput:
      print('menos...')
    jogador = int(input('tente novamente!'))
    tent += 1
  if jogador == comput:
    print(
      'acertou...o numero que eu estava pensando era {}, voçê acertou com {} tentativas!'
      .format(comput, tent))

  simounao = str(input('Quer continuar? ')).upper()
  if simounao != 'SIM' and simounao != 'NÃO':
    while simounao != 'SIM' and simounao != 'NÃO ':
      simounao = str(input('\033[31mtente novamente\033[m ')).upper()
