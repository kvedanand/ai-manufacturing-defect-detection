AI-Based Manufacturing Defect Detection System

Overview

An AI-powered manufacturing inspection project that uses computer vision and deep learning to identify surface defects in industrial components. The project aims to improve quality control, reduce manual inspection effort, and support automated visual inspection in manufacturing environments.

Objectives

Develop an automated visual inspection system for manufacturing components. Apply image processing techniques to industrial images. Build a deep learning model for surface defect classification. Evaluate model performance using appropriate classification metrics. Develop an interactive dashboard for image inspection. Explore applications of AI in manufacturing quality control.

Features

Current Features

Upload images of manufactured components. Resize and preprocess images. Display original and preprocessed images. Calculate basic image statistics. Provide an interactive inspection interface.

Planned Features

AI-based defect classification. Identification of different surface defect categories. Prediction confidence scores. Model evaluation using precision, recall, and F1-score. Inspection history and performance summaries. Interactive manufacturing quality inspection dashboard.

Note: The current prototype performs image preprocessing and basic image analysis. Reliable AI-based defect classification requires a trained and evaluated model.

Technologies Used

Python is the main programming language. OpenCV is used for image processing. NumPy supports numerical operations. Pillow handles image loading and manipulation. Streamlit provides the interactive web application. PyTorch will be used for deep learning model development. Git and GitHub support version control and project hosting.

Project Structure

```text
ai-manufacturing-defect-detection/
    app.py
    requirements.txt
    README.md
    .gitignore
    src/
        __init__.py
        preprocessing.py
    data/
        README.md
    models/
        README.md
```

Installation and Setup

Prerequisites

Python 3.10 or a compatible version, Git, and a code editor such as Visual Studio Code are required.

Step 1: Clone the Repository

```bash
git clone https://github.com/kvedanand/ai-manufacturing-defect-detection.git
```

Step 2: Navigate to the Project Directory

```bash
cd ai-manufacturing-defect-detection
```

Step 3: Create a Virtual Environment

```bash
python -m venv .venv
```

On Windows, activate the environment using:

```bash
.venv\Scripts\activate
```

On macOS or Linux, activate the environment using:

```bash
source .venv/bin/activate
```

Step 4: Install Dependencies

```bash
python -m pip install -r requirements.txt
```

Step 5: Run the Application

```bash
python -m streamlit run app.py
```

Open the local address displayed in the terminal to access the application.

How It Works

The system begins by accepting an image of a manufactured component. The image is resized and normalized during preprocessing. Once a suitable deep learning model has been trained, it will analyze visual patterns and classify components according to their surface condition. Model performance will be evaluated using labeled test images, and the results will be presented through an interactive interface.

The current prototype implements image uploading, preprocessing, basic image statistics, and visualization. Model training and reliable defect classification remain development tasks.

Potential Industrial Applications

The project may support automotive component inspection, metal surface quality inspection, manufacturing quality assurance, industrial component inspection, production-line visual inspection, and smart manufacturing systems. Its suitability for these applications will depend on the training data, model performance, and validation under realistic inspection conditions.

Model Evaluation

After training, the model will be evaluated using accuracy, precision, recall, F1-score, confusion matrix, and inference time. Recall is particularly important in manufacturing inspection because missed defects can have significant consequences. Evaluation will use held-out test images to assess performance on unseen samples.

Future Improvements

Future development will include training a deep learning model using a documented manufacturing defect dataset, supporting multiple defect categories, adding defect localization where supported by the model, generating inspection reports, improving inference speed, and exploring integration with industrial cameras and production-line systems.

Engineering Relevance

This project connects mechanical engineering with modern manufacturing technologies. It explores manufacturing processes, quality control, industrial automation, computer vision, artificial intelligence, and smart manufacturing. The project demonstrates how software and AI can support engineering inspection workflows.

Author

K. Vedanand

GitHub: https://github.com/kvedanand

Project Status

The project is in the initial prototype stage. Image preprocessing and basic image analysis are implemented. Deep learning model training, defect classification, and model evaluation are planned for subsequent development.

License

A license has not yet been selected. Licensing will be added after reviewing project requirements and dataset licensing obligations.
