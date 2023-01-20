#Import-------------------------------------------------------------
#  Program modules
import RLC_functions
import RLC_relations

#  Other Modules
import os
from enum import Enum



#Program Constants
#  Input states
class statesInput(Enum):

    SELECT_CALCULATOR = 0

    RLC_CALCULATOR = 1
    L_CALCULATOR = 2
    C_CALCULATOR = 3


#  Names for the RLC variables
NAME_INDUCTANCE = "L"
NAME_CAPACITANCE = "C"
NAME_Z_RESONANCE = "Z_0"
NAME_F_RESONANCE = "f_0"
NAME_X_RESONANCE = "X_0"
NAME_QUALITY_FACTOR = "Q"
NAME_LOSS_FACTOR = "d"
NAME_BANDWIDTH = "b"
NAME_VOLTAGE_INPUT = "U"
NAME_CURRENT = "I"
NAME_VOLTAGE_L = "U_L"
NAME_VOLTAGE_C = "U_C"

LIST_VARIABLE_NAMES = [NAME_INDUCTANCE, NAME_CAPACITANCE, NAME_Z_RESONANCE, NAME_F_RESONANCE, NAME_X_RESONANCE, NAME_QUALITY_FACTOR,
                       NAME_LOSS_FACTOR, NAME_BANDWIDTH, NAME_VOLTAGE_INPUT, NAME_CURRENT, NAME_VOLTAGE_L, NAME_VOLTAGE_C]
DICT_UNITS = {NAME_INDUCTANCE : "H", NAME_CAPACITANCE : "F", NAME_Z_RESONANCE : "Ohm", NAME_F_RESONANCE : "Hz", NAME_X_RESONANCE : "Ohm",
               NAME_QUALITY_FACTOR : "", NAME_LOSS_FACTOR : "", NAME_BANDWIDTH : "Hz", NAME_VOLTAGE_INPUT : "V", NAME_CURRENT : "A",
               NAME_VOLTAGE_L : "V", NAME_VOLTAGE_C : "V"}





#Program Functions--------------------------------------------------
def convert_to_si_prefix(value):
    #  A list of the positive prefixes we want to use
    positive_prefixes = ['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']

    #  A list of the negative prefixes we want to use
    negative_prefixes = ['m', 'μ', 'n', 'p', 'f', 'a', 'z', 'y']


    #  Divide the value by 1000 or multiply it by 1000 until it falls within the desired range
    if (value >= 1) or (value <= -1):
        for prefix in positive_prefixes:
            if -1000 < value < 1000:
                #  If the value is within the desired range, return it with the appropriate prefix
                return f"{value:.2f}{prefix}"
            else:
                #  If the value is outside the desired range, divide it by 1000 and try again
                value /= 1000
    else:
        for prefix in negative_prefixes:

            value *= 1000
            if (value <= -1) or (value >= 1):
                #  If the value is within the desired range, return it with the appropriate prefix
                return f"{value:.2f}{prefix}"

    #  If the value is still outside the desired range after all the prefixes have been tried,
    #  return it with the appropriate prefix for its sign
    if value > 0:
        return f"{value:.2f}Y"
    else:
        return f"{value:.2f}y"

#  Print the calculated valus in a row.
def print_calculated_values(valuesDict : dict):
    
    strStandardValues : str= ""
    strResonanceValues : str = ""
    strDynamicValues : str = ""


    for i in range(3):
        if LIST_VARIABLE_NAMES[i] in valuesDict:
            strStandardValues += LIST_VARIABLE_NAMES[i]+": "+convert_to_si_prefix(valuesDict[LIST_VARIABLE_NAMES[i]])+DICT_UNITS[LIST_VARIABLE_NAMES[i]]+"\n"
        else:
            strStandardValues += LIST_VARIABLE_NAMES[i]+": "+"?"+"\n"
    strStandardValues += "\n"

    for i in range(3, 8):
        if LIST_VARIABLE_NAMES[i] in valuesDict:
            strResonanceValues += LIST_VARIABLE_NAMES[i]+": "+convert_to_si_prefix(valuesDict[LIST_VARIABLE_NAMES[i]])+DICT_UNITS[LIST_VARIABLE_NAMES[i]]+"\n"
        else:
            strResonanceValues += LIST_VARIABLE_NAMES[i]+": "+"?"+"\n"
    strResonanceValues += "\n"


    for i in range(8, 12):
        if LIST_VARIABLE_NAMES[i] in valuesDict:
            strDynamicValues += LIST_VARIABLE_NAMES[i]+": "+convert_to_si_prefix(valuesDict[LIST_VARIABLE_NAMES[i]])+DICT_UNITS[LIST_VARIABLE_NAMES[i]]+"\n"
        else:
            strDynamicValues += LIST_VARIABLE_NAMES[i]+": "+"?"+"\n"
    strDynamicValues += "\n"


    print(strStandardValues + strResonanceValues + strDynamicValues)

