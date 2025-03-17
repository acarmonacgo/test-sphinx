@echo off

rmdir /s /q docs
mkdir docs

xcopy /E /I /Y build\html docs

echo Build copied to docs successfully!
pause
