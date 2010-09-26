# numkit --- some numerical functions for analysis of molecular simulations
# Copyright (c) 2010 Oliver Beckstein <orbeckst@gmail.com>
# Released under the "Modified BSD Licence" (see COPYING).
"""
:mod:`numkit` --- Helper functions for scipy and friends
========================================================

:Author:  Oliver Beckstein <orbeckst@gmail.com>
:Year:    2010
:Licence: Modified BSD

A collection of functions and classes that support the analysis of molecular
dynamics trajectories (i.e. mostly time series). Because these functions could
conceivably be useful in other contexts as well they were moved into a separate
package with a very permissive licence.

Please note that these functions are provided "as is" and no guarantee is given
that they are accurate or free from error. Bug reports and test cases are very
welcome. Please submit them through the Github `Issue Tracker`_.

.. _Issue Tracker: http://github.com/orbeckst/GromacsWrapper/issues
"""

__all__ = ['fitting', 'timeseries', 'integration', 'observables']

class LowAccuracyWarning(Warning):
    """Warns that results may possibly have low accuracy."""