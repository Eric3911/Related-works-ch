#!/bin/bash -eu

output_path=$1

# Collect the locations of included files.
included_files=$(grep -Ern --include \*.md '^\[include \"(.*)\"\]$' ${PWD}/$output_path \
              | tac \
              | sed -E 's/(.*)\[include \"(.*)\"\]$/\1\2/g')

# Inline the contents of the included files.
for val in $included_files; do
    read -r file line include <<< $(echo $val | sed -E 's/^(.*)\:([0-9]+)\:(.*)$/\1 \2 \3/g')

    # Strip the title from any included files.
    if [[ $(head -1 $output_path$include) == '---' ]]; then
        tail -n +6 $output_path$include > "include.tmp" && mv "include.tmp" $output_path$include
    fi
    sed -e "$line {r $output_path$include" -e 'd' -e '}' "$file" > "$file.tmp" && mv -- "$file.tmp" "$file"
done

# Make sure the included files are removed after processing.
for val in $included_files; do
    rm "$output_path/$(echo $val | sed -E 's/^.*\:[0-9]+\:(.*)$/\1/g')" || true
done
