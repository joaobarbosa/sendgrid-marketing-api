#!/bin/bash

py.test --pep8 --cov=../sendgridmarketingapi --cov-report=term-missing -r a

printf "\n-- Up next: radon\n-- Press [ENTER] key to keep going...\n"
read

radon cc ../ -as --ignore=tests
