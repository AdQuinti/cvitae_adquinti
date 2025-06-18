# Actualización forzada a repositorio git
# https://github.com/AdQuinti/cvitae_adquinti.git
#echo "\n=== Subiendo cambios a GitHub - Forzado ==="
#git add .
#git commit -m "Actualización automática $(date)"
#git push -u -f origin main
#echo "\n¡Proceso completado!"

#!/bin/bash
echo "⚙️  Añadiendo todos los archivos, incluyendo ignorados forzadamente..."

# Fuerza agregar avatar.jpg (aunque esté en .gitignore)
git add -f assets/external/avatar.jpg

# Añade el resto normalmente (no forzará ignorados, solo avatar.jpg si quieres asegurarlo)
git add .

echo "📦 Escriba su mensaje de commit:"
read mensaje

git commit -m "$mensaje"

echo "⬆️ Subiendo a GitHub..."
git push origin main

echo "✅ ¡Subida completada!"
