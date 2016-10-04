from Classes import *
from menus import *

def new_formula_menu():
        menuhead()
        formula_name=input('Enter Formula Name:')
        ingredient=''
        percent=''
        I={}
        while True:
                ingredient=input('Ingredient:')
                if ingredient=='':
                        break
                percent=input('Percent:')
                if percent=='':
                        break
                I[ingredient]=float(percent)
        to_save=input('save formula?y/n')
        if to_save=='y':
                saved_objects[formula_name]=Formula(formula_name,I)
                save()


def formula_adjust_menu():
        menuhead
        for item in saved_objects.keys():
                if type(saved_objects[item])==type(Formula()):
                        print('\t\t{0}'.format(item))
        formula_choice=saved_objects[input('\nFormula to edit?\n')]
        while True:
                formula_choice.print_formula()
                choice=input('Type -e- to edit load, type -d- to delete existing.\n')
                if choice=='e':
                        
                        ingredient=input('Ingredient:')
                        if ingredient=='':
                                return
                        percent=input('Percent:')
                        if percent=='':
                                return
                        formula_choice.formula[str(ingredient)]=int(percent)
                        save()
                
                if choice=='d':
                        try:
                                ingredient=input('Ingredient:')
                                formula_choice.formula.pop(ingredient)
                                save()
                        except:
                                print('That ingredient does not exist')
                return
           
                        
                
def formula_menu():
        menuhead
        print('/nCURRENT FORMULAS ARE:\n')
        for item in sorted(saved_objects.keys()):
                if type(saved_objects[item])==type(Formula()):
                        print('\t\t{0}'.format(item))
        menu_input=input("Type 'n' to create a new formula,'a' to adjust an existing\n\tor 'r' to return to main menu\n")
        if menu_input=='n':
                new_formula_menu()
                formula_menu()
        if menu_input=='a':
                formula_adjust_menu()
                formula_menu()