#  Calculate the remaining RLC values and return it in form of a dictionary.
def calculate_Values_RLC(valuesGiven : dict):
    
    calculatedValues : dict  = valuesGiven.copy()


    continueCalculation : bool = True

    while continueCalculation:

        continueCalculation = False


        #  Check for the resonance frequency and then calculate
        if NAME_F_RESONANCE not in calculatedValues:

            isCalculated = True

            if (NAME_INDUCTANCE in calculatedValues) and (NAME_CAPACITANCE in calculatedValues) and isCalculated:
                calculatedValues[NAME_F_RESONANCE] = RLC_functions.get_f_res_lc(calculatedValues[NAME_INDUCTANCE], calculatedValues[NAME_CAPACITANCE])
                isCalculated = False
                continueCalculation = True                
            
            if (NAME_QUALITY_FACTOR in calculatedValues) and (NAME_BANDWIDTH in calculatedValues) and isCalculated:
                calculatedValues[NAME_F_RESONANCE] = RLC_functions.get_f_res_band(calculatedValues[NAME_QUALITY_FACTOR], calculatedValues[NAME_BANDWIDTH])
                isCalculated = False
                continueCalculation = True


        #  Check for the resonance reactance and then calculate
        if NAME_X_RESONANCE not in calculatedValues:

            isCalculated = True

            if (NAME_INDUCTANCE in calculatedValues) and (NAME_CAPACITANCE in calculatedValues) and isCalculated:
                calculatedValues[NAME_X_RESONANCE] = RLC_functions.get_x_res_lc(calculatedValues[NAME_INDUCTANCE], calculatedValues[NAME_CAPACITANCE])
                isCalculated = False
                continueCalculation = True


            if (NAME_QUALITY_FACTOR in calculatedValues) and (NAME_Z_RESONANCE in calculatedValues) and isCalculated:
                calculatedValues[NAME_X_RESONANCE] = RLC_functions.get_x_res_q(calculatedValues[NAME_QUALITY_FACTOR], calculatedValues[NAME_Z_RESONANCE])
                isCalculated = False
                continueCalculation = True

            if (NAME_CURRENT in calculatedValues) and (NAME_VOLTAGE_L in calculatedValues) and isCalculated:
                calculatedValues[NAME_X_RESONANCE] = RLC_functions.get_x_res_ul(calculatedValues[NAME_CURRENT], calculatedValues[NAME_VOLTAGE_L])
                isCalculated = False
                continueCalculation = True

            if (NAME_CURRENT in calculatedValues) and (NAME_VOLTAGE_C in calculatedValues) and isCalculated:
                calculatedValues[NAME_X_RESONANCE] = RLC_functions.get_x_res_uc(calculatedValues[NAME_CURRENT], calculatedValues[NAME_VOLTAGE_C])
                isCalculated = False
                continueCalculation = True


        #  Check for the quality factor and then calculate
        if NAME_QUALITY_FACTOR not in calculatedValues:

            isCalculated = True

            if (NAME_X_RESONANCE in calculatedValues) and (NAME_Z_RESONANCE in calculatedValues) and isCalculated:
                calculatedValues[NAME_QUALITY_FACTOR] = RLC_functions.get_q_impedance(calculatedValues[NAME_X_RESONANCE], calculatedValues[NAME_Z_RESONANCE])
                isCalculated = False
                continueCalculation = True

            if (NAME_LOSS_FACTOR in calculatedValues) and isCalculated:
                calculatedValues[NAME_QUALITY_FACTOR] = RLC_functions.get_q_d(calculatedValues[NAME_LOSS_FACTOR])
                isCalculated = False
                continueCalculation = True

            if (NAME_F_RESONANCE in calculatedValues) and (NAME_BANDWIDTH in calculatedValues) and isCalculated:
                calculatedValues[NAME_QUALITY_FACTOR] = RLC_functions.get_q_band(calculatedValues[NAME_F_RESONANCE], calculatedValues[NAME_BANDWIDTH])
                isCalculated = False
                continueCalculation = True


        #  Check for the loss factor and then calculate
        if  NAME_LOSS_FACTOR not in calculatedValues:

            isCalculated = True

            if (NAME_QUALITY_FACTOR in calculatedValues) and isCalculated:
                calculatedValues[NAME_LOSS_FACTOR] = RLC_functions.get_d(calculatedValues[NAME_QUALITY_FACTOR])
                isCalculated = False
                continueCalculation = True


        #  Check for the band width and then calculate
        if NAME_BANDWIDTH not in calculatedValues:

            isCalculated = True

            if (NAME_F_RESONANCE in calculatedValues) and (NAME_QUALITY_FACTOR in calculatedValues) and isCalculated:
                calculatedValues[NAME_BANDWIDTH] = RLC_functions.get_bandwidth(calculatedValues[NAME_F_RESONANCE], calculatedValues[NAME_QUALITY_FACTOR])
                isCalculated = False
                continueCalculation = True


        #  Check for the inductance and then calculate
        if NAME_INDUCTANCE not in calculatedValues:

            isCalculated = True

            if (NAME_X_RESONANCE in calculatedValues) and (NAME_CAPACITANCE in calculatedValues) and isCalculated:
                calculatedValues[NAME_INDUCTANCE] = RLC_functions.get_inductance_x_res(calculatedValues[NAME_X_RESONANCE], calculatedValues[NAME_CAPACITANCE])
                isCalculated = False
                continueCalculation = True

            if (NAME_F_RESONANCE in calculatedValues) and (NAME_CAPACITANCE in calculatedValues) and isCalculated:
                calculatedValues[NAME_INDUCTANCE] = RLC_functions.get_inductance_f_res(calculatedValues[NAME_F_RESONANCE], calculatedValues[NAME_CAPACITANCE])
                isCalculated = False
                continueCalculation = True


        #  Check for the capacitance and then calculate
        if NAME_CAPACITANCE not in calculatedValues:

            isCalculated = True

            if (NAME_X_RESONANCE in calculatedValues) and (NAME_INDUCTANCE in calculatedValues) and isCalculated:
                calculatedValues[NAME_CAPACITANCE] = RLC_functions.get_capacitance_x_res(calculatedValues[NAME_X_RESONANCE], calculatedValues[NAME_INDUCTANCE])
                isCalculated = False
                continueCalculation = True

            if (NAME_F_RESONANCE in calculatedValues) and (NAME_INDUCTANCE in calculatedValues) and isCalculated:
                calculatedValues[NAME_CAPACITANCE] = RLC_functions.get_capacitance_x_res(calculatedValues[NAME_F_RESONANCE], calculatedValues[NAME_INDUCTANCE])
                isCalculated = False
                continueCalculation = True


        #  Check for the resonance impedance and then calculate
        if NAME_Z_RESONANCE not in calculatedValues:

            isCalculated = True

            if (NAME_QUALITY_FACTOR in calculatedValues) and (NAME_X_RESONANCE in calculatedValues) and isCalculated:
                calculatedValues[NAME_Z_RESONANCE] = RLC_functions.get_impedance_q(calculatedValues[NAME_QUALITY_FACTOR], calculatedValues[NAME_X_RESONANCE])
                isCalculated = False
                continueCalculation = True

            if (NAME_VOLTAGE_INPUT in calculatedValues) and (NAME_CURRENT in calculatedValues) and isCalculated:
                calculatedValues[NAME_Z_RESONANCE] = RLC_functions.get_impedance_u(calculatedValues[NAME_VOLTAGE_INPUT], calculatedValues[NAME_CURRENT])
                isCalculated = False
                continueCalculation = True


        #  Check for the input voltage and then calculate
        if NAME_VOLTAGE_INPUT not in calculatedValues:

            isCalculated = True

            if (NAME_CURRENT in calculatedValues) and (NAME_Z_RESONANCE in calculatedValues) and isCalculated:
                calculatedValues[NAME_VOLTAGE_INPUT] = RLC_functions.get_voltage_input(calculatedValues[NAME_CURRENT], calculatedValues[NAME_Z_RESONANCE])
                isCalculated = False
                continueCalculation = True


        #  Check for the input current and then calculate
        if NAME_CURRENT not in calculatedValues:

            isCalculated = True

            if (NAME_VOLTAGE_INPUT in calculatedValues) and (NAME_Z_RESONANCE in calculatedValues) and isCalculated:
                calculatedValues[NAME_CURRENT] = RLC_functions.get_current_input(calculatedValues[NAME_VOLTAGE_INPUT], calculatedValues[NAME_Z_RESONANCE])
                isCalculated = False
                continueCalculation = True

            if (NAME_X_RESONANCE in calculatedValues) and (NAME_VOLTAGE_L in calculatedValues) and isCalculated:
                calculatedValues[NAME_CURRENT] = RLC_functions.get_current_u_i(calculatedValues[NAME_X_RESONANCE], calculatedValues[NAME_VOLTAGE_L])
                isCalculated = False
                continueCalculation = True

            if (NAME_X_RESONANCE in calculatedValues) and (NAME_VOLTAGE_C in calculatedValues) and isCalculated:
                calculatedValues[NAME_CURRENT] = RLC_functions.get_current_u_c(calculatedValues[NAME_X_RESONANCE], calculatedValues[NAME_VOLTAGE_C])
                isCalculated = False
                continueCalculation = True


        #  Check for the inductor voltage and then calculate
        if NAME_VOLTAGE_L not in calculatedValues:

            isCalculated = True

            if (NAME_CURRENT in calculatedValues) and (NAME_X_RESONANCE in calculatedValues) and isCalculated:
                calculatedValues[NAME_VOLTAGE_L] = RLC_functions.get_u_inductor(calculatedValues[NAME_CURRENT], calculatedValues[NAME_X_RESONANCE])
                isCalculated = False
                continueCalculation = True


        #  Check for the capacitor voltage and then calculate
        if NAME_VOLTAGE_C not in calculatedValues:

            isCalculated = True

            if (NAME_CURRENT in calculatedValues) and (NAME_X_RESONANCE in calculatedValues) and isCalculated:
                calculatedValues[NAME_VOLTAGE_C] = RLC_functions.get_u_capacitor(calculatedValues[NAME_CURRENT], calculatedValues[NAME_X_RESONANCE])
                isCalculated = False
                continueCalculation = True


    return calculatedValues







