====================================
Using SQLiteStudio to view databases
====================================

Up to this point, we've gone over how to create databases, add data to databases,
run scenarios, and visualize scenarios.


Downloading and installing SQLiteStudio
=======================================

There are many programs out there that allow you to view and edit SQL databases,
but in this workshop we'll recommend you work with `SQLiteStudio`_.

You can download SQLiteStudio via `this link`_.
If you are using a Windows system, download the ``sqlitestudio-3.3.3.zip`` file.
If you are using a macOS system, download the ``sqlitestudio-3.3.3.dmg`` file.

Installation should be straightforward, much like downloading and installing any other software.


Viewing a database file
=======================

Windows
#######

Open the SQLiteStudio app.



macOS
#####

Open the SQLiteStudio app.

To add a database, you can do one of three things:

* click on the third from the left icon with the green plus arrow (if you hover over it, it should say ``Add a database``)
* click on the ``Database`` > ``Add a database`` in the top menu bar
* press command + O on your keyboard

In the window that appears, under ``File``,
click on the folder icon that says ``Browse for existing database file on local computer``.
After you click on that, a Finder window should appear.
Navigate to your root GridPath folder, then navigate into the ``db`` subfolder.
Find the ``sapp.db`` file and click on it.
Click OK on the remaining window.

The ``sapp.db`` window should appear in the list of databases on the left side of the window now.
If you click on ``sapp``, the drop-down menu should expand to show all of the tables inside of the database.
From here, you can peruse through the inputs and outputs of the database.



.. _`SQLiteStudio`: https://www.sqlitestudio.pl/
.. _`this link`: https://github.com/pawelsalawa/sqlitestudio/releases


