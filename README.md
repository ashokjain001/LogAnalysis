Log Analysis Project
====================
This project is part of Udacity's Full stack nanodegree program.
The objective of this project is to create a reporting tool using Python DB-API that prints out reports based on data in the database.
The 'news' database contains newspaper articles, authors, as well as the web server log for the site.

Reporting tool developed in this project will aim to answer these 3 question:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

Skills learnt and demonstrated in this project are:
* Joining 2 or more Database tables.
* Using basic select, where statements.
* Utilizing aggregations functions to answer metric questions.
* Writing code with Python DB-API.
* Effectively using Common Table Expression.

## Download and Configuration
You need to have Virtual Machine and Vagrant installed in order to run the DB and Python script.
Please refer [Instructions](https://classroom.udacity.com/nanodegrees/nd004/parts/8d3e23e1-9ab6-47eb-b4f3-d5dc7ef27bf0/modules/bc51d967-cb21-46f4-90ea-caf73439dc59/lessons/5475ecd6-cfdb-4418-85a2-f2583074c08d/concepts/14c72fe3-e3fe-4959-9c4b-467cf5b7c3a0)
 for installing Vagrant and VM.
Inside the vagrant subdirectory, clone this git repository and content of the cloned repository will be shared with your virtual machine.
```
git clone https://github.com/ashokjain001/LogAnalysis.git
```
 Unzipping newsdata.zip will create newsdata.sql file.

If you need to bring the virtual machine back online, do so now by running the following command in terminal,
```
vagrant up
 ```
 Then log into it with,
 ```
 vagrant ssh.
 ```
 Once logged into VM, cd into the vagrant/LogAnalysis
and run the command below to load the data.
```
psql -d news -f newsdata.sql
```
## Executing
Run this code in vagrant terminal,
```
python logAnalysis.py
```
This will run the python script and output 3 reports one after the other. You can access the output file logAnalysisOutput.txt for the output without running the code.