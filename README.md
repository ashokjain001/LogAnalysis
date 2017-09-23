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
1. Joining 2 or more Database tables.
2. Using basic select, where statements.
3. Utilizing aggregations functions to answer metric questions.
4. Writing code with Python DB-API.
5. effectively using Common Table Expression.

## Download
You need to have Virtual Machine and Vagrant installed in order to run the DB and Python script.
Inside the vagrant subdirectory, clone this git repository and content of the cloned repository will be shared with your virtual machine.
```
git clone https://github.com/ashokjain001/LogAnalysis.git
```
 Unzipping newsdata.zip will create newsdata.sql file.

If you need to bring the virtual machine back online, do so now by running,
```
vagrant up
 ```
 Then log into it with,
 ```
 vagrant ssh.
 ```
 once logged into VM, cd into the vagrant/LogAnalysis
and run the command below to load the data.
```
psql -d news -f newsdata.sql.
```Q
## Executing
Run this code in vagrant terminal,
```
python logAnalysis.py
```
This will run the python script and output 3 reports one after the other. You can access the output file logAnalysisOutput.txt for the output without running the code.