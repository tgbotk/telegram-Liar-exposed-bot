import re
from datetime import datetime

import pymysql
from pyrogram import Client, filters
from pyrogram.errors import MessageNotModified
from pyrogram.types import CallbackQuery, InputMediaPhoto
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup

bot_token = "5116615962:AAFf8Qo6hglhS3iXfNTs5Qy5TCwz4Gynv1E"
api_id = 24985337
api_hash = "6b835cc9023283e151b6ae37d3966ca9"
host = "localhost"
user = "pianzi"
password = "pianzi"
database = "pianzi"


def chaxun(sql):
    db = pymysql.connect(host=host, user=user, password=password, database=database)
    sqla = (sql)
    cursor = db.cursor()
    cursor.execute(sqla)
    result = cursor.fetchall()
    db.close()
    return result


def charu(sql):
    db = pymysql.connect(host=host, user=user, password=password, database=database)
    sqla = (sql)
    cursor = db.cursor()
    cursor.execute(sqla)
    db.commit()
    db.close()


def gengxin(sql):
    # 假设您已经设置好了数据库连接的参数
    db = pymysql.connect(host=host, user=user, password=password, database=database)
    sqla = (sql)
    cursor = db.cursor()

    try:
        # 执行更新操作
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print("更新失败:", e)
        db.rollback()
    finally:
        # 关闭数据库连接
        cursor.close()
        db.close()


app = Client(
    "mybot",
    bot_token=bot_token,
    api_id=api_id,
    api_hash=api_hash)

adminid = -1002472144705
baoguang = -1002472144705
pindao = "v666"
# 媒体组列表，包含多个媒体对象
media_ids = []
# 初始化一个标志，表示用户是否上传完所有图片

# 用户状态管理器
user_states = {}


@app.on_message(filters.command("start") & filters.private)
async def start_command(client, message):
    user_id = message.from_user.id
    caidan = ReplyKeyboardMarkup([["🆘曝光骗子", "🔍查询骗子"], ["🤝劳务之家"]], resize_keyboard=True)
    sql = chaxun(f'select * from user where telegramid = "{user_id}" limit 1;')
    if not sql:
        now = datetime.now()
        registration_time = now.strftime("%Y-%m-%d %H:%M:%S")
        charu(
            f'insert into user (telegramid,time) values ("{user_id}","{registration_time}")')
    await message.reply_text("""<b>📣欢迎使用此机器人🤖

你可以发送骗子信息
提供证据越多越好
审核通过，永久云端保存
🤝来帮助更多的人

👇点击下方按钮选择功能👇</b>""", quote=False, disable_web_page_preview=True, reply_markup=caidan)


@app.on_message(filters.text & filters.regex("🆘曝光骗子"))
async def zhuanshu(client, message):
    keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("🚫请认真观看新增骗子步骤🚫", callback_data=f"kaishibaog")]
        ]
    )
    keyboards = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("✅确认曝光✅", callback_data=f"shagnchuanwb")]
        ]
    )
    await message.reply_text("""<b>🆕新增骗子请注意：

1️⃣禁止发送虚假曝光

2️⃣禁止发布黄色内容

3️完成曝光</b>""", quote=False, disable_web_page_preview=True, reply_markup=keyboards)


@app.on_message(filters.text & filters.regex("🔍查询骗子"))
async def zhuanshu(client, message):
    keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("🌐查询方法🌐", callback_data=f"kaishibaog")]
        ]
    )
    await message.reply_text("""<b>🆘查询骗子方法

1️⃣转发他的消息到本机器人

2️⃣发送骗子名称 or 骗子用户名</b>""", quote=False, disable_web_page_preview=True, reply_markup=keyboard)


@app.on_message(filters.text & filters.regex("🤝劳务之家"))
async def zhuanshu(client, message):
    keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("🤝劳务之家", url=f"https://t.me/laowuzj")]
        ]
    )
    await message.reply_text("""<b>担保联系劳务之家 @laowuzj</b>""", quote=False, disable_web_page_preview=True, reply_markup=keyboard)


