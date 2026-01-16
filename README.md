# 🎧 Mood-Based Music Recommendation System

A simple and interactive **Flask-based web application** that recommends songs based on the user’s mood.  
This micro-project was developed as part of a **college subject** to demonstrate backend–frontend integration using Python and Flask.

---

## 🌐 Live Demo
🔗 **Live Application:**  
https://mood-based-music-recommendation-system-pdfs.onrender.com/

> ⚠️ Note: The application is hosted on Render (Free Tier).  
> The first request may take some time due to server cold start.

---

## 📌 Project Overview

The Mood-Based Music Recommendation System allows users to:
- Select a mood (Happy, Sad, Energetic, Calm)
- Get song recommendations matching the selected mood
- Search recommended songs directly on YouTube

The system reads music data from a CSV file and dynamically recommends songs using backend logic.

---

## 🛠️ Technologies Used

- **Backend:** Python, Flask  
- **Frontend:** HTML, CSS, Bootstrap  
- **Data Handling:** Pandas  
- **Deployment:** Render  
- **Version Control:** Git & GitHub  

---

## 🗂️ Project Structure
MRS/
│── app.py
│── mood_tracks.csv
│── process_dataset.py
│── requirements.txt
│
├── templates/
│ └── index.html
│
└── static/
└── style.css

---

## ⚙️ How It Works

1. User selects a mood from the dropdown menu.
2. A POST request is sent to the Flask backend.
3. Flask filters the dataset (`mood_tracks.csv`) using Pandas.
4. Random song recommendations are generated.
5. Results are displayed dynamically on the webpage.
6. Users can search any recommended song on YouTube with one click.

---

## 🚀 How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/apurmusandi/MRS.git
   cd MRS
2. Install dependencies:

3. pip install -r requirements.txt


4. Run the application:

python app.py


5. Open browser and visit:

http://127.0.0.1:5000

📚 Learning Outcomes

Understanding Flask routing and request handling

Integrating frontend with backend

Using Pandas for data filtering

Deploying Python web apps on cloud platforms

Managing dependencies using requirements.txt

👨‍🎓 Academic Information

Project Type: Micro Project

Guide: Prof. P. B. Patil

Developed By: Apurv M.

Course: B.Tech (CSE)

📄 License

This project is created for educational purposes only.

---


