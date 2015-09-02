#!/usr/bin/env bash

export WHO_I_MUST_BE='lgd'
export VIRTUALENV_DIR='/home/lgd/.virtualenvs/paiji'
export REPOS_DIR='/home/lgd/dev/paiji-dep'

function update_packages {

cat << EOF

 #############################
 #     updating packages     #
 #############################

EOF

    echo
    echo "# updating requirements/prod.txt #"
    echo
    pip install -r requirements/prod.txt -U
    curdir=`pwd`
    cd "$REPOS_DIR"
    for dir in *; do
        if [ -d "$dir" ]; then
            cd "$dir"
            echo
            echo "# updating $dir #"
            echo
            git pull
            if [ -f "setup.py" ]; then
                pip install . -U
            fi
            cd ..
        fi
    done
    cd "$curdir"

} # function update_packages

function i18n {
cat << EOF

 #############################
 # translations compilations #
 #############################

EOF

python manage.py compilemessages

} # function i18n

function staticfiles {
cat << EOF

 ###########################
 # collecting static files #
 ###########################

EOF

echo 'yes' | python manage.py collectstatic
} # function staticfiles

function update_db {
cat << EOF

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

cat << EOF

 ##############
 # success  ! #
 ##############

EOF

} # function success

function workon_paiji {

    source "${VIRTUALENV_DIR}/bin/activate"

    echo
    echo '# use the `deactivate` command to leave this virtualenv #'
    echo

} # function workon_paiji

function update_all {
    workon_paiji
    update_packages
    update_project
    success
    deactivate
}
