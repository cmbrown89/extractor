#!/usr/bin/env python


"""Extractor algorithm implementation file
"""

def calculate(pxarray):
    """Algorithm
    Args:
        pxarray(numpy array): RGB pixel data at the plot level
    Returns:
    """

    # Extract the mean red, green, and blue values from the image bands
    r = pxarray[:,:,0].mean()
    g = pxarray[:,:,1].mean()
    b = pxarray[:,:,2].mean()   
    
    exg = 2*g-(r+b)

    return(exg)