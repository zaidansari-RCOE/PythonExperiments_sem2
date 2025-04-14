'''
Title: Statistical Operations
Name: Md. Zaid Mashooque Ansari
Division: C
UIN: 241P057
Roll no: 51
'''

import numpy as np
from scipy import stats

def analyze_array(data):
    """Analyze an array of data and calculate basic statistics."""
    data = np.array(data)
   
    mean = np.mean(data)
    median = np.median(data)
    std_dev = np.std(data, ddof=1)  # Sample standard deviation
    variance = np.var(data, ddof=1)  # Sample variance
    correlation_matrix = np.corrcoef(data)  # Correlation coefficients
   
    print(f"Mean: {mean}")
    print(f"Median: {median}")
    print(f"Standard Deviation: {std_dev}")
    print(f"Variance: {variance}")
    print(f"Correlation Coefficients:\n{correlation_matrix}")
   
    return mean, median, std_dev, variance, correlation_matrix

# Example usage
data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
analyze_array(data)

"""
Sample Output:

Mean: 55.0
Median: 55.0
Standard Deviation: 31.622776601683793
Variance: 1000.0
Correlation Coefficients:
1.0
"""
