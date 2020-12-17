import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
fish_data = pd.read_csv('gandhi_et_al_bouts.csv', skiprows = 4)
def bootstrap_replicate_1d(data, func):
    """Generate bootstrap replicate of 1D data."""
    bs_sample = np.random.choice(data, len(data))
    return func(bs_sample)
def draw_bs_reps(data, func, size=1):
    """Draw bootstrap replicates."""

    # Initialize array of replicates: bs_replicates
    bs_replicates = np.empty(size)

    # Generate replicates
    for i in range(size):
        bs_replicates[i] = bootstrap_replicate_1d(data,func)

    return bs_replicates

mean_wt = np.mean(bout_lengths_wt)
mean_mut = np.mean(bout_lengths_mut)

bs_reps_wt = draw_bs_reps(bout_lengths_wt, np.mean, size=10000)
bs_reps_mut = draw_bs_reps(bout_lengths_mut, np.mean, size=10000)
conf_int_wt = np.percentile(bs_reps_wt, [2.5, 97.5])
conf_int_mut = np.percentile(bs_reps_mut, [2.5, 97.5])

print("""
wt:  mean = {0:.3f} min., conf. int. = [{1:.1f}, {2:.1f}] min.
mut: mean = {3:.3f} min., conf. int. = [{4:.1f}, {5:.1f}] min.
""".format(mean_wt, *conf_int_wt, mean_mut, *conf_int_mut))
