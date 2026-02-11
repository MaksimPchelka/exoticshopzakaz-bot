import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters import CommandStart
from urllib.parse import quote
import os

TOKEN = os.getenv("BOT_TOKEN") or os.getenv("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Обновленный список товаров (добавил прокси сюда)
ITEMS = {
    "view_stars_50": {
        "name": "50 Звезд⭐️",
        "price": "74₽",
        "photo": "https://i.pinimg.com/736x/1e/04/86/1e0486c8814ce9f780925affc6e282a7.jpg",
        "msg": "Привет, я хочу купить 50 звезд"
    },
    "view_stars_100": {
        "name": "100 Звезд⭐️",
        "price": "139₽",
        "photo": "https://i.pinimg.com/736x/1e/04/86/1e0486c8814ce9f780925affc6e282a7.jpg",
        "msg": "Привет, я хочу купить 100 звезд"
    },
    "view_stars_150": {
        "name": "150 Звезд⭐️",
        "price": "209₽",
        "photo": "https://i.pinimg.com/736x/1e/04/86/1e0486c8814ce9f780925affc6e282a7.jpg",
        "msg": "Привет, я хочу купить 150 звезд"
    },
    "view_proxy_de": {
        "name": "Прокси Германия 🇩🇪",
        "price": "39₽",
        "photo": "https://i.pinimg.com/736x/1e/04/86/1e0486c8814ce9f780925affc6e282a7.jpg",
        "msg": "Привет, я хочу купить 🇩🇪 прокси"
    },
    "view_proxy_nl": {
        "name": "Прокси Нидерланды 🇳🇱",
        "price": "45₽",
        "photo": "https://i.pinimg.com/736x/1e/04/86/1e0486c8814ce9f780925affc6e282a7.jpg",
        "msg": "Привет, я хочу купить 🇳🇱 прокси"
    },
    "view_proxy_us": {
        "name": "Прокси США 🇺🇸",
        "price": "39₽",
        "photo": "https://i.pinimg.com/736x/1e/04/86/1e0486c8814ce9f780925affc6e282a7.jpg",
        "msg": "Привет, я хочу купить 🇺🇸 прокси"
    }
}

# --- КЛАВИАТУРЫ ---

def get_start_kb():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="Каталог💼", callback_data="open_catalog"),
        InlineKeyboardButton(text="Инфо📌", callback_data="open_info")
    )
    builder.row(InlineKeyboardButton(text="Задать Вопрос❓", url="https://t.me/exoticshoppodderzka_bot"))
    return builder.as_markup()

def get_categories_kb():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="Звезды ⭐️", callback_data="cat_stars"))
    builder.row(InlineKeyboardButton(text="Прокси 🌐", callback_data="cat_proxy"))
    builder.row(InlineKeyboardButton(text="⬅️ Назад", callback_data="go_back"))
    return builder.as_markup()

def get_stars_kb():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="50⭐️", callback_data="view_stars_50"))
    builder.row(InlineKeyboardButton(text="100⭐️", callback_data="view_stars_100"))
    builder.row(InlineKeyboardButton(text="150⭐️", callback_data="view_stars_150"))
    builder.row(InlineKeyboardButton(text="⬅️ Назад к категориям", callback_data="open_catalog"))
    return builder.as_markup()

def get_proxy_kb():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="Datacenter Прокси 🇩🇪", callback_data="view_proxy_de"))
    builder.row(InlineKeyboardButton(text="Datacenter Прокси 🇳🇱", callback_data="view_proxy_nl"))
    builder.row(InlineKeyboardButton(text="Datacenter Прокси 🇺🇸", callback_data="view_proxy_us"))

    builder.row(
        InlineKeyboardButton(text="⬅️ Назад к категориям", callback_data="open_catalog"),
        InlineKeyboardButton(text="📖 Справочник по прокси", callback_data="proxy_help"))
    
    return builder.as_markup()

# --- ХЕНДЛЕРЫ ---

@dp.message(CommandStart())
async def cmd_start(message: Message):
    photo_url = "https://i.pinimg.com/736x/05/e9/ea/05e9ea256042d738d60a1ba38b311710.jpg"
    user_name = message.from_user.first_name or "Покупатель"
    await message.answer_photo(
        photo=photo_url,
        caption=f"Добро пожаловать, <b>{user_name}</b>! Мы - Магазин <a href='https://t.me/+W6cWciQKAQJlZjc6'>Exotic Shop🖤</a>\n\nЗдесь вы можете просмотреть каталог товаров для покупки.",
        parse_mode="HTML",
        reply_markup=get_start_kb()
    )

@dp.callback_query(F.data == "open_catalog")
async def catalog_categories_callback(callback: CallbackQuery):
    await callback.message.delete()
    photo_url = "https://i.pinimg.com/736x/97/65/3d/97653d6f2bcac8c032bea222b5d1b192.jpg" 
    await callback.message.answer_photo(
        photo=photo_url,
        caption="Выберите интересующую категорию товаров:",
        reply_markup=get_categories_kb()
    )
    await callback.answer()

