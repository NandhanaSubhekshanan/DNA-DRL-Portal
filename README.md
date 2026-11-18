# DNA-DRL Steganography – Project Portal

Project documentation portal for the M.Tech research project
**Intelligent Adaptive DNA Encoding Using Deep Reinforcement Learning for Secure Image Steganography**
Amrita Vishwa Vidyapeetham, Coimbatore Campus · M.Tech Computer Science and Engineering

## Folder structure
```
DNA-DRL-Portal/
├── app.py
├── requirements.txt
└── README.md
```

## Install and run
```bash
cd DNA-DRL-Portal
python -m venv venv
# Windows:  venv\Scripts\activate
# macOS/Linux:  source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```
Open http://localhost:8501 in your browser.

## Updating content (all inside app.py)
- Team details: `TEAM_DEFAULTS` (or the "Edit team details" panel on the site)
- Progress: change a status in `PROGRESS` to "completed", "ongoing" or "pending"
- GitHub link: `GITHUB_URL`
- YouTube videos: `url` fields in `VIDEOS`
- Metrics: fill `value` in `METRICS` only when verified results exist

## Documents
PDFs are uploaded from the Documentation page. They are stored per browser session only
(not on the server), so re-upload after a restart.

## Deploy on Streamlit Community Cloud
1. Push the three files to a public GitHub repository.
2. Go to https://share.streamlit.io and sign in with GitHub.
3. Click "Create app" → select the repository and branch (main).
4. Set "Main file path" to `app.py` and click "Deploy".
