#!/bin/bash

requirements_file_path="requirements.txt"

if [ -e $requirements_file_path ];
then
  echo "Initializing Venv..."

  pip install -r requirements.txt
else
  echo "$requirements_file_path does not exist"
fi

example_env_file_path=".env.example"

if [ -e $example_env_file_path ];
then
  cp $example_env_file_path ".env"
else
  echo "$example_env_file_path does not exist"
fi