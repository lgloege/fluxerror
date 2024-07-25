"""
Weiss 1974: Fractional Uncertainties
-----------------------------------
"""
from fluxuncertpy.solubility.weiss1974.derivative import (
    ko_wrt_temp,
    ko_wrt_salt
)

def ko_wrt_temp(temp_C, S, delta_T):
    """fractional uncertainty of K from temperature

    .. math::
        \\frac{\\partial K / \\partial T]}{\delta T}

    Args:
        temp_C (float): temperature in degrees C
        S (float): salinity in PSU
        delta_T (float): uncertainty in temperature in degrees C

    Returns:
        frac: fractional uncertainty in K from temperature
    """
    T = temp_C + 273.15
    d_ko_dT = ko_wrt_temp(T, S)
    return (d_ko_dT * delta_T)


def ko_wrt_salt(temp_C, delta_S):
    """fractional uncertainty of K from salinity

    .. math::
        \\frac{\\partial K / \\partial S}{\delta S}

    Args:
        temp_C (float): temperature in degrees C
        delta_S (float): uncertainty in salinity

    Returns:
        frac: fractional uncertainty in K from salinity
    """
    T = temp_C + 273.15
    d_ko_ds = ko_wrt_salt(T)
    return d_ko_ds * delta_S