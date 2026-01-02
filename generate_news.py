# generate_news.py

from gtts import gTTS
import feedparser
from datetime import datetime

# === CONFIGURATION ===
RSS_FEED = 'https://countryairradio.com/news/rss'  # Replace with your real RSS feed
OUTPUT_FOLDER = './'  # For GitHub Actions, the current folder
TOP_N_HEADLINES = 7

# === Fetch headlines ===
feed = feedparser.parse(RSS_FEED)
headlines = [entry.title for entry in feed.entries[:TOP_N_HEADLINES]]

# === Build the text ===
intro_text = "Here are your top local news headlines for today."
news_text = "\n".join([f"{i+1}. {headline}" for i, headline in enumerate(headlines)])
full_text = f"{intro_text}\n{news_text}"

# === Create MP3 filename with timestamp ===
timestamp = datetime.now().strftime('%Y%m%d_%H%M')
mp3_filename = f"CAR_LocalNews_{timestamp}.mp3"
mp3_path = OUTPUT_FOLDER + mp3_filename

# === Generate MP3 ===
tts = gTTS(text=full_text, lang='en')
tts.save(mp3_path)

print(f"MP3 generated: {mp3_path}")
