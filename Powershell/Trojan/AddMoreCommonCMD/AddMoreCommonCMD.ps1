$repeatedCommands = @(
    "'Get-Host'",
    "'Get-Date'",
    "'Get-Service'",
    "'Get-Process'",
    "'Get-EventLog -LogName System'"
) * 100 # 重复100次
$originalScript = Get-Content -Path "../RATSample.ps1" -Raw
$obfuscatedScript = $repeatedCommands + $originalScript + $repeatedCommands
$obfuscatedScript -join "`n" | Out-File -FilePath "ObfuscatedRAT.ps1"