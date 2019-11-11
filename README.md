# DSP-Engine
Repository for the development of the Vibraneur DSP-Engine.

## Setup

A build script is provided to initialize a python virtual environment with all dependencies installed       
Note: Please ensure you habe python 3 installed on your local       
run `./scripts/init_venv.sh`

## unit test

    python3 -m unittest discover -s test -p '*.py'

## Deploy to AWS Lambda

A build script is provided to package all relevant file for AWS Lambda deployment       
Note: Please run script from project root level and ensure you have *zip* installed       

To build for Lambda package: run `./scripts/build_lambda.sh`        