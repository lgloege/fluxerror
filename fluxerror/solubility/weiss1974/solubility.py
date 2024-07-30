"""
Solubility
--------------------


"""

from math import log

def weiss1974_f1(temp_C):
    """function 1 of Weiss (1974) parameterization

    .. math::

        f_1(T) = a_1 + a_2 \\cdot \\bigg( \\frac{100}{T} \\bigg ) + a_3 \\cdot \\log \\bigg ( \\frac{T}{100} \\bigg)

    Constants:

    * :math:`a_1 = -58.0931`
    * :math:`a_2 = +90.5069`
    * :math:`a_3 = +22.2940`

    Args:
        temp_C (float): temperature in degrees C

    Returns:
        f1 (float): function 1 of parameterization
    """
    T = temp_C + 273.15

    a1 = -58.0931
    a2 = +90.5069
    a3 = +22.2940
    T100 = T / 100
    return a1 + a2 * (100/T) + a3 * log(T100)

def weiss1974_f2(temp_C):
    """function 2 of Weiss (1974) parameterization

    .. math::

        f_2(T) = b_1 + b_2 \\cdot \\bigg ( \\frac{T}{100} \\bigg)  + b_3 \\cdot \\bigg ( \\frac{T}{100} \\bigg)^2

    Constants:

    * :math:`b_1 = +0.027766`
    * :math:`b_2 = -0.025888`
    * :math:`b_3 = +0.0050578`

    Args:
        temp_C (float): temperature in degrees C

    Returns:
        f2 (float): function 2 of parameterization
    """
    T = temp_C + 273.15

    b1 = +0.027766
    b2 = -0.025888
    b3 = +0.0050578
    T100 = T / 100
    return b1 + b2 * T100 + b3 * T100 ** 2

def weiss1974(temp_C, S):
    """Weiss (1974) solubility parameterization

    .. math::

        K = f_1(T) + S \\cdot f_2(T)

    where

    .. math::

        f_1(T) = a_1 + a_2 \\cdot \\bigg( \\frac{100}{T} \\bigg ) + a_3 \\cdot \\log \\bigg ( \\frac{T}{100} \\bigg)

        f_2(T) = b_1 + b_2 \\cdot \\bigg ( \\frac{T}{100} \\bigg) + b_3 \\cdot \\bigg ( \\frac{T}{100} \\bigg)^2


    Constants:

    * :math:`a_1 = -58.0931`
    * :math:`a_2 = +90.5069`
    * :math:`a_3 = +22.2940`
    * :math:`b_1 = +0.027766`
    * :math:`b_2 = -0.025888`
    * :math:`b_3 = +0.0050578`

    Args:
        temp_C (float): temperature in degrees C
        S (float): salinity if practical salinity units

    Returns:
        K: solubility using Weiss (1974) parameterization
    """
    T = temp_C + 273.15
    ko = weiss1974_f1(T) + ( S * weiss1974_f2(T) )
    return ko

def d_weiss1974_f1_wrt_temp(temp_C):
    """derivative of Weiss (1974) f_1 w.r.t temperature

    .. math::

        \\frac{\\partial f_1}{\\partial T} = \\frac{a_3}{T} - (a_2 \\cdot 100 \\cdot T^{-2})

    Args:
        temp_C (float): temperature in degrees C

    Returns:
        df1_dT: derivative of f_1 w.r.t temperature
    """
    T = temp_C + 273.15

    a2 = +90.5069
    a3 = +22.2940
    return -a2 * 100 * (T ** (-2)) + a3 * (1/T)

def d_weiss1974_f2_wrt_temp(temp_C):
    """derivative of Weiss (1974) f_2 w.r.t temperature

    .. math::

        \\frac{\\partial f_2}{\\partial T} = \\frac{b_2}{100} + \\bigg( \\frac{2 \\cdot b_3 \\cdot T}{100^2}\\bigg )

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

def d_weiss1974_wrt_temp(temp_C, S):
    """Derivative of Weiss (1974) solubility parameterization
    with respect to temperature.

    .. math::

        \\frac{\\partial K}{\\partial T} = \\frac{\\partial f_1(T)}{\\partial T} + S \\cdot \\frac{\\partial f_2(T)}{\\partial T}

        = \\frac{a_3}{T} - (a_2 \\cdot 100 * T^{-2}) + S \\cdot \\bigg [ \\frac{b_2}{100} + \\bigg( \\frac{2 \\cdot b_3 \\cdot T}{100^2}\\bigg ) \\bigg ]


    Args:
        temp_C (float): temperature in degrees Celsius
        S (float): salinity in practical salinity units

    Returns:
        dK_dT: derivative of solubility w.r.t temperature at a given temperature
    """
    T = temp_C + 273.15

    df1_dt = d_weiss1974_f1_wrt_temp(T)
    df2_dt = d_weiss1974_f2_wrt_temp(T)

    return df1_dt + ( S * df2_dt )

def d_weiss1974_wrt_salinity(temp_C):
    """deriviative of Weiss (1974) with respect to salinity

    .. math::

        \\frac{\\partial K}{\\partial S} = b_1 + b_2 \\cdot \\bigg ( \\frac{T}{100} \\bigg)  + b_3 \\cdot \\bigg ( \\frac{T}{100} \\bigg)^2

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

def frac_ko_temp(temp_C, S, delta_T):
    """fractional uncertainty of K from temperature

    .. math::

        \\frac{\\partial K / \\partial T]}{\\delta T}

    Args:
        temp_C (float): temperature in degrees C
        S (float): salinity in PSU
        delta_T (float): uncertainty in temperature in degrees C

    Returns:
        frac: fractional uncertainty in K from temperature
    """
    T = temp_C + 273.15
    d_ko_dT = d_weiss1974_wrt_temp(T, S)
    return (d_ko_dT * delta_T)

def frac_ko_salt(temp_C, delta_S):
    """fractional uncertainty of K from salinity

    .. math::

        \\frac{\\partial K / \\partial S}{\\delta S}

    Args:
        temp_C (float): temperature in degrees C
        delta_S (float): uncertainty in salinity

    Returns:
        frac: fractional uncertainty in K from salinity
    """
    T = temp_C + 273.15
    d_ko_ds = d_weiss1974_wrt_salinity(T)
    return d_ko_ds * delta_S