A lightweight Python + Flask project that demonstrates a simple backend optimizer with a clean web UI. Users can input comma‑separated numbers, and the app computes their mean, standard deviation, and returns an optimized array.

This project is designed as a take‑home assignment style backend challenge, focusing on clarity, functionality, and test coverage.

🚀 Features
Web UI built with Flask and HTML/CSS

Optimization logic using NumPy

Interactive form for user input

Results display with mean, standard deviation, and normalized values

Unit tests with Pytest

📂 Project Structure
Code
mini-optimizer/
│── app.py              # Flask backend
│── optimizer.py        # Core optimization logic
│── templates/
│    └── index.html     # UI page
│── static/
│    └── style.css      # Styling
│── requirements.txt    # Dependencies
│── tests/
│    └── test_optimizer.py
⚙️ Installation
Clone the repository:

bash
git clone https://github.com/your-username/mini-optimizer.git
cd mini-optimizer
Create a virtual environment and install dependencies:

bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt flask
▶️ Running the App
Start the Flask server:

bash
python app.py
Open your browser at:

Code
http://127.0.0.1:5000
🧪 Testing
Run unit tests with Pytest:

bash
pytest tests/
📊 Example
Input:

Code
1, 2, 3, 4
Output:

json
{
  "input": [1, 2, 3, 4],
  "mean": 2.5,
  "std_dev": 1.12,
  "optimized": [0.89, 1.78, 2.67, 3.56]
}
📜 License
This project is released under the MIT License. You’re free to use, modify, and distribute it.
