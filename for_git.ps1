git init
git add .
git status
function Push {
    $message = Read-Host "Enter text message"
    git commit -m $message
    git status

    Write-Host "Press enter to continue"
    $key = $host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
    if ($key.VirtualKeyCode -eq 13) {

        Write-Host "REMOTE_REP:   git@github.com:grigoriy-st/YandexLyceum.git"
        Write-Host "------UPDATED-----"
        Write-Host "--------------SUCCESS--------------"
    }

    git push git@github.com:grigoriy-st/YandexLyceum.git
}

function Pull {
    Write-Host "LOCAL_REP:   git@github.com:grigoriy-st/YandexLyceum.git"
    git push git@github.com:grigoriy-st/YandexLyceum.git
    Write-Host "------UPDATED-----"
    Write-Host "--------------SUCCESS--------------"
}

$operation = Read-Host "Enter option:
1 - push
2 - pull
3 - merge"
switch ($operation) {
    1 { Push }
    2 { Pull}
    3 { Write-Host "merge is not found" }
    Default {Write-Host "ERROR"}
}

Start-Sleep -s 4