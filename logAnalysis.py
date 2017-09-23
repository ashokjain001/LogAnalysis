#!/usr/bin/env python

import psycopg2

DBNAME="news"

def loganalysis():

    # connect to the database news
    conn = psycopg2.connect(database=DBNAME)

    # make a cursor object from a connection, Cursors are used to send SQL statements to the database and fetch results
    cursor = conn.cursor()

    # execute SQL statement on the database
    cursor.execute("select right(log.path,length(log.path)-9), count(*) from log group by path order by count(*) desc OFFSET 1 LIMIT 3;")

    # Fetch all the results from the current statement
    results=cursor.fetchall()

    # printing the results 1
    print "\nThe most popular three articles of all time:"
    for row in results:
        space = " "*(30-len(row[0]))
        print row[0], space,row[1], "views"

    cursor.execute("select authors.name,count(*) from articles inner join authors on articles.author = authors.id inner join log on right(log.path,length(log.path)-9) =articles.slug group by authors.name order by count(*) desc")
    results = cursor.fetchall()

    # printing the results 2
    print "\nThe most popular article authors of all time:"
    for row in results:
        space = " " * (30 - len(row[0]))
        print row[0], space, row[1], "views"

    cursor.execute("with t1 as (select to_char(time,'MONTH DD,YYYY') as days, count(*) as agg from log group by to_char(time,'MONTH DD,YYYY')), t2 as (select to_char(time,'MONTH DD,YYYY') as days, count(*) as agg from log where status like '%NOT%' group by to_char(time,'MONTH DD,YYYY')) select t1.days,to_char((cast(t2.agg as decimal)/t1.agg)*100.0,'99.99%') as errors from t1 inner join t2 on t1.days = t2.days where (cast(t2.agg as decimal)/t1.agg)*100.0> 1.00;")
    results = cursor.fetchall()

    # printing the results 3
    print "\nDays with more than 1% of requests lead to errors:"
    for row in results:
        space = " " * (26 - len(row[0]))
        print row[0], space, row[1], "errors"

    # closing the connection
    conn.close()


# this helps in executing this python file
print loganalysis()