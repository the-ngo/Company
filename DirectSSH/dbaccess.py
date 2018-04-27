from __future__ import print_function

import cx_Oracle

# Connect as user "hr" with password "welcome" to the "oraclepdb" service running on this computer.
connection = cx_Oracle.connect("rdr", "W3nEbraska_3", "5.221.135.11")

cursor = connection.cursor()
cursor.execute('select co_dn, co_name, co_state from utp_common_objects where co_oc_id = 811')
for line in cursor:
    print(cursor)