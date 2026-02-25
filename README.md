# 🎯 Face Recognition Attendance System

A smart attendance system that uses **face recognition** to automatically mark attendance in real time.  
This project eliminates manual attendance, improves accuracy, and prevents proxy attendance by identifying individuals through a webcam.

---

## 🚀 Features

✅ Real-time face detection using webcam  
✅ Face recognition using trained dataset  
✅ Automatic attendance marking  
✅ Stores attendance with date & time  
✅ Duplicate entry prevention  
✅ CSV/Excel attendance report generation  
✅ Simple and user-friendly interface  

---

## 🛠️ Tech Stack

- Python  
- OpenCV  
- NumPy  
- Pandas  
- face_recognition library  
- Tkinter (for GUI – optional)  

---

## 📂 Project Structure

Face-Recognition-Attendance-System
│── dataset/ → Stored face images
│── trainer/ → Trained model
│── attendance/ → Attendance CSV files
│── images/ → Registered user images
│── haarcascade_frontalface_default.xml
│── train_model.py → Train the dataset
│── mark_attendance.py → Recognize face & mark attendance
│── register_face.py → Capture new face
│── main.py → Run the system


---

## ⚙️ How It Works

1️⃣ Capture face images and store them in the dataset  
2️⃣ Train the model using the captured images  
3️⃣ Run the recognition system  
4️⃣ System detects the face in real time  
5️⃣ Attendance is marked automatically with timestamp  

---

## ▶️ Installation & Setup

### 1️⃣ Clone the repository

bash
git clone https://github.com/your-username/Face-Recognition-Attendance-System.git
cd Face-Recognition-Attendance-System

###2️⃣ Install dependencies

pip install opencv-python
pip install numpy
pip install pandas
pip install face_recognition

###3️⃣ Run the project

Capture face:

python register_face.py

Train model:

python train_model.py

Start attendance:

python mark_attendance.py
📊 Output

Attendance is stored in:

attendance/Attendance.csv

With:

Name

Date

Time

🧠 Key Learnings

Face detection & recognition using OpenCV

Image processing with NumPy

Data handling using Pandas

Real-time computer vision application

Automation of manual systems

🔒 Advantages

✔ Contactless attendance
✔ Saves time
✔ Prevents proxy attendance
✔ High accuracy

📌 Future Enhancements

GUI dashboard

Database integration (MySQL / Firebase)

Mask detection

Live cloud attendance

Mobile app support

👨‍💻 Author

Atharva Dhawale
GitHub: https://github.com/Atharva0421
