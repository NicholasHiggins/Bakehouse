from Classes import *


def new_bake_menu():
        menuhead()
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
        menuhead()
        bake=input('Which bake to modify?\n')
        while saved_objects[bake]:
                for item in saved_objects[bake].loads:
                        value=saved_objects[item]
                        print('{0}: {1} {2}kg loaves of {3}\n'.format
                        (item,value.loaves,value.loafsize,value.formula.name))
                batch_adjust_menu()

def delete_bake_menu():
        menuhead()
        bake=input('Which bake to delete?\n')
        while saved_objects[bake]:
                sure=input('Delete this bake? y/n\n')
                if sure=='y':
                     saved_objects.pop(bake)
                save()
                return

def bake_data_menu():
    menuhead()
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
    if choice=='l':
            leaven_schedule(bake)
            
              
def leaven_schedule(bake):
        req_leaven= 1.07*(amount_needed_data(bake,'Leaven'))
        d12=Batch('d-12| Leaven Build',saved_objects['Leaven Build'],1,req_leaven)
        req_leaven= 1.07*(d12.req_ingredient('Leaven'))
        if req_leaven<0.370:
                req_leaven=0.370
        d24=Batch('d-24| 2nd Refresh',saved_objects['Leaven Refresh'],1,req_leaven)
        d36=Batch('d-36| 1st Refresh',saved_objects['Leaven Refresh'],1,0.370)
        d48=Batch('d-48| Revival',saved_objects['Leaven Revive'],1,0.475)
        menuhead()
        print('\t\t\tThe Leaven schedule for',bake,'is:\n\n')
        d48.print_batch()
        d36.print_batch()
        d24.print_batch()
        d12.print_batch()
        print('\n\t\tBake Day| Leaven Store:\n')
        print('\t\t{0:<20} {1:>12.3f}'.format('Leaven',0.075))
        print('\t\t{0:<20} {1:>12.3f}\n\n\n'.format('Whole Wheat',0.200))
        
def amount_needed_data(bake,ingredient):
    T=[]
    for load in saved_objects[bake].loads:
            try:
                    T.append(saved_objects[load].recipe()[ingredient])
            except:
                    pass                
    req=sum(T)
    return req     


def amount_needed(bake,ingredient):
    #T=[(saved_objects[load]).recipe()[ingredient]
     #  for load in saved_objects[bake].loads]
    T=[]
    for load in saved_objects[bake].loads:
            try:
                    T.append(saved_objects[load].recipe()[ingredient])
            except:
                    pass                
    req=sum(T)
    print('{0:>6.3f} {1} {2:<15}'.format(req,'kg of',ingredient))

def bake_ingredients_menu():
        menuhead()
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
        menuhead()
        print('\n\n\n')
        bake=input('Which bake to view?\n')
        print('\n{0} consists of {1} loads as follows:\n'.format(bake,len(saved_objects[bake].loads)))
        for item in saved_objects[bake].loads:
                value=saved_objects[item]
                print('{0}: {1} {2}kg loaves of {3}\n'.format
                (item,value.loaves,value.loafsize,value.formula.name))
                value.print_batch()
        
                
def bake_menu():
        menuhead()
        print('\nEXISTING BAKES ARE:\n')
        for item in saved_objects:
                if type(saved_objects[item])==type(Bake()):
                        print('\t',item)
        print('\n\n')
        menu_input=input('Plan a -n-ew bake?\n-a-djust and existing?\n'
                         'Access bake -d-ata?\n-d-elete a bake?')
        Route={'n':new_bake_menu,'a':adjust_bake_menu,'v':view_bake_menu,'d':bake_data_menu}
        Route.get(menu_input,exitmenu)()
