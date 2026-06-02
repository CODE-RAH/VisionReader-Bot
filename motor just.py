from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters
from deep_translator import GoogleTranslator
from langdetect import detect
import requests
import os

TOKEN = "8765244446:AAGQkSNYZqIL7EyZzeL0Nt8nYK__SyYe92w"
OCR_API_KEY = "helloworld"


async def photo_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    image_path = None

    try:
        photo = update.message.photo[-1]

        file = await context.bot.get_file(photo.file_id)

        image_path = "image.jpg"
        await file.download_to_drive(image_path)

        with open(image_path, "rb") as f:
            response = requests.post(
                "https://api.ocr.space/parse/image",
                files={"image": f},
                data={
                    "apikey": OCR_API_KEY,
                    "language": "auto",
                    "isOverlayRequired": False,
                    "OCREngine": 2
                },
                timeout=30
            )

        result = response.json()

        if result.get("IsErroredOnProcessing"):
            error_msg = result.get("ErrorMessage", "خطای نامشخص")
            await update.message.reply_text(
                f"❌ خطا در پردازش تصویر:\n{error_msg}"
            )
            return

        parsed_results = result.get("ParsedResults")

        if not parsed_results:
            await update.message.reply_text(
                "❌ هیچ متنی در تصویر پیدا نشد."
            )
            return

        text = parsed_results[0].get("ParsedText", "").strip()

        if not text:
            await update.message.reply_text(
                "❌ هیچ متنی در تصویر پیدا نشد."
            )
            return

        try:
            language = detect(text)
        except:
            language = "unknown"

        if language == "en":
            try:
                translated = GoogleTranslator(
                    source="en",
                    target="fa"
                ).translate(text)

                message = (
                    "📝 متن استخراج شده:\n\n"
                    f"{text}\n\n"
                    "🌍 ترجمه فارسی:\n\n"
                    f"{translated}"
                )

            except:
                message = (
                    "📝 متن استخراج شده:\n\n"
                    f"{text}\n\n"
                    "⚠️ ترجمه انجام نشد."
                )

        else:
            message = (
                "📝 متن استخراج شده:\n\n"
                f"{text}"
            )

        await update.message.reply_text(message)

    except Exception as e:
        await update.message.reply_text(
            f"❌ خطا:\n{str(e)}"
        )

    finally:
        if image_path and os.path.exists(image_path):
            os.remove(image_path)


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(
        MessageHandler(filters.PHOTO, photo_handler)
    )

    print("Bot Started...")
    app.run_polling()


if __name__ == "__main__":
    main()