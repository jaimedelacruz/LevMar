import LevMar as lm
import numpy as np
import matplotlib.pyplot as plt
from importlib import reload
reload(lm)


# User provided function that takes (par, user_data, get_J=True/False)
# Note that if the user wants to use auto_derivatives=True, then
# this function does not need to calculate J, so get_J becomes a dummy
# argument.

def getFX(par, x, get_J = False):
    syn = x*par[0] + np.exp(par[1]*x)
    if(get_J):
        J = np.zeros((par.size, x.size), dtype='float64')
        J[0] =  x
        J[1] =  np.exp(par[1]*x) * x
        
        return syn, J
    else:
        return syn


if __name__ == "__main__":

    # Create an X-array 
    x = (np.arange(101, dtype='float64') - 50)/50.0 * 3.0

    # We will have a model f(x) = x*p0 + exp(p1*x)
    # Let's assume that our real parameters are these:
    par = np.float64([2.0, -0.75])

    # Noise level, to be added to the "observed" data
    sig = 0.15
    y = getFX(par, x) + np.random.normal(loc=0.0, scale=sig, size=x.size)
    s = np.ones(x.size, dtype='float64')*sig # Estimate of the noise level
    
    # Create a list of pinfo with parameter limits and scale norms
    pinfo = [None]*2
    pinfo[0] = lm.Pinfo(scale=1.0, min = 0, max=5.0)
    pinfo[1] = lm.Pinfo(scale=1.0, min =-2, max=1.0)

    # Initial parameters of the fit
    pinit = np.float64([1.0, -0.2])

    # Call the fitting routine, it returns the final Chi2, fitted parameters, synthetic data and the Jacobian of the final model. Try using auto_derivatives, then getFX does not need to estimate them
    chi2, pp, syn, J = lm.LevMar(getFX, pinit, y, s, pinfo, x, Niter=20, auto_derivatives=False, init_lambda=10.0, verbose=True, chi2_thres=1.0, fx_thres=0.001, lmin=1.e-4, lmax=1.e4, lstep=10.0**0.5)

    print("Real parameters:")
    print(par)
    print("Fitted parameters:")
    print(pp)
    
    # Plot the result and the original data
    plt.close("all"); plt.ion()
    plt.plot(x,y,'k.',label='data')
    plt.plot(x,syn,color='orangered', label='fitted')
    plt.plot(x, getFX(pinit, x), label='Initial')
    plt.legend()
    plt.xlabel("x")
    plt.ylabel("y")
    plt.tight_layout()
    plt.show()
    
