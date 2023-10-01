FILE_NAME=$(find ./xml -name "*$1*")
cat $FILE_NAME | tr -d '∣' | ./py/emit_pages.py > ./html/tmp.html
open -a Safari ./html/tmp.html
