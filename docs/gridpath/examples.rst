====================================
Running example models and scenarios
====================================

Using Jupyter/python notebooks
==============================

If using Jupyter notebooks for this portion,
access the notebooks located in the ``notebooks`` subfolder of the workshop materials (``PATH\TO\WORKSHOP\notebooks``)
and follow along with the workshop instructors.


Using command line
==================

Navigate to ``PATH\TO\GRIDPATH`` in your CMD by entering:

.. code::

    cd PATH\TO\GRIDPATH

From there, navigate to the ``db`` subdirectory by typing:

.. code::

    cd db

At this point, your working directory should look like ``PATH\TO\GRIDPATH\db``, but you can check the full directory by typing in the pwd command like below:

.. code::

    pwd

**Create database**

See the options available for the ``create_database.py`` script by entering:

.. code::

    python create_database.py --help

Then, create an empty database:

.. code::

    python create_database.py --database csv_examples.db

Then, we will populate the database using data in the ``csvs_test_examples`` folder using two scripts in the ``db/utilities``.
The database is populated in two stages:

1. All input data is populated using ``port_csvs_to_db.py``.
2. The scenarios are specified using in ``scenarios.py``.

To see the options available for the first stage, enter:

.. code::

    python utilities\port_csvs_to_db.py --help

Then run that script by pointing to the data in the ``csvs_test_examples`` folder and the empty database that you just created (``csv_examples.db``):

.. code::

    python utilities\port_csvs_to_db.py --database csv_examples.db --csv_location csvs_test_examples

Then we will import the scenarios data using the ``scenarios.py`` script in the ``utilities`` subfolder.
To see the options available for this script, run:

.. code::

    python utilities\scenarios.py --help

We are going to add scenarios already created/supplied in the ``csvs_test_examples`` folder, named ``scenarios.csv``.
Note that for future use, your scenarios csv can be located anywhere locally,
as long as it follows the same formatting, there are no errors in the file,
and you point to the correct file when running the `scenarios.py` script.

Add the example scenarios to ``csv_examples.db`` by running:

.. code::

    python utilities\scenario.py --database csv_examples.db --csv_path csvs_test_examples\scenarios.csv


**Running scenarios**

Now we can run the scenarios using the data in the database.

Navigate to the ``gridpath`` folder by entering:

.. code::

    cd ../gridpath

The script we will be using to model a scenario is the ``run_end_to_end.py`` script.
See the options for running this script by entering:

.. code::

    python run_end_to_end.py --help

As an example, we are going to run the ``2periods_new_build_2zones_transmission`` scenario.

To do so, run the following command:

.. code::

    python run_end_to_end.py --database ../db/csv_examples.db --scenario 2periods_new_build_2zones_transmission


