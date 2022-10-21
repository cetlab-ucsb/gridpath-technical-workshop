# Prerequisites

## Python 3.9

GridPath is tested in Python 3.8, 3.9, and 3.10. For the purposes of this workshop, we will be using Python 3.9. Please download Python 3.9 here: https://www.python.org/downloads/release/python-3913/

Use the Windows Installer (64-bit).

Please select Add Python 3.9 to PATH at the bottom when you first launch the installer.

When setup is successful, open a new Command Prompt window and type ‘python’

You should see something like this:
```commandline
Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

If not, you still need to add Python to your system variables.

Search for ‘environment variables’ and click ‘Edit the system environment variables’. (Make sure to select “system environment variables” and not “environment variables for your account”. For the latter choice, the system environment variables’ edit buttons will be grayed out.) Under ‘User variables’ at the top (the ‘System variables’ are at the bottom), double click on Path. The top two variables should be the recently installed Python 3.9.

For me they are as follows:
```commandline
C:\Users\bluemarble\AppData\Local\Programs\Python\Python39\Scripts\
C:\Users\bluemarble\AppData\Local\Programs\Python\Python39\
```
Now copy those variables and add them to the Path under ‘System variables’. Click on the System variables Path, click New, then add the two directories above individually. Make sure to move them to the top (before all other paths) with the buttons on the right.

Open a new CMD window and type `python`. You should see this:
```commandline
Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

To exit the python console, type `quit()`.

## Python Virtual Environment

Once you have installed Python 3.9, you can create the virtual environment for GridPath by running from CMD:

```commandline
python -m venv PATH\TO\PYTHON\ENV
```
E.g.

```commandline
python -m venv C:\Users\bluemarble\gridpath_sa_workshop_env
```

This will create the virtual environment in the `PATH\TO\PYTHON\ENV` directory. Please remember this directory. On Windows, you can activate the virtual environment by running the appropriate activation script from inside the “Scripts” directory of the virtual environment directory. From cmd.exe:

```commandline
\PATH\TO\PYTHON\ENV\Scripts\activate.bat
```

E.g. 
```commandline
C:\Users\bluemarble\gridpath_sa_workshop_env\Scripts\activate.bat
```

If you see the environment name in parenthesis before your current directory, this step has been successful.

## Jupyter Lab

Install JupyterLab with `pip` by running the following line in your terminal:

```commandline
pip install jupyterlab
```

Note: If you install JupyterLab with conda or mamba, we recommend using the [conda-forge channel](https://conda-forge.org/).

Once installed, launch JupyterLab with:

```commandline
jupyter-lab
```

This will open Jupyter Lab in the current folder/working directory of your terminal. A browser window should open if run successfully.