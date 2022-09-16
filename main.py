import pandas as pd
import numpy as np
import datetime as dt


def daterange(date1, date2):
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + dt.timedelta(n)


def timedelta_calc(kommen, gehen, pause):
    
    #ALle Zeiten in Integer umrechnen
    if kommen[0] == '0':
        zeit_kommen_stunden = int(kommen[1])
        zeit_kommen_minuten = int(kommen[3:5])
    else:
        zeit_kommen_stunden = int(kommen[0:2])
        zeit_kommen_minuten = int(kommen[3:5])
    
    if gehen[0] == '0':
        zeit_gehen_stunden = int(gehen[1])
        zeit_gehen_minuten = int(gehen[3:5])
    else:
        zeit_gehen_stunden = int(gehen[0:2])
        zeit_gehen_minuten = int(gehen[3:5]) 
    
    pause = int(pause[3:5])
    
    #Pause von der Gehen Zeit abziehen
    if zeit_gehen_minuten - pause < 0:
        zeit_gehen_minuten = 60 + zeit_gehen_minuten - pause
        zeit_gehen_stunden -= 1
    else:
        zeit_gehen_minuten -= pause
    
    #Die Stunden ausrechnen wie lange ich da war
    
    zeit_stunden = zeit_gehen_stunden - zeit_kommen_stunden    
    
    #Die Minuten ausrechnen wie lang ich da war
    
    if zeit_gehen_minuten - zeit_kommen_minuten < 0:
        zeit_minuten = 60 + zeit_gehen_minuten - zeit_kommen_minuten
        zeit_stunden -= 1
    else:
        zeit_minuten = zeit_gehen_minuten - zeit_kommen_minuten
    
    if len(str(zeit_minuten)) == 1:
        zeit_minuten = f'0{zeit_minuten}'
                
    if len(str(zeit_stunden)) == 1:
        return f"0{zeit_stunden}:{zeit_minuten}" 
    
    return f"{zeit_stunden}:{zeit_minuten}"  


def zeitkonto_calc(ist_zeit, soll_zeit):

    ist_zeit_stunden = int(ist_zeit[0:2])
    ist_zeit_minuten = int(ist_zeit[3:5])
    
    soll_zeit_stunden = int(soll_zeit[0:2])
    soll_zeit_minuten = int(soll_zeit[3:5])
    
    
    if ist_zeit_stunden < soll_zeit_stunden:
        if ist_zeit_minuten > soll_zeit_minuten:
            zeit_stunden = f'0{abs(int(ist_zeit_stunden + 1 - soll_zeit_stunden))}'
            zeit_minuten = f'{ist_zeit_minuten - soll_zeit_minuten}'
                    
            if len(zeit_minuten) == 1:
                zeit_minuten = f'0{zeit_minuten}'
            if int(zeit_stunden) == 0:
                return f"{zeit_stunden}:{zeit_minuten}"
            return f"-{zeit_stunden}:{zeit_minuten}"
        else:    
            zeit_stunden = f'{ist_zeit_stunden - soll_zeit_stunden}'
            zeit_minuten = f'{ist_zeit_minuten - soll_zeit_minuten}'
            if int(zeit_stunden) < 10:
                zeit_stunden = f'0{abs(int(zeit_stunden))}'
            if len(zeit_minuten) == 1:
                zeit_minuten = f'0{zeit_minuten}'    
            return f"-{zeit_stunden}:{zeit_minuten}"
    else: 
        zeit_stunden = f'{ist_zeit_stunden - soll_zeit_stunden}'
        zeit_minuten = f'{ist_zeit_minuten - soll_zeit_minuten}'
        if len(zeit_stunden) == 1:
            zeit_stunden = f'0{zeit_stunden}'
        if len(zeit_minuten) == 1:
            zeit_minuten = f'0{zeit_minuten}' 
        return f" {zeit_stunden}:{zeit_minuten}"

    
def zeitkonto_insgesamt(zeitkonto):
    zeit = 0
    for i in range(len(zeitkonto)):
        #if zeitkonto[i] != '00:00':
            #print(zeitkonto[i])
        if zeitkonto[i][0] == ' ':
            zeitkonto_std = int(zeitkonto[i][0:3])
            zeitkonto_min = int(zeitkonto[i][4:6])
       
        elif zeitkonto[i][0] == '-':  
            zeitkonto_std = int(zeitkonto[i][0:3])
            zeitkonto_min = int(f'-{zeitkonto[i][4:6]}')
            
        else:
            zeitkonto_std = int(zeitkonto[i][0:2])
            zeitkonto_min = int(zeitkonto[i][3:5])          
        if zeitkonto_min >= 0:
            zeit += zeitkonto_std * 60 + zeitkonto_min
        else: 
            zeit -= (zeitkonto_min + 60 * zeitkonto_std)          
    if zeit >= 60:
        zeit_min = f'{zeit % 60}'
        if len(zeit_min) == 1:
            zeit_min = f'0{zeit_min}'
        zeit_std = f' {(zeit - int(zeit_min)) // 60}'
        if len(zeit_std) == 1:
            zeit_std = f'0{zeit_std}'
        return f' {zeit_std}:{zeit_min}'   


dates = [dtt.strftime('%Y-%m-%d') for dtt in daterange(dt.datetime.strptime(f"{dt.datetime.now().year-2}-01-01", "%Y-%m-%d"),
                                                                                             dt.datetime.strptime("2025-09-30", "%Y-%m-%d"))]
