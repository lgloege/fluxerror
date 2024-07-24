"""
Gas Transfer Velocity
--------------------


"""

from numpy import nanmedian

def schmidt_number(temp_C):
    """Calculates the Schmidt number as defined by Jahne et al. (1987) and listed
    in Wanninkhof (2014) Table 1.

    .. math::
        Sc = a + b * T + c * T^2 + d * T^3 + e * T^4

    constants:

    * :math:`a = +2116.8`
    * :math:`b = -136.25`
    * :math:`c = +4.7353`
    * :math:`d = -0.092307`
    * :math:`e = +0.0007555`

    Args:
        temp_C (array): temperature in degrees C

    Returns:
        array: Schmidt number (dimensionless)

    Examples:
        >>> schmidt_number(20)  # from Wanninkhof (2014)
        668.344

    References:
        Jähne, B., Heinz, G., & Dietrich, W. (1987). Measurement of the
        diffusion coefficients of sparingly soluble gases in water. Journal
        of Geophysical Research: Oceans, 92(C10), 10767–10776.
        https://doi.org/10.1029/JC092iC10p10767
    """
    if nanmedian(temp_C) > 270:
        raise ValueError("temperature is not in degC")

    T = temp_C

    a = +2116.8
    b = -136.25
    c = +4.7353
    d = -0.092307
    e = +0.0007555

    Sc = a + b * T + c * T ** 2 + d * T ** 3 + e * T ** 4

    return Sc

def d_schmidt_number_wrt_temp(temp_C):
    """Calculates the derivative of the Schmidt number
    with respect to (wrt) temperature

    .. math::
        B + 2*C*T + 3*D*T^2 + 4*E*T^3

    Args:
        temp_C (array): temperature in degrees C

    Returns:
        array: derivative of Schmidt number wrt temperature, dSc/dT, (1/degC)

    Examples:
        >>> schmidt_number(20)  # from Wanninkhof (2014)
        668.344

    See Also:
        schmidt_number()
    """
    if nanmedian(temp_C) > 270:
        raise ValueError("temperature is not in degC")

    T = temp_C

    A = 2_116.8
    B = -136.25
    C = 4.7353
    D = -0.092307
    E = 0.000755
    return B + 2*C*temp_C + 3*D*(temp_C**2) + 4*E*(temp_C**3)

def d_wann14_wrt_umean(temp_C, u_mean, a=0.251):
    """deriviative of kw wrt to mean wind speed

    .. math::
        2 * a * U_{mean} * \\bigg(\\frac{Sc}{660}\\bigg)^{0.5}

    Args:
        temp_C (float): temperature in degrees C
        u_mean (float): mean wind speed in m/s
        a (float, optional): constant. Defaults to 0.251.

    Returns:
        float: derivative of kw wrt to mean wind speed
    """
    Sc = schmidt_number(temp_C)
    return a * (2 * u_mean) * (Sc / 660)**(0.5)

def d_wann14_wrt_ustd(temp_C: float, u_std: float, a: float=0.251) -> float:
    """deriviative of kw wrt to standard deviation of wind speed

    .. math::
        2 * a * U_{std} * \\bigg(\\frac{Sc}{660}\\bigg)^{0.5}

    Args:
        temp_C (float): temperature in degrees C
        u_std (float): standard deviation of wind speed in m/s
        a (float, optional): constant. Defaults to 0.251.

    Returns:
        float: derivative of kw wrt to standard deviation of wind speed
    """
    Sc = schmidt_number(temp_C)
    return a * (2 * u_std) * (Sc / 660)**(0.5)

def frac_kw_umean(u_mean: float, u_std:float, delta_umean: float) -> float:
    """fractional uncertainy kw wrt to mean wind speed

    Args:
        u_mean (float): mean wind speed m/s
        u_std (float): standard deviation of wind speed m/s
        delta_umean (float): uncertainty in mean wind speed m/s

    Returns:
        float: fractional uncertainty in kw wrt to mean wind speed
    """
    numerator = 2 * u_mean * delta_umean
    denominator = (u_mean*u_mean) + (u_std*u_std)
    return (numerator / denominator )

def frac_kw_ustd(u_mean: float, u_std: float, delta_ustd: float) -> float:
    """fraction uncertainty in kw wrt to std of wind speed

    Args:
        u_mean (float): mean wind speed in m/s
        u_std (float): standard deviatino of wind speed m/s
        delta_ustd (float): uncertainty in standard deviation of wind speed m/s

    Returns:
        float: fractional uncerttainty kw wrt to U std
    """
    numerator = 2 * u_std * delta_ustd
    denominator = u_mean*u_mean + u_std*u_std
    return (numerator / denominator )

def frac_kw_sc(temp_C: float, delta_T: float) -> float:
    """fractional uncertainty in kw wrt to schmidt number

    Args:
        temp_C (float): temperature in degrees C
        delta_T (float): uncertainty in temperature in degrees C

    Returns:
        float: fractional uncertainty in kw wrt to Sc
    """
    Sc = schmidt_number(temp_C)
    dSc_dT = d_schmidt_number_wrt_temp(temp_C)
    delta_Sc = dSc_dT * delta_T
    return (0.5 * delta_Sc) / Sc