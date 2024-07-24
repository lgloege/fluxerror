def fractional_uncertainty(value, delta):
    """Fractional uncertainty calculation:
    fractional_uncertainty = delta / value

    Parameters
    ----------
    value : float
        data point
    delta : float
        uncertainty in the value

    Returns
    -------
    fractional uncertainty : float
        fractional uncertainty calculated as delta / value


    Examples
    --------
    frac_unc = fractional_uncertainty(10, 2) # returns 0.2
    """

    assert value != 0, f"!! value can not be 0"
    return delta / value

def fractional_uncertainty_squared(delta, value):
    """Fractional uncertainty squared calculation:
    frac_uncert_squared = (delta / value)**2

    Parameters
    ----------
    value : float
        data point
    delta : float
        uncertainty in the value

    Returns
    -------
    fractional uncertainty_squared : float
        squared fractional uncertainty calculated as (delta / value)**2


    Examples
    --------
    frac_unc_squared = fractional_uncertainty_squared(10, 2) # returns 0.04
    """
    assert value != 0, f"!! value can not be 0"
    return fractional_uncertainty(delta, value) * fractional_uncertainty(delta, value)


def frac_pco2ocn(pco2, delta_pco2):
    return delta_pco2 / pco2

