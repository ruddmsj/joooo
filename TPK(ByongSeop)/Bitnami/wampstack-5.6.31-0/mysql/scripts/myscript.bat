@echo off
"C:\Users\aa\Documents\joooo\TPK(ByongSeop)\Bitnami\wampstack-5.6.31-0/mysql\bin\mysql.exe" --defaults-file="C:\Users\aa\Documents\joooo\TPK(ByongSeop)\Bitnami\wampstack-5.6.31-0/mysql\my.ini" -u root -e "UPDATE mysql.user SET Password=password('%1') WHERE User='root';"
"C:\Users\aa\Documents\joooo\TPK(ByongSeop)\Bitnami\wampstack-5.6.31-0/mysql\bin\mysql.exe" --defaults-file="C:\Users\aa\Documents\joooo\TPK(ByongSeop)\Bitnami\wampstack-5.6.31-0/mysql\my.ini" -u root -e "DELETE FROM mysql.user WHERE User='';"
"C:\Users\aa\Documents\joooo\TPK(ByongSeop)\Bitnami\wampstack-5.6.31-0/mysql\bin\mysql.exe" --defaults-file="C:\Users\aa\Documents\joooo\TPK(ByongSeop)\Bitnami\wampstack-5.6.31-0/mysql\my.ini" -u root -e "FLUSH PRIVILEGES;"
