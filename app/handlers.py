from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery

import app.database.requests as rq
import app.keyboard as kb

router = Router()


@router.message(CommandStart())
async def cmd_start(msg: Message) -> None:
    await rq.set_user(msg.from_user.id, msg.from_user.username)
    await msg.answer('Hi', reply_markup=kb.start)


@router.message(Command('help'))
async def cmd_help(msg: Message) -> None:
    await msg.answer('There is nothing u needs')


@router.message(F.data == 'Room')
async def room(cb: CallbackQuery) -> None:
    await cb.answer('')
    await cb.message.answer('What', reply_markup=kb.room)


@router.callback_query(F.data == 'Events')
async def events(cb: CallbackQuery) -> None:
    await cb.answer('')
    await cb.message.answer('there is no events')
