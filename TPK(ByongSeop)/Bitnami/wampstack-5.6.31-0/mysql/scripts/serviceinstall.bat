@echo off
rem -- Check if argument is INSTALL or REMOVE

if not ""%1"" == ""INSTALL"" goto remove

"C:\Users\aa\Documents\joooo\TPK(ByongSeop)\Bitnami\wampstack-5.6.31-0/mysql\bin\mysqld.exe" --install "wampstackMySQL" --defaults-file="C:\Users\aa\Documents\joooo\TPK(ByongSeop)\Bitnami\wampstack-5.6.31-0/mysql\my.ini"

net start "wampstackMySQL" >NUL
goto end

:remove
rem -- STOP SERVICES BEFORE REMOVING

net stop "wampstackMySQL" >NUL
"C:\Users\aa\Documents\joooo\TPK(ByongSeop)\Bitnami\wampstack-5.6.31-0/mysql\bin\mysqld.exe" --remove "wampstackMySQL"

:end
exit
