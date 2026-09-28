import math


def my_pi(target_error):
    """
    Implementation of Gauss–Legendre algorithm to approximate PI from https://en.wikipedia.org/wiki/Gauss%E2%80%93Legendre_algorithm

    :param target_error: Desired error for PI estimation
    :return: Approximation of PI to specified error bound
    """

    ### YOUR CODE HERE ###
    a0 = 1
    b0 = 1 / math.sqrt(2)
    t0 = 1 / 4 
    p0 = 1

    for i in range(1, 10):
        a = ((a0 + b0) / 2 )
        b = math.sqrt(a0*b0)
        t = t0-p0*(a0-a)**2
        p = 2*p0

        a0 = a 
        b0 = b
        t0 = t
        p0 = p

    pi_estimate = ((a0 + b0)**2) / (4*(t0))

    return(pi_estimate)




desired_error = 1E-10

approximation = my_pi(desired_error)

print("Solution returned PI=", approximation)

error = abs(math.pi - approximation)

if error < abs(desired_error):
    print("Solution is acceptable")
else:
    print("Solution is not acceptable")
