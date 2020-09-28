#!/usr/bin/env python3
'''convert fahrenheit to celsius and v´classifiý values based temperatures.

Usage:
    ./temp_functions.py

Author:
    Kari Korpinen - 28.9.2020
'''
def fahr_to_celsius(temp_fahrenheit):
    """
    Function for converting temperature in Fahrenheit to Celsius.

    Parameter
    ----------
    temp_fahrenheit: <numerical>
        Temperature in Fahrenheit
    convert_to: <float>
        Target temperature is Celsius. Supported values: numerical

    Returns
    -------
    <float>
        Converted temperature.
    """
    # convert fahrenheit to celsius degrees using formula
    converted_temp = (temp_fahrenheit - 32)/1.8 
    return converted_temp

def temp_classifier(temp_celsius):
    """
    Function for classifying temperatures in Celsius

    Parameters
    ----------
    temp_celsius: <numerical>
        Temperature in Celsius
    convert_to: <int>
        check value ranges and classify values based to 
        if temperatures below -2 degrees Celsius return 0
        if temperatures equal or warmer than -2, but less than +2 degrees Celsius return 1
        if temperatures equal or warmer than +2, but less than +15 degrees Celsius return 2
        if temperatures equal or warmer than +15 degrees Celsius return 3
        
    Returns
    -------
    <int>
        class value.
    """
    # test if < -2
    if(temp_celsius < -2): 
        return 0
    # test range >= -2 to < 2
    elif((temp_celsius >= -2) and (temp_celsius < 2)): 
        return 1 
    # test range >= 2 to < 15
    elif((temp_celsius >= 2) and (temp_celsius < 15)):
        return 2
    # test if >= 15
    else:  
        return 3
