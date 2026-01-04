from gtts import gTTS
import feedparser
from datetime import datetime
import os

# --- CONFIG ---
RSS_FEED = 'https://countryairradio.com/category/newsrss/feed/'  # Your actual RSS feed
OUTPUT_FOLDER = './auto_news/'  # Folder for generated MP3s
TOP_N_HEADLINES = 5  # Number of headlines to include
INTRO_TEXT = "Here at CountryAirRadio.com we don't create the news, we promote the headlines from those who do! Letting you choose to further investigate those you find most interesting!"

# Ensure output folder exists
if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

# MP3 file name with timestamp
MP3_FILENAME = f"CAR_LocalNews_{datetime.now().strftime('%Y%m%d_%H%M')}.mp3"

# --- PARSE RSS ---
feed = feedparser.parse(RSS_FEED)

# Get top headlines
headlines = [entry.title for entry in feed.entries[:TOP_N_HEADLINES]]

# Combine intro with headlines
if headlines:
    news_text = INTRO_TEXT + " Here are the top headlines: " + " ... ".join(headlines)
else:
    news_text = INTRO_TEXT + " There are currently no new headlines available."

# --- GENERATE MP3 ---
tts = gTTS(news_text)
output_path = os.path.join(OUTPUT_FOLDER, MP3_FILENAME)
tts.save(output_path)

print(f"Generated MP3: {output_path}")
