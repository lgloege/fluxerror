
"""
Delta pCO2
===========================

Fractional Uncertainties
------------------------------------------

"""

def pco2ocn(pco2, delta_pco2):
    """fractional uncertainty in pCO2

    .. math::
        \\frac{pCO_2}{\\delta pCO_2}

    Args:
        pco2 (float): ocean partial pressure of CO2
        delta_pco2 (float): uncertainty in pCO2

    Returns:
        frac_pco2: fractional uncertainty in pCO2
    """
    return delta_pco2 / pco2