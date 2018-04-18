#!/bin/bash

NAME="lambda-test1"
pushd src
zip -r ../dist/${NAME}.zip ./* 

aws --help
