# Actualización forzada a repositorio git
# https://github.com/AdQuinti/cvitae_adquinti.git
echo "\n=== Subiendo cambios a GitHub - Forzado ==="
git add .
git commit -m "Actualización automática $(date)"
git push -u -f origin main
echo "\n¡Proceso completado!"