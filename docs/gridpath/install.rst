===================
Setting up GridPath
===================

GridPath source code
====================

GridPath’s source code is stored in a GitHub repository. You can download the latest GridPath release at https://github.com/blue-marble/gridpath/releases. We will be using GridPath v0.14.1 for this workshop.

Download the source code from https://github.com/blue-marble/gridpath/archive/refs/tags/v0.14.1.zip and extract the files to a directory.
Make sure to remember the directory path.
We’ll call it ``PATH\TO\GRIDPATH``.

From CMD navigate to this directory.

Install GridPath
================

Make sure your GridPath environment is activated. You need to see the environment name in parentheses before your current directory.

You can then install GridPath and its graphical user interface by navigating to the GridPath directory ``PATH\TO\GRIDPATH`` by running ``cd PATH\TO\GRIDPATH``.

E.g.

.. code::

    cd C:\Users\bluemarble\dev\gridpath-0.14.1\gridpath-0.14.1

Once you have navigated to `PATH\TO\GRIDPATH`, run the following to install GridPath:

.. code::

    pip install .[ui]

Testing GridPath installation
=============================

To test the GridPath and solver installation, navigate to the main GridPath folder in CMD and enter:

.. code::

    python -m unittest discover tests

The command should run without errors.
Errors that you could encounter are: ``solver not found``, in which case, check whether the folder path to your cbc solver in your system environment variables is correct.

Once the test runs successfully, run an example problem from the main GridPath folder or any of its sub-folders.
To run the scenario ``2horizons``, enter ``gridpath_run --scenario 2horizons --scenario_location LOCATION/OF/EXAMPLES/FOLDER``. No slashes before or after examples folder path.

UI
==

You can download the GridPath UI for Windows from here:

https://github.com/blue-marble/gridpath/releases/download/v0.14.1/GridPath_v0.14.1_UI_Win.exe

See these instructions for how to specify the Scenarios Directory, GridPath Database, GridPath Python Environment Directory, and Solver settings.

https://gridpath.readthedocs.io/en/latest/ui.html

Note that the UI has limited support at this point.
