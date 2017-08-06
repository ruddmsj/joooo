@echo off
rem START or STOP Services
rem ----------------------------------
rem Check if argument is STOP or START

if not ""%1"" == ""START"" goto stop

if exist "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\hypersonic\scripts\servicerun.bat" (start "" /MIN "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\server\hsql-sample-database\scripts\servicerun.bat" START)
if exist "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\ingres\scripts\servicerun.bat" (start "" /MIN "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\ingres\scripts\servicerun.bat" START)
if exist "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\mysql\scripts\servicerun.bat" (start "" /MIN "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\mysql\scripts\servicerun.bat" START)
if exist "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\postgresql\scripts\servicerun.bat" (start "" /MIN "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\postgresql\scripts\servicerun.bat" START)
if exist "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\elasticsearch\scripts\servicerun.bat" (start "" /MIN "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\elasticsearch\scripts\servicerun.bat" START)
if exist "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\logstash\scripts\servicerun.bat" (start "" /MIN "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\logstash\scripts\servicerun.bat" START)
if exist "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\logstash-forwarder\scripts\servicerun.bat" (start "" /MIN "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\logstash-forwarder\scripts\servicerun.bat" START)
if exist "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\apache2\scripts\servicerun.bat" (start "" /MIN "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\apache2\scripts\servicerun.bat" START)
if exist "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\openoffice\scripts\servicerun.bat" (start "" /MIN "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\openoffice\scripts\servicerun.bat" START)
if exist "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\apache-tomcat\scripts\servicerun.bat" (start "" /MIN "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\apache-tomcat\scripts\servicerun.bat" START)
if exist "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\resin\scripts\servicerun.bat" (start "" /MIN "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\resin\scripts\servicerun.bat" START)
if exist "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\activemq\scripts\servicerun.bat" (start "" /MIN "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\activemq\scripts\servicerun.bat" START)
if exist "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\jboss\scripts\servicerun.bat" (start "" /MIN "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\jboss\scripts\servicerun.bat" START)
if exist "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\wildfly\scripts\servicerun.bat" (start "" /MIN "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\wildfly\scripts\servicerun.bat" START)
if exist "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\jetty\scripts\servicerun.bat" (start "" /MIN "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\jetty\scripts\servicerun.bat" START)
if exist "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\subversion\scripts\servicerun.bat" (start "" /MIN "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\subversion\scripts\servicerun.bat" START)
rem RUBY_APPLICATION_START
if exist "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\lucene\scripts\servicerun.bat" (start "" /MIN "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\lucene\scripts\servicerun.bat" START)
if exist "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\mongodb\scripts\servicerun.bat" (start "" /MIN "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\mongodb\scripts\servicerun.bat" START)
if exist "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\third_application\scripts\servicerun.bat" (start "" /MIN "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\third_application\scripts\servicerun.bat" START)
goto end

:stop
echo "Stopping services ..."
if exist "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\third_application\scripts\servicerun.bat" (start "" /MIN "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\third_application\scripts\servicerun.bat" STOP)
if exist "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\lucene\scripts\servicerun.bat" (start "" /MIN "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\lucene\scripts\servicerun.bat" STOP)
rem RUBY_APPLICATION_STOP
if exist "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\subversion\scripts\servicerun.bat" (start "" /MIN "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\subversion\scripts\servicerun.bat" STOP)
if exist "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\jetty\scripts\servicerun.bat" (start "" /MIN "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\jetty\scripts\servicerun.bat" STOP)
if exist "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\hypersonic\scripts\servicerun.bat" (start "" /MIN "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\server\hsql-sample-database\scripts\servicerun.bat" STOP)
if exist "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\jboss\scripts\servicerun.bat" (start "" /MIN "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\jboss\scripts\servicerun.bat" STOP)
if exist "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\wildfly\scripts\servicerun.bat" (start "" /MIN "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\wildfly\scripts\servicerun.bat" STOP)
if exist "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\resin\scripts\servicerun.bat" (start "" /MIN "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\resin\scripts\servicerun.bat" STOP)
if exist "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\activemq\scripts\servicerun.bat" (start "" /MIN "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\activemq\scripts\servicerun.bat" STOP)
if exist "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\apache-tomcat\scripts\servicerun.bat" (start "" /MIN /WAIT "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\apache-tomcat\scripts\servicerun.bat" STOP)
if exist "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\openoffice\scripts\servicerun.bat" (start "" /MIN "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\openoffice\scripts\servicerun.bat" STOP)
if exist "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\apache2\scripts\servicerun.bat" (start "" /MIN "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\apache2\scripts\servicerun.bat" STOP)
if exist "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\logstash-forwarder\scripts\servicerun.bat" (start "" /MIN "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\logstash-forwarder\scripts\servicerun.bat" STOP)
if exist "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\logstash\scripts\servicerun.bat" (start "" /MIN "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\logstash\scripts\servicerun.bat" STOP)
if exist "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\elasticsearch\scripts\servicerun.bat" (start "" /MIN "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\elasticsearch\scripts\servicerun.bat" STOP)
if exist "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\ingres\scripts\servicerun.bat" (start "" /MIN "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\ingres\scripts\servicerun.bat" STOP)
if exist "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\mysql\scripts\servicerun.bat" (start "" /MIN "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\mysql\scripts\servicerun.bat" STOP)
if exist "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\mongodb\scripts\servicerun.bat" (start "" /MIN "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\mongodb\scripts\servicerun.bat" STOP)
if exist "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\postgresql\scripts\servicerun.bat" (start "" /MIN "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\postgresql\scripts\servicerun.bat" STOP)

:end
