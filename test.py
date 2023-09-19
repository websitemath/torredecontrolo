import random
import os
import time
os.system('copy dados.csv dados_backup.csv')
os.system('cp dados.csv dados_backup.csv')


dados = [] #6,A,7,MariaAna,16900,,,,,

f  = open("dados.csv", "r", encoding='windows-1252')

for i in f.readlines():
    x = i.split(";")
    x[-1] = x[-1].replace("\n","")        
    dados.append(x)
    
#se der erro é pq existe uma linha amais no .csv


def nivandstuff():
    pontosList = [0,500,700,1000,2000,4000,8000,9000,10000 ,10600,12000,14000,16000,17000,18000,19000,20000,20500,21000,21490]
    
    for m in range(len(dados)):
        if m > 0:
            dados[m][5] = ""
            dados[m][6] = ""
            dados[m][7] = ""

    for i in range(len(dados)):
        try:#vai fazer a partir da 2 linha, pois  a primeira é info
            xp = int(dados[i][4])
            for e in pontosList:
                if dados[i][5]:
                    break
                if xp >= pontosList[-1]:
                    nivel = 20
                    dados[i][5] = nivel
                    dados[i][6] = 0
                    dados[i][7] = 0
                elif xp > e and xp < pontosList[pontosList.index(e) + 1]:
                    nivel = pontosList.index(e) + 1
                    dados[i][5] = nivel
                    dados[i][6] = xp - e
                    dados[i][7] = pontosList[pontosList.index(e) + 1] - xp
                elif xp == e:
                    nivel = pontosList.index(e) + 1
                    dados[i][5] = nivel
                    dados[i][6] = xp - e
                    dados[i][7] = pontosList[pontosList.index(e) + 1] - xp


        except:
            print("")
    
nivandstuff()


def trofeus(nivelBronze,nivelFerro,nivelOuro,nivelPlatina):
    a= 0
    for i in dados:
        if(a != 0):
            nivel = int(i[5])
            if nivel >= nivelBronze:
                i[8] = 1
            else:
                i[8] = 0
            if nivel >= nivelFerro:
                i[9] = 1
            else:
                i[9] = 0
            if nivel >= nivelOuro:
                i[10] = 1
            else:
                i[10] = 0
            if nivel >= nivelPlatina:
                i[11] = 1
            else:
                i[11] = 0
        a += 1



trofeus(6,14,18,20)

def writedata(data):
    f2 = open("dados.csv", "w")
    for l in data:
        str2add = ""
        x = 0
        for k in l:
            if(x == 11):
                str2add += str(k)
            else:
                 str2add += str(k) + ";"
            x += 1
        f2.write(str2add + "\n")

def calcperc(line):
    try:
        perc  = (float(line[6])* 100) / (float(line[6]) + float(line[7]))
    except ZeroDivisionError:
        perc = 0
    return perc

writedata(dados)

dadosOP = [] #dados organizado por pontos

def write2html(line,barra_perc):
    #print("-------------------------------------------------")
    print(dadosOP)
    ranking = dadosOP.index(line) + 1;

    randomNum = random.randint(0,33)
    barra_perc = str(barra_perc)
    f2 = open("htmls/" + str(line[0]) + str(line[1]) + "_" + str(line[2]) + ".html", "w")
    msg = """<!DOCTYPE html>
        <html lang="pt-pt">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <head>
            <link rel="stylesheet" href="../samplestyle.css">
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>""" + str(line[3]) + """</title>
        </head>
        <body>
            <h1 id="nomealuno"> """ + 'Estat&iacute;sticas do aluno' + """</h1>
            <h1 id="rankingaluno">Ranking #""" + str(ranking) + """</h1>
            <div id="caixa">
                <div id="nome">""" + 'N&uacute;mero ' + str(line[2]) + " da turma " + str(line[0]) + str(line[1]) + """</div> 
                <div id="nivelbarra">
                    <div id="circulonum">
                        <div id="circulo">
                            <img id="imagem" src="../avatar/""" + str(random.randint(1, 33)) + """.svg" alt="avatar">
                        </div>
                        <div id="num">
                            """ + str(ranking) + ' lugar' + """
                        </div>
                    </div>
                </div>

                <div id="nada"></div>
                <div id="block">
                    <p id="cat">Pontos</p>        
                    <p id="subcat">""" + str(line[4]) + """</p>
                </div>

            </div>
        </body>
        </html>"""
    f2.write(msg)


