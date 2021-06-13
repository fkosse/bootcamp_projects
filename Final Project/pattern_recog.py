$ pip install TA-Lib


import talib



# All the CDL functions are under the Pattern Recognition group

# O, H, L, C = Open, High, Low, Close
O = [ 167.07, 170.8, 178.9, 184.48, 179.1401, 183.56, 186.7, 187.52, 189.0, 193.96 ]
H = [ 167.45, 180.47, 185.83, 185.48, 184.96, 186.3, 189.68, 191.28, 194.5, 194.23 ]
L = [ 164.2, 169.08, 178.56, 177.11, 177.65, 180.5, 185.611, 186.43, 188.0, 188.37 ]
C = [ 166.26, 177.8701, 183.4, 181.039, 182.43, 185.3, 188.61, 190.86, 193.39, 192.99 ]



for cdl in talib.get_function_groups()['Pattern Recognition']:
    # get the function object
    cdl_func = talib.abstract.Function(cdl)

    # you can use the info property to get the name of the pattern
    print('Checking', cdl_func.info['display_name'], 
'pattern')

    # run the function as usual
    cdl_func(np.array(O), np.array(H), np.array(L), np.array(C))