# MainframeIBM_DB2_Cloud_Python
Python script launched on a local computer allowing to connect to and to work with a DB2 database in the IBM cloud. 

## Getting Started

This Python program allows to connect and perfom SQL statements from a local computer to a DB2 database which is in IBM Cloud

My local computer is a Windows 10 laptop and I tested this Python program in a Linux Ubuntu disto inside a VMware in my local Windows 10

## Prerequsites

My platform:
- DB2 database in IBM cloud
- Visual Studio Code (in Linux or Windows)
- Python 3.10
- module ibm_db (installed via pip)
- Ubuntu [22.04 LTS]
- VMware (personal free edition) 

## Connecting parameters

These parameters have to be retrieved from IBM Cloud DB2 (Sign in via IBM id), in "Service credentials" and then click on arrow in front of credential name to reveal these parameters.
![](https://github.com/johnmarcc/MainframeIBM_DB2_Cloud_Python/blob/fc4abd13ca05d1d95c4d10a3fd25a2b2cfbd6d62/IBMCloud%20credentials.png)

(these parameters are proper to a database and not proper to each user of the database)

dsn_hostname = Hostname is a long string ending by ".appdomain.cloud"
dsn_uid = User name
dsn_pwd = password
dsn_database = name of the database (eg "BLUDB") 
dsn_port = port  

## Testing

As a simple test, I perform a SELECT from one of my table "MYSCHEM.HOLDING" that I created in IBM DB2 Cloud console (could have been created in this Python script anyway)

select * from MYSCHEM.HOLDING;

It contains also calls to DB2 PROCEDURE that extract ticker fullname and currency

![](https://github.com/johnmarcc/MainframeIBM_DB2_Cloud_Python/blob/8aa9a09eb88486c229283c92ac4aca6e976e626a/selectQueryResult.png)
