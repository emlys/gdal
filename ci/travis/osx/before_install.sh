#!/bin/sh

set -e

conda update -n base -c defaults conda
conda install -y compilers automake pkgconfig cmake

conda config --set channel_priority strict
conda install --yes --quiet proj swig lxml jsonschema numpy requests -y
conda install --yes --quiet libgdal=3.7.0=hc13fe4b_4  --only-deps -y
