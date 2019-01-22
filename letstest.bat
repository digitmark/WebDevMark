@echo off
set /p gitname="Enter the Repository name: "\r\n
mkdir "%gitname%"
cd "%gitname%"
type nul > hello.txt
timeout 1
git init
git add .
timeout 2
set /p repourl="Enter the Repository URL: "\r\n
timeout 1
set /p commitmsg="Enter Commit Description: "\r\n
git commit -m "%commitmsg%"
git remote add origin "%repourl%"
git push -u origin master