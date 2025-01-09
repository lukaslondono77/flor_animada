# **Flor Animada: Flask Application Lab Instructions**

Welcome to the **Flor Animada** lab! In this lab, you'll deploy and interact with a dynamic Flask application that displays images based on user input. Follow the instructions below to set up, run, and customize the project.

---

## **Objective**
By completing this lab, you will:
1. Set up a Python Flask environment.
2. Deploy a Flask application locally.
3. Customize and interact with the application.

---

## **Prerequisites**
Before you begin, ensure you have the following:
- **Python 3.x** installed.
- A code editor like **VS Code** (optional).
- Basic knowledge of Python and web applications.

---

## **Step 1: Clone the Repository**
1. Open a terminal.
2. Clone the repository from GitHub:
   ```bash
   git clone https://github.com/lukaslondono77/flor_animada.git
   ```
3. Navigate to the project directory:
   ```bash
   cd flor_animada
   ```

---

## **Step 2: Set Up the Environment**
1. Create a virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   ```
2. Activate the virtual environment:
   - **Linux/Mac**:
     ```bash
     source venv/bin/activate
     ```
   - **Windows**:
     ```bash
     venv\Scripts\activate
     ```

3. Install Flask:
   ```bash
   pip install flask
   ```

---

## **Step 3: Run the Application**
1. Start the Flask development server:
   ```bash
   python app.py
   ```
2. Open a web browser and go to:
   [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## **Step 4: Interact with the Application**
1. Enter one of the valid names (`Arturo`, `Julian`, `Gina`) into the input field.
2. Observe the loading animation for 3 seconds.
3. View the corresponding image displayed for the entered name.
4. Use the **Reset** button to clear the input and start over.

---

## **Step 5: Customize the Application (Optional)**
### **Add More Names and Images**
1. Add a new image to the `static/images` folder.
2. Update `app.py` to include the new name and image:
   ```python
   elif nombre == "newname":
       imagen = "newimage.jpeg"
   ```

### **Change Styles**
1. Open `static/styles.css`.
2. Modify styles (e.g., background color, fonts, button styles).

Example:
```css
body {
    background-color: #f0f8ff;
    font-family: 'Arial', sans-serif;
}
```

---

## **Step 6: Stop the Application**
When you're done, stop the Flask server by pressing `Ctrl + C` in the terminal.

To deactivate the virtual environment:
```bash
deactivate
```

---

## **Troubleshooting**
- **Issue**: Flask not installed.
  - **Solution**: Run `pip install flask`.
- **Issue**: Application not running.
  - **Solution**: Check for errors in `app.py` and ensure Flask is installed.
- **Issue**: Images not displaying.
  - **Solution**: Ensure the image files exist in the `static/images` folder and their names match the code in `app.py`.

---

## **Lab Completion**
Congratulations! 🎉 You have successfully deployed and interacted with the **Flor Animada** Flask application.

