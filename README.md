# OBJECT DETECTION OF PPE (PERSONAL PROTECTICE EQUIPMENT)

---

In the construction, manufacturing and laboratory industries, the use of Personal Protective Equipment (PPE) is very important to maintain work safety. A system that can automatically recognize PPE use can help ensure that all workers comply with safety standards.

## Documentation of Dataset 📊

---

### Data Source

This dataset is obtained from Kaggle, an online platform that provides access to various datasets, competitions, and other resources in the field of data science and machine learning.

Source: [PPE Dataset - CCTV - Muhammad Fahmy](https://www.kaggle.com/datasets/muhfahmy/dataset-ppe-ex-cctv)

### Dataset Description

The dataset consists of a series of surveillance videos from various locations capturing everyday activities involving the usage of PPE. Each video is recorded using CCTV and captures various situations and conditions.

### Dataset Usage

This dataset can be used for various purposes, including:

1. Training object detection models to recognize the usage of PPE such as face masks,boots, vest, gloves, helmets and many more.
2. Analyzing compliance with PPE usage in public places, workplaces, or other areas recorded by CCTV.
3. Development and evaluation of image recognition and analysis algorithms for PPE usage compliance monitoring.

### License

The PPE dataset from CCTV is available under the license provided by Kaggle. Be sure to read and understand the terms of the license before using this dataset for your project.

## How to run the application 🚀

---

This section will explain how to explain the lines of code in the listed repository

#### Running Project

1. **Clone the Repository :** Clone the project repository from GitHub to your local machine using the following command:

   ```python
   git clone https://github.com/binerbard/synapsis_challenge_AIEngineer.git
   ```

2. **Navigate to the Project Directory :** Change your current directory to the root directory of the cloned project:
   ```python
   cd synapsis_challenge_AIEngineer
   ```
3. **Install Dependencies:** If the project requires any dependencies, install them using the appropriate package manager. For example, if the project uses Python, you can install dependencies using pip:

   ```python
   pip install -r requirements.txt
   ```

4. **Run the Project:** Execute the main script or application of the project. Depending on the project, this may involve running a Python script.

> **DETECTION OBJECT FROM IMAGE**
>
> ```python
> python setup.py --media=image --src="source image path"
> ```
>
> **Example**
>
> ```python
> python setup.py --media=image --src=./example/images/download. jfif
> ```
>
> ---
>
> **DETECTION OBJECT FROM VIDEO**
>
> ```python
> python setup.py --media=video --src="source video path"
> ```
>
> **Example**
>
> ```python
> python setup.py --media=image --src=./example/video/hardhat.mp4
> ```

5. **Follow Instructions:** Follow any on-screen instructions or documentation provided with the project to interact with or utilize its features.

   ```python
   python setup.py --help
   ```

### Additional Notes

Ensure that you have the necessary software and environment set up to run the project. Refer to any prerequisites or system requirements mentioned in the project documentation.
If you encounter any issues or have questions about running the project, refer to the project's README file or documentation for troubleshooting tips and guidance.

## Example Resource

---

### Sample 1

![IMAGE 1](https://github.com/binerbard/synapsis_challenge_AIEngineer/example/resource/download.png)

### Sample 2

![IMAGE 1](https://github.com/binerbard/synapsis_challenge_AIEngineer/example/resource/sample2.png)
