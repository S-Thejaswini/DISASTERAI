<div style="text-align: center;">
  <img src="https://capsule-render.vercel.app/api?type=cylinder&height=100&color=9C5B4B&text=Welcome%20to%20our%20miniproject&reversal=false&textBg=false&fontSize=52&fontAlign=50&fontAlignY=50&animation=twinkling&fontColor=F9E5E0&stroke=FEDBFF&descSize=51&section=header" />
</div>

<div style="text-align: center;">
  <img src="https://capsule-render.vercel.app/api?type=transparent&height=100&color=141489&text=%20SENTINEL&reversal=false&textBg=false&fontSize=27&fontAlign=50&fontAlignY=50&animation=scaleIn&fontColor=28BAB1&stroke=FEDBFF&descSize=51&section=header" />
</div>


# *****SENTINEL: AI-Powered Disaster Prediction and Prevention System🌊🚨*****

![Logo](https://github.com/S-Thejaswini/DISASTERAI/blob/main/images/logo.img?raw=true)


## ****📝Project Description**** 
**SENTINEL** is an AI-driven web application designed to predict and mitigate flood risks. By leveraging **machine learning**, **real-time weather data**, and an **AI chatbot**, SENTINEL provides users with early warnings, preparedness guidance, and emergency response strategies.  

This system is built with a **Flask backend**, a **user-friendly frontend using HTML, CSS, and Tailwind**, and integrates **OpenWeatherMap API** for real-time updates. The AI chatbot, powered by **Groq**, assists users with safety measures, evacuation plans, and essential documentation.  

With **real-time flood monitoring, instant alerts, and an interactive chatbot**, SENTINEL ensures communities stay informed and prepared, reducing disaster impact and enhancing resilience.

   

## ****🔗API Reference****

### ***OpenWeatherMap API***

The OpenWeatherMap API provides real-time weather data for flood prediction.

#### ***Get Current Weather Data***

```http
GET https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}
```

| Parameter  | Type     | Description                           |
|------------|----------|---------------------------------------|
| `city`     | `string` | **Required**. Name of the city       |
| `API_KEY`  | `string` | **Required**. Your OpenWeatherMap API key |

#### ***Get Forecast Data***

```http
GET https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}
```

| Parameter  | Type     | Description                             |
|------------|----------|-----------------------------------------|
| `city`     | `string` | **Required**. Name of the city         |
| `API_KEY`  | `string` | **Required**. Your OpenWeatherMap API key |

---

### ***Groq API (LLama3-based Chatbot)***

The Groq API is used for the AI chatbot that provides disaster-related assistance.

#### ***Send a Query to the Chatbot***

```http
POST https://api.groq.com/v1/chat/completions
```

**Headers:**

```http
Content-Type: application/json
Authorization: Bearer {API_KEY}
```

**Body:**

```json
{
  "model": "llama3-8b",
  "messages": [
    { "role": "user", "content": "What should I do during a flood?" }
  ]
}
```

| Parameter  | Type     | Description                          |
|------------|----------|--------------------------------------|
| `API_KEY`  | `string` | **Required**. Your Groq API key     |
| `model`    | `string` | **Required**. AI model to be used (`llama3-8b`) |
| `messages` | `array`  | **Required**. User query messages   |

#### ***Example Response***

```json
{
  "id": "response_id",
  "object": "chat.completion",
  "created": 1711501234,
  "model": "llama3-8b",
  "choices": [
    {
      "message": { "role": "assistant", "content": "During a flood, move to higher ground and avoid walking through floodwaters." }
    }
  ]
}
```


## ****✍️Authors****

- [Abhishek M S](https://github.com/abhii124)  
- [Anjithkrishnan K](https://github.com/AnjithKrishnan-946)  
- [Riya S](https://github.com/riyamohandas)  
- [S Thejaswini](https://github.com/S-Thejaswini)  
## ****🎨 Color Reference****

| Color Usage                      | Hex Code     |
|-----------------------------------|-------------|
| Background (🔵 Blue & ⚪ White)    | `#1E3A8A`, `#FFFFFF` |
| No Flood Risk Message (🟢 Green)  | `#16A34A`   |
| No Flood Risk Popup (🟢 Green)    | `#16A34A`   |
| Flood Risk Message (🔴 Red)       | `#DC2626`   |
| Flood Risk Popup (🔴 Red)         | `#DC2626`   |
| Chatbot Background (🔵 Blue & ⚪ White) | `#1E3A8A`, `#FFFFFF` |


## ****🚀 Demo****
Watch this preview:  

[https://github.com/user-attachments/assets/6d979e25-3ef0-4119-a642-745943c73339](https://github.com/user-attachments/assets/6d979e25-3ef0-4119-a642-745943c73339)


## ****📂 Project Structure****

FloodPredictionApp/
├── backend/
│   ├── data/
│   │   ├── original_dataset/  # Contains raw, unprocessed data files
│   │   └── processed_dataset/ # Contains cleaned, transformed data for modeling
│   ├── API_integration.py     # Code for integrating with external APIs (e.g., weather)
│   ├── data_analysis.py       # Scripts for exploratory data analysis (EDA)
│   ├── app.py                 # Main backend application file (e.g., Flask)
│   ├── chatbot_test.py        # Script for testing chatbot functionality
│   ├── feature_columns.pkl    # Saved list/object of feature columns used by the model
│   ├── flood_model.pkl        # The serialized trained machine learning model
│   └── flood_prediction_model.py # Code defining the model, training, and prediction logic
├── frontend/
│   ├── chatbot.html           # HTML page for the chatbot interface
│   ├── forecast.html          # HTML page for displaying weather/flood forecasts
│   ├── landing.html           # The main landing/home page HTML
│   ├── prediction.html        # HTML page for user input for flood prediction
│   └── result.html            # HTML page to display prediction results
├── images/                    # Static assets
│   ├── Project.mp4            # Project demo video
│   └── logo.img               # Project logo 
├── CODE_OF_CONDUCT.md       # Guidelines for contributors
├── CONTRIBUTORS.md          # List of project contributors
├── LICENSE                  # Project's software license (e.g., MIT)
├── README.md                # Project overview, setup, and usage instructions
└── requirements.txt         # List of Python dependencies for the backend



## ****📚 Appendix****

Here are additional details and references related to this project:

- **Project Documentation**: [Link to Documentation](#)  
- **Installation Guide**: [Setup Instructions](#)  
- **API References**: [API Documentation](#)  
- **Acknowledgments**: Special thanks to contributors and resources that helped build this project.  
- **Useful Links**:     
  - [Related Research Papers](#)  

For any queries, feel free to reach out or open an issue. 🚀



## ****🚀 Badges****

[![Project Status](https://img.shields.io/badge/Status-Active-brightgreen)](#)  
[![Tech Stack](https://img.shields.io/badge/Tech-Flask%20%7C%20Python%20%7C%20ML-blue)](#)  
[![Made with AI](https://img.shields.io/badge/Made%20With-AI%20%26%20ML-purple)](#)  
[![Flood Prediction](https://img.shields.io/badge/Feature-Flood%20Prediction-blue)](#)  
[![Chatbot](https://img.shields.io/badge/Feature-AI%20Chatbot-orange)](#)  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Contributors](https://img.shields.io/github/contributors/S-Thejaswini/DISASTERAI.svg)](https://github.com/S-Thejaswini/DISASTERAI/graphs/contributors)  
[![Open Issues](https://img.shields.io/github/issues/S-Thejaswini/DISASTERAI.svg)](https://github.com/S-Thejaswini/DISASTERAI/issues)  
[![Forks](https://img.shields.io/github/forks/S-Thejaswini/DISASTERAI.svg)](https://github.com/S-Thejaswini/DISASTERAI/network/members)  
[![Stars](https://img.shields.io/github/stars/S-Thejaswini/DISASTERAI.svg)](https://github.com/S-Thejaswini/DISASTERAI/stargazers)  
[![Last Commit](https://img.shields.io/github/last-commit/S-Thejaswini/DISASTERAI.svg)](https://github.com/S-Thejaswini/DISASTERAI/commits/main)  
[![Repo Size](https://img.shields.io/github/repo-size/S-Thejaswini/DISASTERAI.svg)](https://github.com/S-Thejaswini/DISASTERAI)  
[![Pull Requests](https://img.shields.io/github/issues-pr/S-Thejaswini/DISASTERAI.svg)](https://github.com/S-Thejaswini/DISASTERAI/pulls)  
[![Watchers](https://img.shields.io/github/watchers/S-Thejaswini/DISASTERAI.svg?style=social)](https://github.com/S-Thejaswini/DISASTERAI/watchers)  
[![Activity](https://img.shields.io/github/commit-activity/m/S-Thejaswini/DISASTERAI.svg)](https://github.com/S-Thejaswini/DISASTERAI/commits/main)  
[![Languages](https://img.shields.io/github/languages/count/S-Thejaswini/DISASTERAI.svg)](https://github.com/S-Thejaswini/DISASTERAI)  
[![Top Language](https://img.shields.io/github/languages/top/S-Thejaswini/DISASTERAI.svg)](https://github.com/S-Thejaswini/DISASTERAI)  


## ****🤝 Contributing**** 

Contributions are always welcome!  

- See [`CONTRIBUTORS.md`](https://github.com/S-Thejaswini/DISASTERAI/blob/main/CONTRIBUTORS.md) for ways to get started.  
- Please adhere to this project's [`CODE_OF_CONDUCT.md`](https://github.com/S-Thejaswini/DISASTERAI/blob/main/CODE_OF_CONDUCT.md).  

We appreciate your support in making this project better! 🚀  



## ****📄 Documentation****  

You can find the complete documentation [here](https://github.com/S-Thejaswini/DISASTERAI/wiki).  



## ****🔒 Environment Variables****  

To run this project, you need to add the following environment variables to your `.env` file:  

```ini
API_KEY=your_api_key_here   # API key for OpenWeatherMap or other external services  
GROQ_API_KEY=your_groq_api_key_here   # API key for the Groq AI chatbot  
SECRET_KEY=your_secret_key_here   # Flask secret key for security  
```


 ##****🌟✨FEATURES****

✅ ***Flood Prediction*** – Provides real-time flood risk predictions using AI and weather data.  
✅ ***AI Chatbot Assistance*** – Offers disaster-related guidance, important documents, and safety checklists.  
✅ ***Instant Alerts*** – Sends notifications about flood risks to help users stay prepared.  
✅ ***Minimal Setup*** – No login or database required for easy access.  
✅ ***User-Friendly Interface*** – Simple and intuitive design for smooth navigation.  
✅ ***Fast & Lightweight*** – Optimized for quick performance without heavy dependencies.  



## ****⚙️Installation****

Install my-project with npm

```bash
  npm install my-project
  cd my-project
```
    
## ****📚 Lessons Learned**** 

Building **Sentinel** provided valuable insights into AI-powered disaster management.  

### ***🚀 Technical Skills Gained*** 
- **Machine Learning & Data Processing:** Improved understanding of flood prediction models using **Scikit-Learn, Pandas, and NumPy**.  
- **Web Development:** Learned how to integrate **Flask** with frontend technologies like **HTML, CSS, JavaScript, and Tailwind CSS**.  
- **API Integration:** Successfully implemented **OpenWeatherMap API** for real-time weather data.  
- **AI Chatbot Implementation:** Integrated **Groq API (Llama 3 model)** for disaster-related queries.  

### ***🔍 Challenges Faced & Solutions***  
| Challenge | Solution |  
|-----------|----------|  
| Data availability for flood prediction | Collected historical weather data and rainfall statistics for Kerala. |  
| Deploying Flask without a database | Designed a **lightweight, API-based** approach without user authentication. |  
| UI/UX improvements | Used **Tailwind CSS** for a responsive and visually appealing interface. |  

This project strengthened our understanding of **AI-augmented software development** and real-world disaster management applications. 🚀



## ****📝 License****  

This project is dual-licensed under the **MIT License** and **Apache 2.0 License**.  
- [MIT License](https://choosealicense.com/licenses/mit/)  



## ****🚀 Optimizations**** 

- **Improved Model Efficiency**: Optimized flood prediction model by fine-tuning hyperparameters to enhance accuracy and reduce computation time.  
- **Reduced API Calls**: Minimized unnecessary API requests to OpenWeatherMap for better performance and lower latency.  
- **Lightweight Frontend**: Used **Tailwind CSS** for a faster and more responsive UI.  
- **Optimized Chatbot Processing**: Streamlined chatbot responses to ensure faster query resolution while using a pre-trained model.  
- **Efficient Data Handling**: Utilized **Pandas** efficiently for data processing, reducing memory usage.  
- **Asynchronous Processing**: Implemented async functions in Flask where possible for better request handling.  


## ****🚀 Run Sentinel Locally****  

Follow these steps to set up and run **Sentinel** on your local machine.  

### ***📌 Prerequisites***  
Make sure you have the following installed:  
- Python 3.x  
- pip (Python package manager)  
- Git  

### ***1️⃣ Clone the Repository***  

git clone https://github.com/S-Thejaswini/DISASTERAI.git

### ***2️⃣ Navigate to the Project Directory***

cd DISASTERAI

### ***3️⃣ Create a Virtual Environment (Optional but Recommended)***
python -m venv venv
Activate the virtual environment:

On Windows:
venv\Scripts\activate

On macOS/Linux
source venv/bin/activate

### ***4️⃣ Install Dependencies***
pip install -r requirements.txt

### ***5️⃣ Set Up Environment Variables***
Create a .env file in the root directory and add the required API keys:
env
API_KEY=your_api_key_here
ANOTHER_API_KEY=your_other_api_key_here

### ***6️⃣ Run the Application***
python app.py

### ***7️⃣ Open in Browser***
Once the server is running, open your browser and go to:
http://127.0.0.1:5000/

Now, Sentinel should be up and running locally 🚀🔥



## ****🛠️ Support****  

For support, reach out via:  
📧 Email: [sentinelfloodprediction@gmail.com](sentinelfloodprediction@gmail.com)  



## ****🚀 Sentinel: Technology Stack and Tools****

A comprehensive breakdown of the technology stack and tools used in the **Sentinel** flood prediction system.  

### ***🖥️ Backend Technologies***  
- **Python** - Core programming language  
- **Flask** - Web framework for building the application  
- **Joblib/Pickle** - Model serialization and loading  
- **NumPy** - Numerical operations and array handling  
- **Pandas** - Data manipulation and analysis  
- **Scikit-learn** - Machine learning model implementation  
- **Groq** - AI model provider for the chatbot  

### ***🎨 Frontend Technologies*** 
- **HTML5** - Markup language for web pages  
- **CSS3** - Styling language for web pages  
- **JavaScript** - Client-side scripting  
- **Tailwind CSS** - Utility-first CSS framework  
- **Jinja2** - Template engine for Flask  

### ***🌍 APIs & External Services***  
- **OpenWeatherMap API** - Fetches real-time weather data and forecasts  
- **Groq API** - AI chatbot responses (Llama 3 model)  

### ***🛠️ Development Tools***  
- **Git** - Version control  
- **Python Virtual Environment** - Dependency management  

### ***🗄️ Data Storage***  
- **Pickle/Joblib files** - Storing trained ML models  

### ***🤖 Machine Learning Components***  
- **Flood Prediction Model** - Custom ML model for flood risk prediction  
- **Feature Engineering** - Processing weather data into model features  

### ***🚀 Deployment***  
- **Local Development Server** - Flask’s built-in server  
- **Production Server** - (Future) WSGI server like Gunicorn or uWSGI  

### ***🏗️ User Interface Components*** 
- **Responsive Design** - Mobile-friendly UI using Tailwind CSS  
- **Interactive Elements** - Form inputs, loading states, notifications  
- **Weather Visualization** - Custom weather widgets and forecasts  
- **Notification System** - Alerts for flood risks  

### ***📁 Project Structure***  
- **MVC Architecture** - Model (ML model), View (Jinja templates), Controller (Flask routes)  
- **Template-based Rendering** - Server-side rendering with Jinja2  
- **RESTful API Design** - Fetching and processing weather data    

This **technology stack** enables **Sentinel** to function as a **flood prediction system**, combining web development, data science, and real-time APIs.  

## ****🌟Acknowledgements****

- [OpenWeatherMap API](https://openweathermap.org/api) - For real-time weather data.  
- [Scikit-learn](https://scikit-learn.org/) - Used for ML model implementation.  
- [Flask](https://flask.palletsprojects.com/) - For backend development.  
- [Groq API](https://groq.com/) - AI chatbot support.  
- [Tailwind CSS](https://tailwindcss.com/) - For frontend styling.
  

## ****Running Tests****

To run tests, run the following command

```bash
  npm run test
```



