# EDA [P203] ------------------------------------------------------------

# Versions
# 01 - Apr 22nd, 2022 - Launch
# 02 - Jun 20th, 2023 - Standards and using print_metrics


# Insights
# Choose what type of information to return


# Libraries
import numpy as np

from scipy.stats import kurtosis
from scipy.stats import shapiro


# ----------------------------------------------------------------------

def EDA(data, decimals=5, select=True):
    """
    Performs EDA (Exploratory Data Analysis).


    """
    # Data preparation
    data = np.array(data)

    data_count = data.size
    data_nan = np.isnan(data).sum()
    data_valid = data_count - data_nan


    # Remove nans to perform all others metrics
    data = data[~np.isnan(data)]

    # Simple EDA 
    data_unique = np.unique(data)
    data_nunique = data_unique.size
    
    data_mean = np.mean(data)
    data_stddev = np.std(data)

    data_min = np.min(data)
    data_max = np.max(data)
    data_range = data_max - data_min

    data_q25 = np.quantile(data, q=0.25)
    data_median = np.quantile(data, q=0.50)
    data_q75 = np.quantile(data, q=0.75)
    data_iqr = data_q75 - data_q25


    # Advanced EDA
    data_kurtosis = kurtosis(data)
    wk_stat, wk_pvalue = shapiro(data)

    if(wk_pvalue < 0.05):
        status = "parametric"

    else:
        status = "non_parametric"


    #if(wk_status == "parametric"):
        # Standard Wasserstein Distance

    # Bins Numbers
    bins_min, bins_min_param = float("inf"), ""
    bins_max, bins_max_param = 0, ""

    bins_strategy = ["fd", "doane", "scott", "stone", "rice", "sturges", "sqrt"]
    for strategy in bins_strategy:
        bins = np.histogram_bin_edges(data, bins=strategy).size

        if(bins > bins_max):
            bins_max = bins
            bins_max_param = strategy

        if(bins < bins_min):
            bins_min = bins
            bins_min_param = strategy


    metrics_dict = {"count": data_count, "nan": data_nan, "valid": data_valid, "uniques": data_unique,
                    "mean": data_mean, "stddev": data_stddev,
                    "minimum": data_min, "maximum": data_max, "range": data_range,
                    "q 25%": data_q25, "median": data_median, "q 75%": data_q75, "IQR": data_iqr,
                    "kurtosis": data_kurtosis, "wk_pvalue": wk_pvalue, "status": status,
                    "bins minimum": bins_min, "bins maximum": bins_max}


    if(select == True):
        pass
    
    
    return metrics_dict


