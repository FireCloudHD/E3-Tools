#Import-------------------------------------------------------------
import math
from math import pi
from math import sqrt
from math import pow as power



#Functions----------------------------------------------------------
#  Functions for the resonance frequency
def get_f_res_lc(inductance, capacitance):

    """Calculate the resonance frequency based on
    the inductance and the capacitance of the circuit"""

    #  Calculate the variable
    calculatedValue = 1/(2*pi*sqrt(inductance*capacitance))

    return calculatedValue


def get_f_res_band(qualityFactor, bandwidth):

    """Calculate the resonance frequency based on
    the band width and resonance factor"""

    #  Calculate the variable
    calculatedValue = qualityFactor*bandwidth

    return calculatedValue


#  Functions for the resonance reactance
def get_x_res_lc(inductance, capacitance):

    """Calculate the reactance at the resonance frequency
    based on the inductance and capacitance"""

    #  Calculate the variable
    calculatedValue = sqrt(inductance/capacitance)

    return calculatedValue


def get_x_res_q(qualityFactor, circuitImpedance):

    """Calculate the reactance at the resonance frequency
    based on the quality factor and the circuit impedance"""

    #  Calculate the variable
    calculatedValue = qualityFactor*circuitImpedance

    return calculatedValue


def get_x_res_ul(current, voltageInductor):

    """Calculate the reactance at the resonance frequency
    based on the inductor voltage and the circuit current"""

    #  Calculate the variable
    calculatedValue = (-1*voltageInductor)/current

    return calculatedValue


def get_x_res_uc(current, voltageCapacitor):

    """Calculate the reactance at the resonance frequency
    based on the capacitor voltage and the circuit current"""

    #  Calculate the variable
    calculatedValue = voltageCapacitor/current

    return calculatedValue


#  Functions for the quality factor
def get_q_impedance(resonanceReactance, circuitImpedance):

    """Calculate the quality factor based on the resonance
    reactance and the circuit impedance"""

    #  Calculate the variable
    calculatedValue = resonanceReactance/circuitImpedance

    return calculatedValue


def get_q_d(lossFactor):

    """Calculate the quality factor based on the loss factor"""

    #  Calculate the variable
    calculatedValue = 1/lossFactor

    return calculatedValue


def get_q_band(resonanceFrequency, bandWidth):

    """Calculate the quality factor based on resonance frequency
    and the bandwidth"""

    #  Calculate the variable
    calculatedValue = resonanceFrequency/bandWidth

    return calculatedValue


#  Functions for the loss factor
def get_d(qualityFactor):

    """Calculate the loss factor based on the quality factor"""

    #  Calculate the variable
    calculatedValue = 1/qualityFactor

    return calculatedValue


#  functions for the band width
def get_bandwidth(resonanceFrequency, qualityFactor):

    """Calculate the bandwidth based on the resonance frequency
    and the quality factor"""

    #  Calculate the variable
    calculatedValue = resonanceFrequency/qualityFactor

    return calculatedValue



#  Functions for the inductance
def get_inductance_x_res(resonanceReactance, capacitance):

    """Calculate the inductance based on the resonance
    reactance and the capacitance"""

    #  Calculate the variable
    calculatedValue = power(resonanceReactance, 2)*capacitance

    return calculatedValue


def get_inductance_f_res(resonanceFrequency, capacitance):

    """Calculate the inductance based on the resonance
    frequency and the capacitance"""

    #  Calculate the variable
    calculatedValue = power(1/(2*pi*resonanceFrequency), 2)/capacitance

    return calculatedValue


#  Functions for the capacitance
def get_capacitance_x_res(resonanceReactance, inductance):

    """Calculate the capacitance based on the resonance
    reactance and the inductance"""

    #  Calculate the variable
    calculatedValue = inductance/power(resonanceReactance, 2)

    return calculatedValue


def get_capacitance_f_res(resonanceFrequency, inductance):

    """Calculate the capacitance based on the resonance
    frequency and the inductance"""

    #  Calculate the variable
    calculatedValue = power(1/(2*pi*resonanceFrequency), 2)/inductance

    return calculatedValue


#  Functions for the circuit impedance
def get_impedance_q(qualityFactor, resonanceReactance):

    """Calculate the circuit impedance based on the
    quality factor and the resonance reactance"""

    #  Calculate the variable
    calculatedValue = resonanceReactance/qualityFactor

    return calculatedValue


def get_impedance_u(inputVoltage, current):

    """Calculate the circuit impedance based on the
    input voltage and the input current"""

    #  Calculate the variable
    calculatedValue = inputVoltage/current

    return calculatedValue


#  Functions for the input voltage
def get_voltage_input(current, circuitImpedance):

    """Calculate the input voltage based on the
    circuit impedance and the input current"""

    #  Calculate the variable
    calculatedValue = current*circuitImpedance

    return calculatedValue


#  Functions for the input current
def get_current_input(inputVoltage, circuitImpedance):

    """Calculate the input current based on the
    input voltage and the circuit impedance"""

    #  Calculate the variable
    calculatedValue = inputVoltage/circuitImpedance

    return calculatedValue


def get_current_u_i(resonanceReactance, voltageInductor):

    """Calculate the input current based on the
    resonance reactance and the inductor voltage"""

    #  Calculate the variable
    calculatedValue = (-1*voltageInductor)/resonanceReactance

    return calculatedValue


def get_current_u_c(resonanceReactance, voltageCapacitor):

    """Calculate the input current based on the
    resonance reactance and the capacitor voltage"""

    #  Calculate the variable
    calculatedValue = voltageCapacitor/resonanceReactance

    return calculatedValue


#  Functions for inductor voltage
def get_u_inductor(current, resonanceReactance):

    """Calculate the inductor voltage based on the
    resonance reactance"""

    #  Calculate the variable
    calculatedValue = -1*(current * resonanceReactance)

    return calculatedValue


#  Functions for capacitor voltage
def get_u_capacitor(current, resonanceReactance):

    """Calculate the capacitor voltage based on the
    resonance reactance"""

    #  Calculate the variable
    calculatedValue = current * resonanceReactance

    return calculatedValue