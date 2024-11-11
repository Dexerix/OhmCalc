import os
import math

def treat_exp(raw) -> float:
    if "*" in raw:
            splat_r = raw.split("*")
            mantisse_r = float(splat_r[0])
            exposant = splat_r[1]
            exp_split = exposant.split("^", 1)
            power = int(exp_split[1])
            exposant = 10**power
            
            r = mantisse_r*exposant
    else: 
            r = float(raw)
    
    return r

class Ohm():
    def __init__(self) -> None:
        pass

    def voltage(self):
        raw_r = input("Enter R : ")
        raw_i = input("Enter I : ")
        r = treat_exp(raw_r)
        i = treat_exp(raw_i)

        u = float(r*i)
        print(u,"V")
            
    def amperage(self):
        raw_u = input("Enter U : ")
        raw_r = input("Enter R : ")
        r = treat_exp(raw_r)
        u = treat_exp(raw_u)

        i = float(u/r)
        print(i, "A")
    
    def resistance(self):
        raw_u = input("Enter U : ")
        raw_i = input("Enter I : ")
        u = treat_exp(raw_u)
        i = treat_exp(raw_i)
        
        r = float(u/i)
        print(r, "Ω")

    def section(self):
        diameter = float(input("Enter the diameter(mm) : "))
        a = round(float((math.pi*(diameter**2)/4)), 2)
        print(a, "mm2")

    def resistivity(self):
        raw_r = input("Enter the resistance (Ω) : ")
        a = float(input("Enter the cable's section (mm2) : "))
        l = float(input("Enter the lenght (m) : "))
        r = treat_exp(raw_r)
    
        rho = (r*a)/l
        print(rho, "Ωmm2/M")
        
    def rhosistence(self):
        rho = float(input("Enter the rho(ρ) : "))
        l = float(input("Enter the lenght(m) : "))
        a = float(input("Enter the section (mm2) : "))
        r = (rho*l)/a
        print(r, "Ω")

def display_menu():
    menu = "===============================================\n"
    menu += "             Choose your formula\n"
    menu += "-----------------------------------------------\n"
    menu += " U - Voltage\n"
    menu += " R - Resistance (Ohm's law)\n"
    menu += " I - Current\n"
    menu += " P - Resistivity\n"
    menu += " A - Section\n"
    menu += " O - Resistence (with ρ)\n"
    menu += "...\n"
    menu += ' Q - Quit\n'
    menu += "===============================================\n"
    print(menu)

def ask_user_choice(question:str):
    choice = input(question)
    try:
        letter_choice = choice
    except:
        pass
    return letter_choice

def main():
    is_end_loop = False
    while not is_end_loop:
        os.system('cls')
        display_menu()
        user_choice = ask_user_choice("Your choice : ")
        user_choice = user_choice.lower()
        print()

        if user_choice == "u":
            ohms.voltage()
            input()
        elif user_choice == "r":
            ohms.resistance()
            input()
        elif user_choice == "i":
            ohms.current()
            input()
        elif user_choice == "p":
            ohms.resistivity()
            input()
        elif user_choice == "a":
            ohms.section()
            input()
        elif user_choice == "o":
            ohms.rhosistence()
            input()
        elif user_choice == "q":
            is_end_loop = True
            os.system('cls')

ohms = Ohm()
main()