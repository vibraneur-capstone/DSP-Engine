#!/bin/bash

dist_name="dsp-aws-lambda-dist.zip"
dep_target_path="external_libraries"

echo "build start"

sleep 1

rm $dist_name
rm -rf $dep_target_path

printf "\nInstall dependency \n"
sleep 3

python3 -m pip install -r requirements.txt --target $dep_target_path

printf "\nPackaging dependency \n"
sleep 3

cd $dep_target_path || exit

#zip -g -r $dist_name $dep_target_path/*

zip -r9 ${OLDPWD}/$dist_name .

cd ${OLDPWD} || exit

printf "\nPackaging project modules \n"
sleep 3
zip -g -r $dist_name src/*

printf "\nCleaning up \n"
rm -rf $dep_target_path

printf "\nFinished Building \n"
