source .venv/Scripts/activate
pip install --upgrade pip
pip install -r requirements.txt
reflex init
reflex export --frontend-only 
reflex -fr public
unzip frontend.zip -d public
rm -f frontend.zip
desactivate


