import random
import os
import time

os.system('copy dados.csv dados_backup.csv') # windows
#os.system('cp dados.csv dados_backup.csv') # linux


# aluno -> Ano,Turma,numero,id,pontos,ranking


def DatafromFile():
    f  = open("dados.csv", "r")
    dados = []

    for line in f.readlines():
        row = line.split(";")
        row[-1] = row[-1].replace("\n","")
        row[3] = float(row[3].replace(",","."))
        dados.append(row)
    f.close()
    return dados

def WriteDataToFile(dados):
    f2  = open("dados.csv", "w")
    sorted_data = sorted(data, key=lambda x: (int(x[0]), x[1], int(x[2])))
    print(sorted_data)
    for l in dados:
        f2.write(str(f"{l[0]};{l[1]};{l[2]};{l[3]};{l[4]}\n"))
    f2.close()


def DataDividedCiclo(dados):# -> (ciclo2,ciclo3)
    data2ciclo = []
    data3ciclo = []

    for aluno in dados:
        if int(aluno[0]) < 7:
            data2ciclo.append(aluno)
        else:
            data3ciclo.append(aluno)
    return (data2ciclo,data3ciclo)


def updaterankingSpecificData(listaCiclo): # parametro tem que ser um dos ciclos obrigatoriamente
    pointsLista = []
    for aluno in listaCiclo:
        if not (aluno[3] in pointsLista):
            pointsLista.append(aluno[3])
    pointsLista = sorted(pointsLista,reverse=True)

    for i in range(0,len(listaCiclo)):
        listaCiclo[i][4] = pointsLista.index(listaCiclo[i][3])+1
    listaCiclo.sort(key=lambda x: x[4])
    

def AlunoWriteHtml(aluno):
    f2 = open("htmls/" + str(aluno[0]) + str(aluno[1]) + "_" + str(aluno[2]) + ".html", "w")
    msg = """<!DOCTYPE html>
        <html lang="pt-pt">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <head>
            <link rel="stylesheet" href="../samplestyle.css">
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>""" + str(aluno[0]) + str(aluno[1]) + "_" + str(aluno[2]) + """</title>
        </head>
        <body>
            <h1 id="nomealuno"> """ + 'Estat&iacute;sticas do aluno' + """</h1>
            <h1 id="rankingaluno">Ranking #""" + str(aluno[4]) + """</h1>
            <div id="caixa">
                <div id="nome">""" + 'N&uacute;mero ' + str(aluno[2]) + " da turma " + str(aluno[0]) + str(aluno[1]) + """</div> 
                <div id="nivelbarra">
                    <div id="circulonum">
                        <div id="circulo">
                            <img id="imagem" src="../avatar/""" + str(random.randint(1, 33)) + """.svg" alt="avatar">
                        </div>
                        <div id="num">
                            """ + str(aluno[4]) + ' lugar' + """
                        </div>
                    </div>
                </div>

                <div id="nada"></div>
                <div id="block">
                    <p id="cat">Pontos</p>        
                    <p id="subcat">""" + str(aluno[3]).replace(",",".") + """</p>
                </div>

            </div>
        </body>
        </html>"""
    f2.write(msg)
    f2.close()


def CreateAllAlunosHtmls(dados):
    for aluno in dados:
        AlunoWriteHtml(aluno)


def createMainPagesHtmls(dados2ciclo,dados3ciclo):
    f2 = open("main/ciclo2.html", "w")
    f3 = open("main/ciclo3.html", "w")

    msg2add2ciclo = ""
    for index,aluno in enumerate(dados2ciclo):
        if index % 2:
            backgroundstring = "background-color: #ffffff18;"
        else:
            backgroundstring = ""
        msg2add2ciclo += """<tr style=" """ + str(backgroundstring)  + """ ">
                                <th>""" + str(aluno[0]) + "&deg;" + str(aluno[1]) + """</th>
                                <th>""" + str(aluno[2]) + """</th>
                                <th>""" + str(aluno[3]) + """</th>
                                <th>""" + str(aluno[4]) + """</th>
                                </tr>\n            """
    msg = """<!DOCTYPE html>
    <html lang="pt-pt">
    <head>
        <link rel="stylesheet" href="../style.css">
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
        <h1 id="maintitle">Ranking do Desafio Matematico Mensal <br> 2&deg;Ciclo</h1>
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
                """ + msg2add2ciclo + """
            </table>
        </div>
    
    </body>
    </html>"""
    f2.write(msg)
    f2.close()

    msg2add3ciclo = ""
    for index,aluno in enumerate(dados3ciclo):
        if index % 2:
            backgroundstring = "background-color: #ffffff18;"
        else:
            backgroundstring = ""
        msg2add3ciclo += """<tr style=" """ + str(backgroundstring)  + """ ">
                                <th>""" + str(aluno[0]) + "&deg;" + str(aluno[1]) + """</th>
                                <th>""" + str(aluno[2]) + """</th>
                                <th>""" + str(aluno[3]) + """</th>
                                <th>""" + str(aluno[4]) + """</th>
                                </tr>\n            """
    msg = """<!DOCTYPE html>
    <html lang="pt-pt">
    <head>
        <link rel="stylesheet" href="../style.css">
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
        <h1 id="maintitle">Ranking do Desafio Matematico Mensal <br> 3&deg;Ciclo</h1>
        <h1>Coloca os teus dados no formato: ANOTURMA_NUMERO</h1>
        <input type="text" id="turmanum" placeholder="Exemplo: 7A_11"><br>
        <button id="botao" onclick="botao()">Carrega aqui</button>
        <div id="tablediv">
            <table>
                <tr>
                    <th>Turma/Ano</th>
                    <th>N&uacute;mero</th>
                    <th>Pontos</th>
                    <th>Ranking</th>
                </tr>
                """ + msg2add3ciclo + """
            </table>
        </div>
    
    </body>
    </html>"""
    f3.write(msg)
    f3.close()



data = DatafromFile()
data2ciclo = DataDividedCiclo(data)[0]
data3ciclo = DataDividedCiclo(data)[1]
updaterankingSpecificData(data2ciclo)
updaterankingSpecificData(data3ciclo)
dataWithRanking = data2ciclo+data3ciclo

WriteDataToFile(dataWithRanking)
CreateAllAlunosHtmls(dataWithRanking)
createMainPagesHtmls(data2ciclo,data3ciclo)
