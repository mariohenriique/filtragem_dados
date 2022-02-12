arquivo = open('parametros.txt', 'r')
with open('parametro_para_rodar_programa.txt','w') as arquivopronto:
  for e in range(3): 
    semlinha = arquivo.readline()
    semlinhas = ''.join(semlinha.split()) 
    arquivopronto.write(semlinhas + '\n')
arquivo.close()

#(criar uma variavel q ler um arquivo dos parametros que serão utilizados) (colocar um modelo de como será este arquivo no programa)

#importar o pacote pandas

import pandas as pd

arquivo = pd.read_csv('parametro_para_rodar_programa.txt')

df_test = pd.DataFrame(arquivo)

df_test.head()

for i in range(len(df_test)):
  #criar uma variavel e usar o pandas para ler o arquivo
  aglomerados = pd.read_csv(df_test.nomedoarquivo.iloc[i])

  #transformar o arquivo em um dataframe
  parametro = pd.DataFrame(aglomerados)

  #mostrar os primeiros elementos do dataframe
  parametro.head()

  #filtro = parametro#['Nper'] > 8 (aplicar a equação 1 do filtro do arenou)
  #filtro_arenou1 = parametro[filtro]
  #filtro_arenou1.head()

  #filtro = filtro_arenou1#['Nper'] > 8 (aplicar a equação 2 do filtro do arenou)
  #filtro_arenou2 = filtro_arenou1[filtro]
  #filtro_arenou2.head()

  #mudar nome da variável parametro depois q colocar a equação 1 e 2
  if df_test.equação3.iloc[0] == 0:
    filtro_arenou3 = parametro[parametro['Nper'] > 8]
    filtro_arenou3.head()

  #o usuário irá definir qual o corte para Gmag
  #G = float (input('Qual o corte a ser realizado para Gmag? '))
  #Gma = df_test['G'].iloc[0]

  #definir uma lista com os valores em que o parametro é menor que o
  #fornecido anteriormente
  filtro_Gmag = filtro_arenou3[filtro_arenou3['Gmag'] < G[i]]
  filtro_Gmag.head()

  #Perguntar ao usuário qual o corte a ser realizado em BP_RP
  #BP = float (input('Qual o corte a ser realizado para BP-RP? '))

  #aplicar o corte na coluna 'BP-RP'
  filtro_BPRP = filtro_Gmag[filtro_Gmag['bp_rp'] < BP[i]]
  filtro_BPRP.head()

  #nome = input('Qual o nome do arquivo? ')

  with open(nomearquivofinal[i],'w') as arquivo:
  #adicionei o 'a' como nome de uma coluna já que ao escrever o 
    arquivo.write('# a')
    filtro_BPRP.to_csv(arquivo)