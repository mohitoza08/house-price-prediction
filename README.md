🚀 Project Title & Tagline
==========================
### House Price Prediction Web Application 🏠  
> "Predicting the future, one house at a time." ⏰  

📖 Description
---------------
The **House Price Prediction Web Application** is a Flask-based machine learning project that predicts house prices based on user-input features like bedrooms, bathrooms, square footage, location, and more.  

It uses a **trained multiple linear regression model** built with **scikit-learn**, providing users with an instant estimated house price through an interactive and user-friendly web interface.  

The app takes inputs from an HTML form, processes them through a pre-trained model, and returns the predicted price dynamically on the same page — offering a smooth and responsive user experience.  

✨ Features
-----------
Here are the key features of this project:
* 🧠 **Machine Learning-based predictions** — uses a trained Linear Regression model.
* 💻 **Flask backend integration** — handles user inputs and model predictions seamlessly.
* 🎨 **Interactive UI** — clean, minimal, and responsive web design using HTML, CSS, and Bootstrap.
* ⚡ **Instant predictions** — shows results in real-time without page reload.
* 🔒 **Secure and lightweight** — runs locally and can be deployed easily on hosting platforms.
* 📊 **Easily customizable** — can be extended to include new features like charts or data visualization.

🧰 Tech Stack
--------------
| Technology | Description |
| --- | --- |
| **Frontend** | HTML, CSS, JavaScript |
| **Backend** | Flask (Python) |
| **Machine Learning** | scikit-learn |
| **IDE / Tools** | Jupyter Notebook, VS Code |
| **Version Control** | Git, GitHub |

📁 Project Structure
----------------------
The project is organized into the following folders:

- **app**: This folder contains the Flask application code.
  - **templates**: HTML templates for the application.
  - **static**: CSS, JS, and image files.
- **model**: Trained machine learning model (`house_price_model.pkl`).
- **kc_house_data.csv**: Dataset used for training the model.
- **app.py**: Main Flask application file.
- **requirements.txt**: Python dependencies.
- **README.md**: Project documentation.



⚙️ How to Run
---------------
Follow these steps to run the project locally 👇  
1. **Clone the repository**
   ```bash
   git clone https://github.com/mohitoza08/house-price-prediction.git
   cd house-price-prediction

2. **Create a virtual environment**
   ```bash
   python -m venv venv

   # For Windows
   venv\Scripts\activate

   # For Mac/Linux
   source venv/bin/activate

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt

4. **Run the Flask app**
   ```bash
   python app.py

5. Open in browser
   http://127.0.0.1:5000/


🧠 Model Details
Algorithm Used: Multiple Linear Regression
Library: scikit-learn
Training Data: Historical house pricing dataset
Target Variable: price
Input Features: bedrooms, bathrooms, sqft_living, sqft_lot, floors, waterfront, view, condition, grade, year_built, zipcode, etc.

📸 Screenshots


📦 Future Improvements
Add interactive charts for visual insights
Integrate map API for location-based predictions
Deploy the app on platforms like Render, Railway, or Hugging Face Spaces

👤 Author
-----------
The House Price Prediction Web Application was created by [Mohit Oza](https://github.com/mohitoza08).

📝 License
-----------
The House Price Prediction Web Application is licensed under the [MIT License](https://opensource.org/licenses/MIT).

   
   

