# ENOtv

## Overview
ENOtv is a comprehensive online platform designed to provide users with a vast array of entertainment options. From the latest movies and TV series to live events, documentaries, and sports, ENOtv offers something for everyone. Our goal is to create a user-friendly and engaging experience that caters to diverse entertainment preferences.

## Features
Extensive Content Library: Access a vast collection of movies, TV shows, documentaries, and live events.
Live Streaming: Enjoy real-time coverage of sports events, concerts, and other live programs.
User Profiles: Create personalized profiles to track viewing history, recommendations, and preferences.
Search and Discovery: Easily find content using advanced search filters and personalized recommendations.
Multiple Devices: Seamlessly access ENOtv on various devices, including desktops, laptops, tablets, and smartphones.
High-Quality Video: Experience stunning visuals and immersive audio with support for HD and 4K streaming.

### Technology Stack
* **Frontend:** HTML, CSS, JavaScript
* **Backend:** Python, Flask
* **Database:** SQLite
* **Video Streaming:** third-party API - YouTube 
* **Templating:** Jinja2

### Project Structure
* **app:** Contains the Flask application code, including routes, views, models, and controllers.
* **static:** Stores static files like CSS, JavaScript, and images.
* **templates:** Stores HTML templates rendered by Jinja2.
* **requirements.txt ⤵**

  ```python
  blinker==1.8.2
  click==8.1.7
  colorama==0.4.6
  Flask==3.0.3
  gunicorn==22.0.0
  importlib_metadata==8.2.0
  itsdangerous==2.2.0
  Jinja2==3.1.4
  MarkupSafe==2.1.5
  packaging==24.1
  psycopg2==2.9.9
  Werkzeug==3.0.3
  zipp==3.19.2
  ```

### Installation and Setup
1. **Create a virtual environment:**
   ```bash
   python -m venv env
   source env/bin/activate  # or env\Scripts\activate on Windows

2. **Install dependencies:**
   ```Bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```Bash
   python app.py
   ```
