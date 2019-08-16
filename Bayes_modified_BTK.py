#!/usr/bin/env python
"""
An example of how to use bilby to perform paramater estimation for
non-gravitational wave data. In this case, fitting a linear function to
data with background Gaussian noise

"""
from __future__ import division
import bilby
import numpy as np
import matplotlib.pyplot as plt
from modules.Simpson_BTK import BTK_Diff
import pandas as pd

# A few simple setup steps
label = 'Bayes_Modified_BTK'
outdir = 'outdir'
bilby.utils.check_directory_exists_and_if_not_mkdir(outdir)

# Rename .cvs file's columns
def arrange_dataframe(df):
    df.columns = ['Vdc', 'G/GN']
    return df

# First, we define our "signal model", in this case a simple linear function
def model(V,Delta, Gama, Z, P):
    return BTK_Diff(V,T,Delta, Gama, Z, P)

# Get file name and temperature 
filename = input("Please input data file name!\n")
global T 
T = float(input("Please input sample temperature!\n"))

# Inject standard Gaussian noise
sigma = 1

# Now we define the injection parameters which we make simulated data with
injection_parameters = dict(Delta=1.3, Gama=0.5, Z=1, P=0,)

# Read file and extract data
filename = 'Datas/' + filename
df2 = pd.read_csv(filename)
df2 = arrange_dataframe(df2)
V = df2['Vdc'].values
G_experiment = df2['G/GN'].values 
data = G_experiment

# We quickly plot the data to check it looks sensible
fig, ax = plt.subplots()
ax.plot(V, data, 'o', label='data')
ax.plot(V, BTK_Diff(V,T, **injection_parameters), '--r', label='signal')
ax.set_xlabel('Voltage')
ax.set_ylabel('G')
ax.legend()
fig.savefig('{}/{}_data.png'.format(outdir, label))

# Now lets instantiate a version of our GaussianLikelihood, giving it
# the time, data and signal model
likelihood = bilby.likelihood.GaussianLikelihood(V, data, model, sigma)

# From hereon, the syntax is exactly equivalent to other bilby examples
# We make a prior
priors = dict()
priors['Delta'] = bilby.core.prior.Uniform(0.2, 5, 'Delta')
priors['Gama'] = bilby.core.prior.Uniform(0, 6, 'Gama')
priors['Z'] = bilby.core.prior.Uniform(0, 10, 'Z')
priors['P'] = bilby.core.prior.Uniform(0, 1, 'P')


# And run sampler
result = bilby.run_sampler(
    likelihood=likelihood, priors=priors, sampler='dynesty', nlive=500,
    sample='unif', injection_parameters=injection_parameters, outdir=outdir,
    label=label)
result.plot_corner()
