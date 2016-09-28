#!usr/bin/env python
# -*- coding: utf-8 -*-
"""This is a docstring for assignment 4 Synthesizing task"""


from decimal import Decimal 

ABSOLUTE_DIFFERENCE = Decimal(273.15)


def fahrenheit_to_celsius(degrees):
    """function will return celsius.

    Args:
        degrees(mixed): fahrenheit will be converted to celsi
        
    Returns:
        decimal: Returns value in Celsius
        
    Examples:
        >>> fahrenheit_to_celsius(212)
        Decimal ('100')
    """

    degrees = Decimal(degrees)
    return (degrees - 32) * 5 /9


def celsius_to_kelvin(degrees):
    """This function will convert Celsius  to Kelvin.

    Args:
        degrees(mixed): celsius will be converted to kelvin
        
    Returns:
        decimal: Returns value in Kelvin
        
    Examples:
        >>> celsius_to_kelvin(100)
        Decimal('373.1499999999999772626324557')
    """

    degrees = Decimal(degrees)
    return degrees + ABSOLUTE_DIFFERENCE


def fahrenheit_to_kelvin(degrees):
    """This function will convert Fahrenheit to Kelvin.

    Args:
        degrees(mixed): fahrenheit will be converted to kelvin
        
    Returns:
        decimal: Returns value in Kelvin
        
    Examples:
        >>> fahrenheit_to_kelvin(212)
        Decimal('373.1499999999999772626324557')
    """

    exm1 = fahrenheit_to_celsius(degrees)
    exm2 = celsius_to_kelvin(exm1)
    return exm2



    

