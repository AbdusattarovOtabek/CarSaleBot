from aiogram import types, Router
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from database.models import User, async_session
from keyboards import handle_role, lang_btn

router = Router()

async def set_contact(message: types.Message):
    user_id = message.from_user.id

    try:
        async with async_session() as session:
            stmt = select(User).where(User.id == user_id)
            result = await session.execute(stmt)
            existing_user = result.scalars().first()

            if existing_user:
                # Agar foydalanuvchi mavjud bo'lsa, u holda ma'lumotlarni yangilash
                existing_user.first_name = message.from_user.first_name
                existing_user.last_name = message.from_user.last_name
                existing_user.username = message.from_user.username
                # phone_number maydonini qo'shishingiz mumkin, agar kerak bo'lsa
                await session.commit()
                await message.answer("Siz allaqachon ro'yxatdan o'tgansiz. Ma'lumotlaringiz yangilandi.")
            else:
                # Agar foydalanuvchi mavjud bo'lmasa, yangi foydalanuvchi qo'shish
                new_user = User(
                    id=user_id,
                    first_name=message.from_user.first_name,
                    last_name=message.from_user.last_name,
                    username=message.from_user.username
                )
                session.add(new_user)
                await session.commit()
                await message.answer("Ro'yxatdan o'tish muvaffaqiyatli. Iltimos, tilni tanlang:", reply_markup=lang_btn)
    except IntegrityError as e:
        await session.rollback()  # Xato bo'lganda o'zgarishlarni bekor qilish
        await message.answer(f"Xatolik yuz berdi: {str(e)}")

@router.message(lambda message: message.text in ["🇺🇿 Uzbek", "🇷🇺 Rus", "🇬🇧 Ingliz"])
async def set_language(message: types.Message):
    user_id = message.from_user.id
    language = message.text

    try:
        async with async_session() as session:
            stmt = select(User).where(User.id == user_id)
            result = await session.execute(stmt)
            user = result.scalars().first()

            if user:
                user.language = language
                await session.commit()  # O'zgarishlarni bazaga yozish
                await message.answer("Rolni tanlang:", reply_markup=handle_role)
            else:
                await message.answer("Foydalanuvchi topilmadi. Iltimos, ro'yxatdan o'ting.")
    except IntegrityError:
        await session.rollback()  # Xato bo'lganda o'zgarishlarni bekor qilish
        await message.answer("Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")

@router.message(lambda message: message.text in ["Sotuvchi", "Haridor"])
async def set_role(message: types.Message):
    user_id = message.from_user.id
    role = message.text

    try:
        async with async_session() as session:
            stmt = select(User).where(User.id == user_id)
            result = await session.execute(stmt)
            user = result.scalars().first()

            if user:
                user.role = role
                await session.commit()  # O'zgarishlarni bazaga yozish
                await message.answer("Siz muvaffaqiyatli ro'yxatdan o'tdingiz! Botni ishlatishni boshlashingiz mumkin.")
            else:
                await message.answer("Foydalanuvchi topilmadi. Iltimos, ro'yxatdan o'ting.")
    except IntegrityError:
        await session.rollback()  # Xato bo'lganda o'zgarishlarni bekor qilish
        await message.answer("Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
