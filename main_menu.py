from Classes import*
from formula_menus import *
from batch_menus import *
from bake_menus import *

def main_menu():
        
        Route={'f':formula_menu,'l':batch_menu,'b':bake_menu,'x':quit}
        M={'f': 'to access formulas','l':'to access loads',
                 'b':'to access bakes','x':'to exit'}
        for item in sorted(M.keys()):
            print('\tEnter {0:<1} {1:<10}'.format(item,M[item]))
        menu_input=input('\n')
        Route.get(menu_input,'not an option')()
        main_menu()
        
if __name__=='__main__':
        print('-'*80,'\n\n\t\t\t\tWelcome to Bakehouse\n\n')
        main_menu()
