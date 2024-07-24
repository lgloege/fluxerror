"""
Solubility
===========================

Weiss 1974 Derivatives
------------------------------------------

"""
from fluxuncertpy.solubility.weiss1974._utils import weiss1974_f2

def _weiss1974_f1_wrt_temp(temp_C):
    """derivative of Weiss (1974) f_1 w.r.t temperature

    .. math::
        \\frac{\\partial f_1}{\\partial T} = \\frac{a_3}{T} - (a_2 * 100 * T^{-2})

    Args:
        temp_C (float): temperature in degrees C

    Returns:
        df1_dT: derivative of f_1 w.r.t temperature
    """
    T = temp_C + 273.15

    a2 = +90.5069
    a3 = +22.2940
    return -a2 * 100 * (T ** (-2)) + a3 * (1/T)

def _weiss1974_f2_wrt_temp(temp_C):
    """derivative of Weiss (1974) f_2 w.r.t temperature

    .. math::
        \\frac{\\partial f_2}{\\partial T} = \\frac{b_2}{100} + \\bigg( \\frac{2 * b_3 * T}{100^2}\\bigg )

    Args:
        temp_C (float): temperature in degrees C

    Returns:
        df2_dT: derivative of f_2 w.r.t temperature
    """
    T = temp_C + 273.15

    b1 = +0.027766
    b2 = -0.025888
    b3 = +0.0050578
    T100 = T / 100
    return (b2 /100) + ( (2 * b3 * T) / (100 ** 2) )

def ko_wrt_temp(temp_C, S):
    """Derivative of Weiss (1974) solubility parameterization
    with respect to temperature.

    .. math::
        \\frac{\\partial K}{\\partial T} = \\frac{\\partial f_1(T)}{\\partial T} + S * \\frac{\\partial f_2(T)}{\\partial T}

        = \\frac{a_3}{T} - (a_2 * 100 * T^{-2}) + S * \\bigg [ \\frac{b_2}{100} + \\bigg( \\frac{2 * b_3 * T}{100^2}\\bigg ) \\bigg ]

    Args:
        temp_C (float): temperature in degrees Celsius
        S (float): salinity in practical salinity units

    Returns:
        dK_dT: derivative of solubility w.r.t temperature at a given temperature
    """
    T = temp_C + 273.15

    a2 = +90.5069
    a3 = +22.2940
    b2 = -0.025888
    b3 = +0.0050578

    df1_dt = -a2 * 100 * (T ** (-2)) + a3 * (1/T) #weiss1974_f1_wrt_temp(T)
    df2_dt = (b2 /100) + ( (2 * b3 * T) / (100 ** 2) ) #weiss1974_f2_wrt_temp(T)

    return df1_dt + ( S * df2_dt )

def ko_wrt_salt(temp_C):
    """deriviative of Weiss (1974) with respect to salinity

    .. math::
        \\frac{\\partial K}{\\partial S} = b_1 + b_2 * \\bigg ( \\frac{T}{100} \\bigg)  + b_3 * \\bigg ( \\frac{T}{100} \\bigg)^2

    Constants:

    * :math:`b_1 = +0.027766`
    * :math:`b_2 = -0.025888`
    * :math:`b_3 = +0.0050578`

    Args:
        temp_C (float): temperature in degrees C

    Returns:
        dK_dS: deriviative of K with respect to salinity
    """
    T = temp_C + 273.15
    d_ko_d_salt = weiss1974_f2(T)
    return d_ko_d_salt
