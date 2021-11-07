# HHS Exercise 3

This Project is created by Oscar Wellner, 21144192, and is structured as follows:

```
Project (isid)
|    README.md
|    main.py
└─── assets
|    └─── data
|    |        students.csv
|    |
|    └─── images
|             biker-banner.png
|
└─── src
|    └─── layout
|    |        studentInformationSystemApp.py
|    |        overviewFrame.py
|    |
|    └─── models
|    |        student.py
|    |
|    └─── utils
|             dataReader.py
└────────────────────────────
```

The `data` folder holds all the raw data and acts as the database location for the application. The `layout` folder
holds all the logic that is necessary to produce the GUI of the application. The `models` folders holds all the
information about the class models that are used in this application. The `utils` folder holds all the logic to
transform the raw data located in the `data` folder, into Python class objects.

This structure was chosen based on the MVC ideology that helps with separating logic used for setting up the Views (GUI),
from the logic used for declaring the domain (Models).

The `__init__.py` files are necessary for declaring packages and could be left empty if desired. I however specifically
specified what is imported into those files, to limit what is exposed from those packages. This helps with keeping code
private, which should not be used in other locations of the application.
