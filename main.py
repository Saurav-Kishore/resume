from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

# ── Profile Data ─────────────────────────────────────────────────────────────

PROFILE = {
    "name": "Saurav Kishore",
    "title": "Senior Engineer at Qualcomm | AI & Android Expert",
    "location": "Hyderabad, India",
    "education": "B.Tech in Computer Science & Engineering",
    "university": "The LNM Institute of Information Technology, Jaipur",
    "cgpa": "9.01/10.00",
    "bio": "Engineered a 24/7 autonomous Multi-Agent AI system for TrustZone security at Qualcomm. Recognised as a top 10% performer at Samsung, spearheaded one of the first AI projects at Samsung Noida — which led to a dedicated 15-engineer AI task force. Built an AI-driven Knowledge Graph powering personalised recommendations for 20M+ OneUI 7 devices.",
    "skills": [
        "Java",
        "Kotlin",
        "Python",
        "Android",
        "MVVM",
        "Kotlin Coroutines",
        "Jetpack Compose",
        "System Design",
        "LLM / AI Agents",
        "RxJava",
        "Hilt / Dagger",
        "Room / SQLite",
        "Retrofit",
        "Scikit-learn",
        "Git / Gerrit",
        "CI/CD",
    ],
    "experience": [
        {"role": "Senior Engineer", "company": "Qualcomm", "years": "Jul 2025 – Present"},
        {"role": "Engineer / Android App Developer", "company": "Samsung Electronics", "years": "Jul 2021 – Jul 2025"},
        {"role": "R&D Intern", "company": "Samsung Electronics", "years": "Jan 2021 – May 2021"},
    ],
    "projects": [
        "Galaxy Z Flip5 Cover Screen Phone App — led 3 devs, 10M+ users, won Excellence Award",
        "24/7 Autonomous Multi-Agent AI System — reduced manual monitoring by ~64%, saved ~35 hrs/week",
        "AI Knowledge Graph for Personalised Recommendations — deployed to 20M+ OneUI 7 devices",
        "WearOS Phone App Refactoring — led 5 devs, Kotlin/MVVM migration, ~48% faster launch, ~85% test coverage",
    ],
    "patents": [
        "System & Method for Prioritising and Contextualising User Data on User Equipment (Indian Patent, filed Dec 2024)",
    ],
    "socials": {
        "linkedin": "linkedin.com/in/sauravkishore",
        "github": "github.com/Saurav-Kishore",
        "email": "saurav_kishore@outlook.com",
    },
}


@app.get("/api/profile")
async def get_profile():
    """Return Saurav Kishore's professional profile data."""
    return PROFILE


@app.get("/")
async def index():
    """Serve the static dashboard — works standalone, no server needed."""
    return FileResponse("index.html")
