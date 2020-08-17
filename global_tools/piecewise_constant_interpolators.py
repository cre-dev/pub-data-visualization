

import numpy as np
import numbers
import pandas as pd

def piecewise_constant_interpolators(x,
                                     y,
                                     smoother = None,
                                     ):
    #
    X, Y = levels_to_points(x, y)
    
    # Simplify X and Y
    if smoother == 'basic':
        X = np.array([X[0],
                      *[e
                        for ii in range(int(X[1:-1].shape[0]/2))
                        for e in [X[2*ii + 1] - min(pd.Timedelta(hours = 6),
                                                    (X[2*ii + 1] - X[2*ii])/4,
                                                    (X[2*ii + 3] - X[2*ii + 2])/4,
                                                    ),
                                  X[2*ii + 2] + min(pd.Timedelta(hours = 6),
                                                    (X[2*ii + 1] - X[2*ii])/4,
                                                    (X[2*ii + 3] - X[2*ii + 2])/4,
                                                    ),
                                  ]
                        ],
                      X[-1],
                      ])
    else:
        X, Y = remove_redundant_interpolators(X, Y)

    return X, Y



def levels_to_points(x, y):
    Y = [e
         for e in y[:-1]
         for ii in range(2)
         ]
    #    
    for ee in Y:
        assert isinstance(ee, numbers.Number), '{0}\n{1}'.format(type(ee), ee)
    #
    X = [d 
         for d in x
         for ii in range(2)
         ][1:-1]
        
    X = np.array(X)
    Y = np.array(Y)
    
    return X, Y



def remove_redundant_interpolators(X, Y):
    cond_plot = np.array([(   ii in {0, len(X) - 1}
                           or Y[ii-1] != Y[ii]
                           or Y[ii+1] != Y[ii]
                           )
                          for ii in range(len(X))
                          ])
    X = X[cond_plot]
    Y = Y[cond_plot]
    return X, Y    
     
