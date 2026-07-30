#!/bin/bash

set -e

echo "======================================"
echo " ERMETES GITHUB SYNC"
echo "======================================"

PROJECT=$(basename "$PWD")

echo "Progetto: $PROJECT"

# controllo git
if [ ! -d ".git" ]; then
    echo "Git non inizializzato. Creo repository locale..."
    git init
fi


# mostra stato

echo ""
echo "STATO FILE:"
git status


echo ""
read -p "Messaggio commit: " MSG

if [ -z "$MSG" ]; then
    MSG="Aggiornamento progetto Ermetes"
fi


echo ""
echo "Aggiungo file..."

git add .


echo ""
echo "Creo commit..."

git commit -m "$MSG" || echo "Nessun cambiamento da committare"


echo ""
echo "Controllo remote..."

REMOTE=$(git remote -v | head -1 || true)


if [ -z "$REMOTE" ]; then

    echo ""
    echo "NESSUN REMOTE GITHUB CONFIGURATO"

    read -p "Inserisci URL repository GitHub: " URL

    git remote add origin "$URL"

fi


echo ""
echo "Push GitHub..."

BRANCH=$(git branch --show-current)

if [ -z "$BRANCH" ]; then
    git branch -M main
    BRANCH="main"
fi


git push -u origin "$BRANCH"


echo ""
echo "======================================"
echo " COMPLETATO"
echo " GitHub aggiornato"
echo "======================================"
