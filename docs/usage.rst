Quickstart Guide
====================================================

Installation
------------

.. code-block:: bash

   # for latest release
   pip install fluxuncertpy

   # for bleeding-edge up-to-date commit
   pip install -e git+https://github.com/lgloege/fluxuncertpy.git


Calculating fractional uncertainty
----------------------------------------------------
To calculate fractional uncertainty from the Weiss (1974)
solubility parameterization, you can use the following

.. code-block:: python

   from fluxuncertpy import solubility as sol

   # fractional uncertainty in Weiss (1974)
   frac_sol = sol.weiss1974.frac.ko_wrt_temp(temp_C =32, delta_S = 0.1)
