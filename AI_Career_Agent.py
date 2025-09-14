import json
import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename

# Import the core AI agent logic from the career_agent.py file.
# Note: You need to have career_agent.py in the same directory.
from Agentic_AI_Integration import CareerAgent

app = Flask(__name__)
CORS(app)  # This will allow cross-origin requests from your frontend.

# Configuration for file uploads
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'doc', 'docx'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Initialize the AI Agent.
# IMPORTANT: In a real-world scenario, you would use a secure method to
# manage your API keys and not hardcode them.
agent = CareerAgent(granite_api_key="YOUR_GRANITE_API_KEY")

def allowed_file(filename):
    """Check if the uploaded file has an allowed extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/api/find_jobs', methods=['POST'])
def find_jobs():
    """API endpoint to find jobs based on user skills."""
    data = request.json
    skills = data.get('skills', [])
    if not skills:
        return jsonify({"status": "Error", "report": "Please provide a list of skills."}), 400
    
    # Run the agent's workflow for finding jobs
    # Note: The CareerAgent class's run_agent() method is designed for a full workflow.
    # For a simple "find jobs" tool, we can call the tool directly.
    try:
        job_listings = agent._find_jobs_tool(skills)
        if not job_listings:
            return jsonify({"status": "Success", "matches": [], "report": "No suitable jobs found."})

        # To demonstrate the agent's full capability, we'll run the analysis as well.
        user_profile = {"skills": skills}
        report = agent.run_agent(user_profile)
        return jsonify(report)
    except Exception as e:
        return jsonify({"status": "Error", "report": f"An error occurred: {str(e)}"}), 500

@app.route('/api/analyze_skills', methods=['POST'])
def analyze_skills():
    """API endpoint to analyze user skills from a resume file."""
    if 'resume' not in request.files:
        return jsonify({"status": "Error", "report": "No resume file provided."}), 400
    
    file = request.files['resume']
    if file.filename == '':
        return jsonify({"status": "Error", "report": "No file selected."}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # In a real project, you would parse the file to extract skills.
        # For this hackathon, we'll simulate the parsing.
        # Example: user_skills = parse_resume(filepath)
        user_skills = ["Python", "Algorithms", "Communication", "Data Analysis"] # Simulated skills from file
        
        # Now, run the agent with the simulated skills
        user_profile = {"skills": user_skills, "goal": "general career path"}
        report = agent.run_agent(user_profile)

        # Clean up the uploaded file
        os.remove(filepath)
        
        return jsonify(report)

    return jsonify({"status": "Error", "report": "File type not allowed."}), 400

@app.route('/api/learning_resources', methods=['POST'])
def learning_resources():
    """API endpoint to get learning resources for a specific skill."""
    data = request.json
    skill = data.get('skill', '')
    if not skill:
        return jsonify({"status": "Error", "report": "Please provide a skill to search for."}), 400

    # Simulate a call to the agent's learning tool
    # A real agent would decide which tool to call based on the request.
    # Here, we'll provide a hardcoded list of resources.
    simulated_resources = [
        {"title": f"Intro to {skill}", "url": f"https://example.com/{skill}-intro"},
        {"title": f"Advanced {skill} Course", "url": f"https://example.com/{skill}-advanced"},
        {"title": f"Certification in {skill}", "url": f"https://example.com/{skill}-cert"}
    ]

    return jsonify({"status": "Success", "resources": simulated_resources, "report": ""})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
