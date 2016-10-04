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

menuhead='--'*30+'/n'

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
        #doesn't display in alpabetic format. would be nice . . . 
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

def view_batch_menu():
        batch_choice=input('Which batch to print?')
        batch=saved_objects[batch_choice]
        batch.print_batch()
        

def batch_adjust_menu():
        for item in saved_objects.keys():
                if type(saved_objects[item])==type(Batch()):
                        print('\t\t{0}'.format(int(item)))
        batch_choice=input('\nBatch to edit?\n')
        while saved_objects[batch_choice]:
                batch=saved_objects[batch_choice]
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
                else:
                        batch_menu()
        batch_menu()

def new_batch_menu():
        print('Batch Menu')
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
        print('\nFormulas are:')
        for item in saved_objects:
                if type(saved_objects[item])==type(Formula()):
                        print('\t',item)
        while True:
                bake_name=input('Enter Bake Name:\n')
                if bake_name:
                        if bake_name in saved_objects:
                            print('Name already exists, use a unique name.\n')
                            continue
                        else:
                            break #entered a valid name, now can build bake.
        else: return
        while True:
                more=input('Enter Load Name\n')
                if more=='':
                    break
                if more in saved_objects:
                        print('Name already exists, use a unique name.')
                else:
                    formula=input('Formula:')
                    formula=saved_objects[formula]
                    loaves=input('Number of Loaves:')
                    size=input('Loaf Weight(Kg):')
                    load=saved_objects[more]=Batch(more,formula,loaves,size)
                    L.append(more)
                    print('You have added the following load:\n{0}: {1} {2}kg loaves of {3}\n'.format
                              (more,load.loaves,load.loafsize,load.formula.name))
        saved_objects[bake_name]=Bake(bake_name,L)
        save()
        print('Your bake is:\n')
        for item in L:
                value=saved_objects[item]            
                print('{0}: {1} {2}kg loaves of {3}\n'.format
                (item,value.loaves,value.loafsize,value.formula.name))


"""def new_bake_menu():
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
                (item,value.loaves,value.loafsize,value.formula.name))"""

def adjust_bake_menu():
        bake=input('Which bake to modify?\n')
        while saved_objects[bake]:
                for item in saved_objects[bake].Batches:
                        value=saved_objects[item]
                        print('{0}: {1} {2}kg loaves of {3}\n'.format
                        (item,value.loaves,value.loafsize,value.formula.name))
                batch_adjust_menu()

def delete_bake_menu():
        bake=input('Which bake to delete?\n')
        while saved_objects[bake]:
                sure=input('Delete this bake? y/n\n')
                if sure=='y':
                     saved_objects.pop(bake)
                save()
                return

def bake_data_menu():
    print(menuhead)
    K={'t':'for total ingredients.','l':'for the leaven schedule'}
    bake=input('\nWhich bake to analyze?\n')
    for item in K:
        print('Enter {0:<1} {1:>10}'.format(item,K[item]))
    choice=input('\n')
    S={}
    bakeobject=saved_objects[bake]
    if choice=='t':
        for load in bakeobject.loads:
                load=saved_objects[load]
                for ingredient in load.formula.ingredients:
                        S[ingredient]=ingredient
    print('The bake',bake,'requires the following amounts:')
    for ingredient in sorted(S.keys(),reverse=True):
        amount_needed(bake,ingredient)
              
        
#leaven refresh
#leaven store
#leaven revive
#leaven build
def leaven_schedule(bake):
        req_leaven= 1.07*(amount_needed_data(bake,'Leaven'))
        d12=Batch('d-12| Leaven Build',saved_objects['Leaven Build'],1,req_leaven)
        req_leaven= 1.07*(d12.req_ingredient('Leaven'))
        if req_leaven<0.370:
                req_leaven=0.370
        d24=Batch('d-24| 2nd Refresh',saved_objects['Leaven Refresh'],1,req_leaven)
        d36=Batch('d-36| 1st Refresh',saved_objects['Leaven Refresh'],1,0.370)
        d48=Batch('d-48| Revival',saved_objects['Leaven Revive'],1,0.475)
        print(menuhead)
        print('\t\t\tThe Leaven schedule for',bake,'is:\n\n')
        d48.print_batch()
        d36.print_batch()
        d24.print_batch()
        d12.print_batch()
        print('\n\t\tBake Day| Leaven Store:\n')
        print('\t\t{0:<20} {1:>12.3f}'.format('Leaven',0.075))
        print('\t\t{0:<20} {1:>12.3f}'.format('Whole Wheat',0.200))
        
def amount_needed_data(bake,ingredient):
    T=[(saved_objects[load]).recipe()[ingredient]
       for load in saved_objects[bake].loads]
    req=sum(T)
    return req     


def amount_needed(bake,ingredient):
    T=[(saved_objects[load]).recipe()[ingredient]
       for load in saved_objects[bake].loads]
    req=sum(T)
    print('{0:>6.3f} {1} {2:<15}'.format(req,'kg of',ingredient))

def bake_ingredients_menu():
        print(menuhead)
        bake=saved_objects[input('What bake to query?/n')]
        T={}
        for load in bake.loads:
                load=saved_objects[load]
                for item in load.recipe():
                        if item in T:
                                T[item]+=load.recipe()[item]
                        else:
                                T[item]=load.recipe()[item]
        L=[(x,T[x]) for x in T]
        L.sort(key=lambda x:x[0])
        print('Bake requires:\n')
        for item in L:
                print('{0:05.3f} kg of {1}.'.format(item[1],item[0]))    

def view_bake_menu():
        print('\n\n\n')
        bake=input('Which bake to view?\n')
        print('\n{0} consists of {1} loads as follows:\n'.format(bake,len(saved_objects[bake].loads)))
        for item in saved_objects[bake].loads:
                value=saved_objects[item]
                print('{0}: {1} {2}kg loaves of {3}\n'.format
                (item,value.loaves,value.loafsize,value.formula.name))
                value.print_batch()
        
                
def bake_menu():
        print('\nEXISTING BAKES ARE:\n')
        for item in saved_objects:
                if type(saved_objects[item])==type(Bake()):
                        print('\t',item)
        print('\n\n')
        menu_input=input('Plan a -n-ew bake?\n-a-djust and existing?\n'
                         'Access bake -d-ata?\n-d-elete a bake?')
        Route={'n':new_bake_menu,'a':adjust_bake_menu,'v':view_bake_menu,'d':bake_data_menu}
        Route.get(menu_input,exitmenu)()
        

                        
        
def main_menu():       
        menu_input=input('\n\n\nWHAT ARE WE DOING?\n\t\tType -f- for formulas\n\t\t'
                         '-b- for batch\n\t\t-a- for bake\n\t\t and -exit- to quit\n')
        Route={'f':formula_menu,'b':batch_menu,'a':bake_menu,'exit':quit}
        Route.get(menu_input,'not an option')()
        main_menu()
        
"""if __name__=='__main__':
        print('\t\t\t\tWelcome to Bakehouse')
        main_menu()
"""
