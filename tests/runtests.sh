#!/bin/bash

if [ -z ${SENDGRID_TEST_API_KEY+x} ]; then

    echo "Provide an API key for testing: "
    read apikey

    export SENDGRID_TEST_API_KEY=$apikey
fi

py.test --pep8 --cov=../sendgridmarketingapi --cov-report=term-missing -r a -v -s

printf "\n-- Up next: radon\n-- Press [ENTER] key to keep going...\n"
read

radon cc ../ -as --ignore=tests
