from  Classes import *
import pickle
"""saved_objects is now a dictionary that goes from a string key to one of our defined
        objects, be it a batch,formula or bake"""
  
try:
        saved_objects=pickle.load(open('objects.pkl','rb'))
except FileNotFoundError:
        saved_objects={'test':'test'}
        pickle.dump(saved_objects,open('objects.pkl','wb',-1))

def save():
        pickle.dump(saved_objects,open('objects.pkl','wb',-1))
        pickle.load(open('objects.pkl','rb'))

def exitmenu():
        return

def new_formula_menu():
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
        for item in saved_objects.keys():
                if type(saved_objects[item])==type(Formula()):
                        print('\t\t{0}'.format(item))
        formula_choice=saved_objects[input('\nFormula to edit?\n')] #From string of input, return the object of name using saved_objects dictionary
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
        print('/nCURRENT FORMULAS ARE:\n')
        for item in saved_objects.keys():
                if type(saved_objects[item])==type(Formula()):
                        print('\t\t{0}'.format(item))
        menu_input=input("Type 'n' to create a new formula,'a' to adjust an existing\n\tor 'r' to return to main menu\n")
        if menu_input=='n':
                new_formula_menu()
                formula_menu()
        if menu_input=='a':
                formula_adjust_menu()
                formula_menu()
"""Running into difficulty with printing the batch, because of definition of
        objectsvthrough saved_objects dictionary and in Classes printbatch
        references formula directly. Solutions would be to move saved_objects
        Classes module, or move print_batch elements into menu.
        """
def view_batch_menu():
        batch_choice=input('Which batch to print?')
        batch=saved_objects[batch_choice]
        batch.print_batch()
        

def batch_adjust_menu():
        for item in saved_objects.keys():
                if type(saved_objects[item])==type(Batch()):
                        print('\t\t{0}'.format(item))
        batch_choice=input('\nBatch to edit?\n')
        print(batch_choice)
        batch=saved_objects[str(batch_choice)]
        print(type(batch))
        while True:
                batch.print_batch()
                choice=input('Type -e- to edit load, type -d- to delete existing.\n')
                if choice=='e':
                        formula=input('Formula:')
                        if formula=='':
                            return
                        formula=saved_objects[formula]# get the formula object
                        
                        loaves=input('Number of Loaves:')
                        if loaves=='':
                            return
                        size=input('Loaf Weight:')
                        if size=='':
                            return
                        saved_objects[batch_choice]=Batch(batch_choice,formula,loaves,size)
                        save()
                
                if choice=='d':
                        batch=input('Which load to delete?')
                        saved_objects.pop(batch)
                return

def new_batch_menu():
        while True:
                batch_name=input('Enter Batch Name:')
                if batch_name in saved_objects:
                        print('Name already exists, use an identifying name.')
                else:
                        break
        formula=input('Formula:')
        formula=saved_objects[formula]
        loaves=input('Number of Loaves:')
        size=input('Loaf Weight:')
        to_save=input('save formula?y/n')
        if to_save=='y':
                saved_objects[batch_name]=Batch(batch_name,formula,loaves,size)
                save()

def batch_menu():
        print('\nCURRENT FORMULAS ARE:\n')
        for item in saved_objects.keys():
                if type(saved_objects[item])==type(Formula()):
                        print('\t\t{0}'.format(item))
                       # item[1].print_formula()
        print('\nEXISTING BATCHES ARE:\n')
        for item in saved_objects:
                if type(saved_objects[item])==type(Batch()):
                        value=saved_objects[item]
                        print('{0}: {1} {2}kg loaves of {3}\n'.format
                              (item,value.loaves,value.loafsize,value.formula.name))
        menu_input=input("\tType 'n' to create a new load,'a' to adjust an "
                         "existing\n\t 'v' to view\n\tor any key to return to main menu\n")
        Route={'n':new_batch_menu,'a':batch_adjust_menu,'v':view_batch_menu}
        Route.get(menu_input,exitmenu)()

def new_bake_menu():
        L=[]
        while True:
                bake_name=input('Enter Bake Name:')
                if bake_name in saved_objects:
                        print('Name already exists, use an identifying name.')
                else:
                        break
        print('\nEXISTING BATCHES ARE:\n')
        for item in saved_objects:
                if type(saved_objects[item])==type(Batch()):
                        value=saved_objects[item]
                        print('{0}: {1} {2}kg loaves of {3}\n'.format
                              (item,value.loaves,value.loafsize,value.formula.name))      
        print('To access batch menu enter -b-')
        menu_input=input('Batch:')
        while menu_input:
                if menu_input=='b':
                        batch_menu()
                if saved_objects[menu_input]:
                        batch=menu_input
                        L.append(batch)
                else:
                        print("Entry is not a valid batch.")
                menu_input=input('Batch')
        saved_objects[bake_name]=Bake(bake_name,L)
        print('Your new bake is:')
        for item in L:
                value=saved_objects[item]
                print('{0}: {1} {2}kg loaves of {3}\n'.format
                (item,value.loaves,value.loafsize,value.formula.name))
                
                

                        
        
def main_menu():       
        print('\t\t\t\tWelcome to Bakehouse')

        menu_input=input('\n\n\nWHAT ARE WE DOING?\n\t\tType -f- for formulas\n\t\t'
                         '-b- for batch\n\t\t-a- for bake\n\t\t and -exit- to quit\n')
        Route={'f':formula_menu,'b':batch_menu,'a':bake_menu,'exit':quit}
        Route.get(menu_input,'not an option')()
        main_menu()
        
if __name__=='__main__':
        main_menu()
