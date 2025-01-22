
#Plant Disease Prediction System

This project is an AI-driven system for predicting plant diseases using a trained TensorFlow model. The system uses Streamlit for the web interface and TensorFlow for the machine learning model.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Project Structure](#project-structure)
6. [Model Training](#model-training)
7. [Contributing](#contributing)
8. [License](#license)

## Project Overview
The Plant Disease Prediction System is designed to help farmers and agricultural experts identify plant diseases from images. The system uses a convolutional neural network (CNN) model trained on a dataset of plant images.

## Features
- Web-based interface using Streamlit
- TensorFlow model for disease prediction
- Easy-to-use interface for uploading images and getting predictions

## Installation

### Prerequisites
- Python 3.6 or higher
- Git

### Steps
1. **Clone the repository:**
    ```sh
    git clone <repository-url>
    cd Plant_Disease_Prediction
    ```

2. **Create a virtual environment:**
    ```sh
    python -m venv myenv
    ```

3. **Activate the virtual environment:**
    - On Windows:
        ```sh
        myenv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source myenv/bin/activate
        ```

4. **Install the required packages:**
    ```sh
    pip install -r requirement.txt
    ```

## Usage
1. **Run the Streamlit application:**
    ```sh
    streamlit run main.py
    ```

2. **Navigate to the Streamlit web interface:**
    Open your web browser and go to [http://localhost:8501](http://_vscodecontentref_/1).

3. **Upload an image:**
    Use the interface to upload an image of a plant leaf.

4. **Get the prediction:**
    The system will display the predicted disease based on the uploaded image.

## Project Structure
Plant_Disease_Prediction/ │ ├── .idea/ │ ├── .gitignore │ ├── inspectionProfiles/ │ ├── misc.xml │ ├── modules.xml │ ├── Plant_Disease_Prediction.iml │ └── workspace.xml ├── .streamlit/ │ └── secrets.toml ├── myenv/ │ ├── Include/ │ ├── Lib/ │ ├── pyvenv.cfg │ └── Scripts/ ├── ppt/ │ └── NRCS.pptx ├── test/ │ └── ... ├── train/ │ ├── Train_plant_disease.ipynb │ ├── trained_model.keras │ ├── trained_plant_disease_model.keras │ └── training_hist.json ├── valid/ ├── main.py ├── readme.txt ├── requirement.txt └── runcode.txt



## Model Training
To train the model, follow these steps:

1. **Prepare the dataset:**
    Ensure you have a dataset of plant images categorized by disease.

2. **Run the training script:**
    Open the [Train_plant_disease.ipynb](http://_vscodecontentref_/2) notebook and run all cells to train the model.

3. **Save the trained model:**
    The trained model will be saved as [trained_model.keras](http://_vscodecontentref_/3).
## Gemini API Key Setup
To use the Gemini API, you need to create an API key and save it in the appropriate location.

### Steps to Create an API Key
1. **Sign up or log in to Gemini:**
    Go to the Gemini website and sign up for an account or log in if you already have one.

2. **Create an API key:**
    Navigate to the API section in your account settings and create a new API key. Make sure to note down the API key and secret.

### Save the API Key
1. **Create a [.streamlit](http://_vscodecontentref_/3) directory:**
    If it doesn't already exist, create a [.streamlit](http://_vscodecontentref_/4) directory in the root of your project.

2. **Create a `secrets.toml` file:**
    Inside the [.streamlit](http://_vscodecontentref_/5) directory, create a file named `secrets.toml`.

3. **Add your API key to `secrets.toml`:**
    Open the `secrets.toml` file and add the following content:
    ```toml
    [gemini]
    api_key = "your_api_key"
    api_secret = "your_api_secret"
    ```
    ,

## follow this video for full understanding 
https://youtu.be/TRo9EpnE7AI?si=jjlN92PKxAgWrOw7

##download this files
https://drive.google.com/file/d/1OK9jIeN8ErK-5sWHYvrsS9La2JNldMcL/view


## Contributing
Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License
This project is licensed under the MIT License.

