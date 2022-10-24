============================
Accessing workshop materials
============================

Workshop documentation
======================

The workshop documentation is hosted at the following URL: https://gridpath-technical-workshop.readthedocs.io/.

Workshop source code
====================

The source code (for materials such as notebooks, documentation, etc) is located in the following GitHub repo: https://github.com/cetlab-ucsb/gridpath-technical-workshop.

You can feel free to clone the repo if you are familiar/comfortable with ``git``.
If not, please go ahead and download the source code as a .zip file using the following link: https://github.com/cetlab-ucsb/gridpath-technical-workshop/archive/refs/heads/main.zip.
Extract the files from the zip into a folder/directory and note the location of the folder.
We will call this folder ``PATH\TO\WORKSHOP``.

Install Jupyter Lab
======================

In this workshop, we will be interfacing with GridPath through the use of a Jupyter notebook,
although GridPath is usually run from the command line.
The principle is mostly the same, with slightly different commands when running a GridPath script in a Jupyter versus in command line.

Install JupyterLab with ``pip`` by running the following line in your terminal (again, with your environment activated):

.. code::

    pip install jupyterlab

Note: If you've installed JupyterLab with conda or mamba, we recommend using the `conda-forge channel`_.

Launch Jupyter Lab
==================

Once Jupyter Lab has been installed, navigate to the root directory of the workshop folder installed:

.. code::

    cd PATH\TO\WORKSHOP

From there, we can navigate into the ``notebooks`` subdirectory:

.. code::

    cd notebooks

Launch JupyterLab by running:

.. code::

    jupyter-lab

This will open Jupyter Lab in the current folder/working directory of your terminal.
A browser window should open if run successfully.

**Note:** By installing Jupyter Lab with the environment activated,
that means Jupyter Lab is installed only in this environment and not universally on your machine.
Therefore, if you try to run ``jupyter-lab`` again without the environment activated, it might not work.
A workaround would be to install Jupyter Lab (using the same instructions as above) without your virtual environment activated.
However, that might not be good practice in terms of version control.

Installing the environment with this virtual environment also means that once you have the environment activated,
every other package in the environment comes with it.
In our case, because we installed GridPath (and all of the packages needed to run GridPath) in the same environment beforehand,
when we launch the Jupyter Lab installed in the same environment, we are able to run GridPath in the notebooks.



.. _`conda-forge channel`: https://conda-forge.org/
