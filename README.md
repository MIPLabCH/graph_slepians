# Graph Slepians and Fiddlers

Python version for [code](https://codeocean.com/capsule/5202042/tree). Other in-house [softwares](https://miplab.epfl.ch/index.php/software) are offered by the group. 
Alternative Documentation: 

## Requirements

Our requirements are listed in `requirements.txt`

* Unix is supported, but we mostly used Mac OS.
* 64-bit Python 3.8.10 is the version we use (or later version can be used).
* CUDA toolkit 11.1 or later.
* Python libraries: see [requirements.txt](./requirements.txt) for exact library dependencies. You can use the following
  commands with Miniconda3 to create and activate your `graph_slepians` Python environment:
    - `conda create -n "graph_slepians" python=3.8.13`
    - `conda activate graph_slepians`
    - `<PATH TO YOUR CONDA PYTHON EXEC> python -m pip install -r requirements.txt`

* Docker users:
    - Ensure you have correctly installed
      the [NVIDIA container runtime](https://docs.docker.com/config/containers/resource_constraints/#gpu).
    - Use the [Dockerfile](./Dockerfile) to build an image with the required library dependencies.

## Acknowledgement


Dimitri Van De Ville, Robin Demesmaeker, Maria Giulia Preti (2017) Graph Slepians [Source Code]. https://doi.org/10.24433/CO.30374eaf-4b20-4124-97f4-7cef4658c4fd

Van De Ville, Dimitri, Robin Demesmaeker, and Maria Giulia Preti. "When Slepian Meets Fiedler: Putting a Focus on the Graph Spectrum". IEEE Signal Processing Letters 24.7 (2017): 1001-1004
