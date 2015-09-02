#!/usr/bin/env bash

set -e

if [ -f "libupdate.sh" ]; then
    source libupdate.sh && update_all
    exit 0;
else
    echo 'no "libupdate.sh" found'
    echo 'cf. "libupdate_example.sh"'
    exit 1;
fi
