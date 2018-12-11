@echo off
call git add .
set /p id="Enter Commit Description: "\r\n
call git commit -m "%id%"
echo Wait for Process to complete.....
call git push origin master
pause