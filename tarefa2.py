import re
import time
import random
import os
import sys
from os import system, name
from tqdm import tqdm
# -*- coding: utf-8 -*-
#ataque de força bruta em cifra de cesar e em cifra monoalfabetica

# define our clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 



def DesenhaTelaMono():
    print("+-------------------------------------------+")
    print("|=== Decriptador de cifra monoalfabética ===|")
    print("+-------------------------------------------+\n")




def DesenhaTelaCesar():
    print("+-------------------------------------+")
    print("|=== Decriptador de cifra de césar ===|")
    print("+-------------------------------------+\n")



def monoalphabeticSolver(textoEncriptado):
    #seta os dois alfabetos usados, um mantem a forma original e o outro é embaralhado
    alfabeto = ["A", "E", "O", "C", "L", "P", "R", "T"]
    #alfabeto que sera embaralhado
    alfabetoRand = ["A", "E", "O", "C", "L", "P", "R", "T"]
    #variavel de controle do loop
    retorno = False
    contador = 0
    qnt = 0

    textoEncriptado = textoEncriptado.upper()

    clear()
    DesenhaTelaMono()
    if len(textoEncriptado) > 6:
        print("!!! Palavra é maior que 6 caracteres !!!")
        print("    Finalizando ", end="")
        time.sleep(1)
        print(". ", end="")
        time.sleep(1)
        print(". ", end="")
        time.sleep(1)
        print(". ", end="")
        time.sleep(1)
        print(". ", end="")
        time.sleep(1)
        print(". ", end="")
        time.sleep(1)
        sys.exit()
        
    print("Digite a quantidade de resultados possíveis (maior o número, maior o tempo de execução): ", end="")
    qnt = input()

    if qnt.isdigit():
        qnt = int(qnt)
    else:
        print("Valor de entrada inválido, usando a quantidade padrão de 10 resultados!")
        qnt = 10


    #variabvel que recebe o texto encripado
    palavra1 = str(textoEncriptado).replace(" ", "")

    clear()
    DesenhaTelaMono()
    print("Executando...")

    #define arrays usados no loop
    palavrasEncontradas = []
    alfabetosEncontrados = []
    alfabetosRandomizados = []

    pbar = tqdm(total=qnt, ascii=True)

    #loop que faz a verificação
    while(retorno == False):
        #embaralha de forma aleatoria alfabeto
        random.shuffle(alfabetoRand)
        
        #verifica se alfabeto embaralhado ja esta dentro da list
        if alfabetoRand in alfabetosRandomizados:
            #se true embaralha novamente
            random.shuffle(alfabetoRand)
        else:
            #coloca alfabeto embaralhado na list
            alfabetosRandomizados.append(alfabetoRand)

        #limpa a variavel
        palavra2 = ""

        #corre letra por letra na palavra encriptada
        for i in range(len(palavra1)):
            #corre letra por letra no alfaneto
            for j in range(8):
                #se ele encontra a letra 
                if palavra1[i] == alfabetoRand[j]:
                    #a palavra recebe a letra de mesma posicao do alfabeto original
                    palavra2 += str(alfabeto[j]).lower()                

        
        #abre o dicionario cujas palavras tem no maximo 6 letras
        with open("dictionary_brazilian_six.dic", "r") as dicionario:
            #corre de linha em linha
            for line in dicionario:
                #verifica se encontra a palabra
                if re.search(r'\b' + palavra2 + r'\b', line):
                    #verifica se a palavra que ele encontrou ja existe na list
                    if palavra2 in palavrasEncontradas:
                        contador = contador + 1
                    else:
                        #coloca palavra encontrada na list
                        palavrasEncontradas.append(palavra2)
                        #adiciona o alfabeto encontrado para a list
                        alfabetosEncontrados.append(str(alfabetoRand))
                        pbar.update(1)
        #verifica a qnt de palavras encontradas

        if len(palavrasEncontradas) == qnt:
            retorno = True

    pbar.close()

    clear()
    DesenhaTelaMono()
    print("Mostrando "+str(qnt)+" principais resultados possíveis para a mensagem criptografada - "+palavra1.replace(" ", "")+" -:")
    print("")

    #printa na tela as palabras e alfabetos encontrados
    for x in range(len(palavrasEncontradas)):
        print("+-", end="")
        for i in range(len(textoEncriptado)):
            print("-", end="")
        print("-+------------------------------------------+\n", end="")
        print("| "+palavrasEncontradas[x]+" | "+alfabetosEncontrados[x]+" |")

    print("+-", end="")
    for i in range(len(textoEncriptado)):
        print("-", end="")
    print("-+------------------------------------------+\n", end="")
    print("")



def cesarBruteForce(textoEncriptado):
    #defie variavel
    global resultadoArray
    #define array
    resultadoArray = [None]*25
    clear()
    DesenhaTelaCesar()
    textoEncriptado = textoEncriptado.replace(" ", "")

    print("Possíveis saídas para a mensagem criptografada -",palavra,"-:")
    print("")

    for j in range(25):
        resultado = ""
        #for que corre de letra em letra na palavra encriptada
        for i in range(len(textoEncriptado)):            
            #define caracter
            caracter = textoEncriptado[i]
            resultado += chr((ord(caracter) - j - 97) % 26 + 97)
        #adiciona o resultado na array
        resultadoArray[j] = resultado
        #if feito apenas para melhorar visualizaçao
        if j > 9:
            print("+------+-", end="")
            for i in range(len(resultado)):
                print("-", end="")
            print("---+\n", end="")
            print("| +",j,"| ",resultado," |")
        else:
            print("+------+-", end="")
            for i in range(len(resultado)):
                print("-", end="")
            print("---+\n", end="")
            print("| +",j," | ",resultado," |")

    print("+------+-", end="")
    for i in range(len(resultado)):
        print("-", end="")
    print("---+\n", end="")
    #retorna array
    return resultadoArray