@dp.callback_query(F.data == "cat_stars")
async def stars_menu_callback(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer_photo(
        photo="https://i.pinimg.com/736x/1e/04/86/1e0486c8814ce9f780925affc6e282a7.jpg",
        caption="Выберите количество звёзд для покупки:",
        reply_markup=get_stars_kb()
    )
    await callback.answer()

@dp.callback_query(F.data == "cat_proxy")
async def proxy_menu_callback(callback: CallbackQuery):
    await callback.message.delete()
    # ТУТ БЫЛА ОШИБКА. Заменил заглушку на реальную ссылку.
    proxy_main_photo = "https://i.pinimg.com/736x/a6/29/d2/a629d280a01f0f504c01151d25bca62a.jpg"
    await callback.message.answer_photo(
        photo=proxy_main_photo, 
        caption="Выберите подходящий прокси-сервер:",
        reply_markup=get_proxy_kb()
    )
    await callback.answer()

@dp.callback_query(F.data == "go_back")
async def back_callback(callback: CallbackQuery):
    await callback.message.delete()
    photo_url = "https://i.pinimg.com/736x/05/e9/ea/05e9ea256042d738d60a1ba38b311710.jpg"
    user_name = callback.from_user.first_name or "Покупатель"
    await callback.message.answer_photo(
        photo=photo_url,
        caption=f"Добро пожаловать, <b>{user_name}</b>! Мы - Магазин <a href='https://t.me/+W6cWciQKAQJlZjc6'>Exotic Shop🖤</a>",
        parse_mode="HTML",
        reply_markup=get_start_kb()
    )

@dp.callback_query(F.data == "open_info")
async def info_callback(callback: CallbackQuery):
    await callback.message.delete()
    
    photo_url = "https://i.pinimg.com/736x/a6/29/d2/a629d280a01f0f504c01151d25bca62a.jpg" 
    
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="⬅️ Назад", callback_data="go_back"))
    
    await callback.message.answer_photo(
        photo=photo_url,
        caption=(
            "<b>📌 Информация о магазине</b>\n\n"
            "<a href='https://t.me/+W6cWciQKAQJlZjc6'>Exotic Shop</a> - Магазин цифровых товаров\n\n"
            "Способы оплаты 💳 :: Перевод в ₽ по номеру\n\n"
            "Основные товары 📦 :: Telegram Stars по курсу 1.39₽ , Proxy-Сервера\n\n"
            "Время работы менеджера ⏱️:: с 13 до 23 будни / с 10 до 23 выходные UTC+3.\n\n"
            "<i>Лучший сервис только у нас!</i>"
        ),
        parse_mode="HTML",
        reply_markup=builder.as_markup()
    )
    await callback.answer()

@dp.callback_query(F.data.startswith("view_"))
async def show_item(callback: CallbackQuery):
    item_id = callback.data
    item = ITEMS.get(item_id)
    if not item:
        await callback.answer("Товар не найден")
        return

    await callback.message.delete()
    encoded_text = quote(item['msg'])
    pay_url = f"https://t.me/maksimpchelka?text={encoded_text}"
    
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="💳 Оформить заказ", url=pay_url))
    # Возврат в каталог (к категориям)
    builder.row(InlineKeyboardButton(text="⬅️ Назад в каталог", callback_data="open_catalog"))
    
    await callback.message.answer_photo(
        photo=item["photo"],
        caption=f"📦 <b>Заказ :: {item['name']}</b>\n💰 <b>Стоимость :: {item['price']}</b>\n\nНажмите для оплаты.",
        parse_mode="HTML",
        reply_markup=builder.as_markup()
    )
    await callback.answer()

@dp.callback_query(F.data == "proxy_help")
async def proxy_help_callback(callback: CallbackQuery):
    await callback.message.delete()
    
    help_photo = "https://i.pinimg.com/736x/a6/29/d2/a629d280a01f0f504c01151d25bca62a.jpg" # Твоя картинка
    
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="⬅️ Назад к прокси", callback_data="cat_proxy"))
    
    await callback.message.answer_photo(
        photo=help_photo,
        caption=(
            "<b>📖 Справочник по Proxy</b>\n\n"
            "• <b>Тип:</b> SOCKS5 IPv4\n"
            "• <b>Локации ::</b> Германия 🇩🇪, Нидерланды 🇳🇱, США 🇺🇸\n"
            "• <b>Подробнее ::</b> <a href='https://t.me/ExoticShopKanal/79'>Клик...</a>\n"
            "• <b>Гайд по Proxy ::</b> <a href='https://t.me/ExoticShopKanal/89'>Клик...</a>\n\n"
            "<i>После оплаты менеджер выдаст данные в формате ip:port@login:password</i>"
        ),
        parse_mode="HTML",
        reply_markup=builder.as_markup()
    )
    await callback.answer()

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())