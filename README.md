# Password Strength Tester

This is a simple Password Strength Tester web application built with HTML, CSS, JavaScript, and Flask (Python). It checks the strength of a password in real-time, provides feedback, and displays a humorous pop-up based on the password strength.

### Features:
- **Real-time password strength analysis**: As the user types, the strength of their password is evaluated.
- **Strength bar**: A color-coded bar visualizes the strength of the password.
- **Humorous feedback**: A pop-up with funny and rude messages that "make fun" of the password strength.
- **Responsive design**: Works on both desktop and mobile devices.
- **Smooth animations**: The pop-up slides in after the user leaves the password input field.

---

## Installation

### Backend Setup (Flask)

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/password-strength-tester.git
    cd password-strength-tester
    ```

2. Install Flask:

    ```bash
    pip install Flask
    ```

3. Run the Flask server:

    ```bash
    python app.py
    ```

    The Flask server will run at `http://127.0.0.1:5000/`.

---

### Frontend Setup

1. Open the `index.html` file in a web browser.
2. Enter a password in the input field.
3. Watch the strength bar change color as you type.
4. After leaving the password field, a pop-up will appear with a humorous message based on your password strength.

---

## How It Works

- **Flask Backend**: The Flask app (in `app.py`) receives the password from the frontend, checks its strength, and sends the result back as a JSON response.
- **Frontend**: The frontend uses JavaScript to send the password to the Flask backend for evaluation. Based on the response, it updates the strength bar and displays the corresponding feedback.

---

## Customization

You can modify the strength levels and pop-up messages by editing the `checkStrength()` and `showPopup()` functions in the `script.js` section.

### Strength Categories:
The strength categories are defined as:
- **Weak**: Password is too short or simple.
- **Moderate**: Password is decent but could be stronger.
- **Strong**: Password is sufficiently strong with a mix of characters.

### Pop-Up Messages:
The pop-up messages are defined based on the password strength:
- Weak: "Your password is as weak as a wet noodle."
- Moderate: "Your password is decent, but you can do better."
- Strong: "Great job! Your password is rock solid!"

You can change these messages in the `showPopup()` function within the JavaScript.

---

## Technologies Used

- **HTML**: Structure of the web page.
- **CSS**: Styling for the layout, strength bar, and pop-up animations.
- **JavaScript**: Password strength evaluation, dynamic updates of the UI, and pop-up interactions.
- **Python (Flask)**: Backend server that checks the password strength based on rules.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICSENSE) file for details.

---

### Notes:
- The current password strength evaluation is done using basic rules in Flask (such as checking length, uppercase letters, numbers). You can further enhance this with more advanced algorithms or integrate libraries like `zxcvbn`.
- The pop-up is triggered once the user leaves the password field, offering humorous feedback based on the password's strength.

---

Feel free to customize the application and use it as a learning project or add more features like a password generator, password validation rules, etc.

---

This README includes both the **Flask backend** and **frontend** setup, along with how everything works together.
