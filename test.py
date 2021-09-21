import random
import os
import time
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
            numTrofeus = str(l[7] + l[8] + l[9] + l[10])
            stringg = ""
            if i % 2:
                stringg = "background-color: #ffffff18;"
            msg2add += """<tr style=" """ + str(stringg)  + """ ">
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
        <button id="botao" onclick="botao()">Carrega aqui</button>
        <div id="tablediv">
            <table>
                <tr>
                    <th>Turma/Ano</th>
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


# ano;turma;numero;nome_completo;pontos;nivel;xp_sobra;xp_prasubir;t_bronze;t_ferro;t_ouro;t_platina
# 7;A;1;Carolina Magina;0;1;0;500;0;0;0;0
# 7;A;2;Duarte Valentim;0;1;0;500;0;0;0;0
# 7;A;3;Gabriel Pereira;0;1;0;500;0;0;0;0
# 7;A;4;Goncalo Mendes;0;1;0;500;0;0;0;0
# 7;A;5;Ines Ferreira;0;1;0;500;0;0;0;0
# 7;A;6;Ines Neto;0;1;0;500;0;0;0;0
# 7;A;7;Joana Almeida;0;1;0;500;0;0;0;0
# 7;A;8;Karaaaaaaaaaaaaaaa Rodrigues;0;1;0;500;0;0;0;0
# 7;A;9;Lara Carvalho;0;1;0;500;0;0;0;0
# 7;A;10;Maria Cardoso;0;1;0;500;0;0;0;0
# 7;A;11;Maria Barros;0;1;0;500;0;0;0;0
# 7;A;12;Maria Leonor Silva;0;1;0;500;0;0;0;0
# 7;A;13;Matias Mendes;0;1;0;500;0;0;0;0
# 7;A;14;Matilde Neves;0;1;0;500;0;0;0;0
# 7;A;15;Matilde Vilela;0;1;0;500;0;0;0;0
# 7;A;16;Pedro Maximino;0;1;0;500;0;0;0;0
# 7;A;17;Pedro Monteiro;0;1;0;500;0;0;0;0
# 7;A;18;Rafael Correia;0;1;0;500;0;0;0;0
# 7;A;19;Rodrigo Fernandes;0;1;0;500;0;0;0;0
# 7;A;20;Tiago Flor;0;1;0;500;0;0;0;0
# 7;B;1;Alexandre Goncalves;0;1;0;500;0;0;0;0
# 7;B;2;Camila Pereira;0;1;0;500;0;0;0;0
# 7;B;3;Dinis Gabriel;0;1;0;500;0;0;0;0
# 7;B;4;Fábio Simao;0;1;0;500;0;0;0;0
# 7;B;5;Francisco Cardoso;0;1;0;500;0;0;0;0
# 7;B;6;Gabriel Martins;0;1;0;500;0;0;0;0
# 7;B;7;Guilherme Loureiro;0;1;0;500;0;0;0;0
# 7;B;8;Gustavo Martins;0;1;0;500;0;0;0;0
# 7;B;9;Janice Joaquim;0;1;0;500;0;0;0;0
# 7;B;10;Lara Madeira;0;1;0;500;0;0;0;0
# 7;B;11;Lara Silva;0;1;0;500;0;0;0;0
# 7;B;12;Leandro Antunes;0;1;0;500;0;0;0;0
# 7;B;13;Madalena Vide;0;1;0;500;0;0;0;0
# 7;B;14;Madalena Pereira;0;1;0;500;0;0;0;0
# 7;B;15;Maria Batista;0;1;0;500;0;0;0;0
# 7;B;16;Maria Sousa;0;1;0;500;0;0;0;0
# 7;B;17;Rodrigo Miranda;0;1;0;500;0;0;0;0
# 7;B;18;Safira Joaquim;0;1;0;500;0;0;0;0
# 7;B;19;Taaaaaaaaaaaaaasa Fernandes;0;1;0;500;0;0;0;0
# 7;B;20;Tiago Jesus;0;1;0;500;0;0;0;0
# 7;C;1;Adriel Evans;0;1;0;500;0;0;0;0
# 7;C;2;Afonso Monteiro;0;1;0;500;0;0;0;0
# 7;C;3;Alberto Abreu;0;1;0;500;0;0;0;0
# 7;C;4;Andre Fernandes;0;1;0;500;0;0;0;0
# 7;C;5;Carolina Cardoso;0;1;0;500;0;0;0;0
# 7;C;6;Duarte Rodrigues;0;1;0;500;0;0;0;0
# 7;C;7;Edgar Santos;0;1;0;500;0;0;0;0
# 7;C;8;Iris Figueiredo;0;1;0;500;0;0;0;0
# 7;C;9;Iuri Marques;0;1;0;500;0;0;0;0
# 7;C;10;Joao Oliveira;0;1;0;500;0;0;0;0
# 7;C;11;Leandro Lopes;0;1;0;500;0;0;0;0
# 7;C;12;Lisandro Melo;0;1;0;500;0;0;0;0
# 7;C;13;Lucas Ferreira;0;1;0;500;0;0;0;0
# 7;C;14;Laaaaaaaaaaaaaaaaaaaaaaaaaaacia Alves;0;1;0;500;0;0;0;0
# 7;C;15;Martim Marques;0;1;0;500;0;0;0;0
# 7;C;16;Matilde Lopes;0;1;0;500;0;0;0;0
# 7;C;17;Nuno Matias;0;1;0;500;0;0;0;0
# 7;C;18;Pedro Silva;0;1;0;500;0;0;0;0
# 7;C;19;Simeon Jesus;0;1;0;500;0;0;0;0
# 7;C;20;Vanessa Mendes;0;1;0;500;0;0;0;0
# 7;D;1;Afonso Guerra;0;1;0;500;0;0;0;0
# 7;D;2;Ana Nunes;0;1;0;500;0;0;0;0
# 7;D;3;Bernardo Simoes;0;1;0;500;0;0;0;0
# 7;D;4;Carlota Gomes;0;1;0;500;0;0;0;0
# 7;D;5;Gabriel Fernandes;0;1;0;500;0;0;0;0
# 7;D;6;Henrique Nunes;0;1;0;500;0;0;0;0
# 7;D;7;Juliana Lopes;0;1;0;500;0;0;0;0
# 7;D;8;Liliana Martins;0;1;0;500;0;0;0;0
# 7;D;9;Lilou Bafoll;0;1;0;500;0;0;0;0
# 7;D;10;Maria Gouveia;0;1;0;500;0;0;0;0
# 7;D;11;Martim Eusebio;0;1;0;500;0;0;0;0
# 7;D;12;Martim Fernandes;0;1;0;500;0;0;0;0
# 7;D;13;Matilde Rebelo;0;1;0;500;0;0;0;0
# 7;D;14;Ot Dam;0;1;0;500;0;0;0;0
# 7;D;15;Rafael Fernandes;0;1;0;500;0;0;0;0
# 7;D;16;Ricardo Pina;0;1;0;500;0;0;0;0
# 7;D;17;Ruben Silva;0;1;0;500;0;0;0;0
# 7;D;18;Samuel Carvalho;0;1;0;500;0;0;0;0
# 7;D;19;Santiago Oliveira;0;1;0;500;0;0;0;0
# 7;D;20;Simao Figueiredo;0;1;0;500;0;0;0;0
# 7;D;21;Sofia Oliveira;0;1;0;500;0;0;0;0
# 7;D;22;Xavier Amandola;0;1;0;500;0;0;0;0
# 7;E;1;Ana Martins;0;1;0;500;0;0;0;0
# 7;E;2;Ana Cabral;0;1;0;500;0;0;0;0
# 7;E;3;Bárbara Jerónimo;0;1;0;500;0;0;0;0
# 7;E;4;Beatriz Albuquerque;0;1;0;500;0;0;0;0
# 7;E;5;Beatriz Batista;0;1;0;500;0;0;0;0
# 7;E;6;Beatriz Pires;0;1;0;500;0;0;0;0
# 7;E;7;Beatriz Gomes;0;1;0;500;0;0;0;0
# 7;E;8;Camila Nogueira;0;1;0;500;0;0;0;0
# 7;E;9;Daniela Alves;0;1;0;500;0;0;0;0
# 7;E;10;Dinis Marques;0;1;0;500;0;0;0;0
# 7;E;11;Dinis Silva;0;1;0;500;0;0;0;0
# 7;E;12;Emaaaaaaalia Santos;0;1;0;500;0;0;0;0
# 7;E;13;Francisca Pereira;0;1;0;500;0;0;0;0
# 7;E;14;Guilhermo Fidalgo;0;1;0;500;0;0;0;0
# 7;E;15;Hugo Moreira;0;1;0;500;0;0;0;0
# 7;E;16;Ines Ferreira;0;1;0;500;0;0;0;0
# 7;E;17;Joao Henriques;0;1;0;500;0;0;0;0
# 7;E;18;Lara Silva;0;1;0;500;0;0;0;0
# 7;E;19;Laura Garcia;0;1;0;500;0;0;0;0
# 7;E;20;Lucas Almeida;0;1;0;500;0;0;0;0
# 7;E;21;Maria Moura;0;1;0;500;0;0;0;0
# 7;E;22;Matilde Figueiredo;0;1;0;500;0;0;0;0
# 7;E;23;Matilde Fernandes;0;1;0;500;0;0;0;0
# 7;E;24;Raquel Campos;0;1;0;500;0;0;0;0
# 7;E;25;Salvador Ye;0;1;0;500;0;0;0;0
# 7;E;26;Tiago Garcia;0;1;0;500;0;0;0;0
