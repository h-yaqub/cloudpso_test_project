#!/usr/bin/env bash


dropdb --host=db -U postgres cloudpso_test

createdb --host=db -U postgres -O postgres -E utf8 -T template0 cloudpso_test
