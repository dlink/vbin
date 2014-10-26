vbin
====

vbin is a collection of Command Line Tools for Unix.  They are used with other Unix Bash commands to form a formiable arsenal of tools.

Source: https://github.com/dlink/vbin

Documentation: http://crowfly.net/vbin

Commands Listing
----------------
### General Tools ###

<table><tr><td>

<li> clip <br/>
<li> dos2unix <br/>
<li> flatten <br/>
<li> histogram <br/>
<li> lshead <br/>
<li> orig <br/>
<li> origdiff <br/>
<li> phplook <br/>

</td><td>

<li> pllook <br/>
<li> psgrep <br/>
<li> pylook <br/>
<li> revver <br/>
<li> sav <br/>
<li> savdiff <br/>
<li> show_env.pl <br/>
<li> ssh_setauth <br/>

</td><td valign='top'>

<li> striphtml <br/>
<li> t2c <br/>
<li> tildadiff <br/>
<li> txt2html <br/>
<li> unflatten <br/>
<li> unix2dos <br/>
<li> unorig <br/>
<li> unsav <br/>

</td></tr></table>


### CSV Tools ###

* col_sum
* csv2html
* csv2inserts
* csv2wiki
* csvformat
* csvformat2
* show_header

### SQL Tools ###

* count
* count_distinct
* desc
* explain
* sql_pretty
* show_create
* show_indexes
* show_tables
* select5
* selectall
* selecthistogram
* selectmax
* selectsome
* tally

DETAIL DESCRIPTIONS
===================
* col_sum 

  Add up a column of numbers

  Syntax:
     col_sum [ <col_num> ]

      col_num - zero based.
                Default is 0.

  Example:

     Sum available diskspace across all drives in MB.

        df -m | col_sum +3

     Count number of classes all python programs: 
    
        grep -c class *.py | cut -d':' -f2 | col_sum


* fwk_usage

  List all foreign keys that refer to a given table

  Example:

    fwk_usage central order_items | mysql <signature> -t

    Returns:

      +-----------------+------------+-----------------------+
      | constraint_name | table_name | referenced_table_name |
      +-----------------+------------+-----------------------+
      | shipping_ibfk_1 | shipping   | order_items           |
      +-----------------+------------+-----------------------+


* histogram 

  Generate a histogram from a list of data.   

  Example:

    Given spreadsheet of names and addresses, as a csv file, answer
    the question: How many people come from each state:

    cut -d',' -f6 professors.csv | histogram


