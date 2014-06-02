MusicCategory
=============

a tool to category unknown singer songs. use Baidu to find the information of the song and automatically copy the song to a directory named by the singer's name.


Usage:
=============

    python music.py <filename>[filename[filename]..]

you can define alias:

    alias mu='python ~/share/music_category/music.py '

the script will find possible singer name and sort the names by possibility. like below

    mu 泡沫.mp3

    0 泡沫
    1 G.E.M.邓紫棋
    2 李婧
    3 邰正宵
    4 简红
    5 泡沫泡沫G.E.M.邓紫棋
    6 花儿乐队
    7 新秀团队
    8 泡沫电视剧《熊猫人》2010插曲
    9 谢婉婷
    10 泡沫泡沫—G.E.M.邓紫棋
    11 王韵婵
    12 邓紫棋
    13 祝兰兰
    14 路绮欧
    15 Days
    16 거품
    17 吴彤
    18 河村隆一
    19 Beautiful
    20 夏天Alex
    21 李炆
    22 奥华子
    23 南拳妈妈
    24 泡沫电视剧《撞车》主题曲
    25 陈晓东
    select a most probably one: 
    12
    Sure to copy to category 邓紫棋? (Y/n)

    泡沫.mp3 邓紫棋
    cp '泡沫.mp3' /media/cxh/exdisk/百度云同步盘/music//邓紫棋

Result:

    /media/cxh/exdisk/百度云同步盘/music/邓紫棋 > tree
    .
    └── 泡沫.mp3

It's 琪 instead of 棋 actually.......

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