def checktrofeu(linha):
    msg = ""
    #print(str(linha[8]) == "1")
    #print(linha[7])
    if str(linha[8]) == "1":
        #print(linha[3] + ", tem medalha ferro")
        msg = """<div id="block"><img id="trofeu" src="../trofeu/bronzepsn.png" alt="" srcset=""></div>"""
    if str(linha[9]) == "1":
        msg = msg + " " + """<div id="block"><img id="trofeu" src="../trofeu/ferropsn.png" alt="" srcset=""></div>"""
    
    if str(linha[10]) == "1":
        msg = msg + " " + """<div id="block"><img id="trofeu" src="../trofeu/ouropsn.png" alt="" srcset=""></div>"""
    if str(linha[11]) == "1":
        msg = msg + " " + """<div id="block"><img id="trofeu" src="../trofeu/platinapsn.png" alt="" srcset=""></div>"""
    return msg





#pontos -> dados[l][4]
#nome -> dados[l][3]


#print(dados)

pontos = []
#dadosOP = [] #dados organizado por pontos

dados.pop(0)
print("-------------------------------------------------")
print(dados)
print("-------------------------------------------------")


def listRanking():
    for l in dados:
        print(l[4])
        pontos.append(int(l[4]))

    pontos.sort()
    pontos.reverse()

    print(pontos)
    print(dadosOP)

    while(len(pontos) != len(dadosOP)):
        for e in pontos:
            print(e)
            ind = pontos.index(e)
            while(dadosOP == [] or dadosOP[-1][4] != str(e)):
                time.sleep(1.6)
                print("ponto a procura: " + str(e))
                for l in dados:
                    if(l[4] == str(e)):
                        if(l not in dadosOP):
                            print(l)
                            dadosOP.append(l)
                            print("adicionou-se : " + l[3])
                            print(dadosOP)
                
            # for l in dadosTemp:
            #     try:
            #         time.sleep(0.6)
            #         print(l[3])
            #         print(l[4])
            #         print(e)
            #         if(l[4] == e and l not in dadosOP):
            #             print("valor na linha atual do loop")
            #             print(l[3])
            #             dadosOP.append(l)
            #         print(l[3])
            #     except ValueError:
            #         continue
            #         pass

                # print(l.index(str(e)))
                # try:
                #     print(l)
                #     print(l.index(str(e)))
                #     print(e)
                #     if(pontos.index(e) == len(dadosOP)):
                #         dadosOP.append(l)
                # except ValueError:
                #     print("ada")
                #     print(e)
                #     pass

listRanking()


for l in dados:
    write2html(l,calcperc(l))

#print(pontos)
print(dadosOP)

def writeindex(dadosOrganizadosPorPontos,top):
    i = 1
    msg2add = ""
    xy = 0
    for l in dadosOrganizadosPorPontos:
        if i < (top + 1):#aparaece ate top -1 
            nome = l[3]
            anoTurma = l[0] + "&deg;" + l[1]
            num = l[2]
            pontos = l[4]
            nivel = l[5]
            numTrofeus = str(l[8] + l[9] + l[10] + l[11])
            stringg = ""
            if i % 2:
                stringg = "background-color: #ffffff18;"
            msg2add += """<tr style=" """ + str(stringg)  + """ ">
                            <th>""" + str(anoTurma) + """</th>
                            <th>""" + str(num) + """</th>
                            <th>""" + str(pontos) + """</th>
                            <th>""" + str(i) + """</th>
                            </tr>\n            """
        i += 1
        

    f2 = open("index.html", "w")
    msg = """<!DOCTYPE html>
    <html lang="pt-pt">
    <head>
        <link rel="stylesheet" href="style.css">
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Torre de Controlo</title>
        <script>
            function botao(){
                value = String(document.getElementById("turmanum").value).toUpperCase();
                window.open("https://websitemath.github.io/torredecontrolo/htmls/" + value + ".html", "_self");
            }
        </script>
    </head>
    <body>
        <h1 id="maintitle">Ranking do Desafio Matematico Mensal</h1>
        <h1>Coloca os teus dados no formato: ANOTURMA_NUMERO</h1>
        <input type="text" id="turmanum" placeholder="Exemplo: 6A_11"><br>
        <button id="botao" onclick="botao()">Carrega aqui</button>
        <div id="tablediv">
            <table>
                <tr>
                    <th>Turma/Ano</th>
                    <th>N&uacute;mero</th>
                    <th>Pontos</th>
                    <th>Ranking</th>
                </tr>
                """ + msg2add + """
            </table>
        </div>
    
    </body>
    </html>"""
    f2.write(msg)


writeindex(dadosOP,10)
print("---------------------")
print("ja podes fechar isto")
print("---------------------")

print(dadosOP[2])
#print(e)


# ano;turma;numero;nome_completo;pontos;nivel;xp_sobra;xp_prasubir;t_bronze;t_ferro;t_ouro;t_platina
