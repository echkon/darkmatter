import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

"""
bayesian_inference.py
Performs Bayesian inference on a given phase distribution.
"""

def likelihood(phase, k):
    """Likelihood function P(k|phase)."""
    return (1 - k) * np.cos(phase/2) ** 2 + k * np.sin(phase/2) ** 2

def bayesian_update(phase, k, prior):
    """Compute posterior distribution P(phase|k) using Bayes' theorem."""
    P_k_given_phase = likelihood(phase, k)
    posterior = P_k_given_phase * prior
    posterior /= np.trapz(posterior, phase)
    return posterior

def stat_properties(f, x, true_phase):
    """Computes the statistical properties of a given distribution."""
    mean = x @ f/np.sum(f)
    bias = mean-true_phase
    var = (mean-x)**2 @ f/np.sum(f)
    std = np.sqrt(var)
    return mean, bias, var, std

def gaussian(x, mean, std):
    """Create gaussian distribution."""
    return np.exp(-0.5 * ((x - mean)/std)**2) / (std * np.sqrt(2*np.pi))

def main():
    # Variables
    true_phase = np.pi/2
    num_k_list = list(range(1, 501))
    mean_list = []
    std_list = []
    var_list = []

    for num_k in num_k_list:
        # Initialize prior distribution
        phase = np.linspace(-np.pi, np.pi, 500)
        prior = norm.cdf(phase, loc=0, scale=1)
        prior /= np.trapz(prior, phase)

        # Generate measurement data
        k_values = np.random.choice([0, 1], num_k, p=[likelihood(true_phase, 0), likelihood(true_phase, 1)])

        # Perform sequential Bayesian updates
        for k in k_values:
            posterior = bayesian_update(phase, k, prior)
            prior = posterior.copy()  # Update prior for next iteration
        
        # Statistic properties of the posterior distribution
        mean, var, std = stat_properties(posterior, phase, true_phase)
        mean_list.append(mean)
        var_list.append(var)
        std_list.append(std)
    
    # Posterior distribution (num_k = 200)
    mean = mean_list[-1]
    var = var_list[-1]
    std = std_list[-1]
    print(f"Posterior, num_k = {num_k}")
    print("Mean, var, std:", mean, var, std)

    # Gaussian distribution
    gaussian_dist = gaussian(phase, np.pi/2, 0.1)
    gmean, gvar, gstd = stat_properties(gaussian_dist, phase, true_phase)
    print("Gaussian")
    print("Mean, var, std:", gmean, gvar, gstd)

    # Plot var and std vs num_k
    plt.figure()
    plt.plot(num_k_list, bias_list, label="BIAS")
    plt.plot(num_k_list, var_list, label="VAR")
    plt.grid()
    plt.legend()
    plt.xlabel('Number of Measurements')
    plt.ylabel('Uncertainty')
    plt.yscale("log")
    plt.title('Variance and Standard Deviation')
    plt.savefig("_figures/bayesian_inference/bias_var.png", dpi=300)
    plt.savefig("_figures/bayesian_inference/bias_var.eps", format='eps')

    ## Plot posterior and gaussian distribution
    plt.figure()
    plt.plot(phase, posterior, alpha=0.5, label='Posterior Distribution')
    plt.plot(phase, gaussian_dist, alpha=0.5, label=f'Gaussian Distribution')
    plt.axvline(true_phase, color='red', linestyle='--', label='True Phase')
    plt.grid()
    plt.xlabel('Phase')
    plt.ylabel('Probability Density')
    plt.title(f"Posterior Distribution, num_k = {num_k}")
    plt.legend()
    plt.savefig("_figures/bayesian_inference/posterior.png", dpi=300)
    plt.savefig("_figures/bayesian_inference/posterior.eps", format='eps')

if __name__ == "__main__":
    main()