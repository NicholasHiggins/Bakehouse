"""This module handles the pickling of formulas, there is no reason not to
expand it to also pickle batches and bakes"""

import pickle
from Classes import *

try:
        saved_objects=pickle.load(open('objects.pkl','rb'))
except FileNotFoundError:
        saved_objects={'test':'test'}
        pickle.dump(saved_objects,open('objects.pkl','wb',-1))

        
def delete(item):
        #This will remove formula from list but formula will
        #persist until next session. A quirk I'll leave.
        saved_objects.pop(item.name)
        pickle.dump(saved_objects,open('objects.pkl','wb',-1))




        
                
