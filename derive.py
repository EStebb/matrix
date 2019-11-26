# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 10:53:10 2018

@author: emst
"""

def derive(IOT):
    """ Derive the A matrix and Leontief inverse for a given n x m Input Output Table (IOT)"""
    """ Takes the IOT in the detailed format published by the Office For National Statistics,
    with 13 final demand columns, 7 skippable row headings, and 1 row total that can be ommitted.
    IOT should first be read into a DataFrame"""
    import pandas as pd
    import numpy as np
    from pandas import ExcelWriter

    # Import data and remove NaN
    Z = IOT.iloc[:-7, :-13]
    x = IOT.iloc[:-7, [-1]]
    x = np.array(x).T
    Z = np.nan_to_num(Z)
    x = np.nan_to_num(x)

    # Diagonalise the vector array of total output
    xdinv = np.diag(x[0])
    xdinv = np.matrix(xdinv)

    #Invert matrix
    xdinv = np.linalg.inv(xdinv)

    # Matrix multipication
    A = np.matmul(Z, xdinv)
    I = np.matrix(np.identity(len(A)))
    L = np.linalg.inv((I-A))

    # Export
    L = pd.DataFrame(L)
    Z = pd.DataFrame(Z)
    A = pd.DataFrame(A)
    x = pd.DataFrame(x)
    writer = ExcelWriter('Derived matrix.xlsx')
    L.to_excel(writer, 'L')
    Z.to_excel(writer, 'Z')
    A.to_excel(writer, 'A')
    x.to_excel(writer, 'x')
    writer.save()
