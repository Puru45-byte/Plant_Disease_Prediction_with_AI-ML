import streamlit as st
import tensorflow as tf
import numpy as np
import requests
import asyncio
import sys

# Fix for RuntimeError: Event loop is closed (Windows + Python 3.8)
if sys.platform.startswith('win') and sys.version_info < (3, 9):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# TensorFlow Model Prediction
def model_prediction(test_image):
    try:
        model = tf.keras.models.load_model("trained_plant_disease_model.keras")
    except Exception as e:
        st.error(f"Error loading the model: {e}")
        return None

    try:
        image = tf.keras.preprocessing.image.load_img(test_image, target_size=(128, 128))
        input_arr = tf.keras.preprocessing.image.img_to_array(image)
        input_arr = np.array([input_arr])  # Convert single image to batch
        predictions = model.predict(input_arr)
        result_index = np.argmax(predictions)
        return result_index
    except Exception as e:
        st.error(f"Error processing the image: {e}")
        return None

# Function to fetch disease information using Gemini API
def fetch_disease_info_gemini(disease_name, gemini_api_key):
    endpoint = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"
    query = f"What are the causes, symptoms and management tips for {disease_name} plant disease?"
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "contents": [{
            "parts": [{
                "text": query
            }]
        }],
        "generationConfig": {
            "maxOutputTokens": 500,
            "temperature": 0.9
        }
    }

    params = {"key": gemini_api_key}

    try:
        response = requests.post(endpoint, headers=headers, json=payload, params=params)
        st.subheader(f"Information about {disease_name}:")

        if response.status_code == 200:
            data = response.json()
            candidates = data.get("candidates", [])

            if candidates:
                for candidate in candidates:
                    parts = candidate.get("content", {}).get("parts", [])
                    for part in parts:
                        st.write(part.get("text", "No detailed text available"))
                        st.write("---")
            else:
                st.write(f"No detailed information found for {disease_name}.")
        else:
            st.error(f"Failed to fetch information from Gemini API. Status code: {response.status_code}")
    except Exception as e:
        st.error(f"Error connecting to the Gemini API: {e}")

# Sidebar
st.sidebar.title("Dashboard")
app_mode = st.sidebar.selectbox("Select Page", ["Home", "About", "Disease Recognition"])

# Main Page
if app_mode == "Home":
    st.header("AI Driven Crop Prediction and Management System")
    image_path = "home_page.jpeg"
    st.image(image_path, use_container_width=True)
    st.markdown("""
    AI Driven Crop Disease Prediction System!

    Our mission is to help in identifying plant diseases efficiently. Upload an image of a plant, and our system will analyze it to detect any signs of diseases. Together, let's protect our crops and ensure a healthier harvest!

    ### How It Works
    1. **Upload Image:** Go to the **Disease Recognition** page and upload an image of a plant with suspected diseases.
    2. **Analysis:** Our system will process the image using advanced algorithms to identify potential diseases.
    3. **Results:** View the results and recommendations for further action.

    ### Get Started
    Click on the **Disease Recognition** page in the sidebar to upload an image and experience the power of our AI Driven Crop Disease Prediction System!

    ### About Us
    Our Team\n
    ### Pushkar Patil.\n
    """)

# About Project
elif app_mode == "About":
    st.header("About")
    st.markdown("""
                ### About me 
                
                Hi, I’m **Pushkar Patil**, currently pursuing my engineering degree with a passion for technology and innovation. I’m dedicated to learning, growing, and applying my skills to solve real-world problems. My journey is driven by curiosity, a strong work ethic, and a commitment to building a brighter future through engineering solutions.
                #### About Dataset
                This dataset is recreated using offline augmentation from the original dataset. The original dataset can be found on this github repo.
                This dataset consists of about 87K RGB images of healthy and diseased crop leaves, categorized into 38 different classes. The total dataset is divided into an 80/20 ratio of training and validation sets, preserving the directory structure.
                A new directory containing 33 test images was created later for prediction purposes.
                #### Content
                1. train (70295 images)
                2. test (33 images)
                3. validation (17572 images)
                """)

# Prediction Page
elif app_mode == "Disease Recognition":
    st.header("Disease Recognition")
    st.markdown("""Capture Image 📷  """)

    # Toggle button for camera
    if 'camera_on' not in st.session_state:
        st.session_state.camera_on = False

    if st.button("Toggle Camera"):
        st.session_state.camera_on = not st.session_state.camera_on

    # Camera input feature
    camera_image = None
    if st.session_state.camera_on:
        camera_image = st.camera_input("Take a picture", key="camera")

    # File uploader feature
    test_image = st.file_uploader("Choose an Image 📁", type=["jpg", "jpeg", "png"])

    # Select the input source for prediction
    input_image = None
    if camera_image is not None:
        input_image = camera_image
    elif test_image is not None:
        input_image = test_image

    # Predict button
    if input_image is not None and st.button("Predict"):
        st.snow()
        st.write("Our Prediction")
        result_index = model_prediction(input_image)
        if result_index is not None:
            # Reading Labels
            class_name = ['Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy',
                          'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew',
                          'Cherry_(including_sour)___healthy', 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
                          'Corn_(maize)___Common_rust_', 'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy',
                          'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
                          'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot',
                          'Peach___healthy', 'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy',
                          'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy',
                          'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew',
                          'Strawberry___Leaf_scorch', 'Strawberry___healthy', 'Tomato___Bacterial_spot',
                          'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold',
                          'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite',
                          'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus',
                          'Tomato___healthy']
            predicted_disease = class_name[result_index]
            st.success(f"Model is Predicting it's a {predicted_disease}")

            # Fetch and display disease information using Gemini API
            gemini_api_key = st.secrets.get("gemini_api_key")  # Store your API key in a variable
            if gemini_api_key:
                fetch_disease_info_gemini(predicted_disease, gemini_api_key)
            else:
                st.error("Gemini API key is not set in secrets.")