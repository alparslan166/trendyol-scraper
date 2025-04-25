#!/usr/bin/env bash
set -o errexit

# Google Chrome için resmi repo ekleme
curl -sSL https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list

# Gerekli bağımlılıkları kur
apt-get update
apt-get install -y \
    google-chrome-stable \
    libx11-xcb1 \
    libxcb1 \
    libxcomposite1 \
    libxcursor1 \
    libxdamage1 \
    libxi6 \
    libxtst6 \
    libnss3 \
    libcups2 \
    libxss1 \
    libxrandr2 \
    libasound2 \
    libatk1.0-0 \
    libgtk-3-0 \
    libdrm2 \
    mesa-utils

# Python bağımlılıkları
pip3 install -r requirements.txt