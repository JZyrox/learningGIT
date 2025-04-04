from telegram import Update
from telegram.ext import Application, MessageHandler, filters, CallbackContext, CommandHandler
from archivotron import verificar_palabra

TOKEN = "8134663089:AAG_VEvt-IAj2nHECZ6d4jr9KBKDzQFHWiM"  # Reemplaza con tu token real

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "¡Hola! Soy un bot de verificación de palabras. Envíame una palabra y te diré si está en mis recursos.\n\n"
        "Ejemplo: 'rojo', 'verde', etc."
    )

async def procesar_palabra(update: Update, context: CallbackContext):
    palabra = update.message.text.strip()
    respuesta = verificar_palabra(palabra)
    await update.message.reply_text(respuesta)

def main():
    app = Application.builder().token(TOKEN).build()
    
    # Handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, procesar_palabra))
    
    print("🤖 Bot iniciado...")
    app.run_polling()

if __name__ == "__main__":
    main()