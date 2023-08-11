# base64Decode

function base64Decode {
    param(
        [Parameter(Mandatory = $true, Position = 0)]
        [string]$base64String
    )

    $bytes = [System.Convert]::FromBase64String($base64String)
    $decodedString = [System.Text.Encoding]::UTF8.GetString($bytes)
    return $decodedString
}

# 测试用例: Y2FzZGZkY3dlcg==
$base64String = "Y2FzZGZkY3dlcg=="
$decodedString = base64Decode $base64String
Write-Host $decodedString

