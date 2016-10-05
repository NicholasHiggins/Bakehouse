from Classes import*
def view_batch_menu():
        menuhead()
        batch_choice=input('Which batch to print?')
        batch=saved_objects[batch_choice]
        batch.print_batch()
        

def batch_adjust_menu():
        menuhead()
        for item in sorted(saved_objects.keys()):
                if type(saved_objects[item])==type(Batch()):
                        print('\t\t{0}'.format(item))
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
                #need to make seperate function to delete a batch and move to main batch
                if choice=='d':
                        batch=input('Which load to delete?')
                        saved_objects.pop(batch)
                else:
                        batch_menu()
        batch_menu()

def new_batch_menu():
        menuhead()
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
        menuhead()
        print('\nCURRENT FORMULAS ARE:\n')
        for item in sorted(saved_objects.keys()):
                if type(saved_objects[item])==type(Formula()):
                        print('\t\t{0}'.format(item))
                       # item[1].print_formula()
        print('\nEXISTING BATCHES ARE:\n')
        for item in sorted(saved_objects.keys()):
                if type(saved_objects[item])==type(Batch()):
                        value=saved_objects[item]
                        print('{0}: {1} {2}kg loaves of {3}\n'.format
                              (item,value.loaves,value.loafsize,value.formula.name))
        menu_input=input("\tType 'n' to create a new load,'a' to adjust an "
                         "existing\n\t 'v' to view\n\tor any key to return to main menu\n")
        Route={'n':new_batch_menu,'a':batch_adjust_menu,'v':view_batch_menu}
        Route.get(menu_input,exitmenu)()
