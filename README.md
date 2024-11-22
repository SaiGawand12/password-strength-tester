

# Password Strength Tester

This is a simple Password Strength Tester web application built with HTML, CSS, and JavaScript. It checks the strength of a password in real-time and provides feedback to the user, including a fun pop-up with humorous messages based on the password strength.

### Features:
- **Real-time password strength analysis**: As the user types, the strength of their password is evaluated.
- **Strength bar**: A color-coded bar visualizes the strength of the password.
- **Humorous feedback**: A pop-up with funny and rude messages that "make fun" of the password strength, such as:
  - Weak Password: "Your password is as weak as a wet noodle."
  - Moderate Password: "Your password is decent, but you can do better."
  - Strong Password: "Great job! Your password is rock solid!"
- **Responsive design**: Works on both desktop and mobile devices.
- **Smooth animations**: The pop-up slides in after the user leaves the password input field.

---

## Installation

To get started with the Password Strength Tester, follow these steps:

### 1. Clone the repository

Clone the project to your local machine using:

```bash
git clone https://github.com/SaiGawnd12/password-strength-tester.git
```

### 2. Open the project in a web browser

You can simply open the `index.html` file in any modern web browser. No server setup is required for the basic functionality.

---

## How to Use

1. Open the `index.html` file in your browser.
2. Enter a password in the input field.
3. Watch the strength bar change color as you type, indicating the strength of your password.
4. After leaving the password field, a pop-up will appear with a humorous message based on your password strength.

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

---

## License

This project is licensed under the MIT License - see the [https://github.com/SaiGawand12/password-strength-tester/blob/main/LICENSE](LICENSE) file for details.

---

### Notes:
- If you'd like to implement a backend for more accurate password strength evaluation, you can use libraries like `zxcvbn` or integrate it with any server-side language like Python, Node.js, etc.
- The current version only simulates password strength with basic client-side JavaScript.

---

Feel free to customize the application and use it as a learning project, or add more features like a password generator, password validation rules, etc.

