# Medical Image Processing Software Development Brief

## Project Overview

This project aims to develop a Windows-based desktop application for medical image processing. The primary functionalities include loading MRI and X-Ray images, manual and automated image overlay, and post-overlay editing features. This document outlines the key technologies, tools, and libraries required to set up the development environment.

## Core Technologies

- **Programming Language**: Python
- **GUI Framework**: PyQt5
- **Version Control**: Git
- **IDE**: MS Code
- **Development and Experimentation**: Jupyter Lab

## Required Libraries and Tools

### Core Libraries

1. **PyQt5**
    - **Purpose**: GUI development.
    - **Installation**: Included in `requirements.txt`

### Image Processing

1. **OpenCV**
    - **Purpose**: Handling image processing tasks.
    - **Installation**: Included in `requirements.txt`

2. **pydicom**
    - **Purpose**: Reading and writing DICOM files for MRI images.
    - **Installation**: Included in `requirements.txt`

3. **PIL (Pillow)**
    - **Purpose**: Basic image manipulation tasks.
    - **Installation**: Included in `requirements.txt`

### Scientific Computing

1. **NumPy**
    - **Purpose**: Numerical operations.
    - **Installation**: Included in `requirements.txt`

2. **SciPy (Optional)**
    - **Purpose**: Advanced scientific computing.
    - **Installation**: Included in `requirements.txt`

### File Handling

1. **os and shutil (Built-in)**
    - **Purpose**: File and directory manipulation.

### Future AI Capabilities

1. **TensorFlow or PyTorch**
    - **Purpose**: Implementing machine learning models.
    - **Installation**: Included in `requirements.txt`

2. **scikit-learn (Optional)**
    - **Purpose**: Simpler machine learning tasks.
    - **Installation**: Included in `requirements.txt`

### Testing

1. **pytest**
    - **Purpose**: Writing unit tests.
    - **Installation**: Included in `requirements.txt`

### Documentation

1. **Sphinx**
    - **Purpose**: Generating documentation.
    - **Installation**: Included in `requirements.txt`

## Environment Setup Steps

1. **Clone the Repository**: Clone the Git repository to your local machine.

2. **Create a Conda Environment**: Create a new Conda environment for the project.
    ```bash
    conda create --name myenv python=3.8
    ```

3. **Activate the Conda Environment**:
    ```bash
    conda activate myenv
    ```

4. **Install Required Libraries**: Install all required libraries from the `requirements.txt` file.
    ```bash
    pip install -r requirements.txt
    ```

5. **IDE Setup**: Open the project in MS Code and configure it to use the Conda environment you just created.

6. **Jupyter Lab Setup**: If you're using Jupyter Lab for development and experimentation, install it within your Conda environment.
    ```bash
    conda install -c conda-forge jupyterlab
    ```

7. **Run Jupyter Lab**: Navigate to your project folder and run Jupyter Lab.
    ```bash
    jupyter lab
    ```

---
