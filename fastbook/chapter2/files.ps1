Get-ChildItem "$PWD" -Recurse -File | ForEach-Object {
    # Do something with the file size
    Write-Host "File: $($_.FullName), Size: $($_.Length)"
}