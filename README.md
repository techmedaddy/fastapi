# FastAPI CRUD App with Hello Kitty Frontend

A simple FastAPI CRUD application with a Hello Kitty themed frontend, using SQLite for persistent storage.
## 🚀 Features & Concepts

- FastAPI for backend API
- SQLite database with SQLAlchemy ORM
- Full CRUD operations (Create, Read, Update, Delete)
- Cute Hello Kitty themed HTML/CSS/JS frontend
- Environment variable management with `.env`
- Easy deployment on Render or similar platforms
## 🛠️ How to Run Locally

1. **Clone the repository:**
   ```
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
   ```

2. **Create a virtual environment and activate it:**
   ```
   python -m venv .venv
   .venv\Scripts\activate   # On Windows
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Start the FastAPI server:**
   ```
   uvicorn main:app --reload
   ```
## 🌐 How to Deploy on Render

1. **Push your code to GitHub.**

2. **Create a `start.sh` file (already included):**
   ```bash
   #!/bin/bash
   uvicorn main:app --host 0.0.0.0 --port 10000
   ```

3. **On Render:**
   - Create a new Web Service.
   - Connect your GitHub repo.
   - Set the build command: `pip install -r requirements.txt`
   - Set the start command: `bash start.sh`
   - Deploy!

4. **Access your app via the public Render URL.**
## 📚 Learning Outcomes

- Building RESTful APIs with FastAPI
- Using SQLAlchemy ORM with SQLite
- Managing environment variables with `.env`
- Creating and styling a frontend with HTML/CSS/JS
- Deploying Python web apps for
5. **Open the frontend:**
   - Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.
