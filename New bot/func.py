from aiogram import Router, types
# from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
# from aiogram.fsm.state import StatesGroup, State
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from keyboards import contact_btn, lang_btn  
from sqlalchemy import select
from database.models import User, async_session

router = Router()


async def cmd_start(message: types.Message):
    user_id = message.from_user.id
    async with async_session() as session:
        stmt = select(User).where(User.id == user_id)
        result = await session.execute(stmt)
        user = result.scalars().first()

        if user:
            await message.answer("Siz allaqachon ro'yxatdan o'tgansiz. Til va rolni tanlang.", reply_markup=lang_btn)
        else:
            await message.answer("Ro'yxatdan o'tish uchun telefon raqamingizni yuboring:", reply_markup=contact_btn)


async def get_help(message: types.Message):
    await message.answer("Bu botdan siz mashinalarni sotishingiz yoki sotib olishingiz mumkin \nSiz ro'yhatdan o'tish "
                         "paytida o'z pozitsiyangizni tanlashingiz va botdan to'liq foydalanishingiz mumkin.")


async def get_news(message: types.Message):
    await message.answer(
        f"Mashinalar haqida eng so'nggi yangiliklardan xabardor bo'lish uchun shu kanalga a'zo bo'ling <a "
        f"href='https://t.me/botforlearning'>KANAL</a>",
        HTML='HTML')



# @router.message(lambda message: message.text == "Ma'lumotlarni tahrirlash")
# async def edit_profile(message: types.Message):
#     user_id = message.from_user.id

#     async with get_session() as session:
#         stmt = select(User).where(User.id == user_id)
#         result = await session.execute(stmt)
#         user = result.scalars().first()

#         if user:
#             await message.answer("Ma'lumotlaringizni tahrirlash uchun quyidagi variantlarni tanlang:",
#                                  reply_markup=ReplyKeyboardMarkup(
#                                      keyboard=[
#                                          [KeyboardButton(text="Ism va Familiya"), KeyboardButton(text="Telefon raqam")],
#                                          [KeyboardButton(text="Til"), KeyboardButton(text="Rol")]
#                                      ],
#                                      resize_keyboard=True
#                                  ))
#         else:
#             await message.answer("Foydalanuvchi topilmadi. Iltimos, ro'yxatdan o'ting.")


# @router.message(lambda message: message.text == "Ism va Familiya")
# async def edit_name(message: types.Message, state: FSMContext):
#     user_id = message.from_user.id
#     await message.answer("Iltimos, yangi ismingiz va familiyangizni kiriting:")

#     @router.message()
#     async def handle_new_name(message: types.Message, state: FSMContext):
#         new_name = message.text.split(" ")
#         first_name = new_name[0]
#         last_name = new_name[1] if len(new_name) > 1 else ""

#         async with get_session() as session:
#             stmt = select(User).where(User.id == user_id)
#             result = await session.execute(stmt)
#             user = result.scalars().first()

#             if user:
#                 user.first_name = first_name
#                 user.last_name = last_name
#                 await session.commit()
#                 await message.answer("Ismingiz va familiyangiz muvaffaqiyatli yangilandi.")
#             else:
#                 await message.answer("Foydalanuvchi topilmadi. Iltimos, qayta urinib ko'ring.")


# @router.message(lambda message: message.text == "Telefon raqam")
# async def edit_phone_number(message: types.Message):
#     await message.answer("Iltimos, yangi telefon raqamingizni yuboring:", reply_markup=ReplyKeyboardMarkup(
#         keyboard=[
#             [KeyboardButton(text="📞 Telefon raqam", request_contact=True)]
#         ],
#         resize_keyboard=True
#     ))


# @router.message()
# async def handle_new_contact(message: types.Message):
#     user_id = message.from_user.id
#     contact = message.contact

#     async with get_session() as session:
#         stmt = select(User).where(User.id == user_id)
#         result = await session.execute(stmt)
#         user = result.scalars().first()

#         if user:
#             user.phone_number = contact.phone_number
#             await session.commit()
#             await message.answer("Telefon raqamingiz muvaffaqiyatli yangilandi.")
#         else:
#             await message.answer("Foydalanuvchi topilmadi. Iltimos, qayta urinib ko'ring.")


# @router.message(lambda message: message.text == "Til")
# async def edit_language(message: types.Message):
#     user_id = message.from_user.id
#     await message.answer("Iltimos, yangi tilni tanlang:", reply_markup=ReplyKeyboardMarkup(
#         keyboard=[
#             [KeyboardButton(text="🇺🇿 Uzbek"), KeyboardButton(text="🇷🇺 Rus"), KeyboardButton(text="🇬🇧 Ingliz")]
#         ],
#         resize_keyboard=True
#     ))


# @router.message(lambda message: message.text in ["🇺🇿 Uzbek", "🇷🇺 Rus", "🇬🇧 Ingliz"])
# async def handle_new_language(message: types.Message):
#     user_id = message.from_user.id
#     language = message.text

#     async with get_session() as session:
#         stmt = select(User).where(User.id == user_id)
#         result = await session.execute(stmt)
#         user = result.scalars().first()

#         if user:
#             user.language = language
#             await session.commit()
#             await message.answer("Til muvaffaqiyatli yangilandi.")
#         else:
#             await message.answer("Foydalanuvchi topilmadi. Iltimos, qayta urinib ko'ring.")


# @router.message(lambda message: message.text == "Rol")
# async def edit_role(message: types.Message):
#     user_id = message.from_user.id
#     await message.answer("Iltimos, yangi rolni tanlang:", reply_markup=ReplyKeyboardMarkup(
#         keyboard=[
#             [KeyboardButton(text="Sotuvchi"), KeyboardButton(text="Haridor")]
#         ],
#         resize_keyboard=True
#     ))


# @router.message(lambda message: message.text in ["Sotuvchi", "Haridor"])
# async def handle_new_role(message: types.Message):
#     user_id = message.from_user.id
#     role = message.text

#     async with get_session() as session:
#         stmt = select(User).where(User.id == user_id)
#         result = await session.execute(stmt)
#         user = result.scalars().first()

#         if user:
#             user.role = role
#             await session.commit()
#             await message.answer("Rol muvaffaqiyatli yangilandi.")
#         else:
#             await message.answer("Foydalanuvchi topilmadi. Iltimos, qayta urinib ko'ring.")


