#!/bin/bash

protoc --go_out=. --go_opt=paths=source_relative --go-grpc_out=. --go-grpc_opt=paths=source_relative user_go.proto

go mod tidy

python -m venv .venv

export PYTHON_KEYRING_BACKEND=keyring.backends.null.Keyring

poetry install

python -m grpc_tools.protoc -I. --python_out=python --pyi_out=python --grpc_python_out=python user_go.proto
