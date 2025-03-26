
# **Django Blog Authentication System**

This authentication system provides user registration, login, logout, and profile management for the Django blog project.  

## **Installation and Setup**
### **1. Clone the Repository**
```bash
git clone <your-repo-url>
cd django_blog
```

### **2. Create a Virtual Environment and Activate It**
```bash
python3 -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate  # On Windows
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Apply Database Migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

### **5. Create a Superuser (Optional)**
```bash
python manage.py createsuperuser
```
Follow the prompts to set a username, email, and password.

### **6. Run the Django Development Server**
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000/` in your browser.

---

## **Authentication URLs**
| URL Path   | Description |
|------------|-------------|
| `/register/` | User registration page |
| `/login/` | Login page |
| `/logout/` | Logout page |
| `/profile/` | User profile page |

---

## **Security Measures**
- ✅ **CSRF Protection**: All forms include CSRF tokens to prevent CSRF attacks  
- 🔑 **Password Hashing**: Django’s built-in password hashing ensures secure storage  

---

## **Troubleshooting**
**1. "Command not found: python3"**  
- Ensure Python is installed and added to your system PATH.  

**2. "ModuleNotFoundError: No module named 'django'"**  
- Activate the virtual environment and install dependencies:  
  ```bash
  source venv/bin/activate
  pip install -r requirements.txt
  ```

**3. "Page Not Found (404)" for `/login/`, `/register/`, etc.**  
- Ensure URLs are correctly defined in `urls.py`  
--- 