$ErrorActionPreference = 'SilentlyContinue'

For ($i=0; $i -le 10; $i++) {
    Stop-Process -name oscp -Force 
    Stop-Process -name ImmunityDebugger.exe -Force 
    #Stop-Job -Name OSCP

    $oscp_j = Start-Job -Name OSCP -ScriptBlock { C:\Users\admin\Desktop\vulnerable-apps\oscp\oscp.exe }
    Start-Sleep 1 # Waitfor oscp process run
    $oscp_pid = (Get-Process -name oscp).id
    Write-Host "Pid of OSCP: $oscp_pid"
    #start Immunity Debugger
    Start-Sleep 1
    Start-Process -FilePath "C:\Program Files\Immunity Inc\Immunity Debugger\ImmunityDebugger.exe" -Wait

    Stop-Job -Name OSCP
}