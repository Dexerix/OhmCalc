import os
import math

def treat_exp(raw_v) -> float:
    '''
    Takes the value from the input, checks if the symbol '*' is present.
    If yes, splits and calculates the value into a float to work with.

    Parameter
        raw_v (str) : value from the input
    
    Return:
        float
    '''
    if "*" in raw_v:
            splat_v = raw_v.split("*")
            mantisse_v = float(splat_v[0])
            exposant = splat_v[1]
            exp_split = exposant.split("^", 1)
            power = int(exp_split[1])
            exposant = 10**power
            
            v = mantisse_v*exposant
    else: 
            v = float(raw_v)
    
    return v

# Creation of the "Ohm" class
class Ohm():
    '''Groups the calculation methods'''
    def __init__(self) -> None:
        pass

    def voltage(self):
        '''Calculates the voltage using the resistance(Ω) and the current(Ampere)'''
        raw_r = input("Enter R : ")
        raw_i = input("Enter I : ")
        r = treat_exp(raw_r)
        i = treat_exp(raw_i)

        u = float(r*i)
        print(u,"V")
            
    def amperage(self):
        '''Calculates the current using the voltage(Volts) and resistance(Ω)'''
        raw_u = input("Enter U : ")
        raw_r = input("Enter R : ")
        r = treat_exp(raw_r)
        u = treat_exp(raw_u)

        i = float(u/r)
        print(i, "A")
    
    def resistance(self):
        '''Calculates the resistance using the voltage(Volts) and the current(Ampere)'''
        raw_u = input("Enter U : ")
        raw_i = input("Enter I : ")
        u = treat_exp(raw_u)
        i = treat_exp(raw_i)
        
        r = float(u/i)
        print(r, "Ω")

    def section(self):
        '''Calculates the cable\'s section using the diameter(millimeter)'''
        diameter = float(input("Enter the diameter(mm) : "))
        a = round(float((math.pi*(diameter**2)/4)), 2)
        print(a, "mm2")

    def resistivity(self):
        '''Calculates the resistivity(ρ) using the resistance(Ω), the section(mm2) and the length(meter)'''
        raw_r = input("Enter the resistance (Ω) : ")
        a = float(input("Enter the cable's section (mm2) : "))
        l = float(input("Enter the lenght (m) : "))
        r = treat_exp(raw_r)
    
        rho = (r*a)/l
        print(rho, "Ωmm2/M")
        
    def rhosistence(self):
        '''Calculates the resistance(Ω) using the resitance(ρ), the section(mm2) and the lenght(meter)'''
        rho = float(input("Enter the rho(ρ) : "))
        l = float(input("Enter the lenght(m) : "))
        a = float(input("Enter the section (mm2) : "))
        r = (rho*l)/a
        print(r, "Ω")

    def parallel_resistor(self):
        askAmoutResistence=int(input('How many resistance are present on the circuit : '))
        r_list=[]
        for idx in range(askAmoutResistence):
            ask_r=input(f'Enter the resistance {idx+1}: ')
            r = treat_exp(ask_r)
            r_list.append(r)
            total_resistance = 0
            if len(r_list) > 1:
                for r in r_list:
                    total_resistance += 1/r
                total_resistance = 1/total_resistance
            else:
                total_resistance = r_list[0]
        print(f"The total resistance is: {total_resistance:.2f} Ω")

# Displays the menu
def display_menu():
    '''Print a menu with the available choices'''
    menu = "===============================================\n"
    menu += "             Choose your formula\n"
    menu += "-----------------------------------------------\n"
    menu += " U - Voltage\n"
    menu += " R - Resistance (Ohm's law)\n"
    menu += " I - Current\n"
    menu += " P - Resistivity\n"
    menu += " A - Section\n"
    menu += " O - Resistence (with ρ)\n"
    menu += "PR - Parallel Resistance\n"
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

# Main function 
def main():
    '''Main function'''
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
        elif user_choice == "pr":
            ohms.parallel_resistor()
            input()
        elif user_choice == "q":
            is_end_loop = True
            os.system('cls')

ohms = Ohm()
main()