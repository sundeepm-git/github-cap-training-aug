#!/bin/bash
# Find all .txt files and count lines in each
find . -type f -name "*.txt" -print0 | while IFS= read -r -d '' file; do
    wc -l "$file"
done