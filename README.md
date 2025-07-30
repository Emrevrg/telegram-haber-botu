# telegram-haber-botu

# 📦 Telegram Haber Botu (Kullanıcı Arayüzlü - Otomatik & Manuel Gönderim)

Bu bot, en güncel haberleri çekerek Telegram kanalınıza veya grubunuza otomatik ya da manuel olarak gönderir. Tamamen kullanıcı dostu bir arayüz ile çalışır. Hiçbir kod bilgisi gerekmez.

---

## ✅ GEREKLİLER

- Python 3.7 veya üzeri kurulu olmalı

### 🔧 Gerekli Paketlerin Kurulumu:
Terminale (komut istemcisine) aşağıdaki komutu yaz:

```
pip install feedparser python-telegram-bot
```

---

## 🚀 BOT NASIL ÇALIŞTIRILIR?

1. Dosyanın bulunduğu klasörde terminali açın.
2. Aşağıdaki komutu yazın:

```
python telegram_gui_haber_botu.py
```

3. Karşınıza çıkan pencere üzerinden işlemleri yapın:

| Buton / Alan               | Açıklama |
|---------------------------|----------|
| `Bot Token:`              | @BotFather'dan aldığınız bot tokenını buraya yapıştırın |
| `🔌 Telegram'a Bağlan`     | Telegram'a bağlantıyı kurar ve komutları dinlemeye başlar |
| `▶️ Otomatik Başlat`       | 30 dakikada bir haber gönderimini başlatır |
| `⏹️ Otomatik Durdur`       | Otomatik gönderimi durdurur |

---

## 📱 TELEGRAM ÜZERİNDE KULLANIM

Bot Telegram grubuna/kanaına **eklenmeli** ve **admin yapılmalıdır**.

Botu aktifleştirmek için grubunuzda şu komutları kullanabilirsiniz:

| Komut      | Açıklama |
|------------|----------|
| `/start`   | Bot çalıştığını bildirir ve grup ID’sini alır |
| `/manual`  | Son 3 haberi hemen gönderir |
| `/leave`   | Bot gruptan ayrılır ve mesaj bırakır |

---

## 💾 TEKNİK DETAYLAR

- Gönderilen haberlerin bağlantıları `sent_links.json` dosyasında tutulur. Aynı haber tekrar gönderilmez.
- Haber formatı: **başlık**, açıklama ve **"haberi oku" bağlantısı**
- `HTML` parse mode kullanılır (Telegram'da şık görünüm)
- Kod arka planda otomatik olarak çalışır, pencere açık kalır.

---

## 🛠️ SIK SORULANLAR

**Q: Bot çalışmıyor, neden?**  
A: Muhtemelen `token` hatalı ya da bot gruba admin yapılmadı.

**Q: Gruptan çıkarınca neden mesaj atıyor?**  
A: Bu özellik, bot ayrılırken kullanıcıyı bilgilendirmek için vardır.

**Q: Aynı haber neden tekrar gelmiyor?**  
A: Daha önce gönderilen linkler `sent_links.json` dosyasında saklanır.

---

Her şey hazır! Sorunsuz şekilde kurulup çalıştırılabilir.

