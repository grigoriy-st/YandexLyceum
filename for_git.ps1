git init
git add .
git status
$message = Read-Host "Enter text message"
git commit -m $message
git status

Write-Host "Press enter to continue"
$key = $host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
if ($key.VirtualKeyCode -eq 13) {

    Write-Host "КREP:   git@github.com:grigoriy-st/YandexLyceum.git"
    Write-Host "\n\n------UPDATED-----\n\n"
}

git push git@github.com:grigoriy-st/YandexLyceum.git

Write-Host "--------------SUCCESS--------------"
Start-Sleep -s 4