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

# Credits

simCataloguer was developed by [Dreaming Spires Software Development Ltd](https://dreamingspires.dev/
) in 2023.

For more details of the type of projects we develop, please contact contact@dreamingspires.dev or visit [dreamingspires.dev](https://dreamingspires.dev/).
