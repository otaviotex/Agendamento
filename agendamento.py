import schedule
import time as tm
import datetime
from class_agend import sms



def tarefa1(anot, numero):
    print(f"{anot}")
    p2 = sms(numero)
    p2.alerta(anot)
    return schedule.CancelJob

def tarefa(compromisso, celular):
    print(f"{compromisso}")
    p1 = sms(celular)
    p1.alerta(compromisso)


def main():
    comp = input("O que deseja inserir na agenda? ")
    cel = input("Informe seu numero com o codigo do pais e o ddd: ")
    
    print ("""
        =======================
        
        1 - Somente uma vez.
        2 - Uma vez por dia.
        3 - Uma vez por semana.
        4 - Uma vez por mes.
        5 - A cada x minutos.
        6 - A cada x horas.
           
        =======================
        """)
    
    opc = int(input("Escolha uma opcao: "))
    match opc:
        case 1:
            dia = int(input("Dia: "))
            mes = int(input("Mes: "))
            ano = int(input("Ano: "))
            
            hoje = datetime.date.today()
            
            if hoje == datetime.date(ano, mes, dia):
                schedule.every().day.at("00:01").do(tarefa1, comp, cel)
        
        case 2:
            hrs = int(input("Horas: "))
            min = int(input("Minutos: "))
            hora = f"{hrs:02d}:{min:02d}"
            schedule.every().day.at(hora).do(tarefa, comp, cel)
        
        case 3:
            print(""" 
                =======================
                1 - Domingo
                2 - Segunda
                3 - Terca
                4 - Quarta
                5 - Quinta
                6 - Sexta
                7 - Sabado
                =======================
            """)
            sem = int(input("Insira o numero: "))

            match sem:
                case 1:
                    schedule.every().sunday.at("00:01").do(tarefa, comp, cel)
                case 2:
                    schedule.every().monday.at("00:01").do(tarefa, comp, cel)
                case 3: 
                    schedule.every().tuesday.at("00:01").do(tarefa, comp, cel)
                case 4: 
                    schedule.every().wednesday.at("00:01").do(tarefa, comp, cel)
                case 5: 
                    schedule.every().thursday.at("00:01").do(tarefa, comp, cel)
                case 6: 
                    schedule.every().friday.at("00:01").do(tarefa, comp, cel)
                case 7: 
                    schedule.every().saturday.at("00:01").do(tarefa, comp, cel)
        case 4:
            schedule.every(4).weeks.do(tarefa, comp, cel)
        case 5:
            mint = int(input("A cada quantos minutos? "))
            if mint == 1:
                schedule.every().minute.do(tarefa, comp, cel)
            else:
                schedule.every(mint).minutes.do(tarefa, comp, cel)
        case 6:
            hor = int(input("A cada quantas horas? "))
            if hor == 1:
                schedule.every().hour.do(tarefa, comp, cel)
            else:
                schedule.every(hor).hours.do(tarefa, comp, cel)


    while True:
        schedule.run_pending()
        tm.sleep(1)

main()
