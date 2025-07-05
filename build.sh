#!/bin/bash

# Activar entorno virtual
echo "🚀 Activando entorno virtual..."
source .venv/Scripts/activate || { echo "❌ Error: no se pudo activar el entorno virtual"; exit 1; }

# Instalar requisitos
echo "📦 Instalando dependencias..."
pip install --upgrade pip
pip install -r requirements.txt || { echo "❌ Error al instalar dependencias"; exit 1; }

# Limpiar carpeta anterior
echo "🧹 Eliminando carpeta public anterior..."
rm -rf public

# Inicializar y exportar el proyecto Reflex
echo "📤 Exportando frontend con Reflex..."
reflex init
reflex export --frontend-only || { echo "❌ Error en exportación Reflex"; exit 1; }

# Descomprimir frontend
echo "📦 Descomprimiendo frontend.zip..."
unzip -o frontend.zip -d public || { echo "❌ Error al descomprimir frontend"; exit 1; }
rm -f frontend.zip
echo "📦 Eliminado frontend.zip..."
# Verificar que avatar.jpg esté exportado
if [ -f "public/avatar.jpg" ]; then
    echo "✅ avatar.jpg encontrado correctamente en carpeta public/"
else
    echo "⚠️ ADVERTENCIA: public/avatar.jpg no existe. ¿Está en la ruta correcta en assets/?"
fi

echo "✅ Build completado con éxito."
deactivate