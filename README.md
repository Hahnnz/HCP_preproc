# Human Connectome Project Preprocess Pipeline
<p align="center">
  <a href="https://www.humanconnectome.org/"><img src="./figures/HCP_logo.png" height=60% width=60%></a>
</p>

The HCP Pipelines product is a set of tools (primarily, but not exclusively, Python3) for processing MRI images for the [Human Connectome Project](https://www.humanconnectome.org/) using [Nipy](https://nipy.org/). Among other things, these tools implement the Minimal Preprocessing Pipeline (MPP)

This Repository is inspired and implemented by [HCPpipelines](https://github.com/Washington-University/HCPpipelines) of Washington-University. And it is based on workfolw made by [fMRIprep](https://fmriprep.readthedocs.io/en/stable/), which is very good tools to implement sMRI or fMRI preprocessing workflows.

## Preprocessing Pipeline Details
* **Gradient Unwrapping**
* **Motion Correction**
* **Fieldmap based EPI distortion correction**
* **brain-boundary based registration of EPI to structural T1-Weighted scan**
* **non-linear registration into MNI152 space**
* **grand-mean intensity normalization**


## Dependencies [Enviroment]
* **Python3** : `3.6.0`
