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

Running base scenario for Namibia
#################################

Now we can run the scenarios using the data in the database.

Navigate to the ``gridpath`` folder by entering:

.. code::

    cd ../gridpath

To run a scenario, we will be using the ``run_end_to_end.py`` script.
To see the options for the script:

.. code::

    python run_end_to_end.py --help

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

    python capacity_total_plot.py --database ../db/sapp.db --scenario namibia_base --load_zone Namibia --show

Plotting new capacity
*********************

We can plot only _new_ capacity added each period, using the ``capacity_new_plot.py`` script.
Check the inputs of the script by running:

.. code::

    python capacity_new_plot.py --help

Checking the new capacity for each period in Namibia:

.. code::

    python capacity_new_plot.py --database ../db/sapp.db --scenario namibia_base --load_zone Namibia --show

More scenarios and visualizations
=================================

Running scenario with only one time period
##########################################

The base scenario runs on 3 time periods,
but we can also change the model to run on any number of time periods, including only one:

.. code::

    cd ../gridpath
    python run_end_to_end.py --database ../db/sapp.db --scenario namibia_1period


Plotting dispatch with only one time period
*******************************************

We can use the `dispatch_plot.py` script to plot dispatch of electricity for a
given scenario and load zone. Enter the following to check the inputs required to run
`dispatch_plot.py`:


.. code::

    cd ../viz
    python dispatch_plot.py --help

To plot the dispatch of generation for the above scenario, run:

.. code::

    python dispatch_plot.py --database ../db/sapp.db --scenario namibia_1period --load_zone Namibia --show

Running scenario with 80% RPS policy
####################################

.. code::

    cd ../gridpath
    python run_end_to_end.py --database ../db/sapp.db --scenario namibia_rps80


Plotting energy targets
***********************

We can use the ``energy_target_plot.py`` script to visualize our RPS goals and
the amount of renewable energy generated each period.

.. code::

    cd ../viz
    python energy_target_plot.py --help

To plot energy targets, run the command below:

.. code::

    python energy_target_plot.py --database ../db/sapp.db --scenario namibia_rps80 --energy_target_zone Namibia --show

Running scenarios with different cost projections
#################################################

The base scenario assumes VRE+battery costs decrease over time and conventional fuels increase over time.
Let's run a scenario where both VRE+battery costs and conventional fuel costs remain the same over time:

.. code::

    cd ../gridpath
    run_end_to_end.py --database ../db/sapp.db --scenario namibia_c0p0

Next, let's run a scenario where VRE+battery costs decrease and fossil fuel costs remain the same:

.. code::

    python run_end_to_end.py --database ../db/sapp.db --scenario namibia_c1p0

Plotting costs
**************

We can plot total costs in each period using the ``cost_plot.py`` script:

.. code::

    cd ../viz
    python cost_plot.py --help

To plot costs for the two different cost trajectory scenarios you ran above:

.. code::

    python cost_plot.py --database ../db/sapp.db --scenario namibia_c0p0 --load_zone Namibia --show
    python cost_plot.py --database ../db/sapp.db --scenario namibia_c1p0 --load_zone Namibia --show


Running scenarios representing dry and wet years
################################################

The base scenario assumes an average year for hydropower production.
We can also run a scenario that is representative of a dry year:

.. code::

    cd ../gridpath
    python run_end_to_end.py --database ../db/sapp.db --scenario namibia_dry

Conversely, we can run a scenario representing a wet year as well:

.. code::

    python run_end_to_end.py --database ../db/sapp.db --scenario namibia_wet

Plotting dispatch under wet and dry years
*****************************************

We can use the ``dispatch_plot.py`` again to plot dispatch for the two scenarios and
see the difference in hydro generation.

.. code::

    cd ../viz
    python dispatch_plot.py --database ../db/sapp.db --scenario namibia_dry --load_zone Namibia --show
    python dispatch_plot.py --database ../db/sapp.db --scenario namibia_wet --load_zone Namibia --show


Running base scenario for South Africa
######################################

Let's move to a different country and run a simple base scenario for South Africa and plot the dispatch:

.. code::

    cd ../gridpath
    python run_end_to_end.py --database ../db/sapp.db --scenario south_africa_base


Plotting dispatch for South Africa base scenario
************************************************

.. code::

    cd ../viz
    python dispatch_plot.py --database ../db/sapp.db --scenario south_africa_base --load_zone SouthAfrica --show

Running a scenario for all of SAPP, with unlimited transmission
###############################################################

For the next step, let's move from running a scenario at the country level and onto the entire SAPP region.
We have a scenario titled `sapp_unlimited_tx` that has all SAPP countries but allows for unlimited transmission.
We also have other scenarios added for SAPP that are more realistic, but those take too long to run using the Cbc solver,
so for now let's run the unlimited transmission scenario.

**Note that this scenario took about 15 minutes to run on my laptop.**

.. code::

    cd ../gridpath
    python run_end_to_end.py --database ../db/sapp.db --scenario sapp_unlimited_tx

Plotting comparison of total capacity between load zones
########################################################

Let's say we want to compare total capacity in each period across load zones.
We can achieve that easily by using the `capacity_total_loadzone_comparison_plot.py` script:

.. code::

    cd ../viz
    python capacity_total_loadzone_comparison_plot.py --help

In this script, we do not need to specify a load zone.
Instead, we need to specify a period, and the script will compare total capacities
across all load zones within that period.
For example, we can use the following to compare total capacity in the period 2030:

.. code::

    python capacity_total_loadzone_comparison_plot.py --database ../db/sapp.db --scenario sapp_unlimited_tx --period 2030 --show
