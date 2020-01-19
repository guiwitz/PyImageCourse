#!/bin/bash

source activate improc_env

jupyter labextension install @jupyterlab/toc --no-build
jupyter labextension install @jupyter-widgets/jupyterlab-manager --no-build
jupyter labextension install ipyvolume --no-build
jupyter labextension install jupyter-threejs js --no-build

jupyter lab build