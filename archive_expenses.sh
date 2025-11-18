#!/bin/bash

# set the archive path and log file
archives="archives"
log_files="archive_log.txt"

echo "Archiving Menu"
echo "1. Archiving file"
echo "2. Search for file"
echo "3. Exit the program"
read -p "choose 1-3: " user_input

if [ "$user_input" -eq 1 ]; then

    # check if the archive exist
    if [ ! -d "$archives" ]; then
        mkdir -p "$archives"
        echo "Dir Created"
    fi

    if ! ls expenses-*.txt 1> /dev/null 2>&1; then
        echo "There is no expenses file..."
        exit 0
    fi

    # archiving the file and register in the log file
    for expenses_file in expenses-*.txt; do
        if [ -f "$expenses_file" ]; then
            moving_dir=$(date +"%Y-%m-%d")
            mkdir -p "$archives/$moving_dir"
            mv "$expenses_file" "$archives/$moving_dir"
            echo "$expenses_file get archived in Time: $(date +%Y-%m-%d)" >> "$log_files"
            echo "the file $expenses_file sucesssful archived"
        else
            echo "there is error in the file $expenses_file"
        fi
    done

# searching
elif [ "$user_input" -eq 2 ]; then

    if [ ! -d "$archives" ]; then
        echo "The archiving dir does not exist"
        exit 0
    fi
    
    # check if log file exist 
    if [ ! -f "$log_files" ]; then
        touch "$log_files"
    fi

    read -p "enter the date in this format(YYYY-mm-dd) that you want to search for: " user_input_date
    if [[ ! "$user_input_date" =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}$ ]]; then
        echo "This date is invaild!"
        echo "You must enter on this format YYYY-mm-dd"
        exit 1
    fi

    if [ -d "$archives/$user_input_date" ]; then
        for search_file in "$archives/$user_input_date"/expenses-*.txt; do
            if [ -f "$search_file" ]; then
                echo "filename $(basename "$search_file")"
                echo "######"
                cat "$search_file"
                echo "######"
            else
                echo "NO file $search_file"
            fi
        done
    else
        echo "NO file with this date"
    fi
elif [ "$user_input" -eq 3 ]; then
    echo "Exit..."
    exit 0
else
    echo "You only chooose from this range [ 1-3 ]"
fi