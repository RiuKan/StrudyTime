@echo off
git add *
setlocal
set /p str= message : 
git commit -m %str%
git push
set /p str= end