@app.on_message(filters.text & filters.regex("💰付费广告"))
async def zhuanshu(client, message):
    keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("🤝江山供需频道", url=f"https://t.me/v000")]
        ]
    )
    await message.reply_text("""<b>发布付费广告严格要求如下
1️⃣禁止携带其他担保平台标识
2️⃣禁止发布虚假内容广告
3️⃣发布广告者禁止诈骗欺骗用户
如有违反条约永久🈲发布广告</b>""", quote=False, disable_web_page_preview=True, reply_markup=keyboard)




@app.on_message(filters.group & filters.regex("查询"))
async def set_qunzu_message_text(client, message):
    user_id = message.from_user.id
    if message.forward_from and message.forward_from.id:
        text = message.forward_from.id
        results_per_page = 10
        # 计算偏移量
        page_number = 1  # 当前页码
        offset = max((page_number - 1) * results_per_page, 0)
        sql = chaxun(
            f'SELECT text, zhengju FROM baoguangs WHERE text = "{text}" AND shenhe = "审核通过" LIMIT {results_per_page} OFFSET {offset}')
        zongji = chaxun(f'SELECT shenhe FROM baoguangs WHERE text = "{text}" AND shenhe = "审核通过"')
        zts = len(zongji)
        num_results = len(sql)

        if num_results == 0:
            return

        result_list = []
        for i, item in enumerate(sql, start=1):
            combined_item = f'{i}.{item[0]}\n'
            result_list.append(combined_item)

        n1 = '\n'
        text = f"📢公告:劳务之家技术支持\n\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n{n1.join(result_list)}\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n<b>搜索关键词<code>【{text}】</code> | 共找到<code>{zts}</code>条搜索结果 | 当前为<code>{page_number}</code>页</b>"
        keyboard = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("劳务之家", url="https://t.me/laowuzj"),
                 InlineKeyboardButton("下一页", callback_data=f"xiaye")]
            ]
        )
        msid = await message.reply_text(text, disable_web_page_preview=True, reply_markup=keyboard)
        return

    else:
        if message.text:
            text = message.text.split("查询")[1]
            results_per_page = 10
            # 计算偏移量
            page_number = 1  # 当前页码
            offset = max((page_number - 1) * results_per_page, 0)
            sql = chaxun(
                f'SELECT name, shenfen, shouji,yuanyin FROM baoguangs '
                f'WHERE name = "{text}" or shenfen = "{text}" or shouji = "{text}" '
                f'AND shenhe = "审核通过" '
                f'LIMIT {results_per_page} OFFSET {offset}'
            )
            print(sql)
            zongji = chaxun(
                f'SELECT shenhe FROM baoguangs '
                f'WHERE name = "{text}" or shenfen = "{text}" or shouji = "{text}" '
                f'AND shenhe = "审核通过"'
            )
            zts = len(zongji)
            num_results = len(sql)

            if num_results == 0:
                await message.reply_text("没有找到匹配的结果。")
                return

            result_list = []
            for i, item in enumerate(sql, start=1):
                # 证据连接： t.me/{pindao}/{item[1]}
                combined_item = f'{i}.姓名：{item[0]}\n身份信息：{item[1]}\n手机号：{item[2]}\n原因：{item[3]}\n'
                result_list.append(combined_item)

            n1 = '\n'
            text = f"📢公告:劳务之家技术支持\n\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n{n1.join(result_list)}\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n<b>搜索关键词<code>【{text}】</code> | 共找到<code>{zts}</code>条搜索结果 | 当前为<code>{page_number}</code>页</b>"
            keyboard = InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("劳务之家", url="https://t.me/laowuzj"),
                     InlineKeyboardButton("下一页", callback_data=f"xiaye")]
                ]
            )
            msid = await message.reply_text(text, disable_web_page_preview=True, reply_markup=keyboard)
            charu(f'insert into sousuo (text,xxid) values ("{message.text}","{msid.id}")')


