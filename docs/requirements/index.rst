============
Requirements
============

Python 3.9
==========

GridPath is tested in Python 3.8, 3.9, and 3.10.
For the purposes of this workshop, we will be using Python 3.9.

Please download Python 3.9 here: https://www.python.org/downloads/release/python-3913/

Windows
#######

Use the Windows Installer (64-bit).

Please select Add Python 3.9 to PATH at the bottom when you first launch the installer.

When setup is successful, open a new Command Prompt window and type ``python``.

You should see something like this:

.. code::

    Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
    Type "help", "copyright", "credits" or "license" for more information.


If not, you still need to add Python to your system variables.

Search for ‘environment variables’ and click ‘Edit the system environment variables’. (Make sure to select “system environment variables” and not “environment variables for your account”. For the latter choice, the system environment variables’ edit buttons will be grayed out.) Under ‘User variables’ at the top (the ‘System variables’ are at the bottom), double click on Path. The top two variables should be the recently installed Python 3.9.

For me they are as follows:

.. code::

    C:\Users\bluemarble\AppData\Local\Programs\Python\Python39\Scripts\
    C:\Users\bluemarble\AppData\Local\Programs\Python\Python39\

Now copy those variables and add them to the Path under ‘System variables’. Click on the System variables Path, click New, then add the two directories above individually. Make sure to move them to the top (before all other paths) with the buttons on the right.

Open a new CMD window and type ``python``. You should see this:

.. code::

    Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
    Type "help", "copyright", "credits" or "license" for more information.

To exit the python console, type ``quit()``.


macOS
#####

Download the macOS 64-bit, installer
(Intel-only if your processor is an Intel one, otherwise download the universal2 installer).

Wait for the download to complete.
Once it's finished, double-click the package to start the installation process.
You can follow the on-screen instructions in the Python installer for this step.

Once the installation is complete,
the installer will automatically open Python's installation directory in a new Finder window.

Open a new terminal window (you can spotlight search for ``terminal`` and it should appear).
Enter:

.. code::

    python --version

If your laptop is like mine and came with an older version of Python installed, your output might be something like this:

.. code::

    Python 2.7.16

Instead, try running this:

.. code::

    python3.9 --version

If the Python installation you did above installed correctly, you should see something like this:

.. code::

    Python 3.9.13


Python virtual environment
==========================

Windows
#######

Once you have installed Python 3.9,
you can create the virtual environment for GridPath by running from CMD:

.. code::

    python -m venv PATH\TO\PYTHON\ENV

E.g.

.. code::

    python -m venv C:\Users\bluemarble\gridpath_sa_workshop_env

This will create the virtual environment in the ``PATH\TO\PYTHON\ENV`` directory. Please remember this directory. On Windows, you can activate the virtual environment by running the appropriate activation script from inside the “Scripts” directory of the virtual environment directory. From cmd.exe:

.. code::

    \PATH\TO\PYTHON\ENV\Scripts\activate.bat

E.g.

.. code::

    C:\Users\bluemarble\gridpath_sa_workshop_env\Scripts\activate.bat

If you see the environment name in parentheses before your current directory,
this step has been successful.

macOS
#####

You can create a new environment in the terminal by running something like:

.. code::

    python3.9 venv -m /PATH/TO/ENV

So, in my case, if wanted to create a virtual environment titled ``gridpath_sa_workshop_env``
in ``/Users/bluemarble/``, then my command will look something like:

.. code::

    python3.9 venv -m /Users/bluemarble/gridpath_sa_workshop_env

After the virtual environment has been created, you can activate it by running:

.. code::

    source /PATH/TO/ENV/bin/activate

In the example above, I would be running:

.. code::

    source /Users/bluemarble/gridpath_sa_workshop_env/bin/activate

If the activation was successful,
you should see the environment name in parentheses in front of your current command line.


Cbc solver
==========

Windows
#######

On Windows, you can also download the Cbc executable from the `AMPL website`_, specifically here for `64-bit Windows`_.

GridPath allows you to specify the location of the solver executable; to get it to be recognized, automatically, you can also add the folder path to your PATH system environment variables (see instructions for Python above; `general instructions for Windows`_).

Make sure to close all windows of the system environment variables.
Type ``cbc`` in CMD and the cbc solver should execute with a “Coin” prompt.
If the cbc solver is not recognized at the CMD command prompt, restart CMD and try typing ``cbc`` again.
Windows should be able to find the cbc executable as long as its folder is in the system environment path.


macOS
#####

On Mac, use your terminal to navigate to where you want to download/install CBC by entering:

.. code::

    cd /path/to/cbc

Then, in your terminal, copy and paste the following:

.. code::

    wget https://raw.githubusercontent.com/coin-or/coinbrew/master/coinbrew
    chmod u+x coinbrew
    ./coinbrew fetch Cbc@master
    ./coinbrew build Cbc
    ./coinbrew install Cbc

This process can take quite some time.
After the installation, you may see something like this:

.. code::

    Installation is done automatically following build and test of each project.

    Installation directory is writable.

    Package will be installed to /Users/meas/Downloads/cbc-path/dist

    Disabling uninstalled packages

    Install completed. If executing any of the installed
    binaries results in an error that shared libraries cannot
    be found, you may need to
      - add 'export LD_LIBRARY_PATH=/Users/meas/Downloads/cbc-path/dist/lib' to your ~/.bashrc (Linux)
      - add 'export DYLD_LIBRARY_PATH=/Users/meas/Downloads/cbc-path/dist/lib' to ~/.bashrc (OS X)

Please note the given directories. In order to get CBC to work, you need to enter something like the following:

.. code::

    export PATH="$PATH:/Users/meas/Downloads/cbc-path/dist/bin"
    export export LD_LIBRARY_PATH="/Users/meas/Downloads/cbc-path/dist/lib"
    export export DYLD_LIBRARY_PATH="/Users/meas/Downloads/cbc-path/dist/lib"

Except replace the directories seen there with the directories given by your own terminal
(which is based on where you downloaded the CBC file).

I would recommend copying and saving the above ``export`` commands somewhere because that only impacts
your current environment. If you close your terminal, you might need to enter them again
(or save them to your ``bash``/``zsh`` environment, which is a bit more complicated and
probably out of the scope of this workshop).

To check if CBC is properly installed, run the following in your terminal:

.. code:: bash

    cbc

You should see something like the following:

.. code-block:: bash

    Welcome to the CBC MILP Solver
    Version: Devel (unstable)
    Build Date: Oct 24 2022
    Cbc takes input from arguments ( - switches to stdin)
    Enter ? for list of commands or help
    Cbc:

Type and enter ``exit`` to exit out of CBC.

.. _`AMPL website`: https://ampl.com/products/solvers/open-source/#cbc
.. _`64-bit Windows`: https://ampl.com/dl/open/cbc/cbc-win64.zip
.. _`general instructions for Windows`: https://www.java.com/en/download/help/path.xml
.. _`Read the Docs Sphinx theme`: https://github.com/readthedocs/sphinx_rtd_theme
