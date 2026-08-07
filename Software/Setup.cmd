@echo off
REM Sets up Bonsai for the behaviour box: downloads Bonsai if needed, restores
REM the packages listed in Bonsai.config, and checks the Spinnaker SDK.
REM Setup.ps1 lives beside Bonsai.exe because it must run from that folder.
pushd "%~dp0Behaviour_Box_Mini\.bonsai"
powershell -ExecutionPolicy Bypass -File ./Setup.ps1
popd
