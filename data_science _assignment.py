# import necessaary modules
import pandas as pd
import numpy as np
# define main function
def main():
# importing the data
    fish_data = pd.read_csv('gandhi_et_al_bouts.csv', skiprows = 4)
# generating bootstrap replicates of 1D data
    def bootstrap_replicate_1d(data, func):
        """Generate bootstrap replicate of 1D data."""
        bs_sample = np.random.choice(data, len(data))
        return func(bs_sample)
#This function draws bootstrap replicates from the data assigned to it
    def draw_bs_reps(data, func, size=1):
        """Draw bootstrap replicates."""

# Initialize array of replicates
        bs_replicates = np.empty(size)
# Generate replicates
        for i in range(size):
            bs_replicates[i] = bootstrap_replicate_1d(data,func)

        return bs_replicates
# generating lists of fish bout length for the two deifferent types of genotype fish
    bout_lengths_wt =  fish_data[fish_data.genotype =='wt'].bout_length
    bout_lengths_mut =  fish_data[fish_data.genotype =='mut'].bout_length
# computing the mean active bout length
    mean_wt = np.mean(bout_lengths_wt)
    mean_mut = np.mean(bout_lengths_mut)
#Draw Bootstrap replicates
    bs_reps_wt = draw_bs_reps(bout_lengths_wt, np.mean, size=10000)
    bs_reps_mut = draw_bs_reps(bout_lengths_mut, np.mean, size=10000)
# Compute 95% confidence intervals
    conf_int_wt = np.percentile(bs_reps_wt, [2.5, 97.5])
    conf_int_mut = np.percentile(bs_reps_mut, [2.5, 97.5])
# Print the results
    print("""
    wt:  mean = {0:.3f} min., conf. int. = [{1:.1f}, {2:.1f}] min.
    mut: mean = {3:.3f} min., conf. int. = [{4:.1f}, {5:.1f}] min.
    """.format(mean_wt, *conf_int_wt, mean_mut, *conf_int_mut))
main()
