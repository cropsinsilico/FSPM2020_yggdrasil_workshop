# FSPM2020_yggdrasil_workshop
Materials for the FSPM2020 yggdrasil workshop

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/cropsinsilico/FSPM2020_yggdrasil_workshop/master)

References:

["Plant-2"](https://sketchfab.com/3d-models/plants-2-f4636a80dcec4ca9a29f52fa32182721) by [FALCON](https://sketchfab.com/qewr1324) is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), converted into .obj format with texture and grouping removed.

## Running Notebook Locally

### Download:
git clone https://github.com/cropsinsilico/FSPM2020_yggdrasil_workshop.git
cd FSPM2020_yggdrasil_workshop

### Set up environment:
conda env create -f environment.yml
conda activate fspm-yggdrasil-environment

### Finish Installing yggdrasil (linux/mac):
source postBuild

### Finish Installing yggdrasil (windows):
call postBuild.bat

### Run notebook:
jupyter notebook
