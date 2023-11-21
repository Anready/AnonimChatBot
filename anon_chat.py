from aiogram import *

API_TOKEN = 'API_TOKEN'

chat_rooms = {}
waiting_rooms = set()

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def handle_start(message: types.Message):
    user_id = message.from_user.id
    await bot.send_message(chat_id=user_id, text="Привет напиши /next чтобы начать поиск собеседника. Создатели бота - "
                                                 "Anready")


@dp.message_handler(commands=['next'])
async def handle_start(message: types.Message):
    my_user_id = message.from_user.id
    try:
        try:
            another_user_id = chat_rooms[my_user_id]
            del chat_rooms[my_user_id], chat_rooms[another_user_id]
            await bot.send_message(chat_id=another_user_id, text="Твой собеседник завершил беседу")
            await bot.send_message(chat_id=my_user_id, text="Ты завершил беседу")
        except KeyError:
            another_user_id = waiting_rooms.pop()
            chat_rooms[another_user_id] = my_user_id
            chat_rooms[my_user_id] = another_user_id

            await bot.send_message(chat_id=my_user_id, text="Собеседник найден!")
            await bot.send_message(chat_id=another_user_id, text="Собеседник найден!")
    except KeyError:
        waiting_rooms.add(my_user_id)
        await bot.send_message(chat_id=my_user_id, text="Идет подбор собеседника")


@dp.message_handler(commands=['stop'])
async def handle_start(message: types.Message):
    my_user_id = message.from_user.id
    try:
        another_user_id = chat_rooms[my_user_id]
        del chat_rooms[my_user_id], chat_rooms[another_user_id]
        await bot.send_message(chat_id=another_user_id, text="Твой собеседник завершил беседу")
        await bot.send_message(chat_id=my_user_id, text="Ты завершил беседу")
    except KeyError:
        await bot.send_message(chat_id=my_user_id, text="Ты сейчас не переписываешься, напиши /next чтобы начать")


@dp.message_handler()
async def handle_all(message: types.Message):
    my_user_id = message.from_user.id
    try:
        await bot.send_message(chat_id=chat_rooms[my_user_id], text=message.text)
    except KeyError:
        await bot.send_message(chat_id=my_user_id, text="Ты сейчас не переписываешься, напиши /next чтобы начать")


@dp.message_handler(content_types=[types.ContentType.STICKER])
async def handle_sticker(message: types.Message):
    # Обработка стикера
    sticker_id = message.sticker.file_id
    my_user_id = message.from_user.id
    try:
        await bot.send_sticker(chat_rooms[my_user_id], sticker_id)
    except KeyError:
        await bot.send_message(chat_id=my_user_id, text="Ты сейчас не переписываешься, напиши /next чтобы начать")


@dp.message_handler(content_types=[types.ContentType.PHOTO])
async def handle_photo(message: types.Message):
    # Обработка фото
    my_user_id = message.from_user.id
    photo_id = message.photo[-1].file_id
    try:
        await bot.send_photo(chat_rooms[my_user_id], photo_id)
    except KeyError:
        await bot.send_message(chat_id=my_user_id, text="Ты сейчас не переписываешься, напиши /next чтобы начать")


@dp.message_handler(content_types=[types.ContentType.DOCUMENT])
async def handle_document(message: types.Message):
    # Обработка документа
    my_user_id = message.from_user.id
    try:
        document_id = message.document.file_id
        await bot.send_document(chat_rooms[my_user_id], document_id)
    except KeyError:
        await bot.send_message(chat_id=my_user_id, text="Ты сейчас не переписываешься, напиши /next чтобы начать")


@dp.message_handler(content_types=[types.ContentType.AUDIO])
async def handle_audio(message: types.Message):
    # Обработка аудио
    my_user_id = message.from_user.id
    try:
        audio_id = message.audio.file_id
        await bot.send_audio(chat_rooms[my_user_id], audio_id)
    except KeyError:
        await bot.send_message(chat_id=my_user_id, text="Ты сейчас не переписываешься, напиши /next чтобы начать")


@dp.message_handler(content_types=[types.ContentType.VIDEO])
async def handle_video(message: types.Message):
    my_user_id = message.from_user.id
    try:
        video_id = message.video.file_id
        await bot.send_video(chat_rooms[my_user_id], video_id)
    except KeyError:
        await bot.send_message(chat_id=my_user_id, text="Ты сейчас не переписываешься, напиши /next чтобы начать")


@dp.message_handler(content_types=[types.ContentType.VOICE])
async def handle_voice(message: types.Message):
    my_user_id = message.from_user.id
    try:
        voice_id = message.voice.file_id
        await bot.send_voice(chat_rooms[my_user_id], voice_id)
    except KeyError:
        await bot.send_message(chat_id=my_user_id, text="Ты сейчас не переписываешься, напиши /next чтобы начать")


@dp.message_handler(content_types=[types.ContentType.VIDEO_NOTE])
async def handle_video_note(message: types.Message):
    my_user_id = message.from_user.id
    try:
        video_note_id = message.video_note.file_id
        await bot.send_video_note(chat_rooms[my_user_id], video_note_id)
    except KeyError:
        await bot.send_message(chat_id=my_user_id, text="Ты сейчас не переписываешься, напиши /next чтобы начать")


@dp.message_handler(content_types=[types.ContentType.LOCATION])
async def handle_location(message: types.Message):
    my_user_id = message.from_user.id
    try:
        latitude = message.location.latitude
        longitude = message.location.longitude
        await bot.send_location(chat_rooms[my_user_id], latitude, longitude)
    except KeyError:
        await bot.send_message(chat_id=my_user_id, text="Ты сейчас не переписываешься, напиши /next чтобы начать")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
