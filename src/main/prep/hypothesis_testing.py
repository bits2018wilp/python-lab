
from scipy.stats import ttest_1samp
import numpy as np
from statsmodels.stats import weightstats as stests

pop_mean = 1500
pop_std_div = 100

sample_size = 9
sample_mean = 1600
sample_std_div = 1600

sig_level = .01

standard_error = pop_std_div / np.sqrt(sample_size)

z_score = (sample_mean - pop_mean)/standard_error

