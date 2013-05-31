#!/bin/bash

# TODO
# add usage (if argv < 3)
# change defaults

TIME_LIMIT=${1:-3600}
MESSAGE_RECIPIENTS=${2:-martin@martindengler.com,mary@marydengler.com,marydengler@yahoo.com}
MESSAGE_SUBJECT=${3:-operation started}

MESSAGE_TEXT=${MESSAGE_TEXT:-$MESSAGE_SUBJECT}

TEST_FILE=${TEST_FILE:-~/.bash_history}
TEST_INTERVAL=${TEST_INTERVAL:-10}

touch $TEST_FILE

while [ $(expr $(date +%s) - $(stat --format %Y $TEST_FILE)) -lt $TIME_LIMIT ]; do
    sleep $TEST_INTERVAL
done

echo $MESSAGE_TEXT | mail -s "$MESSAGE_SUBJECT" "$MESSAGE_RECIPIENTS"



