
# **Django Blog Authentication System**

This authentication system provides user registration, login, logout, and profile management for the Django blog project.  

## **Features**
- 🔐 User registration with email validation  
- 🛠️ User login/logout using Django’s built-in authentication system  
- 👤 Profile management (view and update email)  
- 🔒 Secure authentication with CSRF protection and password hashing  

---

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

## **Usage Guide**
### **User Registration**
1. Go to `/register/`
2. Fill in the registration form (username, email, password)
3. Submit the form to create an account

### **User Login**
1. Visit `/login/`
2. Enter your credentials and log in

### **User Logout**
1. Click the logout button or visit `/logout/`

### **Profile Management**
1. Log in and visit `/profile/`
2. View or update your email address

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
- 🔒 **Login Required**: Profile management is protected with `@login_required`  

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

## **Contributing**
1. Fork the repository  
2. Create a feature branch: `git checkout -b feature-new-auth-functionality`  
3. Commit changes: `git commit -m "Added new authentication feature"`  
4. Push to the branch: `git push origin feature-new-auth-functionality`  
5. Open a pull request  

---

## **License**
This project is open-source under the [MIT License](LICENSE).  