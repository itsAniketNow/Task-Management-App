# **Task Management App**
Welcome to the Task Manager Application repository! 🎉 This project is designed to manage tasks efficiently, offering a seamless login/logout experience using Google OAuth2 Authentication, along with CRUD operations for tasks.

---

## **Tech Stack 💻**
### **1. Frontend**

-  HTML5, CSS3, Bootstrap 5

    - Bootstrap is used to create a responsive and visually appealing user interface.
    Custom CSS styles enhance the user experience.

### **2. Backend**
* Django 5.1.3

    * A robust Python web framework that simplifies the development of complex applications.
    Handles routing, authentication, and database operations. 

### **3. Authentication**

- Google OAuth2

    - Implemented using the social-auth-app-django library.
    - Allows secure login via Google accounts.

### **4. Database**

- SQLite
    -   A lightweight and file-based database used for storing tasks and user information.

### **5. Environment Configuration**

- Python-Decouple & dotenv
    - Used to manage environment variables securely.
    - Stores sensitive information like secret keys and API credentials.  

    ---
## **Key Features 🌟**

**1. Google Login Integration**

- Secure login using Google OAuth2.
- Redirection to the task management dashboard upon successful login.

**2. Task Management**

- Add, edit, and delete tasks.
- View all tasks in a clean, tabular format.

**3. Logout Functionality**

- Proper session management ensures users can log in and out repeatedly without errors.

**4. User-Friendly Interface**

- Clean and modern design powered by Bootstrap 5.
- Responsive layout for all screen sizes.

---
## **Folder Structure 📂**

        ├── task_manager/               # Main Django project directory  
        │   ├── settings.py             # Project settings and configurations  
        │   ├── urls.py                 # URL routing  
        │   ├── wsgi.py                 # WSGI configuration  
        ├── tasks/                      # Task management app  
        │   ├── models.py               # Database models  
        │   ├── views.py                # Request handling logic  
        │   ├── urls.py                 # Task-specific URLs  
        │   ├── templates/              # HTML templates  
        │   │   ├── base.html           # Base layout  
        │   │   ├── login.html          # Login page  
        │   │   ├── task_list.html      # Task list page  
        │   │   ├── task_form.html      # Add/Edit task page  
        ├── static/                     # Static assets (CSS, JS)  
        ├── db.sqlite3                  # SQLite database  
        ├── requirements.txt            # List of dependencies  
        ├── README.md                   # Documentation (you’re here!)  

---
## **How to Run the Project 🛠️**

### **Prerequisites**
1. Python 3.12+
2. Virtual Environment (venv)
3. Google API credentials for OAuth2 setup

### **Steps**
1. Clone the Repository
~~~
git clone https://github.com/<your-username>/task-manager.git
cd task-manager
~~~
2. Set Up Virtual Environment
~~~
python -m venv venv
source venv/bin/activate   # For Linux/Mac  
venv\Scripts\activate      # For Windows  
~~~
3. Install Dependencies
~~~
pip install -r requirements.txt
~~~
4. Set Up Environment Variables
~~~
SECRET_KEY=<your-django-secret-key>
GOOGLE_CLIENT_ID=<your-google-client-id>
GOOGLE_CLIENT_SECRET=<your-google-client-secret>
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
~~~
5. Run Migrations
~~~
python manage.py migrate
~~~
6. Start the Server
~~~
python manage.py runserver
~~~
7. Access the App
- Open http://127.0.0.1:8000 in your browser.

---
## **Screenshots 📸**

Login Page

![Login Page](Images\Login_page.png)


Task Dashboard
![My Task](Images\My_Task.png)

Add/Edit Task
![Creating_Task](Images\Task_Create.png)
![Deleting_Task](Images\Delete_page.png)

---

## **Dependencies 📦**

- **Django==5.1.3**
- **social-auth-app-django**
- **python-decouple**
- **dotenv**
- **Bootstrap 5**
---
## **Contributors ✨**

- **Aniket Surwade**
    
    - Role: Python Developer, Data Analyst
    