#Define funcao que verifica no dicionario referente a cifra de cesar
def verificaDicionario():
    #variavel de salto
    salto = 0
    #variavel para quebrar loop
    find = False
    #for que corre em toda array de resultados
    for item in resultadoArray:
        #abre arquivo de dicionario
        with open("dictionary_brazilian.dic", "r") as dicionario:
            #le o arquivo linha por linha
            for line in dicionario:
                #verifica se encontra alguma das palabras do array
                if re.search(r'\b' + item + r'\b', line):
                    print("\nResultado mais provável:")
                    print("")

                    print("+------+-", end="")
                    for i in range(len(line)-1):
                        print("-", end="")
                    print("---+\n", end="")
                    
                    if salto > 9:
                        print("| +",salto, "| ", str(line).replace("\n", ""), " |")
                    else:
                        print("| +",salto, " | ", str(line).replace("\n", ""), " |")

                    print("+------+-", end="")
                    for i in range(len(line)-1):
                        print("-", end="")
                    print("---+\n", end="")

                    find = True
                    break
        salto+=1
        #se ele encontrou, quebra o loop
        if find == True:
            break
    
    if find==False:
        print("\n!!! Não foi possível encontrar nenhum resultado compatível !!!\n")



def verificaEscolha(escolha):

    #seta veriavel global palavra
    global palavra 
    #seta variavel global error
    global error

    #seta variavel error = true
    error = True

    if escolha == 1:
        clear()
        DesenhaTelaCesar()
        print("1 - Digitar a palvra criptografada")
        print("2 - Inserir arquivo contendo palavra criptografada")
        print("")
        print("Escolha uma das opções: ", end="")
        escolha = input()

        if int(escolha) == 1:
            clear()
            DesenhaTelaCesar()
            print("Digite a palavra criptografada: ", end="")
            palavra = input()

            cesarBruteForce(str(palavra).lower())
            verificaDicionario()

        elif int(escolha) == 2:
            clear()
            DesenhaTelaCesar()
            while error == True:       
                print("Digite o nome do arquivo com extensão (deve estar no mesmo local que o programa, EX = palavra.txt): ", end="")
                arquivo = input()
                
                try:
                    arquivoAberto = open(arquivo, "r")
                except:
                    print("Arquivo não encontrado!")
                    continue

                palavra = str(arquivoAberto.read())
                error = False
            
            cesarBruteForce(str(palavra).lower())
            verificaDicionario()

        else:
            while(int(escolha) != 1 and int(escolha) != 2):
                print("Opção invalida!")
                print("Escolha uma opção: ", end="")
                escolha = input()
            escolha = int(escolha)

    else:
        clear()
        DesenhaTelaMono()     
        print("1 - Digitar a palvra criptografada")
        print("2 - Inserir arquivo contendo palavra criptografada")
        print("")
        print("Escolha uma das opções: ", end="")
        escolha = input()

        if int(escolha) == 1:
            clear()
            DesenhaTelaMono()
            print("Digite a palavra criptografada: ", end="")
            palavra = input()
            monoalphabeticSolver(str(palavra))

        elif int(escolha) == 2:
            clear()
            DesenhaTelaMono()
            while error == True:       
                print("Digite o nome do arquivo com extensão (deve estar no mesmo local que o programa, EX = palavra.txt): ", end="")
                arquivo = input()
                
                try:
                    arquivoAberto = open(arquivo, "r")
                except:
                    print("Arquivo não encontrado!")
                    continue

                palavra = str(arquivoAberto.read())
                error = False
            monoalphabeticSolver(str(palavra))

        else:
            while(int(escolha) != 1 and int(escolha) != 2):
                print("Opção invalida!")
                print("Escolha uma opção: ", end="")
                escolha = input()
            escolha = int(escolha)

#inicio do programa
print("+--------------------------------------------------------------+")
print("|==============================================================|")
print("|==== Decriptador de cifra de césar e cifra monoalfabética ====|")
print("|==============================================================|")
print("+--------------------------------------------------------------+")
print("\n1 - Cifra de césar")
print("2 - Cifra monoalfabética\n")
print("Escolha uma opção: ", end="")
escolha = input()

if int(escolha) == 1:
    verificaEscolha(1)
elif int(escolha) == 2:
    verificaEscolha(2)
else:
    while(int(escolha) != 1 and int(escolha) != 2):
        print("Opção invalida!")
        print("Escolha uma opção: ", end="")
        escolha = input()
    escolha = int(escolha)
    verificaEscolha(escolha)

#monoalphabeticSolver("OERPA")


#cesarBruteForce("xiwxi")
#verificaDicionario()

input("Digite qualquer tecla para finalizar...")