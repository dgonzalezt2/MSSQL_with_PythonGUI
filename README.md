# MSSQL_with_PythonGUI
Database build with MSSQL connected with python using tkinter user Interface

## Setup

### Install python

to run this code please install python from [Install python](https://www.python.org/downloads/)

once you install python please install these dependencies search the file requirements.txt and run `pip install -r requirements.txt`

### MSSQL

To install Microsoft SQL Server please follow the instructions provide by Microsoft Team [SQL Server installation guide](https://docs.microsoft.com/en-us/sql/database-engine/install-windows/install-sql-server?view=sql-server-ver16)

#### Tables 

One you install microsoft SQL SERVER run the file `TableCreator.sql` to create all the required tables and relationships for the project, once the operation is done please run `ALL_INSERTS.sql` to add default values provied by the teacher

#### Connect with python

Go to `/GUI/Database/conexion.py` and edit this line:

```py
connection = pyodbc.connect('DRIVER={SQL Server};SERVER=<SERVERCONNNECTION>;DATABASE=<C>;Trusted_Connection=yes;')
```

The database is the SERVERCONNNECTION created for this project and the SERVERCONNNECTION select your database and click on propierties and copy the user.

![image](https://user-images.githubusercontent.com/81880494/172930022-7252110d-fb6c-4458-963c-a4db84c77a2a.png)
![image](https://user-images.githubusercontent.com/81880494/172930165-d8aad605-ba43-44ad-88a9-ba97a5d4ec07.png)

### Run the application

There is two ways to run your application 

#### Python Virtualenv
Follow the guide on [Python Virtual Environments: A Primer](https://realpython.com/python-virtual-environments-a-primer/)

once the Virtualenv is finally done run: 

```powershell
pip install -r requirements.txt
python main.py
```
#### Python without Virtualenv

for this option only run 

```powershell
pip install -r requirements.txt
python main.py
```
