# $Id$
# Copyright (c) 2009 Oliver Beckstein <orbeckst@gmail.com>
# Released under the GNU Public License 3 (or higher, your choice)
# See the file COPYING for details.
"""
:mod:`analysis.plugins` -- Plugin Modules
=========================================

Mixin classes for :class:`gromacs.analysis.core.Simulation` that
provide code to analyze trajectory data.

New analysis plugins should follow the API sketched out in
:mod:`gromacs.analysis.core`; see an example for use there.



List of plugins
---------------

Right now the number of plugins is limited. Feel free to contribute your own by
sending it to the `package author`_. You will be acknowledged in the list below.

.. _`package author`: oliver.beckstein@bioch.ox.ac.uk

====================  =======================  ===============================
plugin                author                   description
====================  =======================  ===============================
CysAccessibility      Oliver Beckstein [#OB]_  estimate accessibility of Cys
                                               residues by water
Distances             Oliver Beckstein [#OB]_  time series of distances
====================  =======================  ===============================


.. rubric:: Footnotes
.. [#OB] oliver.beckstein@bioch.ox.ac.uk


Developer notes
---------------

.. autodata:: __plugins__

"""
__docformat__ = "restructuredtext en"

#: all available plugin names are listed; because this is used to
#: automatically set up imports, each plugin class must have the same
#: name as the module.
__plugins__ = ['CysAccessibility', 'Distances']
__all__ = []
__all__.extend(__plugins__)


# 1. Insert all plugin classes into the current module.
# 2. The plugin can/should mask the module of the same name to reduce clutter.
_mod_dict = dict([(m, __import__(m, globals(), locals(), fromlist=[m])) for m in __plugins__])


globals().update(_mod_dict)
#del _mod_dict


