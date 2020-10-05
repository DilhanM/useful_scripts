# delete the char at position=7 of all files starting with name U_*
# tested on bash

position=7

for f in U_*; do
   mv -- "$f" "${f:0:$position-1}${f:$position}"
done

# Credits and link to original code at https://unix.stackexchange.com/questions/399814/how-to-remove-nth-character-from-set-of-filenames
