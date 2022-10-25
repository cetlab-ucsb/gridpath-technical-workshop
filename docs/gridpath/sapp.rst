=================================
Running SAPP models and scenarios
=================================

In this section, we will be running some (simplified) scenarios of the SAPP model.
You can download the input data for the SAPP here:
https://www.dropbox.com/sh/yi3776wy977sgve/AAD295bLVg_e02ZktJusgXCsa?dl=0

You can extract the zip file and place the input CSVs anywhere, as long as you properly point to the files when porting the data and assigning scenarios.
For this workshop, we recommend putting the input CSVs folder in the ``db`` subdirectory in the GridPath root directory.

Using Jupyter/python notebooks
==============================

If using Jupyter notebooks for this portion,
access the notebooks located in the ``notebooks`` subfolder of the workshop materials (``PATH\TO\WORKSHOP\notebooks``)
and follow along with the workshop instructors.

Using command line
==================

Creating a database
###################

Navigate to ``PATH\TO\GRIDPATH`` in your CMD by entering:

.. code::

    cd PATH\TO\GRIDPATH

From there, navigate to the ``db`` subdirectory by typing:

.. code::

    cd db

Create an empty database:

.. code::

    python create_database.py --database sapp.db

Adding data and scenarios to database
#####################################

Port the data in the ``csvs_sapp`` folder and the empty database that you just created (``sapp.db``):

.. code::

    python utilities/port_csvs_to_db.py --database sapp.db --csv_location csvs_sapp_GPv0.14.1_workshop_102022

(This might take a while due to the large number of files needed to be ported.)

In the ``csvs_sapp`` folder, we have provided some already prepared scenarios in the ``scenarios_workshop.csv`` file.
Add the scenarios to ``sapp.db`` by running:

.. code::

    python utilities/scenario.py --database sapp.db --csv_path csvs_sapp_GPv0.14.1_workshop_102022/scenarios_demo.csv

Running base scenario
#####################

Now we can run the scenarios using the data in the database.

Navigate to the ``gridpath`` folder by entering:

.. code::

    cd ../gridpath

We're going to start off with a simple base model for Namibia.
To run the ``namibia_base`` scenario within the ``sapp.db`` database, run:

.. code::

    python run_end_to_end.py --database ../db/sapp.db --scenario namibia_base

This could take a couple of minutes, depending on your computing system's capabilities.

Visualizing capacity in base scenario
*************************************

Next, we will utilize the existing scripts in GridPath to visualize our scenario simulation results. First, let's move from the `gridpath` folder to the `viz` folder:

.. code::

    os.chdir(os.path.join(gp_path, 'viz'))

Plotting total capacity
***********************

The script that can be used to plot total capacity per period (at the load zone level) is `capacity_total_plot.py`. See what input commands are needed for the script by running:

.. code::

    python capacity_total_plot.py --help

Let's say we want to check the total capacity in Namibia. We can do that by running:

.. code::

    %run capacity_total_plot.py --database ../db/sapp.db --scenario namibia_base --load_zone Namibia --show


Running scenario with unlimited transmission
############################################

We can run other scenarios that have been added to the .db, including a scenario with unlimited transmission (``env_r65_wk_simple2_unlimited_tx``):

.. code::

    python run_end_to_end.py --database ../db/sapp.db --scenario env_r65_wk_simple2_unlimited_tx


Visualizing results
###################

Next, we will utilize the existing scripts in GridPath to visualize our scenario simulation results.
First, let's move from the ``gridpath`` folder to the ``viz`` folder:

.. code::

    cd ../viz

Plotting total capacity
***********************

The script that can be used to plot total capacity per period (at the load zone level) is ``capacity_total_plot.py``. See what input commands are needed for the script by running:

.. code::

    python capacity_total_plot.py --help

Let's say we want to check the total capacity in Namibia. We can do that by running:

.. code::

    python capacity_total_plot.py --database ../db/test.db --scenario env_r65_wk_simple1 --load_zone Namibia --show

Plotting new capacity
*********************

If we wanted to plot only new (added) capacity in each period, the correct script to use would be ``capacity_new_plot.py``. Verify the inputs of the script by running:

.. code::

    python capacity_new_plot.py --help

Again, checking the new capacity for each period in Namibia:

.. code::

    python capacity_new_plot.py --database ../db/test.db --scenario env_r65_wk_simple1 --load_zone Namibia --show

Plotting dispatch
*****************

We can use the ``dispatch_plot.py`` script to plot dispatch of electricity for a given scenario and load zone.
Enter the following to check the inputs required to use ``dispatch_plot.py``:

.. code::

    python dispatch_plot.py --help

To plot the dispatch of generation in South Africa for the base (``env_r65_wk_simple1``) scenario, run:

.. code::

    python dispatch_plot.py --database ../db/test.db --scenario env_r65_wk_simple1 --load_zone SouthAfrica --show

Plotting comparison of total capacity between load zones
********************************************************

Let's say we want to compare total capacity in each period across load zones.
We can achieve that easily by using the ``capacity_total_loadzone_comparison_plot.py`` script:

.. code::

    python capacity_total_loadzone_comparison_plot.py --help

In this script, we do not need to specify a load zone.
Instead, we need to specify a period, and the script will compare total capacities across all load zones within that period.
For example, we can use the following to compare total capacity in the period 2030:

.. code::

    python capacity_total_loadzone_comparison_plot.py --database ../db/test.db --scenario env_r65_wk_simple1 --period 2030 --show


