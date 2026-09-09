@echo off
title ABC Trek Website - Local Clean URL Preview
echo ========================================================
echo   Starting Local Preview Server for ABC Trek in Nepal
echo   Clean URLs Enabled (No .html extensions)
echo ========================================================
echo.
echo Opening http://localhost:8080/ in your browser...
echo.
start http://localhost:8080/
python dev_server.py 8080
pause
