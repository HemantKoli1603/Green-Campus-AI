Green Campus AI – Waste Classification System

Green Campus AI is a Streamlit-based Machine Learning web application that uses a trained image classification model to identify different types of waste and suggest the correct waste bin.
The goal of this project is to promote smart waste segregation using AI and simple web technology.


🚀 Project Overview
This project allows users to:
1.Capture an image of waste using a camera
2.Classify the waste using a trained ML model (Teachable Machine / Keras)
3.Identify the type of waste (Plastic, Paper, Organic.)
4.Get guidance on which bin color the waste should go into
5.Interact with an AI assistant (Gemini) for short, clean explanations

How the Project Works (Flow)
1.User opens the Streamlit web app
2.User captures an image using the camera
3.Image is resized and normalized
4.Image is passed to the trained Keras model
5.Model predicts the waste category
6.The result is displayed on the UI
7.Gemini AI explains the correct bin in one sentence
<img width="1043" height="900" alt="image" src="https://github.com/user-attachments/assets/e2766827-42a9-49f6-92fc-c2e26b535547" />
Detailed diagram of our projects work cycle



🛠️ Technologies Used
Technology	Purpose
Python	Core programming language
Streamlit	Frontend web interface
TensorFlow / Keras	Loading and running ML model
NumPy	Image preprocessing and array operations
Pillow (PIL)	Image handling and resizing
Google Gemini API	AI-based explanation
Teachable Machine	Model training

📁 Project Structure
Green-Campus-AI/
│
├── app.py                 # Main Streamlit application
├── keras_model.h5         # Trained ML model
├── requirements.txt       # Required libraries
├── .gitignore             # Ignored files & folders
├── .streamlit/
│   └── secrets.toml       # API keys 
└── README.md              # Project documentation

📷 Model Input Details
Image size: 224 × 224
Color format: RGB (3 channels)
Pixel values normalized between 0.0 – 1.0
Input shape expected by model:
(None, 224, 224, 3)

⚙️ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/your-username/Green-Campus-AI.git
cd Green-Campus-AI

2️⃣ Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate   

3️⃣ Install dependencies
pip install -r requirements.txt

🔐 API Key Setup (Important)
Create a file:
.streamlit/secrets.toml

Add:
GEMINI_API_KEY = "your_api_key_here"
⚠️ This file is ignored using .gitignore for security.

▶️ Run the Application
streamlit run app.py

The app will open in your browser 🚀
🎯 Example Output
Prediction: Plastic
AI Response: “This waste should be disposed of in the blue bin.”
Visual UI feedback using Streamlit
<img width="1066" height="662" alt="image" src="https://github.com/user-attachments/assets/f7afec89-6f49-4de5-8fd0-b9bfeacaf421" />
Working



🌱 Future Improvements
Add more waste categories
Improve model accuracy with more training data
Add multilingual support
Deploy on Streamlit Cloud
Add dataset upload feature

📌 Learning Outcomes
Integrating ML models with frontend
Understanding image preprocessing
Using Streamlit for rapid prototyping
Handling API keys securely
Deploying AI applications for free

👨‍💻 Author

Hemant Koli
AI & Machine Learning
📌 Built with learning-first approach

⭐ Acknowledgements
Google Teachable Machine
Streamlit Community
TensorFlow & Keras
Google Gemini API

You can try it here - https://green-campus-ai.streamlit.app/