@app.on_message(filters.private)
async def set_welcome_message_text(client, message):
    user_id = message.from_user.id
    yonghu = chaxun(f'select * from user where telegramid = "{user_id}" limit 1;')
    upload = yonghu[0][2]
    print(upload)

    if user_id in user_states and user_states[user_id][0] == "设置曝光文字":
        xxid = user_states[user_id][1]
        # 提取名字、身份信息和手机号
        user_id = message.from_user.id
        name_match = re.search(r"名字：(.+)", message.text)
        identity_match = re.search(r"身份信息：(.+)", message.text)
        phone_match = re.search(r"手机号：(.+)", message.text)
        yuanyin_match = re.search(r"原因：(.+)", message.text)

        # 获取匹配到的内容，如果未匹配则为 None
        name = name_match.group(1) if name_match else None
        identity = identity_match.group(1) if identity_match else None
        phone = phone_match.group(1) if phone_match else None
        yuanyin = yuanyin_match.group(1) if yuanyin_match else None
        chongfusql = chaxun(f'select * from baoguangs where shenfen = "{identity}" AND shenhe = "审核通过"')
        print(chongfusql)
        if chongfusql:
            await message.reply_text("该身份信息已被曝光，无法重复曝光")
        else:
            gengxin(
                f'update baoguangs set name = "{name}",shenfen = "{identity}",shouji = "{phone}",yuanyin = "{yuanyin}" where msid = "{xxid}";')
            keyboard = InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("确认曝光", callback_data=f"querenbaoguang_{xxid}")]
                ]
            )
            del user_states[user_id]
            await message.reply_text("✅请确定您要曝光该骗子，并提交审核✅", reply_markup=keyboard)
    else:
        if message.forward_from and message.forward_from.id:
            text = message.forward_from.id
            results_per_page = 10
            # 计算偏移量
            page_number = 1  # 当前页码
            offset = max((page_number - 1) * results_per_page, 0)
            sql = chaxun(
                f'SELECT name, shenfen, shouji,yuanyin FROM baoguangs '
                f'WHERE name = "{text}" or shenfen = "{text}" or shouji = "{text}" '
                f'AND shenhe = "审核通过" '
                f'LIMIT {results_per_page} OFFSET {offset}'
            )
            print(sql)
            zongji = chaxun(
                f'SELECT shenhe FROM baoguangs '
                f'WHERE name = "{text}" or shenfen = "{text}" or shouji = "{text}" '
                f'AND shenhe = "审核通过"'
            )
            zts = len(zongji)
            num_results = len(sql)

            if num_results == 0:
                await message.reply_text("没有找到匹配的结果。")
                return

            result_list = []
            for i, item in enumerate(sql, start=1):
                combined_item = f'{i}.{item[0]}\n'
                result_list.append(combined_item)

            n1 = '\n'
            text = f"📢公告:劳务之家技术支持\n\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n{n1.join(result_list)}\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n<b>搜索关键词<code>【{text}】</code> | 共找到<code>{zts}</code>条搜索结果 | 当前为<code>{page_number}</code>页</b>"
            keyboard = InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("劳务之家", url="https://t.me/laowuzj"),
                     InlineKeyboardButton("下一页", callback_data=f"xiaye")]
                ]
            )
            msid = await message.reply_text(text, disable_web_page_preview=True, reply_markup=keyboard)
            del result_list
            gengxin(f'update user set upload_complete = "False" where telegramid = "{user_id}";')
            charu(f'insert into sousuo (text,xxid) values ("{message.text}","{msid.id}")')

            return

        else:
            if message.text:
                text = message.text
                results_per_page = 10
                # 计算偏移量
                page_number = 1  # 当前页码
                offset = max((page_number - 1) * results_per_page, 0)

                sql = chaxun(
                    f'SELECT name, shenfen, shouji,yuanyin FROM baoguangs '
                    f'WHERE name = "{text}" or shenfen = "{text}" or shouji = "{text}" '
                    f'AND shenhe = "审核通过" '
                    f'LIMIT {results_per_page} OFFSET {offset}'
                )
                print(sql)
                zongji = chaxun(
                    f'SELECT shenhe FROM baoguangs '
                    f'WHERE name = "{text}" or shenfen = "{text}" or shouji = "{text}" '
                    f'AND shenhe = "审核通过"'
                )
                zts = len(zongji)
                num_results = len(sql)

                if num_results == 0:
                    await message.reply_text("没有找到匹配的结果。")
                    return

                result_list = []
                for i, item in enumerate(sql, start=1):
                    combined_item = f'{i}.{item[0]}\n'
                    result_list.append(combined_item)

                n1 = '\n'
                text = f"📢公告:劳务之家技术支持\n\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n{n1.join(result_list)}\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n<b>搜索关键词<code>【{text}】</code> | 共找到<code>{zts}</code>条搜索结果 | 当前为<code>{page_number}</code>页</b>"
                keyboard = InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton("劳务之家", url="https://t.me/laowuzj"),
                         InlineKeyboardButton("下一页", callback_data=f"xiaye")]
                    ]
                )
                msid = await message.reply_text(text, disable_web_page_preview=True, reply_markup=keyboard)
                del result_list
                gengxin(f'update user set upload_complete = "False" where telegramid = "{user_id}";')
                charu(f'insert into sousuo (text,xxid) values ("{message.text}","{msid.id}")')


