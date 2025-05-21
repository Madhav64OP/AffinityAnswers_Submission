#!/bin/bash

URL="https://www.amfiindia.com/spages/NAVAll.txt"

curl -s "$URL"  -o nav_raw.txt

output_file="nav_data.tsv"
> "$output_file"


while IFS= read -r line; do
    if [[ "$line" != *";"* ]]; then
        continue
    fi

    scheme=$(echo "$line" | cut -d ';' -f 4) 
    rate=$(echo "$line" | cut -d ';' -f 5) 

    echo -e "$scheme\t$rate" >> "$output_file"
done < nav_raw.txt

echo "Data has been extracted and saved to $output_file"

