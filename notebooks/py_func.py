import numpy as np
from scipy import stats
from scipy.stats import f


# Define a function called "ftest_p_cdf" to determine if "list1" and "list2" are of equal variance
def ftest_p_cdf(list1, list2):
    
    # Calculate p_cdf for f-test (cumulative distribution function)
    p_cdf = f.cdf(np.var(list1) / np.var(list2), len(list1) - 1, len(list2) - 1)
    
    # If p-cdf is greater than alpha which is by default 0.05 ...
    if p_cdf > 0.05:
        # Accept that the two lists are not equal in variation and mark "equal_var" as "False"
        equal_var = False
    else:
        # On the other hand, the two lists are of equal variation and "equal var" is set to "True"
        equal_var = True
    # Return the status of "equal var" after calling this function
    return equal_var


# Define a function called "ttest" to determine if "list1" and "list2" are of statistical differences
def ttest(list1, list2, equal_var):
    
    # Calculate p_value for t-test
    (t_stat, p) = stats.ttest_ind(list1, list2, equal_var=equal_var)
    
    # If p is greater than alpha which is by default 0.05 ...
    if p > 0.05:
        # Accept that the two lists are not statistically different and set "diff" as "False"
        diff = False
    else:
        # On the other hand, the two lists are statistically different and "diff" is set to "True"
        diff = True
    # Return the status of "diff" after calling this function
    return diff




