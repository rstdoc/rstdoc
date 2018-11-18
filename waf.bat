@setlocal
@set PYEXE=python
@where %PYEXE% 1>NUL 2>NUL
@if %ERRORLEVEL% neq 0 set PYEXE=py
@%PYEXE% -x "%~dp0rstdoc\wafw.py" %*
@exit /b %ERRORLEVEL%
