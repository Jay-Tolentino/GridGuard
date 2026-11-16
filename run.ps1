
# Run GridGuard using its local Python environment

$python = Join-Path $PSScriptRoot ".venv\Scripts\python.exe"

if (-not (Test-Path $python)) {
    Write-Host "Virtual environment not found."
    Write-Host "Create it with: py -3.13 -m venv .venv"
    exit 1
}

Set-Location $PSScriptRoot

& $python -m streamlit run app.py --server.address 127.0.0.1
