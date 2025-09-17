param(
    [string] = '127.0.0.1:8000'
)

 = Split-Path -Parent System.Management.Automation.InvocationInfo.MyCommand.Path
Set-Location 

 = Join-Path  '.venv\Scripts\Activate.ps1'
if (-not (Test-Path )) {
    Write-Error '???? .venv ??????????? python -m venv .venv ??????????'
    exit 1
}

. 

try {
    Write-Host "mkdocs serve --dev-addr "
    mkdocs serve --dev-addr 
}
finally {
    if (Get-Command 'deactivate' -ErrorAction SilentlyContinue) {
        deactivate
    }
}
