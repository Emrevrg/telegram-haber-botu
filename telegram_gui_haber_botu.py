
import tkinter as tk
from tkinter import ttk, messagebox
from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import threading
import feedparser
import time
import json
import os

# Global değişkenler
rss_feeds = [
    "https://www.cnnturk.com/feed/rss/news",
    "https://rss.haberler.com/rss.asp?kategori=guncel",
    "https://www.hurriyet.com.tr/rss/gundem",
    "https://www.milliyet.com.tr/rss/rssNew/gundemRss.xml",
    "https://feeds.bbci.co.uk/turkce/rss.xml"
]

sent_links_file = "sent_links.json"
auto_mode = False
bot_token = ""
chat_id = ""

# Haberleri çek
def fetch_news():
    all_news = []
    for url in rss_feeds:
        feed = feedparser.parse(url)
        all_news.extend(feed.entries[:5])
    return all_news

# Daha önce gönderilenleri kontrol et
def load_sent_links():
    if os.path.exists(sent_links_file):
        with open(sent_links_file, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_sent_links(links):
    with open(sent_links_file, "w", encoding="utf-8") as f:
        json.dump(links, f)

# Otomatik gönderim fonksiyonu
def auto_send(bot):
    global auto_mode
    sent = load_sent_links()
    while auto_mode:
        news = fetch_news()
        for entry in news:
            if entry.link not in sent:
                message = f"<b>{entry.title}</b>\n{entry.get('summary', 'Açıklama yok.')}\n<a href='{entry.link}'>🔗 Haberi Gör</a>"
                try:
                    bot.send_message(chat_id=chat_id, text=message[:1024], parse_mode="HTML")
                    sent.append(entry.link)
                    save_sent_links(sent)
                except Exception as e:
                    print("Gönderim hatası:", e)
        time.sleep(1800)  # 30 dakika

# Telegram komutları
def start_command(update: Update, context: CallbackContext):
    global chat_id
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id, text="✅ Bot başarıyla aktif!")

def leave_command(update: Update, context: CallbackContext):
    cid = update.effective_chat.id
    context.bot.send_message(chat_id=cid, text="👋 Bot gruptan ayrılıyor...")
    context.bot.leave_chat(chat_id=cid)

def manual_news(update: Update, context: CallbackContext):
    news = fetch_news()
    for entry in news[:3]:
        message = f"<b>{entry.title}</b>\n{entry.get('summary', 'Açıklama yok.')}\n<a href='{entry.link}'>🔗 Haberi Gör</a>"
        update.message.reply_text(text=message[:1024], parse_mode="HTML")

# GUI başlat
def run_gui():
    def connect_bot():
        global bot_token, chat_id, auto_mode, updater
        bot_token = token_entry.get().strip()
        if not bot_token:
            messagebox.showerror("Hata", "Token boş olamaz!")
            return

        updater = Updater(token=bot_token, use_context=True)
        dp = updater.dispatcher
        dp.add_handler(CommandHandler("start", start_command))
        dp.add_handler(CommandHandler("manual", manual_news))
        dp.add_handler(CommandHandler("leave", leave_command))

        threading.Thread(target=updater.start_polling, daemon=True).start()
        messagebox.showinfo("Bağlandı", "Bot Telegram'a bağlandı!")

    def start_auto():
        global auto_mode
        if not bot_token or not chat_id:
            messagebox.showerror("Hata", "Bot veya chat ID tanımlı değil!")
            return
        auto_mode = True
        threading.Thread(target=auto_send, args=(Bot(bot_token),), daemon=True).start()
        messagebox.showinfo("Başlatıldı", "Otomatik gönderim başlatıldı.")

    def stop_auto():
        global auto_mode
        auto_mode = False
        messagebox.showinfo("Durduruldu", "Otomatik gönderim durduruldu.")

    root = tk.Tk()
    root.title("Telegram Haber Botu")
    root.geometry("400x250")

    ttk.Label(root, text="Bot Token:").pack(pady=5)
    token_entry = ttk.Entry(root, width=50)
    token_entry.pack(pady=5)

    ttk.Button(root, text="🔌 Telegram'a Bağlan", command=connect_bot).pack(pady=5)
    ttk.Button(root, text="▶️ Otomatik Başlat", command=start_auto).pack(pady=5)
    ttk.Button(root, text="⏹️ Otomatik Durdur", command=stop_auto).pack(pady=5)

    root.mainloop()

# Ana uygulama
if __name__ == "__main__":
    run_gui()
