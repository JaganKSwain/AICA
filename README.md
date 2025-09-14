AI Career Agent: The Proactive Path to Your Next Career
Project Overview
This is an AI Career Agent, an autonomous system designed to help individuals find jobs and navigate their career paths by bridging the gap between their skills and industry demands. Leveraging IBM's open-source technologies, this project demonstrates an end-to-end, agentic workflow that goes beyond traditional keyword matching.

The agent can:

Find jobs based on a user's skills.

Analyze skills from a resume against job requirements.

Identify skill gaps and provide a personalized learning plan.

The project is built as a complete, full-stack application for a hackathon. The architecture is modular and easy to extend.

Architecture
The project consists of three main components:

Frontend (index.html): A single HTML file containing all the UI logic, styling (via Tailwind CSS), and JavaScript for user interaction. It's a single-page application that communicates with the backend via API calls.

Backend (app.py): A Python-based Flask server that acts as the bridge between the frontend and the AI agent's core logic. It handles API requests, processes file uploads, and routes data to the AI agent.

AI Agent Core (career_agent.py): A self-contained Python class that represents the brain of the agent. It contains the logic for planning and executing the workflow, including calling upon various tools to find jobs, analyze skills, and recommend learning resources.

File Structure
index.html: The complete frontend user interface.

app.py: The Flask backend server.

career_agent.py: The core AI agent logic.

mock_job_db.json: A sample database of job listings.

README.md: This file.

Setup and Installation
Prerequisites
You need to have Python and pip installed on your system.

1. Clone the Repository
git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
cd your-repo-name

(Note: Replace the URL with your actual GitHub repository URL)

2. Install Dependencies
Install the required Python libraries using pip.

pip install Flask Flask-Cors

3. Add Your API Key
The AI agent uses IBM Granite models for reasoning. You must add your API key to the career_agent.py file.

Open career_agent.py and replace "YOUR_GRANITE_API_KEY" with your actual API key:

# career_agent.py (find this line and edit)
def __init__(self, granite_api_key):
    self.granite_api_key = granite_api_key

4. Run the Application
Start the Flask server from your terminal.

python app.py

The server will start on http://127.0.0.1:5000.

5. Open the Frontend
Now, open the index.html file in your web browser. This will load the user interface, which will automatically connect to your running backend.

You should now have a fully functional AI Career Agent running locally.

License
This project is licensed under the MIT License.