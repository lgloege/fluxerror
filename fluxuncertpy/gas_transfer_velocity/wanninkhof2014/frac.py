"""
Gas Transfer Velocity
===========================

Wanninkhof 2014 Fractional Uncertainties
------------------------------------------

"""
from fluxuncertpy.gas_transfer_velocity.wanninkhof2014._utils import schmidt_number as _schmidt_number
from fluxuncertpy.gas_transfer_velocity.wanninkhof2014.derivative import schmidt_number_wrt_temp

def kw_umean(u_mean: float, u_std:float, delta_umean: float) -> float:
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

def kw_ustd(u_mean: float, u_std: float, delta_ustd: float) -> float:
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

def kw_sc(temp_C: float, delta_T: float) -> float:
    """fractional uncertainty in kw wrt to schmidt number

    Args:
        temp_C (float): temperature in degrees C
        delta_T (float): uncertainty in temperature in degrees C

    Returns:
        float: fractional uncertainty in kw wrt to Sc
    """
    Sc = _schmidt_number(temp_C)
    dSc_dT = schmidt_number_wrt_temp(temp_C)
    delta_Sc = dSc_dT * delta_T
    return (0.5 * delta_Sc) / Sc