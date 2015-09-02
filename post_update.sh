#!/usr/bin/env bash

function failure {

cat << EOF

 ###########
 # failure #
 ###########

EOF

exit 1;

}

cat << EOF

 #############################
 # translations compilations #
 #############################

EOF

python manage.py compilemessages || failure;

cat << EOF

 ###########################
 # collecting static files #
 ###########################

EOF

echo 'yes' | python manage.py collectstatic || failure;

cat << EOF

 ##########################
 # applying db migrations #
 ##########################

EOF

python manage.py makemigrations && python manage.py migrate || failure;

cat << EOF

 ##############
 # success  ! #
 ##############

EOF

exit 0;
