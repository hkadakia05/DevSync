

# 🚀 **DevSync AI – AI Agents for Developer Productivity**

Automate your developer workflow with **AI agents** that review code, manage meetings, and track tasks — powered by **NVIDIA Riva & NeMo** for speech and language intelligence.

---

## 🎯 **Project Overview**

Developers waste countless hours switching between **code reviews**, **meetings**, and **task tracking**.
**DevSync AI** removes this friction by orchestrating AI agents to handle these repetitive tasks automatically, freeing developers to focus on what matters most: **building great products**.

**What DevSync Does:**

* ✅ Reviews GitHub repositories for code issues
* ✅ Converts meeting audio to text using NVIDIA Riva
* ✅ Detects meeting intent and schedules automatically
* ✅ Extracts tasks from code reviews, emails, and transcripts
* ✅ Summarizes daily activities using NVIDIA NeMo

---

## 🏗 **Architecture**

### **Agent Workflow**

```
[User] → Streamlit UI
   ↓
Merger Agent (Orchestrator)
   ├── Code Review Agent → Suggests fixes → Task Manager
   ├── Riva ASR Agent → Converts meeting audio → text
   ├── Email Analyzer Agent → Detects meeting requests in emails
   ├── Calendar Agent → Books meetings (Google Calendar API or mock)
   ├── Task Manager Agent → Tracks tasks
   ├── Summary Agent (NeMo) → Creates daily update
   └── Data Organizer Agent (SQL) → Stores history
```

---

## ✨ **Key Features**

* **Code Review**: Pull code from GitHub or upload a file for AI analysis
* **Audio-to-Action**: Riva converts speech to text, detects meeting intent
* **Email Analyzer**: Reads emails and extracts scheduling requests
* **Smart Scheduling**: Conflict resolution with fallback options:

  * A) Next available slot
  * B) Schedule without one participant
  * C) Assign async task
  * D) Suggest async review
* **Dashboard**: See tasks, meetings, and summaries in one place
* **Powered by NVIDIA**:

  * **Riva** → Speech recognition
  * **NeMo** → Natural language summarization
  * GPU acceleration for lightning-fast inference

---

## 🛠 **Tech Stack**

* **Frontend**: Streamlit
* **Backend**: Python + LangChain
* **AI/NVIDIA**:

  * Riva (speech-to-text)
  * NeMo (summarization)
* **Database**: SQLite via SQLAlchemy
* **Integrations**: GitHub API, Google Calendar API

---

## ✅ **How to Run**

```bash
# 1. Clone repo
git clone https://github.com/YOUR_USERNAME/DevSync.git
cd DevSync

# 2. Install dependencies
pip install -r requirements.txt

# 3. (Optional) Start NVIDIA Riva for ASR
git clone https://github.com/nvidia-riva/riva-quickstart
cd riva-quickstart && ./riva_init.sh && ./riva_start.sh

# 4. Launch the app
streamlit run app.py
```

---

## ✅ **Demo Flow**

1. Enter a GitHub repo URL → AI reviews code → Creates tasks
2. Upload a meeting audio file → Riva → Transcript → AI schedules meeting
3. Paste an email → Detects meeting intent → Adds to calendar or tasks
4. Dashboard → See all tasks, meetings, and AI summary

---

## 🔥 **Why DevSync?**

Unlike single-purpose tools like **GitHub Copilot** or **SonarQube**, DevSync provides **end-to-end workflow automation**:
✔ Code Review
✔ Speech Understanding
✔ Email Context Analysis
✔ Smart Scheduling
✔ Task Management

---

## ✅ **What’s Next**

* Real Google Calendar API integration
* Slack/Jira sync for enterprise workflows
* Voice commands via Riva TTS
* Full Docker deployment + Triton Inference Server for scalability

---

## ⚡ Built at \[Hackathon Name]

**Powered by NVIDIA GPUs, Riva, NeMo, and Streamlit**

---

✅ Copy everything **above this line** into your `README.md`.

---

🔥 Do you want me to **add tech badges + architecture diagram image + screenshot placeholders** so it looks more polished before you push it to GitHub?
Or should I **start coding your full Streamlit MVP template next**?
