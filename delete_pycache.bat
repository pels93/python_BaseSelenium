@echo off
SET search_tag=Directorio
SET name_folder=_pycache_
dir *%name_folder%* /s /q | findstr %search_tag% >filelist.txt
for /F "delims=*" %%a in ('findstr %search_tag% filelist.txt') do (
set /A i+=1
call set array[%%i%%]=%%a
call set n=%%i%%
)
DEL filelist.txt
for /L %%i in (1,1,%n%) do (
    call cd %%array[%%i]:~15%%
    RD /S /Q __pycache__
    )