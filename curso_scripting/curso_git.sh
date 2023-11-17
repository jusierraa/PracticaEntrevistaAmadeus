#!/bin/bash
#Author Juan Camilo Sierra 
#Este script es para practicar subir cambios a GIT

echo "Nombre de la rama secundaria"
read nombre

git checkout -b $nombre

git status

git add .

git commit -m "Estoy probando scripting con GIT"

git push origin RamaTercera

jusierraa

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

