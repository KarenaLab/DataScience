# T Test Comparison [P364] ---------------------------------------------

# Versions
# 01 - Aug 22rd, 2023 - Starter
# 02 -


# Insights, improvements and bugfix
#


# Libraries
import numpy as np
import pandas as pd

from scipy.stats import shapiro, ttest_ind, wilcoxon


# ----------------------------------------------------------------------

def t_test_comparison(data_a, data_b, nan_policy="omit", trigger=0.05,
                      verbose=True):
    """
    .

    """
    # Data preparation
    data_a = np.array(data_a)
    data_b = np.array(data_b)

    # Testing for normality (parametric)
    _, wk_pvalue_a = shapiro_wilk(data_a, verbose=verbose)
    _, wk_pvalue_b = shapiro_wilk(data_b, verbose=verbose)

    # Comparison
    # T-Test for parametric values
    if(wk_pvalue_a > trigger and wk_pvalue_b > trigger):
        stat, pvalue = t_test(data_a, data_b, verbose=verbose)

    # Wilcoxon Signed for non-parametric values
    else:
        stat, pvalue = wilcoxon_signed_test(data_a, data_b, verbose=verbose)


    if(verbose == True):
        print("")


    return stat, pvalue
        
   
def shapiro_wilk(data, verbose=True):
    """
    Performs Shapiro-Wilk normality test.

    """
    # Data preparation
    data = np.array(data)    

    # Shapiro-Wilk Test
    stat, pvalue = shapiro(data)

    if(verbose == True):
        print(f" > Shapiro-Wilk test p-value: {pvalue:.4f}, ({pvalue:.3%})")


    return stat, pvalue


def t_test(data_a, data_b, nan_policy="omit", verbose=True):
    """
    Performs the T-Test comparison for two means of independent samples.
    Used for comparison of parametric values.
    
    """
    # Data preparation
    data_a = np.array(data_a)
    data_b = np.array(data_b)

    # T-Test comparison
    stat, pvalue = ttest_ind(data_a, data_b, nan_policy=nan_policy)

    if(verbose == True):
        print(f" > T-test p-value: {pvalue:.4f}, ({pvalue:.3%})")


    return stat, pvalue


def wilcoxon_signed_test(data_a, data_b, nan_policy="omit", verbose=True):
    """
    Performs the Wilcoxon signed-rank test, used for comparison of
    non-parametric values.

    """
    # Data preparation
    data_a = np.array(data_a)
    data_b = np.array(data_b)

    # T-Test comparison
    stat, pvalue = wilcoxon(data_a, data_b, nan_policy=nan_policy)

    if(verbose == True):
        print(f" > Wilcoxon signed-rank test p-value: {pvalue:.4f}, ({pvalue:.3%})")


    return stat, pvalue


# end

