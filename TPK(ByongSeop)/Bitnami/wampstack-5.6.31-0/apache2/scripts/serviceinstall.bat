@echo off
rem -- Check if argument is INSTALL or REMOVE

if not ""%1"" == ""INSTALL"" goto remove

"C:/Users/aa/Documents/joooo/TPK(ByongSeop)/Bitnami/wampstack-5.6.31-0/apache2\bin\httpd.exe" -k install -n "wampstackApache" -f "C:/Users/aa/Documents/joooo/TPK(ByongSeop)/Bitnami/wampstack-5.6.31-0/apache2\conf\httpd.conf"

net start wampstackApache >NUL
goto end

:remove
rem -- STOP SERVICE BEFORE REMOVING

net stop wampstackApache >NUL
"C:/Users/aa/Documents/joooo/TPK(ByongSeop)/Bitnami/wampstack-5.6.31-0/apache2\bin\httpd.exe" -k uninstall -n "wampstackApache"

:end
exit
