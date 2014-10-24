vbin
====

Command Line Tools for Unix 

All are short bash, awk, python, or perl scripts that can be used together with other Unix Bash command to form a formiable arsenal of tools.

Created by Dlink
Source: https://github.com/dlink/vbin

Install
-------
A good place to install vbin is in /usr/local/vbin, but you can install where ever you like.  It is best to add it to your Unix PATH environment variable.

Here is an example install:
 
    $ sudo su -
    # cd /usr/local
    # git clone git@github.com:dlink/vbin.git

Now add it to everyones PATH

    # cd /etc/profile.d
    # cat > vbin
    PATH=$PATH:/usr/local/vbin
    ^D
    
Test it:

    $ lshead


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
* cols
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
#### clip ####

  Clip output horizontally. Defaults to 80 columns.  Good to avoid wrapping on the console
  
  Syntax:
     clip [<long>] [<page_num>]
     
  Example:
     # for 80 column screens:
     cat log | clip     # show first page, ie. cut -c1-80)
     cat log | clip 2   # show second page, ie. cut -c81-160
     cat log | clip 3   # show third page, ie. cut -c161-240

     # for wider screens     
     cat log | clip long   # show first long page, ie. cut -c1-158
     cat log | clip long 2 # show second long page, ie. cut -c159-316
     
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


* revver

  Create versioned copies of a file with postfixes: _1, _2, etc.
  It is inspired by VMS O/S.

  Always wise to make a copy of a system file before editing it.

  Syntax:

    revver [-u] filea [fileb, ...]
    -u  to unroll revisions

  Example:

     The following command

        revver list list_1

     Does:

        mv -f list list_1

     After recreating the original list and running the same command a
     second time you will see:

        mv -f list_1 list_2
        mv -f list list_1

     The -u command undoes a revision.  So

        revver -u list

     Does:

        mv -f list_1 list
        mv -f list_2 list_1
         

* sav

  Create a saved copy of a file, preserving timestamp and permissions

  ADMIN: Always wise to save copy of a system file before editing it.

  Example:

     The following command is equivalent to: cp -p professors.csv.sav
  
     sav professors.csv


  See, Also: 

     savdiff, unsav, revver


* savdiff

  Compare a file with its saved version.

  Example:

     The following is equivalent to: diff professors.csv professors.csv.sav
    savdiff professors.csv

  See, Also:
     sav, unsav, revver
  
* unsav

  Un save a copy of a file

  Example:
     The following command is equivalent to: 
      cp -p professors.csv.sav professors.csv

    unsav professors.csv

  See, Also:

     sav, savdiff, revver
