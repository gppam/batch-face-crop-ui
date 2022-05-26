@echo OFF
:: Check if Python is installed
ECHO Checking if there is python
WHERE python >nul 2>nul
IF %ERRORLEVEL% NEQ 0 (ECHO Python wasn't found, please install via the Microsoft Store or through python.org) ELSE (ECHO python found... checking pip)

:: Check if PIP is installed
WHERE pip >nul 2>nul
IF %ERRORLEVEL% NEQ 0 (CALL :func_installpip) ELSE (ECHO pip found, checking for autocrop...)

:: Check if Autocrop is installed
WHERE autocrop >nul 2>nul
IF %ERRORLEVEL% NEQ 0 (CALL :func_installautocrop) ELSE (ECHO autocrop found... launching gui in three seconds)
timeout 2
python crop.py

:: Functions below
EXIT /B %ERRORLEVEL%
:func_installpip
ECHO Pip wasn't found, installing pip
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py


:func_installautocrop
ECHO Autocrop wasn't found, installing autocrop

PAUSE
EXIT /B 0