#Main function------------------------------------------------------
def main():

    inputDict : dict = {NAME_INDUCTANCE : 4.7e-3,  NAME_CAPACITANCE : 100e-6, NAME_Z_RESONANCE : 0.5, NAME_CURRENT : 20}
    inputDict : dict = {NAME_VOLTAGE_C : 130, NAME_VOLTAGE_INPUT : 10}

    dictValues = calculate_Values_RLC(inputDict)



    stateInput = statesInput.SELECT_CALCULATOR           #  The state for the input
    inputedText : str = ""                               #  String which collects input


    flagRepeatInput : bool = True

    while True:

        #Input
        match stateInput:

            #  Case for the selection of the calculator
            case statesInput.SELECT_CALCULATOR:

                print              ("\n\n===================================")
                print              ("===================================")
                print              ("")
                print              ("[L]              [C]             [RLC]")

                inputedText = input("Which calculator would you like to use: ")
                print              ("[L]")
                print              ("[C]")
                print              ("[RLC]")
                inputedText = inputedText.lower()

                #  Decide mode
                if inputedText == "l":
                    stateInput = statesInput.L_CALCULATOR
                elif inputedText == "c":
                    stateInput = statesInput.C_CALCULATOR
                elif inputedText == "rlc":
                    stateInput = statesInput.RLC_CALCULATOR
                elif inputedText == "suicide":
                    exit()
                else:
                    stateInput = ""

            #  Case for the RLC calculator
            case statesInput.RLC_CALCULATOR:

                givenValues : dict = {}
                processedValues : dict = {}

                relManager = RLC_relations.Relation_Manager()

                relManager.add_relation(RLC_relations.Relation_X_0())
                relManager.add_relation(RLC_relations.Relation_f_0())
                relManager.add_relation(RLC_relations.Relation_Q_R())
                relManager.add_relation(RLC_relations.Relation_Q_U())
                relManager.add_relation(RLC_relations.Relation_Q_C())
                relManager.add_relation(RLC_relations.Relation_d())
                relManager.add_relation(RLC_relations.Relation_b())
                relManager.add_relation(RLC_relations.Relation_U_I())
                relManager.add_relation(RLC_relations.Relation_UC_I())
                relManager.add_relation(RLC_relations.Relation_UL_UC())


                isInputGiven: bool = True

                while isInputGiven:
                    os.system("cls")        #  Clear the screen

                    print              ("\n\n============================================")
                    print              ("")
                    print              ("The following values can be specified:")
                    print              ("")
                    print              ("  [L]  -  Circuit Inductance")
                    print              ("  [C]  -  Circuit Capacitance")
                    print              ("[Z_0]  -  Circuit Impedance at Resonance")
                    print              ("")
                    print              ("[f_0]  -  Resonance Frequency")
                    print              ("[X_0]  -  Resonance Reactance")
                    print              ("  [Q]  -  Quality Factor")
                    print              ("  [d]  -  Loss Factor")
                    print              ("  [b]  -  Bandwidth")
                    print              ("")
                    print              ("  [U]  -  Input Voltage")
                    print              ("  [I]  -  Input Current")
                    print              ("[U_L]  -  Voltage Inductor at Resonance")
                    print              ("[U_C]  -  Voltage Capacitor at Resonance")
                    print              ("---------------------------------------------")
                    print              ("     The remaining values are calculated")
                    print              ("     based on the given values.")
                    print              ("---------------------------------------------")
                    print              ("To input a value, first specify the variable, then put")
                    print              ("an equal sign and afterwards write the value that you desire.")
                    print              ("")
                    print              ("The following is an example for the format: X_0=420e-3")
                    print              ("(Scientific notation may be used. If a value does not get)")
                    print              ("(added, then it means that the notaion is incorrect)")
                    print              ("")
                    print              ("Values can be removed with -r <variable name>-")
                    print              ("")
                    print              ("To calculate the remaining values, type <start>")
                    print              ("============================================")
                    print              ("")
                    print              ("============================================")
                    print              ("Given Values:")
                    print              ("")
                    print_calculated_values(givenValues)       #  Display the specified values.
                    print              ("============================================\n")


                    print              ("Calculated Values:")
                    print              ("")
                    print_calculated_values(processedValues)       #  Display the calculated values.
                    print              ("============================================")

                    #  Get the input
                    inputedText = input("Input: ")

                    if inputedText == "stop":
                        isInputGiven = False
                    if inputedText == "suicide":
                        exit()


                    #  Process the input
                    if inputedText.find("-r ") != -1:

                        #  Get the symbol and the number specified
                        givenSymbol = inputedText[len("-r "):]
                        
                        if givenSymbol in LIST_VARIABLE_NAMES:
                            try:
                                del givenValues[givenSymbol]
                            except:
                                pass
                    else:
                        lenSymbol = inputedText.find("=")

                        #  Get the symbol and the number specified
                        givenSymbol = "".join([inputedText[i] for i in range(lenSymbol)])
                        givenNumber = inputedText[lenSymbol+1:]
                        givenNumberFloat : float = 0


                        if givenSymbol in LIST_VARIABLE_NAMES:
                            try:
                                givenNumberFloat = float(givenNumber)
                            except:
                                pass
                            else:
                                givenValues[givenSymbol] = givenNumberFloat

                    processedValues = relManager.calculate_values(givenValues)


                stateInput = statesInput.SELECT_CALCULATOR  #  Go back to the calculator selection.

            #  Case for an unspecified command
            case _:

                os.system("cls")

                print              ("\n\n===================================")
                print              ("")
                print              ("Unknown Command")

                stateInput = statesInput.SELECT_CALCULATOR
    





#Execute the code
if __name__ == "__main__":
    main()