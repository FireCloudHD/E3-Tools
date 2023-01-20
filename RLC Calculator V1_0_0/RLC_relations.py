#Import-------------------------------------------------------------
#  Program modules
from math_relations import Relation_Manager
from math_relations import Relation

#  Other Modules
from math import pi
from math import sqrt
from math import pow as power



class Relation_preset(Relation):

    """Relation class for calculating..."""


    def __init__(self):
        super().__init__()      #  Necessary for parent class.

        #  Variables inside the relation.
        self.requiredValues = ["..."]
        self.numberRequiredValues = len(self.requiredValues)
        

    #  Virtual function for calculating the missing value.
    def calculate_missing_value(self, missingValue : str):
        
        #  Requires the equation for every variable inside the relation.
        match missingValue:

            case "...":
                return
            case "...":
                return
            case "...":
                return


class Relation_f_0(Relation):

    """Relation class for calculating the resonance frequency."""


    def __init__(self):
        super().__init__()      #  Necessary for parent class.

        #  Variables inside the relation.
        self.requiredValues = ["C", "L", "f_0"]
        self.numberRequiredValues = len(self.requiredValues)
        

    #  Virtual function for calculating the missing value.
    def calculate_missing_value(self, missingValue : str):
        
        #  Requires the equation for every variable inside the relation.
        match missingValue:

            case "C":
                return power(1/(2*pi*self.availableValues["f_0"]), 2)/self.availableValues["L"]
            case "L":
                return power(1/(2*pi*self.availableValues["f_0"]), 2)/self.availableValues["C"]
            case "f_0":
                return 1/(2*pi*sqrt(self.availableValues["C"]*self.availableValues["L"]))


class Relation_X_0(Relation):

    """Relation class for calculating the resonance reactance."""


    def __init__(self):
        super().__init__()      #  Necessary for parent class.


        #  Variables inside the relation.
        self.requiredValues = ["X_0", "L", "C"]
        self.numberRequiredValues = len(self.requiredValues)
        

    #  Virtual function for calculating the missing value.
    def calculate_missing_value(self, missingValue : str):
        
        #  Requires the equation for every variable inside the relation.
        match missingValue:

            case "C":
                return self.availableValues["L"]/power(self.availableValues["X_0"], 2)
            case "L":
                return power(self.availableValues["X_0"], 2)*self.availableValues["C"]
            case "X_0":
                return sqrt(self.availableValues["L"]/self.availableValues["C"])


class Relation_b(Relation):

    """Relation class for calculating the bandwidth"""


    def __init__(self):
        super().__init__()      #  Necessary for parent class.

        #  Variables inside the relation.
        self.requiredValues = ["b", "f_0", "Q"]
        self.numberRequiredValues = len(self.requiredValues)
        

    #  Virtual function for calculating the missing value.
    def calculate_missing_value(self, missingValue : str):
        
        #  Requires the equation for every variable inside the relation.
        match missingValue:

            case "b":
                return self.availableValues["f_0"]/self.availableValues["Q"]
            case "f_0":
                return self.availableValues["b"]*self.availableValues["Q"]
            case "Q":
                return self.availableValues["f_0"]/self.availableValues["b"]


class Relation_Q_R(Relation):

    """Relation class for calculating the quality factor
    based on the reactance and real resistance."""


    def __init__(self):
        super().__init__()      #  Necessary for parent class.

        #  Variables inside the relation.
        self.requiredValues = ["Q", "X_0", "Z_0"]
        self.numberRequiredValues = len(self.requiredValues)
        

    #  Virtual function for calculating the missing value.
    def calculate_missing_value(self, missingValue : str):
        
        #  Requires the equation for every variable inside the relation.
        match missingValue:

            case "Q":
                return self.availableValues["X_0"]/self.availableValues["Z_0"]
            case "X_0":
                return self.availableValues["Q"]*self.availableValues["Z_0"]
            case "Z_0":
                return self.availableValues["X_0"]/self.availableValues["Q"]


