#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @vloggerdeven_TG
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import time

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

# the Strings used for this "thing"
from translation import Translation

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)
from pyrogram import filters 
from pyrogram import Client as Mai_bOTs

#from helper_funcs.chat_base import TRChatBase
from helper_funcs.display_progress import progress_for_pyrogram

from pyrogram.errors import UserNotParticipant, UserBannedInChannel 
from pyrogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
# https://stackoverflow.com/a/37631799/4723940
from PIL import Image
from database.database import *
from database.db import *


@Mai_bOTs.on_message(pyrogram.filters.command(["help"]))
async def help_user(bot, update):
    update_channel = Config.UPDATE_CHANNEL
    if update_channel:
        try:
            user = await bot.get_chat_member(update_channel, update.chat.id)
            if user.status == "Banido":
               await update.reply_text("Desculpe, você está banido")
               return
        except UserNotParticipant:
            await update.reply_text(
                text="**Devido ao enorme tráfego, apenas membros do canal podem usar este bot significa que você precisa ingressar no canal mencionado abaixo antes de me usar! **",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text="ᴊᴏɪɴ ᴍʏ ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/{update_channel}")]
              ])
            )
            return
        else:
            await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_USER,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('Renomear', callback_data = "rnme"),
                    InlineKeyboardButton('Arquivo Para Vídeo', callback_data = "f2v")
                ],
                [
                    InlineKeyboardButton('Miniatura Personalizada', callback_data = "cthumb"),
                    InlineKeyboardButton('Legenda Personalizada', callback_data = "ccaption")
                ],
                [
                    InlineKeyboardButton('Sobre', callback_data = "about")
                ]
            ]
        )
    )       

@Mai_bOTs.on_message(pyrogram.filters.command(["start"]))
async def start_me(bot, update):
    if update.from_user.id in Config.BANNED_USERS:
        await update.reply_text("Você está banido")
        return
    update_channel = Config.UPDATE_CHANNEL
    if update_channel:
        try:
            user = await bot.get_chat_member(update_channel, update.chat.id)
            if user.status == "Banido":
               await update.reply_text(" Desculpe, você está me inundando, então meu dono removeu você de me usar se você acha que é um erro entre em contato : @Faris_TG")
               return
        except UserNotParticipant:
            await update.reply_text(
                text="**Devido ao enorme tráfego, apenas membros do canal podem usar este bot significa que você precisa ingressar no canal mencionado abaixo antes de me usar! **",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text="ᴊᴏɪɴ ᴍʏ ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/{update_channel}")]
              ])
            )
            return
        else:
            await update.reply_text(Translation.START_TEXT.format(update.from_user.first_name),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                        InlineKeyboardButton("Ajuda", callback_data = "ghelp")
                ],
                [
                    InlineKeyboardButton('Atualizações', url='https://t.me/dk_botx'),
                    InlineKeyboardButton('Apoio, Suporte', url='https://t.me/dkbotxchats')
                ],
                [
                    InlineKeyboardButton('Desenvolvedor', url='https://t.me/vloggerdeven_TG'),
                    InlineKeyboardButton('Código Fonte', url='https://github.com/DKBOTx/FileRenamerBot')
                ]
            ]
        ),
        reply_to_message_id=update.message_id
    )
            return 

@Mai_bOTs.on_callback_query()
async def cb_handler(client: Mai_bOTs , query: CallbackQuery):
    data = query.data
    if data == "rnme":
        await query.message.edit_text(
            text=Translation.RENAME_HELP,
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('VOLTAR', callback_data = "ghelp"),
                    InlineKeyboardButton("FECHAR", callback_data = "close")
                ]
            ]
        )
     )
    elif data == "f2v":
        await query.message.edit_text(
            text=Translation.C2V_HELP,
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('VOLTAR', callback_data = "ghelp"),
                    InlineKeyboardButton("FECHAR", callback_data = "close")
                ]
            ]
        )
     )
    elif data == "ccaption":
        await query.message.edit_text(
            text=Translation.CCAPTION_HELP,
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('Mostrar Legenda Atual', callback_data = "shw_caption"),
                    InlineKeyboardButton("Excluir Legenda", callback_data = "d_caption")
                ],
                [
                    InlineKeyboardButton('VOLTAR', callback_data = "ghelp"),
                    InlineKeyboardButton('FECHAR', callback_data = "close")
                ]
            ]
        )
     )
    elif data == "cthumb":
        await query.message.edit_text(
            text=Translation.THUMBNAIL_HELP,
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('VOLTAR', callback_data = "ghelp"),
                    InlineKeyboardButton("FECHAR", callback_data = "close")
                ]
            ]
        )
     )
    elif data == "closeme":
        await query.message.delete()
        try:
            await query.message.reply_text(
                text = "<b>Processo Cancelado</b>"
     )
        except:
            pass 
    elif data == "ghelp":
        await query.message.edit_text(
            text=Translation.HELP_USER,
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('RENOMEAR', callback_data = "rnme"),
                    InlineKeyboardButton('ARQUIVO PARA VÍDEO', callback_data = "f2v")
                ],
                [
                    InlineKeyboardButton('Miniatura Personalizada', callback_data = "cthumb"),
                    InlineKeyboardButton('Legenda Personalizada', callback_data = "ccaption")
                ],
                [
                    InlineKeyboardButton(' 🫣 ᴀʙᴏᴜᴛ', callback_data = "about")
                ]
            ]
        )
    )       

    elif data =="shw_caption":
             try:
                caption = await get_caption(query.from_user.id)
                c_text = caption.caption
             except:
                c_text = "Desculpe, mas você ainda não adicionou nenhuma legenda, por favor, defina sua legenda através do comando /scaption" 
             await query.message.edit(
                  text=f"<b>Sua legenda personalizada:</b> \n\n{c_text} ",
                  parse_mode="html", 
                  disable_web_page_preview=True, 
                  reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('VOLTAR', callback_data = "ccaption"),
                    InlineKeyboardButton("FECHAR", callback_data = "close")
                ]
            ]
        )
     )
    elif data == "about":
        await query.message.edit_text(
            text=Translation.ABOUT_ME,
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('VOLTAR', callback_data = "ghelp"),
                    InlineKeyboardButton("FECHAR", callback_data = "close")
                ]
            ]
        )
     )
    elif data == "d_caption":
        try:
           await del_caption(query.from_user.id)   
        except:
            pass
        await query.message.edit_text(
            text="<b>legenda excluída com sucesso</b>",
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('VOLTAR', callback_data = "ccaption"),
                    InlineKeyboardButton("FECHAR", callback_data = "close")
                ]
            ]
        )
     )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
