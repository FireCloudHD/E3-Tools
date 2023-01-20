#Import-------------------------------------------------------------
import math
from math import pi
from math import sqrt
from math import pow as power


class Relation:
    
    """General class for a mathematical relation"""


    def __init__(self):
        self.requiredValues : list = []        #  The values that the object requires.
        self.numberRequiredValues : int = 0    #  Number of variables required for the mathematical relation.

        self.availableValues : dict = {}       #  The values that are available to the object.
        self.numberAvailableValues : int = 0   #  Number of variables available to the object.


#Functions for usage------------------------------------------------

    #  Updates the relation based on given values from a dictionary.
    def update_relation(self, groupDict : dict):

        """Main function called for the instance"""


        self.transfer_values(groupDict)
        

        #  If the respective relation can not be calculated, it returns a false for the update function.
        if self.can_be_calculated():
            missingValue : str = self.get_missing_value()

            self.availableValues[missingValue] = self.calculate_missing_value(missingValue)
            return True
        else:
            return False

    #  Returns a copy of the dictionary with the available values.
    def get_available_values(self):
        return self.availableValues.copy()

    #  Clears all available values.
    def clear_values(self):
        self.availableValues.clear()

    #  Deletes a given value from the relation.
    def remove_value(self, valueName):
        if valueName in self.availableValues:
            del self.availableValues[valueName]

    #  Virtuial function used by child class.
    def calculate_missing_value(self):

        """Should be overwritten by the child class.
        Passes the name of the missing value as a parameter
        which in turn can be used in a match case to return
        the adequate reuslt based on the formula required for
        the respective variable."""

        pass



    #Other functions------------------------------------------------

    #  Transfer the values from the passed dictionary into the object's properties.
    def transfer_values(self, groupDict : dict):
        #  Transfer the dictionary.
        for x in self.requiredValues:
            if x in groupDict:
                self.availableValues[x] = groupDict[x]
        
        #  Transfer the number of available values.
        self.numberAvailableValues = len(self.availableValues)

    #  Returns true if relation can be completed (Relation Axiom).
    #  (Number available values - Number of given values = 1).
    def can_be_calculated(self):
        if (self.numberRequiredValues - self.numberAvailableValues) == 1:
            return True
        elif (self.numberRequiredValues - self.numberAvailableValues) < 0:
            print("Error: Impossible state for number of values inside relation")
        else:
            return False

    def get_missing_value(self):
        for x in self.requiredValues:
            if x not in self.availableValues:
                return x



class Relation_Manager:

    """Manager class for math relations.
    Store instances inside this class to be automatically
    managed by it."""


    def __init__(self):

        self.valuesDict : dict = {}
        self.relationsList : list = []

        pass


    #Functions for usage------------------------------------------------

    #  Calculate the remaining values from the given values.
    def calculate_values(self, valuesDict : dict):

        """Calculate the remaining values based on the given
        values, which are passed as a parameter"""


        calculatedValues = valuesDict.copy()

        self.clear_relations()

        repeatCycle = True

        while repeatCycle:
            repeatCycle = False

            #  Iterate over relation instances
            for x in self.relationsList:

                if isinstance(x, Relation):
                    stateCalculation = x.update_relation(calculatedValues)

                    #  If at least one calculation occured, repeat.
                    if stateCalculation:
                        repeatCycle = True
            
            self.extract_values_from_relations(calculatedValues)

        
        return calculatedValues

    #  Add a new relation to the group.
    def add_relation(self, relationInstance : Relation):
        self.relationsList.append(relationInstance)

    #  Resets all the available values of the relations.
    def clear_relations(self):
        #  Iterate over relation instances
        for x in self.relationsList:
            
            if isinstance(x, Relation):
                x.clear_values()



    #Other functions------------------------------------------------

    #  Get the new values from the relations, which were calculated in the last step.
    def extract_values_from_relations(self, valuesDict : dict):

        #  Iterate over relation instances
        for x in self.relationsList:

            if isinstance(x, Relation):
                valuesInRelation = x.get_available_values()       #  Available values inside relation
                
                #  Iterate over the relation values (dict keys).
                for y in valuesInRelation:
                    if y not in self.valuesDict:

                        #  Put the value inside the values dictionary if not inside.
                        valuesDict[y] = valuesInRelation[y]


