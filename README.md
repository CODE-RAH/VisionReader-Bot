![header](https://capsule-render.vercel.app/api?type=waving&amp;height=240&amp;color=0:0ea5e9,100:0f172a&amp;text=VisionReader%20Bot&amp;fontColor=ffffff&amp;fontSize=40&amp;fontAlignY=40&amp;desc=OCR%20%2B%20Auto%20Translate%20Telegram%20Bot&amp;descAlignY=63&amp;animation=twinkling)

<div align="right">

# 👁️ VisionReader Bot

**توسعه‌دهنده:** امیر فرخانی | **تیم:** CODE RAH

> استفاده، بازنشر یا تولید محتوا از این پروژه، منوط به ذکر منبع و نام تیم CODE RAH است.

</div>

---

## 📌 معرفی پروژه

**VisionReader Bot** یک ربات تلگرام هوشمند است که تصویر دریافت می‌کند، متن داخل آن را با **OCR** استخراج کرده و در صورت انگلیسی بودن، به‌صورت خودکار آن را به **فارسی** ترجمه می‌کند.

---

## ✨ ویژگی‌ها

| ویژگی | توضیح |
|---|---|
| 🔍 استخراج متن (OCR) | پردازش تصویر با موتور OCR.space |
| 🌐 ترجمه خودکار | ترجمه متن انگلیسی به فارسی با `deep-translator` |
| 🧠 تشخیص زبان | تشخیص خودکار زبان متن با `langdetect` |
| 🧹 مدیریت فایل | فایل موقت پس از پردازش به‌صورت خودکار حذف می‌شود |
| ⚡ موتور OCR پیشرفته | استفاده از `OCREngine 2` برای دقت بالاتر |

---

## 🛠️ پیش‌نیازها

- Python 3.8+
- اتصال به اینترنت
- توکن ربات تلگرام (از [@BotFather](https://t.me/BotFather))
- کلید API از [OCR.space](https://ocr.space/ocrapi)

---

## 🚀 نصب و اجرا

**۱. دریافت پروژه**

git clone https://github.com/CodeRah-ir/VisionReaderBot.git
cd VisionReaderBot

**۲. نصب کتابخانه‌ها**
bash
pip install python-telegram-bot deep-translator langdetect requests

**۳. تنظیم توکن و API Key**

در فایل `main.py` مقادیر زیر را جایگزین کن:
python
TOKEN = "YOUR_BOT_TOKEN_HERE"
OCR_API_KEY = "YOUR_OCR_API_KEY_HERE"

**۴. اجرا**
bash
python main.py

---

## 📂 ساختار پروژه


VisionReaderBot/
│
├── main.py          # فایل اصلی ربات
└── README.md        # مستندات

---

## ⚙️ نحوه استفاده

1. ربات را در تلگرام پیدا کن
2. یک تصویر حاوی متن ارسال کن
3. ربات متن را استخراج می‌کند
4. اگر متن انگلیسی باشد، ترجمه فارسی هم نمایش داده می‌شود ✅

---

## 🏢 تیم CODE RAH

تیم **CODE RAH** در حوزه‌های زیر فعالیت می‌کند:

- 💻 **برنامه‌نویسی** — Python, Web, Bot Development
- 🔐 **امنیت سایبری** — Penetration Testing, Network Security
- 🤖 **هوش مصنوعی** — Machine Learning, Computer Vision
- 🌐 **اینترنت اشیاء** — IoT, Embedded Systems

---

## 📬 ارتباط با ما

پروژه‌های بیشتر و دوره‌های آموزشی تیم CODE RAH را دنبال کنید.

---

<div align="center">

*«کدنویسی فقط نوشتن برنامه نیست؛ ساختن آینده است.»*

⭐ اگر این پروژه برات مفید بود، ستاره بده!

![footer](https://capsule-render.vercel.app/api?type=waving&amp;height=120&amp;color=0:0f172a,100:0ea5e9&amp;section=footer)

</div>
`