class Relation_Q_U(Relation):

    """Relation class for calculating quality factor
    based on the capacitors voltage and the circuit voltage."""


    def __init__(self):
        super().__init__()      #  Necessary for parent class.

        #  Variables inside the relation.
        self.requiredValues = ["Q", "U_C", "U"]
        self.numberRequiredValues = len(self.requiredValues)
        

    #  Virtual function for calculating the missing value.
    def calculate_missing_value(self, missingValue : str):
        
        #  Requires the equation for every variable inside the relation.
        match missingValue:

            case "Q":
                return self.availableValues["U_C"]/self.availableValues["U"]
            case "U_C":
                return self.availableValues["Q"]*self.availableValues["U"]
            case "U":
                return self.availableValues["U_C"]/self.availableValues["Q"]


class Relation_Q_C(Relation):

    """Relation class for calculating the quality factor based
    on the capacitance, real resistance and the resonance frequency."""


    def __init__(self):
        super().__init__()      #  Necessary for parent class.

        #  Variables inside the relation.
        self.requiredValues = ["Q", "f_0", "C", "Z_0"]
        self.numberRequiredValues = len(self.requiredValues)
        

    #  Virtual function for calculating the missing value.
    def calculate_missing_value(self, missingValue : str):
        
        #  Requires the equation for every variable inside the relation.
        match missingValue:

            case "Q":
                return 1/(2*pi*self.availableValues["f_0"]*self.availableValues["C"]*self.availableValues["Z_0"])
            case "f_0":
                return 1/(2*pi*self.availableValues["Q"]*self.availableValues["C"]*self.availableValues["Z_0"])
            case "C":
                return 1/(2*pi*self.availableValues["f_0"]*self.availableValues["Q"]*self.availableValues["Z_0"])
            case "Z_0":
                return 1/(2*pi*self.availableValues["f_0"]*self.availableValues["C"]*self.availableValues["Q"])


class Relation_d(Relation):

    """Relation class for calculating loss factor"""


    def __init__(self):
        super().__init__()      #  Necessary for parent class.

        #  Variables inside the relation.
        self.requiredValues = ["d", "Q"]
        self.numberRequiredValues = len(self.requiredValues)
        

    #  Virtual function for calculating the missing value.
    def calculate_missing_value(self, missingValue : str):
        
        #  Requires the equation for every variable inside the relation.
        match missingValue:

            case "d":
                return 1/self.availableValues["Q"]
            case "Q":
                return 1/self.availableValues["d"]


class Relation_U_I(Relation):

    """Relation class for calculating the circuit current,
    voltage and real resistance (URI)"""


    def __init__(self):
        super().__init__()      #  Necessary for parent class.

        #  Variables inside the relation.
        self.requiredValues = ["U", "Z_0", "I"]
        self.numberRequiredValues = len(self.requiredValues)
        

    #  Virtual function for calculating the missing value.
    def calculate_missing_value(self, missingValue : str):
        
        #  Requires the equation for every variable inside the relation.
        match missingValue:

            case "U":
                return self.availableValues["I"]*self.availableValues["Z_0"]
            case "Z_0":
                return self.availableValues["U"]/self.availableValues["I"]
            case "I":
                return self.availableValues["U"]/self.availableValues["Z_0"]


class Relation_UC_I(Relation):

    """Relation class for calculating the capacitors voltage
    based on the reactance and the current."""


    def __init__(self):
        super().__init__()      #  Necessary for parent class.

        #  Variables inside the relation.
        self.requiredValues = ["U_C", "X_0", "I"]
        self.numberRequiredValues = len(self.requiredValues)
        

    #  Virtual function for calculating the missing value.
    def calculate_missing_value(self, missingValue : str):
        
        #  Requires the equation for every variable inside the relation.
        match missingValue:

            case "U_C":
                return self.availableValues["X_0"]*self.availableValues["I"]
            case "X_0":
                return self.availableValues["U_C"]/self.availableValues["I"]
            case "I":
                return self.availableValues["U_C"]/self.availableValues["X_0"]


class Relation_UL_UC(Relation):

    """Relation class for calculating the inductors voltage
    based on the capacitors voltage"""


    def __init__(self):
        super().__init__()      #  Necessary for parent class.

        #  Variables inside the relation.
        self.requiredValues = ["U_L", "U_C"]
        self.numberRequiredValues = len(self.requiredValues)
        

    #  Virtual function for calculating the missing value.
    def calculate_missing_value(self, missingValue : str):
        
        #  Requires the equation for every variable inside the relation.
        match missingValue:

            case "U_L":
                return -1*self.availableValues["U_C"]
            case "U_C":
                return -1*self.availableValues["U_L"]



