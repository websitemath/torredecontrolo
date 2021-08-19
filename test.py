import random
import os
os.system('copy dados.csv dados_backup.csv')
#os.system('cp dados.csv dados_backup.csv')


dados = [] #6,A,7,MariaAna,16900,,,,,

f  = open("dados.csv", "r")

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


"""
        #try:
            xp = int(i[4])
            for e in pontosList:
                print(e)
                if e == pontosList[-1]:
                    if xp > e:
                        nivel = (pontosList.index(e) + 1)
                        #print(xp,nivel)
                        i[5] = nivel
                    elif xp == e:
                        nivel = (pontosList.index(e) + 1)
                        #print(xp,nivel)
                        i[5] = nivel
                    #else:
                        #print("o que raio é que aconteceu, que dados estao no ficheiro")
                    if i[5]:
                        #print("foi encontrado o nivel")
                        i[6] = int(i[4]) - e #xp de sobra
                        i[7] = 0 #"nivmax" #xp pra subir
                        #print(dados)
                        break
                    else:
                        print("nao foi possivelo encontrar nivel")
                else:
                    if xp > e and xp < pontosList[int(pontosList.index(e)) + 1]:
                        nivel = (pontosList.index(e) + 1)
                        i[5] = nivel
                        i[6] = xp - pontosList[pontosList.index(e)]
                        i[7] = pontosList[nivel] - xp
                        print(i)
                    elif xp == e:
                        nivel = (pontosList.index(e) + 1)
                        #print(xp,nivel)
                        i[5] = nivel
                        i[6] = 0
                    if i[5]:
                        #print("foi encontrado o nivel")
                        i[7] = pontosList[nivel + 1] - int(i[4])
                        #print(dados)
                        break
        except ValueError:
            print("")
            """
    #print(dados)


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

def write2html(line,barra_perc):
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
            <h1 id="nomealuno"> """ + 'Estat&iacute;sticas de ' + str(line[3]) + """</h1>
            <div id="caixa">
                <div id="nome">""" + str(line[3]) + """</div> 
                <div id="nivelbarra">
                    <div id="circulonum">
                        <div id="circulo">
                            <img id="imagem" src="../avatar/""" + str(random.randint(1, 33)) + """.svg" alt="avatar">
                        </div>
                        <div id="num">
                            """ + str(line[5]) + """
                        </div>
                    </div>
                    
                    <div id="barra">
                        <div id="barracolorida" style="width: """ + barra_perc +"""%;">
                            a
                        </div>
                    </div>
                </div>

                <div id="nada"></div>
                <div id="block">
                    <p id="cat">Pontos</p>        
                    <p id="subcat">""" + str(line[4]) + """</p>
                </div>

                <div id="block">
                    <p id="cat">N&iacute;vel</p>        
                    <p id="subcat">""" + str(line[5]) + """</p>
                </div>
                <div id="block">
                    <p id="cat">N&uacute;mero de ta&ccedil;as</p>        
                    <p id="subcat">""" + str(line[8] + line[9] + line[10] + line[11]) + """</p>
                </div>
                <div id="block">
                    <p id="cat">Pontos para subir</p>        
                    <p id="subcat">""" + str(line[7]) + """</p>
                </div>

                <div id="trofeusdiv">
                    """ + str(checktrofeu(line)) + """
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



a1 = 0
for l in dados:
    if (a1 > 0):
        write2html(l,calcperc(l))
    a1 += 1

#pontos -> dados[l][4]
#nome -> dados[l][3]

dados.pop(0)#remover a primeira linha de dados

#print(dados)

pontos = []
dadosOP = [] #dados organizado por pontos

def listRanking():
    for l in dados:
        pontos.append(int(l[4]))
        del l[6]

    pontos.sort()
    pontos.reverse()

    while(len(pontos) != len(dadosOP)):
        for l in dados:
            for e in pontos:
                #print("----------" + str(e))
                try:
                    l.index(str(e))
                    #print("Lista" + str(l) + "contem")
                    if(pontos.index(e) == len(dadosOP)):
                        dadosOP.append(l)
                    #    print("adicionado")
                    #else:
                    #    print(pontos.index(e))
                    #    print("----")
                    #    print(len(dadosOP))

                except ValueError:
                    pass 
                    #print("")
                    #print("Lista" + str(l) + "does not contain value")

listRanking()

#print(pontos)
#print(dadosOP)

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
            numTrofeus = str(l[7] + l[8] + l[9] + l[10])
            stringg = ""
            if i % 2:
                stringg = "background-color: #ffffff18;"
            msg2add += """<tr style=" """ + str(stringg)  + """ ">
                            <th>""" + str(nome) + """</th>
                            <th>""" + str(anoTurma) + """</th>
                            <th>""" + str(num) + """</th>
                            <th>""" + str(pontos) + """</th>
                            <th>""" + str(nivel) + """</th>
                            <th>""" + str(numTrofeus) + """</th>
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
                window.location.replace("https://websitemath.github.io/torredecontrolo/htmls/" + value + ".html");
            }
        </script>
    </head>
    <body>
        <h1 id="maintitle">Torre de Controlo</h1>
        <h1>Coloca os teus dados no formato: ANOTURMA_NUMERO</h1>
        <input type="text" id="turmanum" placeholder="Exemplo: 6A_11"><br>
        <button id="botao" onclick="botao()">Redirecionar</button>
        <div id="tablediv">
            <table>
                <tr>
                    <th>Nome</th>
                    <th>Ano/Turma</th>
                    <th>N&uacute;mero</th>
                    <th>Pontos</th>
                    <th>N&iacute;vel</th>
                    <th>N&uacute;mero trofeus</th>
                    <th>Ranking</th>
                </tr>
                """ + msg2add + """
            </table>
        </div>
    
    </body>
    </html>"""
    f2.write(msg)


writeindex(dadosOP,10)
#print(pontos)
#print(e)
