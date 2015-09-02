#!/usr/bin/env bash

set -e

if [ -f "libupdate.sh" ]; then
    source libupdate.sh
    if [ "`whoami`" == ${WHO_I_MUST_BE} ]; then
        update_all
        exit 0;
    else
        echo "please login as \"${WHO_I_MUST_BE}\" before updating !"
        echo
        echo "e.g. :"
        echo
        echo "      sudo -su ${WHO_I_MUST_BE}"
        echo
    fi
else
    echo 'no "libupdate.sh" found'
    echo 'cf. "libupdate_example.sh"'
    exit 1;
fi
