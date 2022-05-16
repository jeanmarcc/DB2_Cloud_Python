# MainframeIBM_DB2_Cloud_Python
Python script to connect and work with a DB2 database in the IBM cloud

## Getting Started

This Python program allows to connect and perfom SQL statements from a local computer to a DB2 database which is in IBM Cloud

My local computer is a Windows 10 laptop and I tested this Python program in a Linux Ubuntu disto inside a VMware in my local Windows 10

## Prerequsites

My platform:
- DB2 database in IBM cloud
- Visual Studio Code (in Linux or Windows)
- Python 3.10
- module ibm_db (intalled via pip)
- Ubuntu [22.04 LTS]
- VMware (personal free edition) 

## Connecting parameters

These parameters have to be retrieved from IBM Cloud DB2 (Sign in via IBM id), in "Service credentials" and then click on arrow in front of credential name to reveal these parameters.

(these parameters are proper to a database and not proper to each user of the database)

dsn_hostname = Hostname is a long string ending by ".appdomain.cloud"
dsn_uid = User name
dsn_pwd = password
dsn_database = name of the database (eg "BLUDB") 
dsn_port = port  

