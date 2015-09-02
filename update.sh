#!/usr/bin/env bash
#
# Script which updates the python code of paiji
# and of all its dependencies and submodules before
# applying the changes to the static files,
# the translations and the database.
#
# cf. libupdate.sh or libupdate_example.sh

set -e

if [ -f "libupdate.sh" ]; then
	source libupdate.sh
	if [ "`whoami`" == ${WHO_I_MUST_BE} ]; then
		update_all && exit 0;
	else
		cat <<-EOF

		please login as "${WHO_I_MUST_BE}" before updating !
		e.g. :

		    sudo -su ${WHO_I_MUST_BE}

		EOF
	fi
else  # (no "libupdate.sh")
	cat <<-EOF

	no "libupdate.sh" found

	cf. "libupdate_example.sh"

	EOF
fi

exit 1;
