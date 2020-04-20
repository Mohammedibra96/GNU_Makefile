@echo off
setlocal EnableDelayedExpansion 

rem this file shall increment the value of the progress \
rem if the file exist or set the progress to 1 if not exist  

set file=Progress.txt 

rem read the file if exist
if exist %file% (
for /f "tokens=1-2" %%a in (%file%) do (
set x=%%a
rem increment the value of the progres 
set /a x=x+1
rem write the new value of the progress in the file 
echo !x! >%file%
)
)
rem set the progress to 1 if the file not exist 
if not exist %file% (
 echo 1 >%file%
)
exit 








