@echo off
rem START or STOP Apache Service
rem --------------------------------------------------------
rem Check if argument is STOP or START

if not ""%1"" == ""START"" goto stop

net start wampstackApache
goto end

:stop

"C:/Users/aa/Documents/joooo/TPK(ByongSeop)/Bitnami/wampstack-5.6.31-0/apache2\bin\httpd.exe" -n "wampstackApache" -k stop

:end
exit
