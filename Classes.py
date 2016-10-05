import pickle
"""saved_objects is now a dictionary that goes from a string key to one of our defined
        objects, be it a batch,formula or bake"""

def menuhead():
    print('--'*30+'\n')
def exitmenu():
        return
    
        
class Formula:
    """Specific object that refers to the bakers formula as a whole.
    it has ingredients as attributes that are linked to their baker's percentage. This is simply the ratios of ingredients, amounts are NOT specified."""
    def __init__(self,name=None,I={}):
        self.ingredients=list(I.keys())
        self.formula=I
        self.name=name

    def print_formula(self):
        X=[(item,self.formula[item]) for item in self.formula.keys()]
        X=sorted(X,key=None, reverse=True)
        i=0
        print('\t\t{0}:\n'.format(self.name))
        while i<len(X):
            print ('\t\t{0:<20} {1:>12.3f}'.format(X[i][0],X[i][1]))
            i+=1
        print('')
"""working on storing created formulas using pickle, difficulty is loading them
    all up at start of program. Solution? Create file seperately that contains
    a list, then at start of program open file, load formula's then, then save
    subsequent formulas to that file."""

class Batch:
    """Specifies a planned Batch of a recipe,
    i.e. 20 loaves of White @ 900g."""
    
    def __init__(self,name=None,formula=None,number_loaves=0,loafsize=0):
        self.name=name
        self.formula=formula
        self.loaves=number_loaves
        self.loafsize=loafsize #in Kg
       
    def recipe(self):
        Total_Percent=sum(self.formula.formula[ingredient]
                            for ingredient in self.formula.ingredients)
        Total_Weight=int(self.loaves)*float(self.loafsize)
        Factor=Total_Weight/Total_Percent
        return {ingredient:round(Factor*self.formula.formula[ingredient],3)
                for ingredient in self.formula.ingredients}

    def print_batch(self):
        K=self.recipe()
        R=Formula(self.name,K)
        R.print_formula()

    def req_ingredient(self,ingredient):
        return float(self.recipe()[ingredient])

class Bake:
    """Specifies a planned Bake or group of batches, ie,
    Friday Bake: 2Wholewheat Batches,1 White Batch,1 Multigrain"""

    def __init__(self,name=None,Loads=[]):
        self.loads=Loads
        self.leaven_schedule=[]

    #def amount_needed(self,ingredient):
     #   
      #  T=[(saved_objects[Batch]).recipe()[ingredient]for Batch in self.Batches]
       # return sum(T)


try:
        saved_objects=pickle.load(open('objects.pkl','rb'))
except FileNotFoundError:
        saved_objects={'test':'test'}
        pickle.dump(saved_objects,open('objects.pkl','wb',-1))

def save():
        pickle.dump(saved_objects,open('objects.pkl','wb',-1))
        pickle.load(open('objects.pkl','rb'))

def delete(item):
        saved_objects.pop(item.name)
        pickle.dump(saved_objects,open('objects.pkl','wb',-1))
        pickle.load(open('objects.pkl','rb'))

""" ::::::::::: TO DO   ::::::::::
    -need to improve the layout of the printed formulas,batches etc. Perhaps
    should print to pdf. Then easy to print hard-copy or view on screen.
    -batches should be saved similarily to Formulas
    -need to clean up the pickling process, more so I'm certain of what is
    happening exactly, specificly with the use of vars() and EOFerror
    -What exactly do I want this program to do?
    -GUI?
    ::::::::::::::::::::::::::::::::::::::::::::::::::::::"""

"""
WhiteLoad=Batch('WhiteLoad',WhiteBread,20,0.8)
WhiteLoad.print_batch()
"""

    
