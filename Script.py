class script(object):
    START_TXT = """𝙷𝙴𝙻𝙾 {},\n𝙸 𝙲𝙰𝙽 𝙿𝚁𝙾𝚅𝙸𝙳𝙴 𝚂𝙴𝚁𝙸𝙴𝚂.\n\nAᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴛᴏ sᴇᴇ ᴛʜᴇ ᴍᴀɢɪᴄ ᴏʀ ʀᴇᴀᴅ ᴍᴏʀᴇ ғʀᴏᴍ ᴛʜᴇ ᴍᴇɴᴜ ʙᴇʟᴏᴡ\n\n⚠️ 𝖬𝗈𝗋𝖾 𝖧𝖾𝗅𝗉 𝖧𝗂𝗍 /help """

    HELP_TXT = """𝙷𝙴𝚈 {}\n𝙷𝙴𝚁𝙴 𝙸𝚂 𝙼𝚈 𝙷𝙴𝙻𝙿 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂."""

    ABOUT_TXT = """✯ 𝙼𝚈 𝙽𝙰𝙼𝙴: {}
✯ 𝙳𝚎𝚟𝚎𝚕𝚘𝚙𝚎𝚛 : <a href=https://t.me/ArrowFlix><b>𝙰𝚛𝚛𝚘𝚠𝙵𝚕𝚒𝚡</b></a>
✯ 𝙻𝙸𝙱𝚁𝙰𝚁𝚈: 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼
✯ 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴: 𝙿𝚈𝚃𝙷𝙾𝙽 𝟹
✯ 𝙳𝙰𝚃𝙰 𝙱𝙰𝚂𝙴: 𝙼𝙾𝙽𝙶𝙾 𝙳𝙱
✯ 𝚅𝚎𝚛𝚜𝚒𝚘𝚗 : 𝚟 𝟼.𝟺 """

    HOW_TXT = """<b><i>𝟷‌◖ ارسل اسم المسلسل او الفيلم في <a href=https://t.me/ArrowFlix/><b>الجروب هنا</b></a>\nSend Series or Movies Name in <a href=https://t.me/ArrowFlix/><b>Group</b></a>\n\n𝟸‌◖ يقوم البوت بارساله لك بعد ثواني\nThe bot will send it to you.</b><i>"""

    NHOW_TXT = """<b><i>𝟷◖ فيديو خام بدون لوجو\n𝟸◖ جودة اصلية و حجم قليل مقارنة بالمواقع\n𝟹◖ جودة صوت افضل\n𝟺◖ اختيار الترجمة المناسبة (المترجم المفضل)\n𝟻◖ عرض اكثر من ترجمة في نفس الوقت\n𝟼◖ المساعدة علي تعلم الإنجليزية عن طريق عرض <u>الترجمة العربية و الإنجليزية معاً</u>، <u>الترجمة الإنجليزية فقط</u> ، <u>بدون اي ترجمة</u>\n𝟽◖ مسلسلات Netflix , AppleTV , Prime تكون بأكثر من 30 ترجمة <a https://telegra.ph/تحميل-المسلسل-و-اضافة-الترجمة-03-19><b>شرح اختيار الترجمة</b></a>\n𝟾◖ آخيرا والأهم هي المشاهدة علي تليجرام بدون اعلانات</b>"""

    HOWADD_TXT = """<b>هنا شرح لاضافة الترجمة والبرامج اختر من الازرار الآتية..</b></a>"""

    EZAY_TXT = """<b>📌 𝗔𝗿𝗮𝗯𝗶𝗰\n• اضغط /Series لطريقة البحث عن <u>مسلسل</u> 📃\n• اضغط /Movie لطريقة البحث عن <u>فيلم</u> 📃\n📌 𝗘𝗻𝗴𝗹𝗶𝘀𝗵\n• 𝖧𝗂𝗍 /eSeries 𝖥𝗈𝗋 𝖲𝖾𝗋𝗂𝖾𝗌 𝖲𝖾𝖺𝗋𝖼𝗁 𝖱𝗎𝗅𝖾𝗌 📃\n• 𝖧𝗂𝗍 /eMovie 𝖥𝗈𝗋 𝖬𝗈𝗏𝗂𝖾 𝖲𝖾𝖺𝗋𝖼𝗁 𝖱𝗎𝗅𝖾𝗌 📃</b>""" 

    IMP_TXT = """<b><u>اولا: الصوت 🎤</u></b>\n• <b>Dubbed مدبلج</b>\nفي المسلسلات غير الإنجليزية [اسباني كوري..] ويكون الصوت هنا مدبلج انجليزي فقط\n• <b>Dual Audio صوت مزدوج</b>\nيعني يوجد مثلا صوت انجليزي وصوت ياباني (ENG-JPN)\n⚠️ عند التحميل من الافضل اذا كان في الوصف اسم لغة غير لغة العمل الاصلي لا تقم بتحميله ⚠️\n\n<b><u>ثانياً: الفيديو 📺</u></b>\n<b>ʜᴅᴛᴠ</b> نسخة تم تسجيلها من التلفاز(مسلسل)\n<b>ᴡᴇʙ-ᴅʟ | ᴡᴇʙʀɪᴘ</b> نسخه مسحوبة من المنصات\n<b>ʙʟᴜʀᴀʏ</b> نسخه مسحوبة من اقراص DVD وهي الافضل\n<b>ʜᴅʀɪᴘ</b> نسخه مسربة وتكون بدقة ضعيفة\n<b>ʜᴅᴄᴀᴍ</b> نسخه تم تصويرها في السينما (فيلم)"""

    SOURCE_TXT = """<b>𝐂𝐫𝐞𝐚𝐭𝐞 𝐎𝐧𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬:</b>"""

    MANUELFILTER_TXT = """ʜᴇʟᴘ: <b>ꜰɪʟᴛᴇʀꜱ</b>
- ꜰɪʟᴛᴇʀ ɪꜱ ᴀ ꜰᴇᴀᴛᴜʀᴇ ᴡᴇʀᴇ ᴜꜱᴇʀꜱ ᴄᴀɴ ꜱᴇᴛ ᴀᴜᴛᴏᴍᴀᴛᴇᴅ ʀᴇᴘʟɪᴇꜱ ꜰᴏʀ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴋᴇʏᴡᴏʀᴅ ᴀɴᴅ ɪ ᴡɪʟʟ ʀᴇꜱᴘᴏɴᴅ ᴡʜᴇɴᴇᴠᴇʀ ᴀ ᴋᴇʏᴡᴏʀᴅ ɪꜱ ꜰᴏᴜɴᴅ ɪɴ ᴛʜᴇ ᴍᴇꜱꜱᴀɢᴇ
<b>ɴᴏᴛᴇ:</b>
1. ᴛʜɪꜱ ʙᴏᴛ ꜱʜᴏᴜʟᴅ ʜᴀᴠᴇ ᴀᴅᴍɪɴ ᴘʀɪᴠɪʟᴇɢᴇ.
2. ᴏɴʟʏ ᴀᴅᴍɪɴꜱ ᴄᴀɴ ᴀᴅᴅ ꜰɪʟᴛᴇʀꜱ ɪɴ ᴀ ᴄʜᴀᴛ.
3. ᴀʟᴇʀᴛ ʙᴜᴛᴛᴏɴꜱ ʜᴀᴠᴇ ᴀ ʟɪᴍɪᴛ ᴏꜰ 64 ᴄʜᴀʀᴀᴄᴛᴇʀꜱ.
Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ:
• /filter - <code>ᴀᴅᴅ ᴀ ꜰɪʟᴛᴇʀ ɪɴ ᴀ ᴄʜᴀᴛ</code>
• /filters - <code>ʟɪꜱᴛ ᴀʟʟ ᴛʜᴇ ꜰɪʟᴛᴇʀꜱ ᴏꜰ ᴀ ᴄʜᴀᴛ</code>
• /del - <code>ᴅᴇʟᴇᴛᴇ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ꜰɪʟᴛᴇʀ ɪɴ ᴀ ᴄʜᴀᴛ</code>
• /delall - <code>ᴅᴇʟᴇᴛᴇ ᴛʜᴇ ᴡʜᴏʟᴇ ꜰɪʟᴛᴇʀꜱ ɪɴ ᴀ ᴄʜᴀᴛ (ᴄʜᴀᴛ ᴏᴡɴᴇʀ ᴏɴʟʏ)</code>"""

    BUTTON_TXT = """ʜᴇʟᴘ: <b>ʙᴜᴛᴛᴏɴꜱ</b>
- ᴛʜɪꜱ ʙᴏᴛ ꜱᴜᴘᴘᴏʀᴛꜱ ʙᴏᴛʜ ᴜʀʟ ᴀɴᴅ ᴀʟᴇʀᴛ ɪɴʟɪɴᴇ ʙᴜᴛᴛᴏɴꜱ.
<b>ɴᴏᴛᴇ:</b>
1. ᴛᴇʟᴇɢʀᴀᴍ ᴡɪʟʟ ɴᴏᴛ ᴀʟʟᴏᴡꜱ ʏᴏᴜ ᴛᴏ ꜱᴇɴᴅ ʙᴜᴛᴛᴏɴꜱ ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴄᴏɴᴛᴇɴᴛ, ꜱᴏ ᴄᴏɴᴛᴇɴᴛ ɪꜱ ᴍᴀɴᴅᴀᴛᴏʀʏ.
2. ᴛʜɪꜱ ʙᴏᴛ ꜱᴜᴘᴘᴏʀᴛꜱ ʙᴜᴛᴛᴏɴꜱ ᴡɪᴛʜ ᴀɴʏ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴇᴅɪᴀ ᴛʏᴘᴇ.
3. ʙᴜᴛᴛᴏɴꜱ ꜱʜᴏᴜʟᴅ ʙᴇ ᴘʀᴏᴘᴇʀʟʏ ᴘᴀʀꜱᴇᴅ ᴀꜱ ᴍᴀʀᴋᴅᴏᴡɴ ꜰᴏʀᴍᴀᴛ
<b>ᴜʀʟ ʙᴜᴛᴛᴏɴꜱ:</b>
<code>[Button Text](buttonurl:https://t.me/ArrowFlix)</code>
<b>ᴀʟᴇʀᴛ ʙᴜᴛᴛᴏɴꜱ:</b>
<code>[Button Text](buttonalert:ᴛʜɪꜱ ɪꜱ ᴀɴ ᴀʟᴇʀᴛ ᴍᴇꜱꜱᴀɢᴇ)</code>"""

    AUTOFILTER_TXT = """ʜᴇʟᴘ: <b>ᴀᴜᴛᴏ ꜰɪʟᴛᴇʀ</b>
<b>ɴᴏᴛᴇ: Fɪʟᴇ Iɴᴅᴇx</b>
1. ᴍᴀᴋᴇ ᴍᴇ ᴛʜᴇ ᴀᴅᴍɪɴ ᴏꜰ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ɪꜰ ɪᴛ'ꜱ ᴘʀɪᴠᴀᴛᴇ.
2. ᴍᴀᴋᴇ ꜱᴜʀᴇ ᴛʜᴀᴛ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴅᴏᴇꜱ ɴᴏᴛ ᴄᴏɴᴛᴀɪɴꜱ ᴄᴀᴍʀɪᴘꜱ, ᴘᴏʀɴ ᴀɴᴅ ꜰᴀᴋᴇ ꜰɪʟᴇꜱ.
3. ꜰᴏʀᴡᴀʀᴅ ᴛʜᴇ ʟᴀꜱᴛ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ᴍᴇ ᴡɪᴛʜ Qᴜᴏᴛᴇꜱ. ɪ'ʟʟ ᴀᴅᴅ ᴀʟʟ ᴛʜᴇ ꜰɪʟᴇꜱ ɪɴ ᴛʜᴀᴛ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴍʏ ᴅʙ.
<b>Nᴏᴛᴇ: AᴜᴛᴏFɪʟᴛᴇʀ</b>
1. Aᴅᴅ ᴛʜᴇ ʙᴏᴛ ᴀs ᴀᴅᴍɪɴ ᴏɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ.
2. Usᴇ /connect ᴀɴᴅ ᴄᴏɴɴᴇᴄᴛ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴛᴏ ᴛʜᴇ ʙᴏᴛ.
3. Usᴇ /settings ᴏɴ ʙᴏᴛ's PM ᴀɴᴅ ᴛᴜʀɴ ᴏɴ AᴜᴛᴏFɪʟᴛᴇʀ ᴏɴ ᴛʜᴇ sᴇᴛᴛɪɴɢs ᴍᴇɴᴜ."""

    CONNECTION_TXT = """ʜᴇʟᴘ: <b>ᴄᴏɴɴᴇᴄᴛɪᴏɴꜱ</b>
- ᴜꜱᴇᴅ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ʙᴏᴛ ᴛᴏ ᴘᴍ ꜰᴏʀ ᴍᴀɴᴀɢɪɴɢ ꜰɪʟᴛᴇʀꜱ 
- ɪᴛ ʜᴇʟᴘꜱ ᴛᴏ ᴀᴠᴏɪᴅ ꜱᴘᴀᴍᴍɪɴɢ ɪɴ ɢʀᴏᴜᴘꜱ.
<b>ɴᴏᴛᴇ:</b>
1. ᴏɴʟʏ ᴀᴅᴍɪɴꜱ ᴄᴀɴ ᴀᴅᴅ ᴀ ᴄᴏɴɴᴇᴄᴛɪᴏɴ.
2. ꜱᴇɴᴅ <code>/ᴄᴏɴɴᴇᴄᴛ</code> ꜰᴏʀ ᴄᴏɴɴᴇᴄᴛɪɴɢ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴘᴍ
Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ:
• /connect  - <code>ᴄᴏɴɴᴇᴄᴛ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴄʜᴀᴛ ᴛᴏ ʏᴏᴜʀ ᴘᴍ</code>
• /disconnect  - <code>ᴅɪꜱᴄᴏɴɴᴇᴄᴛ ꜰʀᴏᴍ ᴀ ᴄʜᴀᴛ</code>
• /connections - <code>ʟɪꜱᴛ ᴀʟʟ ʏᴏᴜʀ ᴄᴏɴɴᴇᴄᴛɪᴏɴꜱ</code>"""

    EXTRAMOD_TXT = """ʜᴇʟᴘ: Exᴛʀᴀ Mᴏᴅᴜʟᴇs
<b>ɴᴏᴛᴇ:</b>
ᴛʜᴇꜱᴇ ᴀʀᴇ ᴛʜᴇ ᴇxᴛʀᴀ ꜰᴇᴀᴛᴜʀᴇꜱ ᴏꜰ ᴛʜɪꜱ ʙᴏᴛ
Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ:
• /id - <code>ɢᴇᴛ ɪᴅ ᴏꜰ ᴀ ꜱᴘᴇᴄɪꜰɪᴇᴅ ᴜꜱᴇʀ.</code>
• /info  - <code>ɢᴇᴛ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴀ ᴜꜱᴇʀ.</code>
• /imdb  - <code>ɢᴇᴛ ᴛʜᴇ ꜰɪʟᴍ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ꜰʀᴏᴍ ɪᴍᴅʙ ꜱᴏᴜʀᴄᴇ.</code>
• /search  - <code>ɢᴇᴛ ᴛʜᴇ ꜰɪʟᴍ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ꜰʀᴏᴍ ᴠᴀʀɪᴏᴜꜱ ꜱᴏᴜʀᴄᴇꜱ.</code>"""

    ADMIN_TXT = """ʜᴇʟᴘ: Aᴅᴍɪɴ Mᴏᴅs
<b>ɴᴏᴛᴇ:</b>
Tʜɪs Mᴏᴅᴜʟᴇ Oɴʟʏ Wᴏʀᴋs Fᴏʀ Mʏ Aᴅᴍɪɴs
Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ:
• /logs - <code>ᴛᴏ ɢᴇᴛ ᴛʜᴇ ʀᴇᴄᴇɴᴛ ᴇʀʀᴏʀꜱ</code>
• /stats - <code>ᴛᴏ ɢᴇᴛ ꜱᴛᴀᴛᴜꜱ ᴏꜰ ꜰɪʟᴇꜱ ɪɴ ᴅʙ. [Tʜɪs Cᴏᴍᴍᴀɴᴅ Cᴀɴ Bᴇ Usᴇᴅ Bʏ Aɴʏᴏɴᴇ]</code>
• /delete - <code>ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ꜰɪʟᴇ ꜰʀᴏᴍ ᴅʙ.</code>
• /users - <code>ᴛᴏ ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴍʏ ᴜꜱᴇʀꜱ ᴀɴᴅ ɪᴅꜱ.</code>
• /chats - <code>ᴛᴏ ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴍʏ ᴄʜᴀᴛꜱ ᴀɴᴅ ɪᴅꜱ</code>
• /leave  - <code>ᴛᴏ ʟᴇᴀᴠᴇ ꜰʀᴏᴍ ᴀ ᴄʜᴀᴛ.</code>
• /disable  -  <code>ᴛᴏ ᴅɪꜱᴀʙʟᴇ ᴀ ᴄʜᴀᴛ.</code>
• /ban  - <code>ᴛᴏ ʙᴀɴ ᴀ ᴜꜱᴇʀ.</code>
• /unban  - <code>ᴛᴏ ᴜɴʙᴀɴ ᴀ ᴜꜱᴇʀ.</code>
• /channel - <code>ᴛᴏ ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴛᴏᴛᴀʟ ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴄʜᴀɴɴᴇʟꜱ</code>
• /broadcast - <code>ᴛᴏ ʙʀᴏᴀᴅᴄᴀꜱᴛ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ᴀʟʟ ᴜꜱᴇʀꜱ</code>
• /group_broadcast - <code>Tᴏ ʙʀᴏᴀᴅᴄᴀsᴛ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀʟʟ ᴄᴏɴɴᴇᴄᴛᴇᴅ ɢʀᴏᴜᴘs.</code>
• /gfilter - <code>ᴛᴏ ᴀᴅᴅ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs</code>
• /gfilters - <code>ᴛᴏ ᴠɪᴇᴡ ʟɪsᴛ ᴏғ ᴀʟʟ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs</code>
• /delg - <code>ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀ sᴘᴇᴄɪғɪᴄ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀ</code>
• /request - <code>Tᴏ sᴇɴᴅ ᴀ Mᴏᴠɪᴇ/Sᴇʀɪᴇs ʀᴇᴏ̨ᴜᴇsᴛ ᴛᴏ ʙᴏᴛ ᴀᴅᴍɪɴs. Oɴʟʏ ᴡᴏʀᴋs ᴏɴ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ. [Tʜɪs Cᴏᴍᴍᴀɴᴅ Cᴀɴ Bᴇ Usᴇᴅ Bʏ Aɴʏᴏɴᴇ]</code>
• /delallg - <code>Tᴏ ᴅᴇʟᴇᴛᴇ ᴀʟʟ Gғɪʟᴛᴇʀs ғʀᴏᴍ ᴛʜᴇ ʙᴏᴛ's ᴅᴀᴛᴀʙᴀsᴇ.</code>
• /deletefiles - <code>Tᴏ ᴅᴇʟᴇᴛᴇ CᴀᴍRɪᴘ ᴀɴᴅ PʀᴇDVD Fɪʟᴇs ғʀᴏᴍ ᴛʜᴇ ʙᴏᴛ's ᴅᴀᴛᴀʙᴀsᴇ.</code>"""

    STATUS_TXT = """<b>᚛› 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code></b>
<b>᚛› 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code></b>
<b>᚛› 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code></b>
<b>᚛› 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code></b>
<b>᚛› 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code></b>"""

    LOG_TEXT_G = """
    #𝐍𝐞𝐰𝐆𝐫𝐨𝐮𝐩

<b>᚛› 𝐆𝐫𝐨𝐮𝐩 ⪼ {a}(<code>{b}</code>)</b>
<b>᚛› 𝐆 𝐈𝐃 ⪼ @{c}
<b>᚛› 𝐓𝐨𝐭𝐚𝐥 𝐌𝐞𝐦𝐛𝐞𝐫𝐬 ⪼ {d}</b>
<b>᚛› 𝐀𝐝𝐝𝐞𝐝 𝐁𝐲 ⪼ {e}</b>
By {f}
"""

    LOG_TEXT_P = """
    #𝐍𝐞𝐰𝐔𝐬𝐞𝐫

<b>᚛› 𝐈𝐃 - <code>{}</code></b>
<b>᚛› 𝐍𝐚𝐦𝐞 - {}</b>
<b>᚛› 𝐔𝐍 - @{}</b>"""

    ALRT_TXT = """Hello {},
This is Not your Request
(الازرار ليست لك..! ارسل طلبك الان)"""

    OLD_ALRT_TXT = """Hey {},
You are using one of old message,
Request Again"""

    CUDNT_FND = """<b><i>
لم استطع تحديد ما كتبت ، تأكد من الكتابة بــ(الطريقة الصحيحة /Help)
𝖨 𝖼𝗈𝗎𝗅𝖽𝗇'𝗍 𝖿𝗂𝗇𝖽 𝖺𝗇𝗒𝗍𝗁𝗂𝗇𝗀 𝗋𝖾𝗅𝖺𝗍𝖾𝖽 𝗍𝗈 𝗍𝗁𝖺𝗍
𝖣𝗂𝖽 𝗒𝗈𝗎 𝗆𝖾𝖺𝗇 𝖺𝗇𝗒 𝗈𝗇𝖾 𝗈𝖿 𝗍𝗁𝖾𝗌𝖾?</i></b>"""

    I_CUDNT = """❌ <b>𝖨 𝖼𝗈𝗎𝗅𝖽𝗇'𝗍 𝖿𝗂𝗇𝖽 𝖺𝗇𝗒𝗍𝗁𝗂𝗇𝗀 𝗋𝖾𝗅𝖺𝗍𝖾𝖽 𝗍𝗈 𝗍𝗁𝖺𝗍\nلم استطع العثور عليه في قاعدة البيانات</b>\n\n‼ <b><i>𝖱𝖾𝗉𝗈𝗋𝗍 𝗍𝗈 𝖺𝖽𝗆𝗂𝗇 ▶ t.me/AFlix_Support/12</i></b>"""

    I_CUD_NT = """❌ <b>𝖨 𝖼𝗈𝗎𝗅𝖽𝗇'𝗍 𝖿𝗂𝗇𝖽 𝖺𝗇𝗒𝗍𝗁𝗂𝗇𝗀 𝗋𝖾𝗅𝖺𝗍𝖾𝖽 𝗍𝗈 𝗍𝗁𝖺𝗍\nلم استطع العثور عليه في قاعدة البيانات</b>\n\n‼ <b><i>𝖱𝖾𝗉𝗈𝗋𝗍 𝗍𝗈 𝖺𝖽𝗆𝗂𝗇 ▶ t.me/AFlix_Support/12</i></b>"""

    MVE_NT_FND = """❌ <b>𝖨 𝖼𝗈𝗎𝗅𝖽𝗇'𝗍 𝖿𝗂𝗇𝖽 𝖺𝗇𝗒𝗍𝗁𝗂𝗇𝗀 𝗋𝖾𝗅𝖺𝗍𝖾𝖽 𝗍𝗈 𝗍𝗁𝖺𝗍\nلم استطع العثور عليه في قاعدة البيانات</b>\n\n‼ <b><i>𝖱𝖾𝗉𝗈𝗋𝗍 𝗍𝗈 𝖺𝖽𝗆𝗂𝗇 ▶t.me/AFlix_Support/12</i></b>"""

    TOP_ALRT_MSG = """𝖢𝗁𝖾𝖼𝗄𝗂𝗇𝗀 𝖿𝗈𝗋 𝗊𝗎𝖾𝗋𝗒 𝗂𝗇 𝖣𝖺𝗍𝖺𝖻𝖺𝗌𝖾..."""

    MELCOW_ENG = """<b>Hey {}, Welcome to {}</b> 
• 𝖠𝗌𝗄 𝖸𝗈𝗎𝗋 𝖬𝗈𝗏𝗂𝖾𝗌 𝖶𝗂𝗍𝗁 𝖢𝗈𝗋𝗋𝖾𝖼𝗍 𝖲𝗉𝖾𝗅𝗅𝗂𝗇𝗀
• 𝖥𝖾𝖾𝗅 𝖥𝗋𝖾𝖾 𝖳𝗈 𝖱𝖾𝗉𝗈𝗋𝗍 𝖠𝗇𝗒 𝖤𝗋𝗋𝗈𝗋𝗌 𝖳𝗈 𝖠𝖽𝗆𝗂𝗇𝗌 𝗎𝗌𝗂𝗇𝗀 @admin
<u>𝗥𝗲𝗾𝘂𝗲𝘀𝘁𝘀 𝗙𝗼𝗿𝗺𝗮𝘁𝘀</u>
• Godfather 1972
• Gotham s03
• 𝖣𝖺𝗋𝗄 𝗌01e02
• The Dark Knight 2008
• 𝖥𝗋𝗂𝖾𝗇𝖽𝗌 𝗌03 1080𝗉
• Blade Runner 2017 x265 
• You Most Read This For More /Help
‼️𝗗𝗼𝗻𝘁 𝗮𝗱𝗱 𝘄𝗼𝗿𝗱𝘀 & 𝘀𝘆𝗺𝗯𝗼𝗹𝘀 𝗹𝗶𝗸𝗲 , . - """


    NORSLTS = """
#NoResults 
ID <b>: {}</b>
Name <b>: {}</b>
Message <b>: {}</b>"""

    
    ALL_FILTERS = """
<b>Hᴇʏ {}, Tʜᴇsᴇ ᴀʀᴇ ᴍʏ ᴛʜʀᴇᴇ ᴛʏᴘᴇs ᴏғ ғɪʟᴛᴇʀs.</b>"""
    
    GFILTER_TXT = """
<b>Wᴇʟᴄᴏᴍᴇ ᴛᴏ Gʟᴏʙᴀʟ Fɪʟᴛᴇʀs. Gʟᴏʙᴀʟ Fɪʟᴛᴇʀs ᴀʀᴇ ᴛʜᴇ ғɪʟᴛᴇʀs sᴇᴛ ʙʏ ʙᴏᴛ ᴀᴅᴍɪɴs ᴡʜɪᴄʜ ᴡɪʟʟ ᴡᴏʀᴋ ᴏɴ ᴀʟʟ ɢʀᴏᴜᴘs.</b>
    
Aᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs:
• /gfilter - <code>Tᴏ ᴄʀᴇᴀᴛᴇ ᴀ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀ.</code>
• /gfilters - <code>Tᴏ ᴠɪᴇᴡ ᴀʟʟ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs.</code>
• /delg - <code>Tᴏ ᴅᴇʟᴇᴛᴇ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀ.</code>
• /delallg - <code>ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀʟʟ ɢʟᴏʙᴀʟ ꜰɪʟᴛᴇʀꜱ.</code>"""
    
    FILE_STORE_TXT = """
<b>Fɪʟᴇ sᴛᴏʀᴇ ɪs ᴛʜᴇ ғᴇᴀᴛᴜʀᴇ ᴡʜɪᴄʜ ᴡɪʟʟ ᴄʀᴇᴀᴛᴇ ᴀ sʜᴀʀᴇᴀʙʟᴇ ʟɪɴᴋ ᴏғ ᴀ sɪɴɢʟᴇ ᴏʀ ᴍᴜʟᴛɪᴘʟᴇ ғɪʟᴇs.</b>
Aᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs:
• /batch - <code>Tᴏ ᴄʀᴇᴀᴛᴇ ᴀ ʙᴀᴛᴄʜ ʟɪɴᴋ ᴏғ ᴍᴜʟᴛɪᴘʟᴇ ғɪʟᴇs.</code>
• /link - <code>Tᴏ ᴄʀᴇᴀᴛᴇ ᴀ sɪɴɢʟᴇ ғɪʟᴇ sᴛᴏʀᴇ ʟɪɴᴋ.</code>
• /pbatch - <code>Jᴜsᴛ ʟɪᴋᴇ /batch, ʙᴜᴛ ᴛʜᴇ ғɪʟᴇs ᴡɪʟʟ ʙᴇ sᴇɴᴅ ᴡɪᴛʜ ғᴏʀᴡᴀʀᴅ ʀᴇsᴛʀɪᴄᴛɪᴏɴs.</code>
• /plink - <code>Jᴜsᴛ ʟɪᴋᴇ /link, ʙᴜᴛ ᴛʜᴇ ғɪʟᴇ ᴡɪʟʟ ʙᴇ sᴇɴᴅ ᴡɪᴛʜ ғᴏʀᴡᴀʀᴅ ʀᴇsᴛʀɪᴄᴛɪᴏɴ.</code>"""

    RESTART_TXT = """
<b>𝖡𝗈𝗍 𝖱𝖾𝗌𝗍𝖺𝗋𝗍𝖾𝖽 !</b>
📅 𝖣𝖺𝗍𝖾 : <code>{}</code>
⏰ 𝖳𝗂𝗆𝖾 : <code>{}</code>
🌐 𝖳𝗂𝗆𝖾𝗓𝗈𝗇𝖾 : <code>Asia/Kolkata</code>
🛠️ 𝖡𝗎𝗂𝗅𝖽 𝖲𝗍𝖺𝗍𝗎𝗌 : <code>𝗏2.7.3 [ 𝖲𝗍𝖺𝖻𝗅𝖾 ]</code></b>"""

    LOGO = """
ArrowFlix"""
