[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/guiwitz/PyImageCourse/master)

## 1. Installation

- Clone or download this repository.
- Open a terminal and ```cd``` to it.
- Create the conda environment by typing:

  ```bash
  conda env create -f binder/environment.yml
  ```
  
- Activate the conda environment by typing:
    ```bash
    conda activate improc_env
    ```
    
- Download the data by typing:

  ```bash
  python installation/download_data.py
  ```

## 2. Exploring the PyImageCourse

Whenever you want to run a course notebook, first activate the environment:

```bash
conda activate improc_env
```

or if that doesn't work try:

```bash
source activate improc_env
```

Then start a Jupyter instance and move to the course folder:

```bash
jupyter notebook
```
