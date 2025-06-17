
# 🌦️ Termux Weather CLI Tool

Ye ek simple aur useful Termux CLI tool hai jo OpenWeatherMap API ka use karke aapko real-time weather batata hai. Aap sirf shehar ka naam likhein, aur tool aapko temperature, weather condition, humidity aur wind speed bata dega — sab CLI me.

---

## 🛠️ Requirements

Start karne se pehle ye packages install kar lena:

```bash
pkg update -y
pkg install python git -y
pip install requests
```

---

## 🔧 Installation

Yeh commands Termux me run karein:

```bash
git clone https://github.com/BasitDeveloperpk/Weather-cli-termux.git
cd Weather-cli-termux
bash install_weather.sh
source ~/.bashrc
```

Installer:
- Script ko `$HOME/.weather` me copy karega
- Bash alias set karega: `weather`
- Pehli baar run pe API key mangta hai (sirf ek martaba)

---

## 🌐 API Key Setup

1. Jaao: https://openweathermap.org/api
2. Sign up karo aur “API key” copy karo
3. Jab tool pehli dafa run hoga, aap se yeh key maangega
4. Key permanent save ho jaayegi

---

## ▶️ Usage

Install hone ke baad bas yeh likho:

```bash
weather
```

Aapse shehar ka naam puchega — jaise:

```
🏙️  Shehar ka naam likho: Lahore
➡️  API key daalein: YOUR_API_KEY
```

Output kuch is tarah aayega:

```
📊 Weather Report:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📍 Shehar       : Lahore
🌡️  Darja Hararat: 33°C
🌥️  Mausam       : Clear Sky
💧 Humidity     : 45%
💨 Wind Speed   : 3.2 m/s
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 🧹 Uninstall

Agar aap tool hataana chahein:

```bash
rm -rf ~/.weather
sed -i '/alias weather=/d' ~/.bashrc
source ~/.bashrc
```

---

## 👨‍💻 Author

Developed by **BasitDeveloperpk**  
GitHub: [https://github.com/BasitDeveloperpk](https://github.com/BasitDeveloperpk)
