Log Analysis Project
====================
This project is part of Udacity Full stack nanodegree program.
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

You can clone this repository in vagrant subdirectory and download all the files required to run this project. The sql file inside is called newsdata.sql. Put this file into the vagrant directory.
ex.
cloning the git repository-
```
git clone https://github.com/ashokjain001/FullStack.git --recursive
```

## Executing
the Log Analysis Project
start your Vagrant by

```

python logAnalysis.py
```

to execute the code and it should open a webpage with movie information.

