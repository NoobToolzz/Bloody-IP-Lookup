@echo off
title Installing Requirements!
color 0C

pip install -r requirements.txt
echo @echo off >> "run.bat"
echo python "Bloody IP Lookup.py" >> "run.bat"
echo pause >> "run.bat"
start run.bat
del setup.bat
