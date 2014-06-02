MusicCategory
=============

a tool to category unknown singer songs. use Baidu to find the information of the song and automatically copy the song to a direction named by the singer's name.


Usage:
=============

    python music.py <filename>[filename[filename]..]

you can define alias:

    alias mu='python ~/share/music_category/music.py '

the script will find possible singer name and sort the names by possibility. like below

    mu \[樊凡\]我想大声告诉你-樊凡.mp3

    0 樊凡
    1 我想大声告诉你
    2 樊凡我想大声告诉你
    3 我想大声告诉你樊凡
    4 伴奏
    5 搜寻你的名字电视剧《裸婚时代》2011插曲
    6 只需要一首歌
    7 忘不掉的海电视剧《裸婚时代》2011主题曲
    8 燃烧翅膀电视剧《蜗居》2009插曲
    9 樊凡我想大声告诉你dj小俞remix
    10 我不想逃电视剧《蜗居》2009主题曲
    11 我想大声告诉你电视剧《蜗居》2009主题曲
    12 守着你到永久电视剧《蜗居》2009插曲
    13 fanfan
    14 搬家电视剧《瞧这一家子》2010片尾曲
    15 风中的英雄
    16 李慧珍/樊凡
    17 重恋旧地电视剧《瞧这一家子》2010主题曲
    18 雨衣
    19 等不到的爱电视剧《裸婚时代》2011片尾曲
    20 不痛电视剧《裸婚时代》2011主题曲
    21 Dj小俞
    22 樊凡版
    23 樊凡聂
    select a most probably one: 
    0
    Sure to copy to category 樊凡? (Y/n)<---------------press Enter for yes

    [樊凡]我想大声告诉你-樊凡.mp3 樊凡
    cp '[樊凡]我想大声告诉你-樊凡.mp3' /media/cxh/exdisk/百度云同步盘/music//樊凡

Config:
=============

    url_pattern = "http://music.baidu.com/search?key=%s"

do not need to change, specify the search api of baidu mp3

    base_dir = "/media/cxh/exdisk/百度云同步盘/music/"

the base directory to store your music files. We will create sub directory(named by singer's name) under this directory.

Requirements:
=============

easy_install BeautifulSoup

use 结巴分词 before， but the result is not satisfied.
use ncurses before. But I can hardly find any documents.Maybe needs an UI.

Not tested under windows which I rarely used.
Maybe tested under mac later. Looking forword to the product launch of apple tonight.