@app.on_callback_query(filters.regex("xiaye"))
async def xiayee(client, update: CallbackQuery):
    xiaoxiid = update.message.id
    text = chaxun(f'select text from sousuo where xxid = "{xiaoxiid}" limit 1;')
    gengxin(f'update sousuo set yeshu = yeshu + 1 where xxid = "{xiaoxiid}";')
    sqll = chaxun(f'select yeshu from sousuo where xxid = "{xiaoxiid}" limit 1;')  # 当前页码
    textt = text[0][0]
    results_per_page = 10
    # 计算偏移量
    page_number = sqll[0][0]
    print(page_number)
    offset = max((page_number - 1) * results_per_page, 0)
    sql = chaxun(
        f'select text,zhengju from baoguang where text LIKE "%{textt}%" AND shenhe = "审核通过" LIMIT {results_per_page} OFFSET {offset}')
    zongji = chaxun(f'select shenhe from baoguang where text LIKE "%{text}%" AND shenhe = "审核通过"')
    zts = len(zongji)

    if sql:
        num_results = len(sql)
        result_list = []
        for i, item in enumerate(sql, start=1):
            combined_item = f'{i}.{item[0]}\n'
            result_list.append(combined_item)

        n1 = '\n'
        text = f"📢公告:劳务之家技术支持\n\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n{n1.join(result_list)}\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n<b>搜索关键词<code>【{textt}】</code> | 共找到<code>{zts}</code>条搜索结果 | 当前为<code>{page_number}</code>页</b>"
        keyboard = ""
        if page_number >= 1:
            keyboard = InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("上一页", callback_data=f"shangye"),
                     InlineKeyboardButton("下一页", callback_data=f"xiaye")]
                ]
            )
        elif page_number <= 1:
            keyboard = InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("劳务之家", url="https://t.me/laowuzj"),
                     InlineKeyboardButton("下一页", callback_data=f"xiaye")]
                ]
            )

        await update.message.edit_text(text, disable_web_page_preview=True, reply_markup=keyboard)

    else:
        await update.answer(text="已到达最后一页", show_alert=True)


@app.on_callback_query(filters.regex("shangye"))
async def shangye(client, update: CallbackQuery):
    try:
        xiaoxiid = update.message.id
        gengxin(f'UPDATE sousuo SET yeshu = CASE WHEN yeshu > 1 THEN yeshu - 1 ELSE 1 END WHERE xxid = "{xiaoxiid}";')
        text = chaxun(f'select text from sousuo where xxid = "{xiaoxiid}" limit 1;')
        sqll = chaxun(f'select yeshu from sousuo where xxid = "{xiaoxiid}" limit 1;')  # 当前页码
        textt = text[0][0]
        # 计算偏移量
        page_number = sqll[0][0]

        sql = chaxun(
            f'select text,zhengju from baoguang where text LIKE "%{textt}%" AND shenhe = "审核通过" LIMIT 10 OFFSET {page_number}')
        zongji = chaxun(f'select shenhe from baoguang where text LIKE "%{text}%" AND shenhe = "审核通过"')
        zts = len(zongji)
        if page_number == 0:
            await update.answer(text="已到达第一页", show_alert=True)
            return
        if sql:
            num_results = len(sql)
            result_list = []
            for i, item in enumerate(sql, start=1):
                combined_item = f'{i}.{item[0]}\n'
                result_list.append(combined_item)

            n1 = '\n'
            text = f"📢公告:劳务之家技术支持\n\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n{n1.join(result_list)}\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n<b>搜索关键词<code>【{textt}】</code> | 共找到<code>{zts}</code>条搜索结果 | 当前为<code>{page_number}</code>页</b>"
            keyboard = ""
            if page_number <= 1:

                keyboard = InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton("劳务之家", url="https://t.me/laowuzj"),
                         InlineKeyboardButton("下一页", callback_data=f"xiaye")]
                    ]
                )
            elif page_number >= 1:
                keyboard = InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton("上一页", callback_data=f"shangye"),
                         InlineKeyboardButton("下一页", callback_data=f"xiaye")]
                    ]
                )

            await update.message.edit_text(text, disable_web_page_preview=True, reply_markup=keyboard)
    except MessageNotModified:
        await update.answer(text="已到达第一页", show_alert=True)


