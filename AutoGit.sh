#!/bin/bash

# Ejecuta el build primero
echo "🔧 Ejecutando build.sh..."
./build.sh || { echo "❌ Error en el build. Revisa antes de subir."; exit 1; }

# Forzar agregar avatar.jpg directamente
echo "📸 Asegurando que avatar.jpg se suba..."
git add -f assets/avatar.jpg
git add -f assets/external/avatar.jpg

# Agregar todos los archivos restantes
echo "📁 Añadiendo todos los archivos..."
git add .

# Mensaje de commit
echo "📝 Escriba el mensaje de commit:"
read mensaje
git commit -m "$mensaje"

# Subir a GitHub
echo "⬆️ Subiendo cambios a GitHub..."
git push origin main

echo "✅ ¡Repositorio actualizado con éxito! Revisa tu web en Vercel."
