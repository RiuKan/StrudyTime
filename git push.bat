git add *
setlocal
set /p str= 메시지 입력:
git commit -m %str%
git push