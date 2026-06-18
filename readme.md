# QR Code Generator

A simple, modular Python application featuring a clean frontend GUI and a robust backend to generate, customize, and save custom QR codes instantly.

## 🚀 Features

* **Instant Generation:** Convert any text or URL into a high-quality QR code.
* **Customization:** Easily configure the QR code's appearance and settings.
* **Save & Export:** Export generated QR codes in standard image formats such as PNG and JPEG.
* **Modular Architecture:** Clean separation of concerns with dedicated frontend and backend components.

---

## 📁 Repository Structure

```text
├── backend.py       # Handles QR code generation logic and processing
├── frontend.py      # Manages the GUI / User Interface
├── .gitignore       # Specifies untracked files to ignore
└── LICENSE          # MIT License
```

---

## 🛠️ Prerequisites

Make sure Python is installed on your system.

Install the required dependencies:

```bash
pip install qrcode pillow pypng customtkinter
```

> **Note:** If you are using Tkinter for the graphical interface, it is usually included with standard Python installations.

---

## 💻 Getting Started

### Clone the Repository

```bash
git clone https://github.com/Kapy2003/Qr-code-Generator.git
cd Qr-code-Generator
```

### Run the Application

```bash
python frontend.py
```

---

## ⚙️ How It Works

### `backend.py`

Handles the QR code generation process using the `qrcode` and `Pillow` libraries. It converts user-provided text or URLs into QR code images and manages customization options.

### `frontend.py`

Provides the graphical user interface (GUI), captures user input, communicates with the backend, and displays the generated QR code.

---

## 📦 Dependencies

* Python 3.x
* qrcode
* Pillow
* customtkinter
* Tkinter (typically pre-installed)

---

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for more information.