@app.on_callback_query(filters.regex("shagnchuanwb"))
async def shagnchuanwbb(client, update: CallbackQuery):
    xiaoxiid = update.message.id
    user_id = update.from_user.id
    gengxin(f'update user set upload_complete = "False" where telegramid = "{user_id}";')
    media_ids_str = ",".join(media_ids)
    charu(f'insert into baoguangs (telegramid,msid) values ("{user_id}","{xiaoxiid}")')
    media_ids.clear()

    keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("上传文字", callback_data=f"chuanwenzi")]
        ]
    )
    user_states[user_id] = ("设置曝光文字", xiaoxiid)
    msid = await update.message.edit_text(f"""<b>请按照以下格式发送曝光内容
    
<code>📣新增骗子一枚🆘
名字：XXX
身份信息：@xxx
手机号：xxxx
原因：这里可以填写具体内容，或者怎么被骗的</code>
</b>""")
    # await app.send_media_group(adminid, media_group)
    # await update.message.edit_text(f"曝光图片已上传完毕，请点击按钮上传文字",reply_markup=keyboard)


@app.on_callback_query(filters.regex("querenbaoguang_"))
async def querenbaoguangg(client, update: CallbackQuery):
    data = update.data
    xxid = int(data.split("querenbaoguang_")[1])
    user_id = update.from_user.id
    sql = chaxun(f'select * from baoguangs where msid = "{xxid}"')
    name = sql[0][2]
    shenfen = sql[0][3]
    shouji = sql[0][4]
    yuanyin = sql[0][5]
    wenzi = f"姓名 {name}\n身份信息 {shenfen}\n手机号 {shouji}\n原因 {yuanyin}"
    keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("通过", callback_data=f"tongguoshenhe"),
             InlineKeyboardButton("拒绝", callback_data=f"jujueshenhe")]
        ]
    )
    text = f"<b>以下是新的曝光内容，请审核</b>\n\n{wenzi}"
    msidd = await app.send_message(chat_id=adminid, text=text, reply_markup=keyboard)
    await update.message.edit_text(f"曝光申请已提交，请耐心等待审核")
    gengxin(f'update baoguangs set qunzuid = "{msidd.id}" where msid = "{xxid}";')
    # await update.message.edit_text(f"曝光图片已上传完毕，请点击按钮上传文字",reply_markup=keyboard)


@app.on_callback_query(filters.regex("tongguoshenhe"))
async def tongguoshenheg(client, update: CallbackQuery):
    xiaoxiid = update.message.id
    sql = chaxun(f'select * from baoguangs where qunzuid = "{xiaoxiid}"')
    name = sql[0][2]
    shenfen = sql[0][3]
    shouji = sql[0][4]
    wenzi = f"名字:{name}\n身份信息:{shenfen}\n手机号:{shouji}"
    keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("我要曝光", url="https://t.me/js8888_bot"),
             InlineKeyboardButton("官方频道", url="https://t.me/XiY888")]
        ]
    )

    # zjlj = await app.send_message(chat_id=baoguang, text=wenzi, reply_markup=keyboard)
    await update.message.edit_text(f"审核通过")
    gengxin(f'UPDATE baoguangs SET shenhe = "审核通过" WHERE qunzuid = "{xiaoxiid}";')


@app.on_callback_query(filters.regex("jujueshenhe"))
async def jujueshenhe(client, update: CallbackQuery):

    # zjlj = await app.send_message(chat_id=baoguang, text=wenzi, reply_markup=keyboard)
    await update.message.edit_text(f"审核拒绝")

app.run()
