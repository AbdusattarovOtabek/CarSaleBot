# Car Sale Bot

Bu loyiha avtomobillarni sotish va xarid qilish uchun Telegram botini yaratishga mo'ljallangan. Bot **Aiogram 3.3** va **SQLAlchemy 2.0** yordamida ishlab chiqilgan.

## Loyihaning asosiy funksiyalari
- Avtomobil e'lonlarini joylashtirish.
- E'lonlarni qidirish va ko'rish.
- Sotuvchi bilan bevosita bog'lanish uchun qulaylik.
- Foydalanuvchilarni ro'yxatdan o'tkazish va autentifikatsiya qilish.

## Texnologiyalar
- **Bot framework:** Aiogram 3.3
- **Ma'lumotlar bazasi:** SQLAlchemy 2.0
- **Til:** Python

## O'rnatish bo'yicha yo'riqnoma
1. Repository’ni klonlash:
   ```bash
   git clone https://github.com/AbdusattarovOtabek/CarSaleBot.git
   cd New bot
   ```
2. Virtual muhitni yaratish va faollashtirish:
   ```bash
   python -m venv env
   source env/bin/activate  # Windows uchun: env\Scripts\activate
   ```
3. Kerakli kutubxonalarni o'rnatish:
   ```bash
   pip install -r requirements.txt
   ```
4. Bot uchun `bot_config.py` faylini sozlash:
   Faylda quyidagi parametrlarni to'ldiring:
   ```python
   BOT_TOKEN = "sizning-bot-tokeningiz"
   DATABASE_URL = "sqlite:///database.db"  # yoki boshqa DB URL
   ```
5. Ma'lumotlar bazasini yaratish:
   ```bash
   python create_db.py
   ```
6. Botni ishga tushirish:
   ```bash
   python main.py
   ```

## Foydalanish
- Telegram botni ishga tushirgandan so'ng, botni o'z akkauntingiz orqali test qilib ko'rishingiz mumkin.
- E'lon joylash va qidirish uchun foydalanuvchi uchun mo'ljallangan buyruqlar mavjud.

## Loyihaning imkoniyatlari
- **E'lonlarni boshqarish:** Foydalanuvchi avtomobillar haqida to'liq ma'lumot bilan e'lon joylashtirishi mumkin.
- **Qidiruv tizimi:** Avtomobillarni turli mezonlar bo'yicha qidirish imkoniyati.
- **SQLAlchemy yordamida barqaror ma'lumotlar bazasi boshqaruvi.**

## Hissa qo'shish
- Pull requestlar qabul qilinadi.
- Har qanday xato yoki taklif haqida [Issues](https://github.com/AbdusattarovOtabek/CarSaleBot/issues) bo'limida xabar bering.

## Litsenziya
Bu loyiha [MIT litsenziyasi](LICENSE) asosida tarqatiladi. Tafsilotlar uchun LICENSE faylini ko'ring.

## Muallif
- **Otabek Abdusattarov**


