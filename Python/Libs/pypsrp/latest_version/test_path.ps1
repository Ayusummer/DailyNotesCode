$path = "C:\Users\233PC\Documents\test"
if (Test-Path -Path $path) {
    Remove-Item -Path $path -Force -Recurse
}
New-Item -Path $path -ItemType Directory