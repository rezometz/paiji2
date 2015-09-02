#!/usr/bin/env bash
#
# Little bash library to manage the deployement
# of the paiji (and its submodules) python code.
#
# It reads the "settings.sh" file which must be
#  set. cf. "settings_example.sh"
#
# Used by "update.sh" to automatically update
# the paiji website.
#
# Please verify the parameters below.
#
# (manual) usage :
#
#		source libupdate.sh
#
# first, to work on the python virtualenv:
# 
#		workon_paiji
#
# then:
#
#		[what you want…]
#
# finally, to leave the python virtualenv:
#
#		deactivate

set -e

SETTINGS='settings.sh'
if [ -f "$SETTINGS" ]; then
	source "$SETTINGS"
else
	cat <<-EOF

	Please set the parameters described
	in "settings_example.sh" in "${SETTINGS}"

	EOF
	exit 1;
fi


function update_packages {
	cat <<-EOF

	 #############################
	 #     updating packages     #
	 #############################

	EOF

	echo -e "\n# updating requirements/prod.txt #\n"
	pip install -r requirements/prod.txt -Uq

	curdir=`pwd`
	cd "$REPOS_DIR"
	for dir in *; do
		if [ -d "$dir" ]; then
			cd "$dir"

			echo -e "\n# updating $dir #\n"
			echo '# running git pull…'
			git pull
			if [ -f "setup.py" ]; then
				echo "# running pip install ${dir}…"
				pip install . -Uq
			fi

			cd ..
		fi
	done
	cd "$curdir"
} # function update_packages


function i18n {
	cat <<-EOF

	 #############################
	 # translations compilations #
	 #############################

	EOF
	python manage.py compilemessages
} # function i18n


function staticfiles {
	cat <<-EOF

	 ###########################
	 # collecting static files #
	 ###########################

	EOF
	python manage.py collectstatic --noinput
} # function staticfiles


function update_db {
	cat <<-EOF

	 ##########################
	 # applying db migrations #
	 ##########################

	EOF
	python manage.py makemigrations && python manage.py migrate
} # function update_db


function update_project {
	git pull
	i18n
	staticfiles
	update_db
} # function update_project


function success {
	cat <<- EOF

	 ##############
	 # success  ! #
	 ##############

	EOF
} # function success


function workon_paiji {
	source "${VIRTUALENV_DIR}/bin/activate"
	echo -e "\n# use the \"deactivate\" command to leave this virtualenv #\n"
} # function workon_paiji


function update_all {
	workon_paiji
	update_packages
	update_project
	success
	deactivate
} # function update_all
