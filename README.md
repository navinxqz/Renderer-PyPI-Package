# Renderer-PyPI-Package

This repo contains the source code for the Renderer package, which is available on PyPI. The Renderer package provides tools and utilities for rendering youtube videos and any web page over the jupyter notebook/colab and visualization in Python applications.

# How to run the package
1. Create a virtual environment:
   ```bash
   conda create -n renderer python=3.8 -y 
   ```
   or to create in a specific path:
   ```bash
    conda create -p ./envs/renderer python=3.8 -y 
    ```
2. Activate the virtual environment:
   ```bash
    conda activate renderer
    ```
    or if created in a specific path:
    ```bash
    conda activate ./envs/renderer
    ```
3. Install the required packages:
    ```bash
    pip install -r requirements_dev.txt
    ```