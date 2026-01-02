from gtts import gTTS
import feedparser
from datetime import datetime
import os

# --- CONFIG ---
RSS_FEED = 'https://countryairradio.com/news/rss'  # Your actual RSS feed
OUTPUT_FOLDER = './auto_news/'  # Folder for generated MP3s
TOP_N_HEADLINES = 5

if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

MP3_FILENAME = f"CAR_LocalNews_{datetime.now().strftime('%Y%m%d_%H%M')}.mp3"

# --- PARSE RSS ---
feed = feedparser.parse(RSS_FEED)
headlines = [entry.title for entry in feed.entries[:TOP_N_HEADLINES]]
news_text = "Here are the top headlines: " + " ... ".join(headlines)

# --- GENERATE MP3 ---
tts = gTTS(news_text)
output_path = os.path.join(OUTPUT_FOLDER, MP3_FILENAME)
tts.save(output_path)

print(f"Generated MP3: {output_path}")
