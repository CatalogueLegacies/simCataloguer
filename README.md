# simCataloguer

simCataloguer is a workflow for generating machine-authored text and images from catalogue data. It was created in 2023 as part of the [Arts and Humanities Research Council](https://www.ukri.org/councils/ahrc/) (AHRC) funded project '[Legacies of Catalogue Descriptions and Curatorial Voice: Opportunities for Digital Scholarship](https://cataloguelegacies.github.io/).'

# Setup

This process assumes assumes familiarity with Windows Powershell.

## System Requirements

Please note that you may require a large amount of VRAM to use this library. Data we have gathered so far: 8Gb is not enough but 24Gb is sufficient.

## Installation

### Clone repo

`git clone --recursive git@github.com:dreamingspires/simCataloguer.git`

### Optional steps

You may need to install zlib, and graphics driver

- get [NVIDIA GPU Computing Toolkit, CUDA 11.7.0](https://developer.nvidia.com/cuda-11-7-0-download-archive)
- get [cuDNN](https://developer.nvidia.com/rdp/cudnn-download).
- install [cuDNN](https://docs.nvidia.com/deeplearning/cudnn/install-guide/index.html).

### Installations

- install [python 3.9](https://www.python.org/downloads/release/python-3913/).
- install [pip](https://pip.pypa.io/en/stable/installation/) (may not be required, check with pip --version)
- install [Poetry](https://python-poetry.org/docs/#installation).
- add poetry to path using on screen instructions.
- reboot shell.
- check with poetry --version.
- run `poetry config virtualenvs.in-project true`.
- `poetry install` (You may need to run this more than once, it fails to parallel process on occasion)
- `poetry run pip install --extra-index-url https://download.pytorch.org/whl/cu117 --no-deps --force-reinstall torch torchvision`

## Run test

- Go into your `examples` directory within `simCataloguer` and run `poetry run python test_writer.py`'

## Notes

- You can adjust `num_cuts` and `quality` settings in `examples/test_writer` depending on the GPU size of your local machine. See the [Pixray documentation](https://dazhizhong.gitbook.io/pixray-docs/docs/primary-settings) for details.
- When you first run `poetry run python test_writer.py` a language model will be built based on the input file in `examples/test_writer`. If this process fails, you may need to download a pre-trained model. For `MDG.txt` a [pre-trained model is available to download here](https://drive.google.com/file/d/1lqEbEo_VMOuAfCvnZ220Z-Wb7GfsE3lA/view?usp=sharing). This should be unzipped and placed at `simCataloguer/checkpoint`.
- When you first run `poetry run python test_writer.py`, four large files will be downloaded to `simCataloguer/.venv/Lib/site-packages/pixray_module/models`. If the downloads fail for any reason, then rerunning `poetry run python test_writer.py` will fail. If this happens four files - `yfcc_2.pth`, `ViB-32.pt`, `ViT-B-16.pt`, and `RN50,pt` can be downloaded seperately and manually placed in this directory. As `yfcc_2.pth` is the largest and most likely to fail, we include a [direct download link here](https://the-eye.eu/public/AI/models/v-diffusion/yfcc_2.pth).

# Reuse

[BM-MDG.zip](https://github.com/CatalogueLegacies/antconc.github.io/blob/gh-pages/data/BM-MDG.zip) is derived from a dataset [published by the British Museum](https://www.britishmuseum.org/about_this_site/terms_of_use/copyright_and_permissions.aspx), data and derived data are licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/) [license](https://github.com/CuratorialVoice/data/blob/master/README.md).

For more info on this dataset see Baker, James, & Salway, Andrew. (2019, June 13). Creation of the BMSatire Descriptions corpus (Version v1.0). Zenodo. doi: [10.5281/zenodo.3245037](http://doi.org/10.5281/zenodo.3245037).

# Credits

simCataloguer was developed by [Dreaming Spires Software Development Ltd](https://dreamingspires.dev/
) in 2023.

For more details of the type of projects we develop, please contact contact@dreamingspires.dev or visit [dreamingspires.dev](https://dreamingspires.dev/).
