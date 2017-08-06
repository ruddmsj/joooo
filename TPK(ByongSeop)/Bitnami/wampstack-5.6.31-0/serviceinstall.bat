@echo off
rem -- Check if argument is INSTALL or REMOVE

if not ""%1"" == ""INSTALL"" goto remove

if exist "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\mysql\scripts\serviceinstall.bat" (start "" /MIN "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\mysql\scripts\serviceinstall.bat" INSTALL)
if exist "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\postgresql\scripts\serviceinstall.bat" (start "" /MIN "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\postgresql\scripts\serviceinstall.bat" INSTALL)
if exist "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\elasticsearch\scripts\serviceinstall.bat" (start "" /MIN "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\elasticsearch\scripts\serviceinstall.bat" INSTALL)
if exist "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\logstash\scripts\serviceinstall.bat" (start "" /MIN "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\logstash\scripts\serviceinstall.bat" INSTALL)
if exist "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\logstash-forwarder\scripts\serviceinstall.bat" (start "" /MIN "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\logstash-forwarder\scripts\serviceinstall.bat" INSTALL)
if exist "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\kibana\scripts\serviceinstall.bat" (start "" /MIN "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\kibana\scripts\serviceinstall.bat" INSTALL)
if exist "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\apache2\scripts\serviceinstall.bat" (start "" /MIN "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\apache2\scripts\serviceinstall.bat" INSTALL)
if exist "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\apache-tomcat\scripts\serviceinstall.bat" (start "" /MIN "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\apache-tomcat\scripts\serviceinstall.bat" INSTALL)
if exist "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\resin\scripts\serviceinstall.bat" (start "" /MIN "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\resin\scripts\serviceinstall.bat" INSTALL)
if exist "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\jboss\scripts\serviceinstall.bat" (start "" /MIN "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\jboss\scripts\serviceinstall.bat" INSTALL)
if exist "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\wildfly\scripts\serviceinstall.bat" (start "" /MIN "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\wildfly\scripts\serviceinstall.bat" INSTALL)
if exist "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\activemq\scripts\serviceinstall.bat" (start "" /MIN "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\activemq\scripts\serviceinstall.bat" INSTALL)
if exist "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\openoffice\scripts\serviceinstall.bat" (start "" /MIN "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\openoffice\scripts\serviceinstall.bat" INSTALL)
if exist "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\subversion\scripts\serviceinstall.bat" (start "" /MIN "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\subversion\scripts\serviceinstall.bat" INSTALL)
rem RUBY_APPLICATION_INSTALL
if exist "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\mongodb\scripts\serviceinstall.bat" (start "" /MIN "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\mongodb\scripts\serviceinstall.bat" INSTALL)
if exist "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\lucene\scripts\serviceinstall.bat" (start "" /MIN "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\lucene\scripts\serviceinstall.bat" INSTALL)
if exist "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\third_application\scripts\serviceinstall.bat" (start "" /MIN "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\third_application\scripts\serviceinstall.bat" INSTALL)
if exist "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\nginx\scripts\serviceinstall.bat" (start "" /MIN "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\nginx\scripts\serviceinstall.bat" INSTALL)
if exist "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\php\scripts\serviceinstall.bat" (start "" /MIN "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\php\scripts\serviceinstall.bat" INSTALL)
goto end

:remove

if exist "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\third_application\scripts\serviceinstall.bat" (start "" /MIN "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\third_application\scripts\serviceinstall.bat")
if exist "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\lucene\scripts\serviceinstall.bat" (start "" /MIN "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\lucene\scripts\serviceinstall.bat")
if exist "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\mongodb\scripts\serviceinstall.bat" (start "" /MIN "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\mongodb\scripts\serviceinstall.bat")
rem RUBY_APPLICATION_REMOVE
if exist "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\subversion\scripts\serviceinstall.bat" (start "" /MIN "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\subversion\scripts\serviceinstall.bat")
if exist "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\openoffice\scripts\serviceinstall.bat" (start "" /MIN "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\openoffice\scripts\serviceinstall.bat")
if exist "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\jboss\scripts\serviceinstall.bat" (start "" /MIN "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\jboss\scripts\serviceinstall.bat")
if exist "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\wildfly\scripts\serviceinstall.bat" (start "" /MIN "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\wildfly\scripts\serviceinstall.bat")
if exist "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\resin\scripts\serviceinstall.bat" (start "" /MIN "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\resin\scripts\serviceinstall.bat")
if exist "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\activemq\scripts\serviceinstall.bat" (start "" /MIN "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\activemq\scripts\serviceinstall.bat")
if exist "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\apache-tomcat\scripts\serviceinstall.bat" (start "" /MIN "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\apache-tomcat\scripts\serviceinstall.bat")
if exist "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\apache2\scripts\serviceinstall.bat" (start "" /MIN "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\apache2\scripts\serviceinstall.bat")
if exist "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\logstash-forwarder\scripts\serviceinstall.bat" (start "" /MIN "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\logstash-forwarder\scripts\serviceinstall.bat")
if exist "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\kibana\scripts\serviceinstall.bat" (start "" /MIN "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\kibana\scripts\serviceinstall.bat")
if exist "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\logstash\scripts\serviceinstall.bat" (start "" /MIN "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\logstash\scripts\serviceinstall.bat")
if exist "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\elasticsearch\scripts\serviceinstall.bat" (start "" /MIN "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\elasticsearch\scripts\serviceinstall.bat")
if exist "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\postgresql\scripts\serviceinstall.bat" (start "" /MIN "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\postgresql\scripts\serviceinstall.bat")
if exist "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\mysql\scripts\serviceinstall.bat" (start "" /MIN "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\mysql\scripts\serviceinstall.bat")
if exist "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\php\scripts\serviceinstall.bat" (start "" /MIN "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\php\scripts\serviceinstall.bat")
if exist "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\nginx\scripts\serviceinstall.bat" (start "" /MIN "C:\Users\aa\DOCUME~1\joooo\TPK(BY~1\Bitnami\WAMPST~1.31-\nginx\scripts\serviceinstall.bat")
:end
