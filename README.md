# Smart-Study-Planner-Multi-Agent-Personal-Exam-Coach
Capstone Project for Google 5-Day AI Agents Intensive Course


# Syllabus-to-StudyAgent  
**Your Personal AI Study Concierge Agent**

**Capstone Project** – Google 5-Day AI Agents Intensive Course  
**Track**: Concierge Agents / Personal Life OS  
**Submitted**: December 2025  

### Project Demo (60 seconds)
https://youtu.be/dQw4w9WgXcQ *(replace with your real video link or delete this line)*

### What This Agent Does
Drop **any syllabus PDF** → Get instantly:
- Clean list of all topics
- Personalized 2-session-per-day study schedule
- 2 high-quality MCQs per topic (Option A = correct)

**Zero typing. Zero planning. Just study.**

### Features
- Fully automatic PDF reading (`pypdf`)
- Smart topic extraction (works with real university syllabi)
- Modular AI agent architecture (`parser_agent`, `planner_agent`, `quiz_agent`)
- Works 100% offline
- One-command demo: `python run_demo.py`

### How to Run (30 seconds)
```bash
git clone https://github.com/YOUR_USERNAME/Syllabus-to-StudyAgent.git
cd Syllabus-to-StudyAgent
pip install pypdf reportlab
python run_demo.py



To use your own syllabus:
Just drop your PDF into the sample_data/ folder (any name) → run again → done!
Project Structure
textSyllabus-to-StudyAgent/
├── run_demo.py                  ← Main script
├── sample_data/
│   └── sample_syllabus.pdf      ← Example (replace with yours)
├── tools/
│   └── pdf_tool.py              ← PDF reader
└── agents/
    ├── parser_agent.py          ← Extracts topics
    ├── planner_agent.py         ← Creates study schedule
    └── quiz_agent.py            ← Generates MCQs
