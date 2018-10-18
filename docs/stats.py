import pandas
import json

file = pandas.read_excel("Respostas.xlsx")

questions = ["Idade", "Género", "Ocupação","Utiliza ou já utilizou transportes públicos?","Com que frequência utiliza transportes públicos?","Que tipo de transportes públicos utiliza?","Como classifica o seu nível de satisfação com os transportes públicos que utiliza?",
"Em que cidade(s) já utilizou transportes públicos?","Que título de transporte costuma adquirir?","Quão justo considera o preço do título de transporte, tendo em conta o serviço prestado?","Já utilizou algum transporte público sem validar ou adquirir o título de transporte?",
"Com que frequência VALIDA o seu título de transporte?","Com que frequência ADQUIRE o seu título de transporte?","Indique todas as razões pelas quais não validou e/ou adquiriu o título de transporte:","O que acha de transportes públicos sem barreiras físicas?",
"Quão útil considera poder adquirir e/ou usar os seus títulos de transporte através de uma aplicação móvel?","Quão útil considera poder consultar horários, preços e outras informações sobre o transporte público numa aplicação móvel?",
"Considera que a aquisição e validação de títulos de transporte através da aplicação móvel iria aumentar se isso permitisse ganhar prémios (tais como viagens e descontos) aos utilizadores?"]

dict_questions = {}
for question in questions:
    dict_questions[question] = {"Não Responderam": 0, "Total": 0}

for question in dict_questions:
    values = file[question].values
    for value in values:
        if(str(value) in dict_questions[question]):
            dict_questions[question][str(value)] += 1
        elif(str(value) == "nan"):
            dict_questions[question]["Não Responderam"] += 1
        else:
            dict_questions[question][str(value)] = 1
        dict_questions[question]["Total"] += 1

dict_questions["Principal motivo de usar transporte público"] = {"Trabalho":0, "Universidade":0, "Escola":0, "Passear":0, "Atividades em Geral": 0, "Total" : 0}
test = ["Ocupação", "Com que frequência utiliza transportes públicos?", "Idade"]

#complete cancer if conditions, wont do a function because i really dont care about the aspect in this useless script
for answer in file[test].values:
    if(answer[0] == "Trabalhador-Estudante"):
        if(answer[1] == "Diariamente"):
            dict_questions["Principal motivo de usar transporte público"]["Trabalho"] += 1
            dict_questions["Principal motivo de usar transporte público"]["Universidade"] += 1
        elif(answer[1] == "Algumas vezes por mês"):
            dict_questions["Principal motivo de usar transporte público"]["Trabalho"] += 1
            dict_questions["Principal motivo de usar transporte público"]["Passear"] += 1
        elif(answer[1] == "Raramente"):
            dict_questions["Principal motivo de usar transporte público"]["Passear"] += 1
        elif(answer[1] == "Algumas vezes por semana"):
            dict_questions["Principal motivo de usar transporte público"]["Universidade"] += 1

    elif(answer[0] == "Reformado"):
        if(answer[1] == "Diariamente"):
            dict_questions["Principal motivo de usar transporte público"]["Atividades em Geral"] += 1
        elif(answer[1] == "Algumas vezes por mês"):
            dict_questions["Principal motivo de usar transporte público"]["Passear"] += 1
        elif(answer[1] == "Raramente"):
            dict_questions["Principal motivo de usar transporte público"]["Passear"] += 1
        elif(answer[1] == "Algumas vezes por semana"):
            dict_questions["Principal motivo de usar transporte público"]["Atividades em Geral"] += 1

    elif(answer[0] == "Empregado"):
        if(answer[1] == "Diariamente"):
            dict_questions["Principal motivo de usar transporte público"]["Trabalho"] += 1
        elif(answer[1] == "Algumas vezes por mês"):
            dict_questions["Principal motivo de usar transporte público"]["Atividades em Geral"] += 1
        elif(answer[1] == "Raramente"):
            dict_questions["Principal motivo de usar transporte público"]["Passear"] += 1
        elif(answer[1] == "Algumas vezes por semana"):
            dict_questions["Principal motivo de usar transporte público"]["Atividades em Geral"] += 1

    elif(answer[0] == "Estudante"):
        if(answer[1] == "Diariamente"):
            if(answer[2] == "Menos de 18 anos"):
                dict_questions["Principal motivo de usar transporte público"]["Escola"] += 1
            else:
                dict_questions["Principal motivo de usar transporte público"]["Universidade"] += 1
        elif(answer[1] == "Algumas vezes por mês"):
            dict_questions["Principal motivo de usar transporte público"]["Atividades em Geral"] += 1
            dict_questions["Principal motivo de usar transporte público"]["Passear"] += 1
        elif(answer[1] == "Raramente"):
            dict_questions["Principal motivo de usar transporte público"]["Atividades em Geral"] += 1
        elif(answer[1] == "Algumas vezes por semana"):
            if(answer[2] == "Menos de 18 anos"):
                dict_questions["Principal motivo de usar transporte público"]["Escola"] += 1
            else:
                dict_questions["Principal motivo de usar transporte público"]["Universidade"] += 1
            dict_questions["Principal motivo de usar transporte público"]["Atividades em Geral"] += 1

    elif(answer[0] == "Desempregado"):
        if(answer[1] == "Diariamente"):
            dict_questions["Principal motivo de usar transporte público"]["Atividades em Geral"] += 1
            dict_questions["Principal motivo de usar transporte público"]["Passear"] += 1
        elif(answer[1] == "Algumas vezes por mês"):
            dict_questions["Principal motivo de usar transporte público"]["Atividades em Geral"] += 1
        elif(answer[1] == "Raramente"):
            dict_questions["Principal motivo de usar transporte público"]["Passear"] += 1
        elif(answer[1] == "Algumas vezes por semana"):
            dict_questions["Principal motivo de usar transporte público"]["Atividades em Geral"] += 1

    dict_questions["Principal motivo de usar transporte público"]["Total"] += 1

print(json.dumps(dict_questions, indent=4, separators=(',', ': ')))
