#!/usr/bin/env python

import psycopg2


# declaring database
DBNAME = "news"


def loganalysis():

    # connect to the database news
    try:
        conn = psycopg2.connect(database=DBNAME)
    except:
        print "Unable to connect to database"

    # make a cursor object from a connection, Cursors are used to send
    # SQL statements to the database and fetch results
    cursor = conn.cursor()

    # calling seperate methods to answer
    # eachreporting questions
    popularArticle(cursor)
    popularAuthors(cursor)
    errorsPerDay(cursor)

    # closing the connection
    conn.close()


def popularArticle(cursor):

    # execute SQL statement on the database
    cursor.execute("""SELECT articles.title, count(*)
                        FROM articles INNER JOIN log ON
                        log.path = '/article/' || articles.slug
                        GROUP BY title
                        ORDER BY COUNT(*) DESC
                        LIMIT 3;""")

    # Fetch all the results from the current statement
    results = cursor.fetchall()

    # printing the results
    print "\nThe most popular three articles of all time:"
    for article, views in results:
        print('{0:<40}{1} views'.format(article, views))


def popularAuthors(cursor):

    # execute SQL statement on the database
    cursor.execute("""SELECT authors.name,count(*)
                      FROM articles INNER JOIN authors
                      on articles.author = authors.id
                      INNER JOIN log ON
                      log.path = '/article/' || articles.slug
                      GROUP BY authors.name
                      ORDER BY count(*) DESC""")

    # Fetch all the results from the current statement
    results = cursor.fetchall()

    # printing the results
    print "\nThe most popular article authors of all time:"
    for author, views in results:
        print('{0:<40}{1} views'.format(author, views))


def errorsPerDay(cursor):

    # execute SQL statement on the database
    cursor.execute("""WITH t1 as
                      (SELECT time::date as days,
                      count(*) as agg
                      FROM log
                      GROUP BY time::date
                      ),t2 as (SELECT time::date as days,
                      count(*) as agg
                      FROM log
                      WHERE status like '%NOT%'
                      GROUP BY time::date
                      )SELECT to_char(t1.days,'FMMONTH DD,YYYY') as days,
                      to_char((cast(t2.agg as decimal)/t1.agg)*100.0,'99.99%')
                      as errors
                      FROM t1 INNER JOIN t2 ON t1.days = t2.days
                      where (cast(t2.agg as decimal)/t1.agg)*100.0> 1.00;""")

    # Fetch all the results from the current statement
    results = cursor.fetchall()

    # printing the results
    print "\nDays with more than 1% of requests lead to errors:"
    for day, error in results:
        print('{0:<40}{1} views'.format(day, error))


# this executes this python module
if __name__ == '__main__':
    loganalysis()
