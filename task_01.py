#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is adocstring for assignment 4 task 1"""

import datetime

CURDATE = None

def get_current_date():
    """Created this function to display today's date.

    Args:
        None
        
    Return:
        date: current system time will be returned.
     
    Example:
        >>> print task_01.CURDATE
        None
        >>> task_01.get_current_date()
        datetime.date(2016, 9, 25)
    
    """
    
    return datetime.date.today()

if __name__ == '__main__':
    CURDATE = get_current_date()
    print CURDATE
