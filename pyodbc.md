# Connect to SQL Database by using Python on Ubuntu Linux

[Python code sample] (sample_python_linux.py) that runs on an Ubuntu Linux client computer, to connect to Microsoft SQL Databases.


## Requirements


- [Python 2.7.6](https://www.python.org/download/releases/2.7.6/).


### Install the required modules


Open your terminal and navigate to a directory where you plan on creating your python script. Enter the following commands to install **Microsoft ODBC Driver for SQL Server** and **pyodbc**. pyodbc uses the ODBC Driver to connect to SQL Databases.

	sudo apt-get --assume-yes update
  sudo su
  wget https://gallery.technet.microsoft.com/ODBC-Driver-13-for-Ubuntu-b87369f0/file/154097/2/installodbc.sh
  sh installodbc.sh
  sudo -H pip install pyodbc


## Create a database and retrieve your connection string


See the [getting started page](http://azure.microsoft.com/documentation/articles/sql-database-get-started/) to learn how to create a sample database and get your connection string. It is important you follow the guide to create an AdventureWorks database template. The samples shown below only work with the AdventureWorks schema. 
