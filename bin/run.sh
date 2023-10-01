
FILE_NAME=$(find ./xml -name "*${2}*")
cat $FILE_NAME | \
tr -d '∣' | \
tr -d '¦' | \
tr '▪' ',' | \
./py/"${1}".py > \
./html/tmp.html
open -a Safari ./html/tmp.html
