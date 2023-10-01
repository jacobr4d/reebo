
FILE_NAME=$(find ./xml -name "*${2}*")
cat $FILE_NAME | tr -d '∣' | ./py/"${1}".py > ./html/tmp.html
open -a Safari ./html/tmp.html
