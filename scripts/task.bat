set ORIGINAL_DIR=%CD%
REM _____PROJECT_FOLDER_____ must be replaced with the project dir in Windows
set PROJ_DIR=_____PROJECT_FOLDER_____

set YYYY=%date:~6,4%
set MM=%date:~3,2%
set DD=%date:~0,2%

set LOGFILE=%PROJ_DIR%\log\task_%YYYY%-%MM%-%DD%.log

echo ################################################################################ >> %LOGFILE% 2>&1
echo Starting - %date% %time% >> %LOGFILE% 2>&1
echo -------------------------------------------------------------------------------- >> %LOGFILE% 2>&1
echo Checking running processes >> %LOGFILE% 2>&1
for /f "tokens=1,2 delims= " %%A in ('tasklist ^| findstr python') do ( echo Found python process %%B & taskkill /f /pid %%B ) >> %LOGFILE% 2>&1
echo -------------------------------------------------------------------------------- >> %LOGFILE% 2>&1

REM _____SOURCE_FOLDER_____ must be replaced with the path of the original Pinterest.xlsx spreadsheet
set SRCFILE="_____SOURCE_FOLDER_____\Pinterest.xlsx"
set DSTFILE="%PROJ_DIR%\data\Pinterest\Pinterest.xlsx"

echo Copying Excel file >> %LOGFILE% 2>&1
echo   - Source: %SRCFILE% >> %LOGFILE% 2>&1
echo   - Destination: %DSTFILE% >> %LOGFILE% 2>&1
copy %SRCFILE% %DSTFILE% /Y >> %LOGFILE% 2>&1

cd %PROJ_DIR%

call %PROJ_DIR%\venv\Scripts\activate.bat

echo -------------------------------------------------------------------------------- >> %LOGFILE% 2>&1

python scripts\boards_get.py >> %LOGFILE% 2>&1
echo -------------------------------------------------------------------------------- >> %LOGFILE% 2>&1

python scripts\pin_repin.py >> %LOGFILE% 2>&1
echo -------------------------------------------------------------------------------- >> %LOGFILE% 2>&1

python scripts\pin_upload_or_repin.py >> %LOGFILE% 2>&1
echo -------------------------------------------------------------------------------- >> %LOGFILE% 2>&1

call %PROJ_DIR%\venv\Scripts\deactivate.bat

cd %ORIGINAL_DIR%

exit /B 1