"""For this code, if a variable is an Object then it is capilalized,
    eg. Flour is an Ingredient, White is a Batch."""

    
        
class Formula:
    """Specific object that refers to the bakers formula as a whole.
    it has ingredients as attributes that are linked to their baker's percentage. This is simply the ratios of ingredients, amounts are NOT specified."""
    def __init__(self,name=None,I={}):
        self.ingredients=list(I.keys())
        self.formula=I
        self.name=name

    def print_formula(self):
        X=[(self.formula[item],item) for item in self.formula.keys()]
        X=sorted(X,key=None, reverse=True)
        i=0
        print('\t\t{0}:\n'.format(self.name))
        while i<len(X):
            print ('\t\t{0:<20} {1:>12.3f}'.format(X[i][1],X[i][0]))
            i+=1
        print('')
"""working on storing created formulas using pickle, difficulty is loading them
    all up at start of program. Solution? Create file seperately that contains
    a list, then at start of program open file, load formula's then, then save
    subsequent formulas to that file."""
#saved_formulas_file=open('formulas.pkl','rb')


#try:
 #   saved_formulas=pickle.load(saved_formulas_file)
#except EOFError:
 #  saved_formulas=[]
 
#for item in saved_formulas:
 #   vars()[item[0]]=item[1] 

#def save_formula(self):
 #   saved_formulas.append([self.name,self])
  #  pickle.dump(saved_formulas,open('formulas.pkl','wb',-1))


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

    
