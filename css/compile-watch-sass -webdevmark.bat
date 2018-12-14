@echo off
REM set /p ip="Enter the input file: "\r\n
REM set /p op="Enter the output file: "\r\n
REM sass --watch app/sass:public/stylesheets - For entire directory
REM class sass --watch input.scss output.css
timeout 1
call sass --watch style.scss style.css