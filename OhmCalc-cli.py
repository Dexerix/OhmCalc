import math
import os
os.system("cls")

class Ohm():
    def __init__(self) -> None:
        pass

    def tension():
        raw_r = input("Enter R : ")
        raw_i = input("Enter I : ")
        if "*" in raw_r:
            splat_r = raw_r.split("*")
            mantisse_r = float(splat_r[0])
            exposant = splat_r[1]
            exp_split = exposant.split("^", 1)
            power = int(exp_split[1])
            exposant = 10**power
            r = mantisse_r*exposant
        else: 
            r = float(raw_r)

        if "*" in raw_i:
            splat_i = raw_i.split("*")
            mantisse_i = float(splat_i[0])
            exposant = splat_i[1]
            exp_split = exposant.split("^", 1)
            power = int(exp_split[1])
            exposant = 10**power
            i = mantisse_i*exposant
        else:
            i = float(raw_i)

        u = float(r*i)
        print(u,"V")
            
    def amperage():
        raw_r = input("Enter R : ")
        raw_u = input("Enter U : ")
        if "*" in raw_r:
            splat_r = raw_r.split("*")
            mantisse_r = float(splat_r[0])
            exposant = splat_r[1]
            exp_split = exposant.split("^", 1)
            power = int(exp_split[1])
            exposant = 10**power
            r = mantisse_r*exposant
        else: 
            r = float(raw_r)
        if "*" in raw_u:
            splat_u = raw_u.split("*")
            mantisse_u = float(splat_u[0])
            exposant = splat_u[1]
            exp_split = exposant.split("^", 1)
            power = int(exp_split[1])
            exposant = 10**power
            u = mantisse_u*exposant
        else: 
            u = float(raw_u)

        i = float(u/r)
        print(i, "A")
    
    def resistence():
        raw_i = input("Enter I : ")
        raw_u = input("Enter U : ")
        if "*" in raw_u:
            splat_u = raw_u.split("*")
            mantisse_u = float(splat_u[0])
            exposant = splat_u[1]
            exp_split = exposant.split("^", 1)
            power = int(exp_split[1])
            exposant = 10**power
            u = mantisse_u*exposant
        else: 
            u = float(raw_u)

        if "*" in raw_i:
            splat_i = raw_i.split("*")
            mantisse_i = float(splat_i[0])
            exposant = splat_i[1]
            exp_split = exposant.split("^", 1)
            power = int(exp_split[1])
            exposant = 10**power
            i = mantisse_i*exposant
        else:
            i = float(raw_i)
        
        r = float(u/i)
        print(r, "Ω")

def afficher_menu():
    menu = "===============================================\n"
    menu += "             Choose your formula\n"
    menu += "-----------------------------------------------\n"
    menu += " U - tension\n"
    menu += " R - resistence\n"
    menu += " I - Current\n"
    menu += "...\n"
    menu += ' Q - Quit\n'
    menu += "===============================================\n"
    print(menu)

def ask_user_choice(question:str):
    choix = input(question)
    try:
        lettre_choix = choix
    except:
        pass
    return lettre_choix

def main():
    if_fin_boucle = False
    while not is_fin_boucle:
        os.system('cls')
        afficher_menu()
        choix_usr = ask_user_choice("Your choice : ")
        print()