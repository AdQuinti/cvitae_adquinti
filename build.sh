source .venv/Scripts/activate
pip install --upgrade pip
echo "Creando archivo requerimientos..."
pip install -r requirements.txt
echo "Construyendo el proyecto Reflex..."
reflex init
reflex export --frontend-only
rm -rf public
unzip frontend.zip -d public
rm -f frontend.zip
deactivate