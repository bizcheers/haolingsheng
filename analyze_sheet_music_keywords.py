import os
import re
from pathlib import Path

# Mapping of search keywords to instrument folder names in /gepu/
INSTRUMENT_MAPPING = {
    'viola': 'viola',
    'clarinet': 'clarinet',
    'cello': 'cello',
    'violin': 'violin',
    'fiddle': 'violin',
    'guitar': 'guitar',
    'uke': 'ukulele',
    'ukulele': 'ukulele',
    'flute': 'flute',
    'piano': 'piano',
    'trumpet': 'trumpet',
    'trombone': 'trombone',
    'recorder': 'recorder',
    'soprano recorder': 'recorder',
    'alto sax': 'alto-sax',
    'tenor sax': 'tenor-sax',
    'saxophone': 'alto-sax',  # default to alto
    'harmonica': 'harmonica',
    'bagpipe': 'bagpipes',
    'bass guitar': 'bass-guitar'
}

# Songs that are restricted by copyright (as mentioned in previous analysis)
COPYRIGHT_RESTRICTED = [
    'how great thou art',
    'feliz navidad' # usually restricted
]

# The raw keyword list from the prompt
RAW_KEYWORDS = """amazing grace viola sheet music	信息	10	站点子链, 图片包, 视频, 视频轮播, 相关搜索	0	0	90	0	https://www.capotastomusic.com/viola-sheet-music/easy/amazing-grace-viola.pdf	2月28日
amazing grace viola sheet music	信息	67	站点子链, 图片包, 视频, 视频轮播, 相关搜索	0	0	90	0	https://www.capotastomusic.com/viola-sheet-music.htm	2月28日
amazing grace viola sheet music	信息	69	站点子链, 图片包, 视频, 视频轮播, 相关搜索	0	0	90	0	https://www.capotastomusic.com/viola-sheet-music.htm	2月28日
deck the halls sheet music pdf free	信息	87	图片, 图片包, 视频, 相关搜索	0	0	40	0	https://www.capotastomusic.com/clarinet-sheet-music/christmas/deck-the-halls-easy-clarinet.pdf	2月11日
cello music sheets for beginners	商务	3	站点子链, 图片, 图片包, 视频, 相关问题, 相关搜索, 热门产品	3	0.08	40	0	https://www.capotastomusic.com/cello-sheet-music/easy.htm	2月22日
we wish you a merry christmas music sheet for violin	信息	42	AI 概览, 图片, 图片包, 视频, 视频轮播, 相关搜索, 购物广告	0	0	70	0	https://www.capotastomusic.com/violin-sheet-music/christmas/we-wish-you-a-merry-christmas-violin.pdf	2月26日
she be coming round the mountain chords	信息	51	图片包, 视频, 视频轮播, 相关搜索	0	0	110	0	https://www.capotastomusic.com/guitar_pages/resources/guitar_tablature/she'll-be-coming-round-the-mountain-gtm.pdf	1月25日
she be coming round the mountain chords	信息	71	图片包, 视频, 视频轮播, 相关搜索	0	0	110	0	https://www.capotastomusic.com/guitar_pages/resources/guitar_tablature/she'll-be-coming-round-the-mountain-gtm.pdf	1月25日
auld lang syne sheet music bagpipes	信息	65	图片, 图片包, 视频, 相关搜索	0	0	40	0	https://www.capotastomusic.com/piano-sheet-music/beginners/auld-lang-syne.pdf	2月28日
auld lang syne sheet music bagpipes	信息	68	图片, 图片包, 视频, 相关搜索	0	0	40	0	https://www.capotastomusic.com/piano-sheet-music/beginners/auld-lang-syne.pdf	2月28日
hark the herald angels sing flute sheet music	信息	14	站点子链, 图片包, 视频, 视频轮播, 相关问题, 相关搜索	0	0	40	0	https://www.capotastomusic.com/flute-sheet-music/christmas/hark-the-herald-angels-sing-flute.pdf	2月15日
christmas songs easy piano free	信息	71	AI 概览, 视频, 视频轮播, 相关搜索, 短视频	0	0	40	0	https://www.capotastomusic.com/piano-sheet-music/christmas.htm	3月05日
angels we have heard on high music sheet pdf	信息	43	图片, 图片包, 视频, 相关搜索	0	0	40	0	https://www.capotastomusic.com/piano-sheet-music/christmas/angels-we-have-heard-on-high-easy-piano.pdf	3月12日
how great thou art piano score	信息	41	图片包, 视频, 视频轮播, 相关搜索	0	0	170	0	https://www.capotastomusic.com/piano-sheet-music/easy/how-great-thou-art.pdf	3月04日
bingo song chords	信息	16	图片包, 视频, 视频轮播, 相关搜索	0	0	50	0	https://www.capotastomusic.com/guitar_pages/resources/easy_guitar_tab/bingo-easy-guitar-tab.pdf	3月01日
o holy night music sheet piano	信息	25	站点子链, 图片包, 视频, 视频轮播, 相关搜索	0	0	70	0	https://www.capotastomusic.com/piano-sheet-music/christmas/o-holy-night-easy-piano.pdf	2月05日
happy birthday piano score pdf	信息	3	图片, 图片包, 视频, 相关搜索	4	0.11	70	0	https://www.capotastomusic.com/piano-sheet-music/beginners/happy-birthday-to-you.pdf	2月07日
row row row your boat tab	信息, 交易	8	图片包, 视频, 视频轮播, 相关搜索	0	0	50	0	https://www.capotastomusic.com/guitar_pages/resources/guitar_tablature/row-your-boat-gtm.pdf	4 天
we wish you a merry christmas cello sheet music	信息	3	图片, 图片包, 视频, 视频轮播, 讨论和论坛, 相关搜索	2	0.05	40	0	https://www.capotastomusic.com/cello-sheet-music/christmas/we-wish-you-a-merry-christmas-cello.pdf	3月21日
simple violin songs for beginners	信息	22	站点子链, AI 概览, 图片, 视频, 视频轮播, 讨论和论坛, 相关搜索	0	0	170	0	https://www.capotastomusic.com/violin-sheet-music/easy.htm	3月22日
trumpet solos pdf	信息	28	站点子链, 视频, 相关搜索	0	0	70	0	https://www.capotastomusic.com/trumpet-sheet-music/easy.htm	2月07日
joy to the world on piano sheet music	信息	30	图片, 图片包, 视频, 视频轮播, 相关搜索	0	0	40	0	https://www.capotastomusic.com/piano-sheet-music/christmas/joy-to-the-world-easy-piano.pdf	3月08日
trombone beginner sheet music	信息	10	站点子链, 图片, 图片包, 视频, 相关搜索	0	0	40	0	https://www.capotastomusic.com/trombone-sheet-music/easy.htm	1月25日
trombone beginner sheet music	信息	76	站点子链, 图片, 图片包, 视频, 相关搜索	0	0	40	0	https://www.capotastomusic.com/trombone-sheet-music.htm	1月25日
old macdonald had a farm piano sheet music	信息	7	站点子链, 图片包, 视频, 视频轮播, 相关搜索	2	0.05	140	0	https://www.capotastomusic.com/piano-sheet-music/beginners/old-mac-donald-had-a-farm-beginner-piano.pdf	3月10日
when the saints piano sheet music	信息	52	图片, 图片包, 视频, 视频轮播, 相关搜索	0	0	110	0	https://www.capotastomusic.com/piano-sheet-music/easy/when-the-saints.pdf	1月28日
america the beautiful guitar tab	信息, 交易	16	图片包, 视频, 视频轮播, 相关搜索	0	0	40	0	https://www.capotastomusic.com/bass-guitar-sheet-music/easy/america-the-beautiful-bass-tab.pdf	2月26日
silent night on recorder sheet music	信息, 交易	5	图片包, 视频, 视频轮播, 相关搜索	0	0	40	0	https://www.capotastomusic.com/soprano-recorder-sheet-music/christmas/silent-night-soprano-recorder.pdf	3月20日
hark the herald angels sing piano score	信息	24	图片, 图片包, 视频, 视频轮播, 相关搜索	0	0	170	0	https://www.capotastomusic.com/piano-sheet-music/christmas/hark-the-herald-angels-sing-easy-piano.pdf	3月16日
jolly old saint nicholas sheet music	信息	34	图片, 图片包, 视频, 相关搜索	0	0	110	0	https://www.capotastomusic.com/piano-sheet-music/christmas/jolly-old-st-nicholas-easy-piano.pdf	1月26日
jolly old saint nicholas sheet music	信息	40	图片, 图片包, 视频, 相关搜索	0	0	110	0	https://www.capotastomusic.com/piano-sheet-music/christmas/jolly-old-st-nicholas-easy-piano.pdf	1月26日
free jingle bells sheet music	信息	46	站点子链, 图片, 图片包, 视频, 视频轮播, 相关搜索	0	0	110	0	https://www.capotastomusic.com/piano-sheet-music/christmas/jingle-bells-beginner-piano.pdf	3月17日
flute sheet music we wish you a merry christmas	信息	24	图片, 图片包, 视频, 视频轮播, 相关搜索	0	0	40	0	https://www.capotastomusic.com/flute-sheet-music/christmas/we-wish-you-a-merry-christmas-flute.pdf	2月20日
angels we have heard on high piano sheet music	信息	39	图片, 图片包, 视频, 视频轮播, 相关搜索	0	0	140	0	https://www.capotastomusic.com/piano-sheet-music/christmas/angels-we-have-heard-on-high-easy-piano.pdf	3月15日
twelve days of christmas sheet	信息	32	图片, 图片包, 视频, 相关搜索	0	0	30	0	https://www.capotastomusic.com/piano-sheet-music/christmas/the-twelve-days-of-christmas-easy-piano.pdf	2月22日
old macdonald had a farm notes for piano	信息, 交易	3	图片包, 视频, 视频轮播, 相关搜索, 短视频	4	0.11	170	0	https://www.capotastomusic.com/piano-sheet-music/beginners/old-mac-donald-had-a-farm-beginner-piano.pdf	3月19日
cello sheet music free popular songs	信息	16	AI 概览, 图片包, 视频, 相关搜索	0	0	30	0	https://www.capotastomusic.com/cello-sheet-music/easy.htm	3月12日
piano sheet music for how great thou art	信息	39	图片, 图片包, 视频, 视频轮播, 相关搜索	0	0	110	0	https://www.capotastomusic.com/piano-sheet-music/easy/how-great-thou-art.pdf	2月12日
easy sheet music violin	信息	15	站点子链, 图片包, 视频, 视频轮播, 相关搜索	0	0	70	0	https://www.capotastomusic.com/violin-sheet-music/easy.htm	3月09日
easy sheet music violin	信息	19	站点子链, 图片包, 视频, 视频轮播, 相关搜索	0	0	70	0	https://www.capotastomusic.com/violin-sheet-music/easy.htm	3月09日
daisy bell guitar chords	信息, 交易	42	图片, 视频, 视频轮播, 相关搜索, 短视频	0	0	40	0	https://www.capotastomusic.com/guitar_pages/resources/guitar_tablature/daisy-bell-guitar-tab.pdf	4 天
daisy bell guitar chords	信息, 交易	52	图片, 视频, 视频轮播, 相关搜索, 短视频	0	0	40	0	https://www.capotastomusic.com/guitar_pages/resources/guitar_tablature/daisy-bell-guitar-tab.pdf	4 天
daisy bell guitar chords	信息, 交易	65	图片, 视频, 视频轮播, 相关搜索, 短视频	0	0	40	0	https://www.capotastomusic.com/bass-guitar-sheet-music/easy/daisy-bell.pdf	4 天
christmas music free pdf	商务, 信息	71	站点子链, 视频, 相关搜索	0	0	40	0	https://www.capotastomusic.com/piano-sheet-music/christmas.htm	2月16日
christmas music free pdf	商务, 信息	90	站点子链, 视频, 相关搜索	0	0	40	0	https://www.capotastomusic.com/piano-sheet-music/christmas.htm	2月16日
christmas music free pdf	商务, 信息	97	站点子链, 视频, 相关搜索	0	0	40	0	https://www.capotastomusic.com/piano-sheet-music/christmas.htm	2月16日
america the beautiful sheet music for flute	商务, 信息	32	图片, 图片包, 视频, 视频轮播, 相关搜索, 热门产品	0	0	50	0	https://www.capotastomusic.com/flute-sheet-music/easy/america-the-beautiful-easy-flute-solo.pdf	2月15日
we shall overcome music sheet	信息	58	图片, 图片包, 视频, 相关搜索	0	0	70	0	https://www.capotastomusic.com/soprano-recorder-sheet-music/easy/we-shall-overcome-soprano-recorder.pdf	3月21日
we shall overcome music sheet	信息	69	图片, 图片包, 视频, 相关搜索	0	0	70	0	https://www.capotastomusic.com/soprano-recorder-sheet-music/easy/we-shall-overcome-soprano-recorder.pdf	3月21日
angels we have heard on high violin sheet music	信息	36	图片, 图片包, 视频, 视频轮播, 相关搜索	0	0	40	0	https://www.capotastomusic.com/violin-sheet-music/christmas/angels-we-have-heard-on-high-violin.pdf	2月28日
angels we have heard on high violin sheet music	信息	43	图片, 图片包, 视频, 视频轮播, 相关搜索	0	0	40	0	https://www.capotastomusic.com/violin-sheet-music/christmas/angels-we-have-heard-on-high-violin.pdf	2月28日
solo music for clarinet	信息	82	站点子链, 视频, 视频轮播, 相关问题, 讨论和论坛, 相关搜索, 短视频	0	0	70	0	https://www.capotastomusic.com/clarinet-sheet-music/easy.htm	1月30日
how great thou art music score	信息	32	图片包, 视频, 视频轮播, 讨论和论坛, 相关搜索	0	0	170	0	https://www.capotastomusic.com/piano-sheet-music/easy/how-great-thou-art.pdf	2月27日
morning has broken ukulele chords	信息	8	视频, 视频轮播, 相关搜索, 短视频	0	0	40	0	https://www.capotastomusic.com/ukulele-sheet-music/songs/morning-has-broken-ukulele-song.pdf	3月12日
away in a manger chords pdf	信息	46	视频, 相关问题, 相关搜索	0	0	40	0	https://www.capotastomusic.com/guitar_pages/resources/christmas_guitar_tab/away-in-a-manger-guitar-tab.pdf	1月29日
joy to the world piano music sheet	信息	27	图片包, 视频, 视频轮播, 相关搜索	0	0	40	0	https://www.capotastomusic.com/piano-sheet-music/christmas/joy-to-the-world-easy-piano.pdf	3月02日
o holy night piano pdf	商务, 信息	28	图片包, 视频, 相关问题, 相关搜索	0	0	40	0	https://www.capotastomusic.com/piano-sheet-music/christmas/o-holy-night-easy-piano.pdf	2月18日
o holy night piano pdf	商务, 信息	39	图片包, 视频, 相关问题, 相关搜索	0	0	40	0	https://www.capotastomusic.com/piano-sheet-music/christmas/o-holy-night-easy-piano.pdf	2月18日
o holy night piano pdf	商务, 信息	48	图片包, 视频, 相关问题, 相关搜索	0	0	40	0	https://www.capotastomusic.com/piano-sheet-music/christmas/o-holy-night-easy-piano.pdf	2月18日
christmas piano sheet music for beginners free	信息	19	站点子链, AI 概览, 图片, 图片包, 视频, 相关搜索	0	0	40	0	https://www.capotastomusic.com/piano-sheet-music/christmas.htm	3月05日
o holy night piano score	信息	36	图片包, 视频, 视频轮播, 相关搜索	0	0	90	0	https://www.capotastomusic.com/piano-sheet-music/christmas/o-holy-night-easy-piano.pdf	3月24日
flute sheet music intermediate	商务, 信息	38	站点子链, 图片, 图片包, 视频, 相关搜索, 热门产品	0	0	30	0	https://www.capotastomusic.com/flute-sheet-music/easy.htm	2月03日
oh holy night piano sheet music pdf free	信息	33	视频, 相关搜索	0	0	40	0	https://www.capotastomusic.com/piano-sheet-music/christmas/o-holy-night-easy-piano.pdf	3月19日
star spangled banner trumpet 2	信息, 交易	21	图片, 图片包, 视频, 视频轮播, 相关搜索	0	0	40	0	https://www.capotastomusic.com/trumpet-sheet-music/easy/the-star-spangled-banner-trumpet.pdf	1月29日
guitar christmas songs sheet music	商务	36	站点子链, 图片, 图片包, 视频, 视频轮播, 讨论和论坛, 相关搜索, 热门产品	0	0	30	0	https://www.capotastomusic.com/guitar_pages/christmas_guitar_tab.htm	3月22日
easy songs on trumpet for beginners	信息	11	站点子链, AI 概览, 视频, 视频轮播, 相关搜索, 短视频	0	0	50	0	https://www.capotastomusic.com/trumpet-sheet-music/easy.htm	3月12日
ukulele music books free	信息	35	站点子链, AI 概览, 视频, 视频轮播, 讨论和论坛, 相关搜索	0	0	70	0	https://www.capotastomusic.com/ukulele-sheet-music/tabs.htm	3月03日
mary had a little lamb piano chords	信息	76	图片包, 视频, 视频轮播, 相关问题, 相关搜索, 短视频	0	0	210	1	https://www.capotastomusic.com/piano-sheet-music/beginners/mary-had-a-little-lamb-beginner-piano-sheet-music.pdf	2月24日
how great thou art sheet music free	信息	39	图片, 图片包, 视频, 视频轮播, 相关搜索	0	0	110	1	https://www.capotastomusic.com/piano-sheet-music/easy/how-great-thou-art.pdf	2月21日
o holy night trumpet sheet music	信息	2	站点子链, 图片包, 视频, 视频轮播, 相关搜索	5	0.14	70	1	https://www.capotastomusic.com/trumpet-sheet-music/christmas/o-holy-night-easy-trumpet.pdf	3月05日
ode to joy sheet music pdf	信息	28	图片包, 视频, 相关搜索	0	0	50	1	https://www.capotastomusic.com/piano-sheet-music/beginners/ode-to-joy.pdf	3月07日
ode to joy sheet music pdf	信息	39	图片包, 视频, 相关搜索	0	0	50	1	https://www.capotastomusic.com/piano-sheet-music/beginners/ode-to-joy.pdf	3月07日
ode to joy sheet music pdf	信息	83	图片包, 视频, 相关搜索	0	0	50	1	https://www.capotastomusic.com/guitar_pages/resources/guitar_tablature/ode-to-joy-gtm.pdf	3月07日
silent night guitar tab pdf	信息, 交易	4	图片包, 视频, 视频轮播, 相关搜索	2	0.05	40	1	https://www.capotastomusic.com/guitar_pages/resources/guitar-christmas-solos/silent-night-guitar-tab-solo.pdf	1月14日
silent night guitar tab pdf	信息, 交易	66	图片包, 视频, 视频轮播, 相关搜索	0	0	40	1	https://www.capotastomusic.com/guitar_pages/resources/christmas_guitar_tab/silent-night-christmas-tablature-melody.pdf	1月14日
christmas sheet music flute free	信息	74	站点子链, 图片, 图片包, 视频, 相关搜索	0	0	30	1	https://www.capotastomusic.com/flute-sheet-music/christmas/o-christmas-tree-flute.pdf	2月20日
fur elise for cello	信息, 交易	12	图片包, 视频, 视频轮播, 相关搜索, 短视频	0	0	70	1	https://www.capotastomusic.com/cello-sheet-music/easy/fur-elise-cello.pdf	3月02日
fur elise for cello	信息, 交易	56	图片包, 视频, 视频轮播, 相关搜索, 短视频	0	0	70	1	https://capotastomusic.com/cello-sheet-music/easy/fur-elise.pdf	3月02日
christmas songs for flute free	信息	21	站点子链, 视频, 相关搜索	0	0	30	1	https://www.capotastomusic.com/flute-sheet-music/christmas.htm	3月11日
jolly good fellow sheet music	信息	60	图片, 图片包, 视频, 视频轮播, 相关搜索	0	0	70	1	https://www.capotastomusic.com/piano-sheet-music/beginners/for-he's-a-jolly-good-fellow.pdf	2月23日
she'll be coming round the mountain tab	信息, 交易	47	图片包, 视频, 视频轮播, 相关问题, 相关搜索	0	0	140	1	https://www.capotastomusic.com/guitar_pages/resources/guitar_tablature/she'll-be-coming-round-the-mountain-gtm.pdf	3月02日
christmas sheet music tenor sax	商务	20	图片, 图片包, 视频, 相关搜索, 热门产品	0	0	30	1	https://www.capotastomusic.com/tenor-saxophone-sheet-music/christmas.htm	3月22日
piano sheet music for beginners popular songs	信息	73	图片, 视频, 视频轮播, 相关搜索	0	0	40	1	https://www.capotastomusic.com/piano-sheet-music/beginners.htm	2月24日
piano sheet music for beginners popular songs	信息	82	图片, 视频, 视频轮播, 相关搜索	0	0	40	1	https://www.capotastomusic.com/piano-sheet-music/beginners.htm	2月24日
row row your boat guitar tab	信息, 交易	3	图片, 图片包, 视频, 视频轮播, 相关搜索	2	0.05	70	1	https://www.capotastomusic.com/guitar_pages/resources/guitar_tablature/row-your-boat-gtm.pdf	3月08日
jesu joy of man's desiring pdf piano	信息	23	图片包, 视频, 相关搜索	0	0	50	1	https://www.capotastomusic.com/piano-sheet-music/easy/jesu-joy-of-man's-desiring.pdf	2月15日
jesu joy of man's desiring pdf piano	信息	33	图片包, 视频, 相关搜索	0	0	50	1	https://www.capotastomusic.com/piano-sheet-music/easy/jesu-joy-of-man's-desiring.pdf	2月15日
come all ye faithful trumpet	信息, 交易	9	图片包, 视频, 视频轮播, 相关搜索, 短视频	0	0	40	1	https://www.capotastomusic.com/trumpet-sheet-music/christmas/o-come-all-ye-faithful-easy-trumpet.pdf	2月10日
music sheets for trumpet beginners	信息	4	图片, 图片包, 视频, 视频轮播, 讨论和论坛, 相关搜索, 热门产品	7	0.2	260	1	https://www.capotastomusic.com/trumpet-sheet-music/easy.htm	3月14日
music sheets for trumpet beginners	信息	10	图片, 图片包, 视频, 视频轮播, 讨论和论坛, 相关搜索, 热门产品	0	0	260	1	https://www.capotastomusic.com/trumpet-sheet-music/easy.htm	3月14日
america the beautiful sheet music trumpet	商务	6	图片包, 视频, 相关搜索, 热门产品	2	0.05	70	1	https://www.capotastomusic.com/trumpet-sheet-music/easy/america-the-beautiful-trumpet.pdf	3月04日
mary had a little lamb music sheet for clarinet	信息	53	视频, 相关搜索	0	0	70	1	https://www.capotastomusic.com/piano-sheet-music/basic/mary-had-a-little-lamb.pdf	3月19日
sheet music for god save the queen	信息	28	图片包, 视频, 视频轮播, 相关搜索	0	0	50	1	https://www.capotastomusic.com/piano-sheet-music/beginners/god-save-the-queen.pdf	3月03日
ukulele christmas music tabs	信息	4	站点子链, 图片, 视频, 视频轮播, 讨论和论坛, 相关搜索	4	0.11	70	1	https://www.capotastomusic.com/ukulele-sheet-music/christmas.htm	3月09日
oh when the saints piano notes	信息, 交易	54	图片, 图片包, 视频, 视频轮播, 相关搜索, 短视频	0	0	40	1	https://www.capotastomusic.com/piano-sheet-music/easy/when-the-saints.pdf	2月24日
o holy night sheet music clarinet	信息	16	图片包, 视频, 视频轮播, 热门产品	0	0	40	1	https://www.capotastomusic.com/clarinet-sheet-music/christmas/o-holy-night-easy-clarinet.pdf	3月07日
o holy night sheet music clarinet	信息	23	图片包, 视频, 视频轮播, 热门产品	0	0	40	1	https://www.capotastomusic.com/clarinet-sheet-music/christmas/o-holy-night-easy-clarinet.pdf	3月07日
home home on the range chords	信息	55	视频, 相关搜索, 短视频	0	0	140	1	https://capotastomusic.com/guitar_pages/resources/guitar_tablature/home-on-the-range-gtm.pdf	2月07日
christmas sheet music for violin and piano	商务	51	站点子链, 图片, 视频, 视频轮播, 讨论和论坛, 相关搜索, 热门产品	0	0	30	1	https://www.capotastomusic.com/violin-sheet-music/christmas.htm	3月22日
christmas sheet music for violin and piano	商务	67	站点子链, 图片, 视频, 视频轮播, 讨论和论坛, 相关搜索, 热门产品	0	0	30	1	https://www.capotastomusic.com/violin-sheet-music/christmas.htm	3月22日
god rest ye merry gentlemen alto sax	信息, 交易	31	图片包, 视频, 视频轮播, 相关搜索	0	0	40	1	https://www.capotastomusic.com/alto-saxophone-sheet-music/christmas/god-rest-ye-merry-gentlemen-alto-saxophone.pdf	3月17日
mary had a little lamb notes saxophone	信息	10	图片包, 视频, 视频轮播, 相关搜索	0	0	50	1	https://www.capotastomusic.com/alto-saxophone-sheet-music/easy/mary-had-a-little-lamb-alto-saxophone.pdf	3月18日
recorder notes for jolly old saint nicholas	信息, 交易	91	图片, 图片包, 视频, 视频轮播, 相关搜索	0	0	40	1	https://www.capotastomusic.com/flute-sheet-music/christmas/jolly-old-st-nicholas-flute.pdf	3月08日
daisy bell chords	信息	58	图片, 视频, 视频轮播, 相关搜索	0	0	170	1	https://www.capotastomusic.com/bass-guitar-sheet-music/easy/daisy-bell.pdf	3月14日
daisy bell chords	信息	81	图片, 视频, 视频轮播, 相关搜索	0	0	170	1	https://www.capotastomusic.com/bass-guitar-sheet-music/easy/daisy-bell.pdf	3月14日
easy christmas songs for violin	信息	38	站点子链, AI 概览, 图片, 图片包, 视频, 视频轮播, 相关搜索	0	0	40	1	https://www.capotastomusic.com/violin-sheet-music/christmas.htm	3月21日
solos for tenor sax	商务	26	图片, 视频, 视频轮播, 热门产品	0	0	90	1	https://www.capotastomusic.com/tenor-saxophone-sheet-music/easy.htm	3月09日
good king wenceslas guitar chords	信息, 交易	40	图片, 图片包, 视频, 视频轮播, 相关搜索	0	0	40	1	https://www.capotastomusic.com/guitar_pages/resources/christmas_guitar_tab/good-king-wenceslas-guitar-tab.pdf	3月14日
violin deck the halls music sheet	信息, 交易	8	站点子链, 图片包, 视频, 视频轮播, 相关搜索	1	0.02	90	1	https://capotastomusic.com/violin-sheet-music/christmas/deck-the-halls-violin.pdf	1月28日
amazing grace bagpipe sheet music	信息, 交易	81	图片, 图片包, 视频, 视频轮播, 相关问题, 相关搜索	0	0	170	1	https://www.capotastomusic.com/soprano-recorder-sheet-music/easy/amazing-grace-soprano-recorder.pdf	2月18日
easy christmas songs for alto sax	信息, 交易	40	站点子链, AI 概览, 图片, 图片包, 视频, 视频轮播, 相关问题, 相关搜索	0	0	40	1	https://www.capotastomusic.com/alto-saxophone-sheet-music/christmas.htm	3月01日
feliz navidad sheet music clarinet	信息	43	图片, 图片包, 视频, 视频轮播, 相关搜索	0	0	50	1	https://www.capotastomusic.com/clarinet-sheet-music/christmas/we-wish-you-a-merry-christmas-easy-clarinet.pdf	3 天
feliz navidad sheet music clarinet	信息	48	图片, 图片包, 视频, 视频轮播, 相关搜索	0	0	50	1	https://www.capotastomusic.com/clarinet-sheet-music/christmas/we-wish-you-a-merry-christmas-easy-clarinet.pdf	3 天
o come all ye faithful sheet music trumpet	信息	3	图片包, 视频, 视频轮播, 相关搜索	2	0.05	40	1	https://www.capotastomusic.com/trumpet-sheet-music/christmas/o-come-all-ye-faithful-easy-trumpet.pdf	3月19日
guitar chords for this land is your land	信息, 交易	73	站点子链, AI 概览, 图片, 视频, 视频轮播, 相关搜索	0	0	110	1	https://www.capotastomusic.com/guitar_pages/resources/easy_guitar_tab/this-land-is-your-land-easy-guitar-tab.pdf	3月18日
old macdonald had a farm violin sheet music	信息	23	图片包, 视频, 视频轮播, 相关搜索	0	0	40	1	https://capotastomusic.com/violin-sheet-music/easy/old-mac-donald-had-a-farm-violin.pdf	2月19日
old macdonald had a farm violin sheet music	信息	66	图片包, 视频, 视频轮播, 相关搜索	0	0	40	1	https://www.capotastomusic.com/piano-sheet-music/beginners/old-mac-donald-had-a-farm-beginner-piano.pdf	2月19日
old macdonald had a farm violin sheet music	信息	88	图片包, 视频, 视频轮播, 相关搜索	0	0	40	1	https://www.capotastomusic.com/piano-sheet-music/beginners/old-mac-donald-had-a-farm-beginner-piano.pdf	2月19日
national anthem on trumpet sheet music	信息	2	图片包, 视频, 视频轮播, 相关搜索	7	0.19	90	1	https://www.capotastomusic.com/trumpet-sheet-music/easy/the-star-spangled-banner-trumpet.pdf	2月05日
oh when the saints music sheet	信息	64	图片, 图片包, 视频, 相关搜索	0	0	70	1	https://www.capotastomusic.com/violin-sheet-music/easy/when-the-saints-go-marching-in-violin.pdf	3月17日
silent night guitar notes sheet	信息	79	图片, 图片包, 视频, 视频轮播, 相关搜索	0	0	50	1	https://www.capotastomusic.com/bass-guitar-sheet-music/christmas/silent-night-bass-guitar.pdf	2月19日
free happy birthday sheet music for piano	信息	27	图片, 图片包, 视频, 视频轮播, 相关搜索	0	0	110	1	https://www.capotastomusic.com/piano-sheet-music/beginners/happy-birthday-to-you.pdf	2月01日
silent night clarinet notes	信息, 交易	8	图片, 图片包, 视频, 视频轮播, 相关搜索	0	0	40	1	https://www.capotastomusic.com/clarinet-sheet-music/christmas/silent-night-easy-clarinet.pdf	3月20日
o holy night pdf sheet music	信息	35	图片, 图片包, 视频, 相关搜索	0	0	50	1	https://www.capotastomusic.com/piano-sheet-music/christmas/o-holy-night-easy-piano.pdf	1月28日
twinkle notes violin	信息	8	站点子链, 图片包, 视频, 视频轮播, 相关问题, 相关搜索, 短视频	0	0	40	1	https://www.capotastomusic.com/violin-sheet-music/easy/twinkle-twinkle-little-star-violin.pdf	1月27日
amazing grace on viola	信息	11	图片包, 视频, 视频轮播, 相关搜索, 短视频	0	0	40	1	https://www.capotastomusic.com/viola-sheet-music/easy/amazing-grace-viola.pdf	2月27日
silent night notes for clarinet	信息, 交易	9	图片包, 视频, 视频轮播, 相关搜索	0	0	40	1	https://www.capotastomusic.com/clarinet-sheet-music/christmas/silent-night-easy-clarinet.pdf	3月20日
mary had a little lamb music sheet piano	信息	22	站点子链, 图片, 图片包, 视频, 相关搜索	0	0	50	1	https://www.capotastomusic.com/piano-sheet-music/beginners/mary-had-a-little-lamb-beginner-piano-sheet-music.pdf	3月16日
sheet music when the saints go marching in	信息	74	视频, 视频轮播, 相关搜索	0	0	70	1	https://www.capotastomusic.com/flute-sheet-music/easy/when-the-saints-go-marching-in-easy-flute-solo.pdf	3月14日
sheet music when the saints go marching in	信息	75	视频, 视频轮播, 相关搜索	0	0	70	1	https://www.capotastomusic.com/flute-sheet-music/easy/when-the-saints-go-marching-in-easy-flute-solo.pdf	3月14日
betty lou guitar tabs	导航	74	视频, 相关搜索	0	0	50	1	https://www.capotastomusic.com/guitar_pages/resources/easy_guitar_tab/skip-to-my-lou-easy-guitar-tab.pdf	2月14日
greensleeves violin sheet music	信息	14	图片, 图片包, 视频, 视频轮播, 相关搜索	0	0	110	1	https://www.capotastomusic.com/violin-sheet-music/violin-piano/greensleeves-violin-piano.pdf	3月21日
she'll be coming round the mountain chords	信息	61	视频, 相关搜索	0	0	140	1	https://www.capotastomusic.com/guitar_pages/resources/guitar_tablature/she'll-be-coming-round-the-mountain-gtm.pdf	3月20日
she'll be coming round the mountain chords	信息	73	视频, 相关搜索	0	0	140	1	https://www.capotastomusic.com/guitar_pages/resources/guitar_tablature/she'll-be-coming-round-the-mountain-gtm.pdf	3月20日
yankee doodle went to town sheet music	信息	46	图片包, 视频, 视频轮播, 相关搜索	0	0	40	1	https://www.capotastomusic.com/piano-sheet-music/beginners/yankee-doodle-beginner-piano.pdf	2月22日
we wish you a merry christmas sheet music flute	信息	16	AI 概览, 图片, 图片包, 视频, 视频轮播, 相关搜索	0	0	70	1	https://www.capotastomusic.com/flute-sheet-music/christmas/we-wish-you-a-merry-christmas-flute.pdf	3月19日
easiest song to play on violin	信息	35	站点子链, AI 概览, 图片, 视频, 视频轮播, 讨论和论坛, 相关搜索	0	0	70	1	https://www.capotastomusic.com/violin-sheet-music/easy.htm	3月08日
christmas trumpet music sheets free	信息	2	站点子链, AI 概览, 图片, 图片包, 视频, 讨论和论坛, 相关搜索	3	0.08	40	1	https://www.capotastomusic.com/trumpet-sheet-music/christmas.htm	3月05日
we wish you a merry christmas for flute	信息, 交易	39	图片包, 视频, 视频轮播, 相关搜索	0	0	70	1	https://www.capotastomusic.com/flute-sheet-music/christmas/we-wish-you-a-merry-christmas-flute.pdf	3月09日
oh holy night sheet music flute	信息	30	图片, 图片包, 视频, 视频轮播, 相关搜索	0	0	30	1	https://www.capotastomusic.com/flute-sheet-music/christmas/o-holy-night-flute.pdf	3月07日
fiddle sheet music for beginners	商务	30	站点子链, 图片, 图片包, 视频, 视频轮播, 相关搜索, 热门产品	0	0	70	1	https://www.capotastomusic.com/violin-sheet-music/easy.htm	3月18日
when the saints go marching in lead sheet	信息	46	图片包, 视频, 视频轮播, 相关搜索	0	0	70	1	https://www.capotastomusic.com/trumpet-sheet-music/easy/when-the-saints-go-marching-in-trumpet.pdf	3月09日
o holy night sheet music pdf	信息	40	图片, 图片包, 视频, 相关搜索	0	0	140	1	https://www.capotastomusic.com/piano-sheet-music/christmas/o-holy-night-easy-piano.pdf	3月24日
oh holy night trumpet sheet music	商务, 信息	2	站点子链, 图片包, 视频, 视频轮播, 相关搜索, 热门产品	3	0.08	40	1	https://www.capotastomusic.com/trumpet-sheet-music/christmas/o-holy-night-easy-trumpet.pdf	3月19日
we wish you a merry christmas alto sax	信息	24	站点子链, 图片包, 视频, 视频轮播, 相关搜索	0	0	40	1	https://www.capotastomusic.com/alto-saxophone-sheet-music/christmas/we-wish-you-a-merry-christmas-alto-sax-sheet-music.pdf	3月09日
we wish you a merry christmas alto sax	信息	26	站点子链, 图片包, 视频, 视频轮播, 相关搜索	0	0	40	1	https://www.capotastomusic.com/alto-saxophone-sheet-music/christmas/we-wish-you-a-merry-christmas-alto-sax-sheet-music.pdf	3月09日
national anthem sheet music for alto sax	信息	21	图片, 图片包, 视频, 视频轮播, 相关搜索	0	0	40	1	https://www.capotastomusic.com/alto-saxophone-sheet-music/easy/the-star-spangled-banner-alto-saxophone.pdf	3月19日
tenor sax star spangled banner	信息, 交易	6	图片包, 视频, 视频轮播, 相关搜索	1	0.02	90	1	https://www.capotastomusic.com/tenor-saxophone-sheet-music/easy/the-star-spangled-banner-tenor-sax.pdf	1 天
tenor sax star spangled banner	信息, 交易	32	图片包, 视频, 视频轮播, 相关搜索	0	0	90	1	https://www.capotastomusic.com/tenor-saxophone-sheet-music/easy/the-star-spangled-banner.pdf	1 天
holy night sheet music piano	信息	33	图片, 图片包, 视频, 视频轮播, 相关搜索	0	0	40	1	https://www.capotastomusic.com/piano-sheet-music/christmas/o-holy-night-easy-piano.pdf	2月03日
o holy night sheet music cello	信息	11	图片, 图片包, 视频, 视频轮播, 相关搜索, 热门产品	0	0	40	1	https://www.capotastomusic.com/cello-sheet-music/christmas/o-holy-night-cello.pdf	3月07日
o little town of bethlehem tabs	信息	28	视频, 视频轮播, 相关搜索	0	0	50	1	https://www.capotastomusic.com/guitar_pages/resources/christmas_guitar_tab/o_little_town_of_bethlehem_tab.pdf	3月19日
greensleeves for violin sheet music	信息	8	图片包, 视频, 视频轮播, 相关搜索	0	0	90	1	https://www.capotastomusic.com/violin-sheet-music/violin-piano/greensleeves-violin-piano.pdf	2月01日
greensleeves for violin sheet music	信息	9	图片包, 视频, 视频轮播, 相关搜索	0	0	90	1	https://www.capotastomusic.com/violin-sheet-music/violin-piano/greensleeves-violin-piano.pdf	2月01日
greensleeves for violin sheet music	信息	64	图片包, 视频, 视频轮播, 相关搜索	0	0	90	1	https://www.capotastomusic.com/violin-sheet-music/easy/greensleeves-violin.pdf	2月01日
jingle bells recorder music sheet	信息	32	站点子链, 图片, 图片包, 视频, 视频轮播, 相关搜索	0	0	50	1	https://www.capotastomusic.com/soprano-recorder-sheet-music/christmas/jingle-bells-soprano-recorder.pdf	3月17日
jingle bells recorder music sheet	信息	45	站点子链, 图片, 图片包, 视频, 视频轮播, 相关搜索	0	0	50	1	https://www.capotastomusic.com/soprano-recorder-sheet-music/christmas/jingle-bells-soprano-recorder.pdf	3月17日
sheet music auld lang syne free	信息	32	图片包, 视频, 相关搜索	0	0	40	1	https://www.capotastomusic.com/piano-sheet-music/beginners/auld-lang-syne.pdf	2月26日
god rest ye merry gentlemen flute sheet music	信息	10	图片包, 视频, 视频轮播, 相关搜索	0	0	70	1	https://www.capotastomusic.com/flute-sheet-music/christmas/god-rest-ye-merry-gentlemen-flute.pdf	2月12日
red river valley harmonica tab	信息, 交易	48	视频, 视频轮播, 相关搜索	0	0	90	1	https://www.capotastomusic.com/ukulele-sheet-music/tabs/red-river-valley-ukulele-tabs.pdf	3月06日
christmas guitar sheet music	商务, 信息	17	图片, 图片包, 视频, 讨论和论坛, 相关搜索, 热门产品	0	0	40	1	https://www.capotastomusic.com/guitar_pages/christmas_guitar_tab.htm	3月01日
trumpet pdf	信息	36	视频, 相关搜索	0	0	70	1	https://www.capotastomusic.com/trumpet-sheet-music/easy/the-star-spangled-banner-trumpet.pdf	2月07日
trumpet pdf	信息	64	视频, 相关搜索	0	0	70	1	https://www.capotastomusic.com/trumpet-sheet-music/easy.htm	2月07日
whiskey in a jar sheet music	信息	53	图片, 图片包, 视频, 相关搜索	0	0	50	1	https://www.capotastomusic.com/clarinet-sheet-music/easy/whiskey-in-the-jar-clarinet.pdf	3月09日
whiskey in a jar sheet music	信息	65	图片, 图片包, 视频, 相关搜索	0	0	50	1	https://www.capotastomusic.com/clarinet-sheet-music/easy/whiskey-in-the-jar-clarinet.pdf	3月09日
cielito lindo sheet music violin	信息, 交易	75	站点子链, 图片包, 视频, 视频轮播, 相关搜索	0	0	50	1	https://www.capotastomusic.com/cello-sheet-music/easy/cielito-lindo-cello.pdf	2月09日
angels we have heard on high clarinet	信息, 交易	19	图片包, 视频, 视频轮播, 相关搜索	0	0	40	1	https://www.capotastomusic.com/clarinet-sheet-music/christmas/angels-we-have-heard-on-high-easy-clarinet.pdf	3月12日
cello amazing grace sheet music	信息	12	图片包, 视频, 视频轮播, 相关搜索	0	0	70	1	https://www.capotastomusic.com/cello-sheet-music/easy/amazing-grace-easy-cello-solo.pdf	3月18日
star spangled banner bass clarinet	信息, 交易	44	图片包, 视频, 视频轮播, 相关搜索, 短视频	0	0	50	1	https://www.capotastomusic.com/clarinet-sheet-music/easy/the-star-spangled-banner-clarinet.pdf	3 天
star spangled banner bass clarinet	信息, 交易	58	图片包, 视频, 视频轮播, 相关搜索, 短视频	0	0	50	1	https://www.capotastomusic.com/clarinet-sheet-music/easy/the-star-spangled-banner-clarinet.pdf	3 天
silent night music for flute	信息	56	图片, 图片包, 视频, 视频轮播, 相关搜索, 短视频	0	0	40	1	https://www.capotastomusic.com/flute-sheet-music/christmas/silent-night-flute.pdf	1月30日
joy to the world sheet music for clarinet	商务	26	站点子链, 视频, 视频轮播, 相关搜索, 热门产品	0	0	40	1	https://www.capotastomusic.com/clarinet-sheet-music/christmas/joy-to-the-world-easy-clarinet.pdf	3月07日
joy to the world sheet music for clarinet	商务	57	站点子链, 视频, 视频轮播, 相关搜索, 热门产品	0	0	40	1	https://www.capotastomusic.com/trumpet-sheet-music/christmas/joy-to-the-world-trumpet.pdf	3月07日
sheet music for trombone free printable	信息	6	图片, 图片包, 视频, 讨论和论坛, 相关搜索	3	0.08	110	1	https://www.capotastomusic.com/trombone-sheet-music/easy.htm	1月27日
sheet music for trombone free printable	信息	38	图片, 图片包, 视频, 讨论和论坛, 相关搜索	0	0	110	1	https://www.capotastomusic.com/trombone-sheet-music.htm	1月27日
fun songs to play on trombone	信息	53	站点子链, AI 概览, 视频, 视频轮播, 相关问题, 讨论和论坛, 相关搜索	0	0	50	1	https://www.capotastomusic.com/trombone-sheet-music/easy.htm	2月19日
free clarinet christmas sheet music	信息	6	图片, 图片包, 视频, 相关搜索	1	0.02	40	1	https://www.capotastomusic.com/clarinet-sheet-music/christmas.htm	3月10日
free clarinet christmas sheet music	信息	30	图片, 图片包, 视频, 相关搜索	0	0	40	1	https://www.capotastomusic.com/clarinet-sheet-music/christmas.htm	3月10日
free clarinet christmas sheet music	信息	38	图片, 图片包, 视频, 相关搜索	0	0	40	1	https://www.capotastomusic.com/clarinet-sheet-music/christmas/we-wish-you-a-merry-christmas-easy-clarinet.pdf	3月10日
what child is this piano sheet music	信息	52	图片包, 视频, 相关搜索	0	0	210	1	https://www.capotastomusic.com/piano-sheet-music/christmas/what-child-is-this-easy-piano.pdf	2月01日
silent night clarinet sheet music easy	信息, 交易	4	图片包, 视频, 视频轮播, 相关搜索	0	0	40	1	https://www.capotastomusic.com/clarinet-sheet-music/christmas/silent-night-easy-clarinet.pdf	3月20日
sheet music for recorder christmas	商务	8	站点子链, AI 概览, 图片, 视频, 视频轮播, 相关搜索, 热门产品	0	0	40	1	https://www.capotastomusic.com/soprano-recorder-sheet-music/christmas.htm	3月11日
sheet music for recorder christmas	商务	18	站点子链, AI 概览, 图片, 视频, 视频轮播, 相关搜索, 热门产品	0	0	40	1	https://www.capotastomusic.com/soprano-recorder-sheet-music/christmas.htm	3月11日
sheet music for recorder christmas	商务	86	站点子链, AI 概览, 图片, 视频, 视频轮播, 相关搜索, 热门产品	0	0	40	1	https://www.capotastomusic.com/soprano-recorder-sheet-music/christmas/the-twelve-days-of-christmas-soprano-recorder.pdf	3月11日
god rest ye merry gentlemen clarinet sheet music	信息	18	图片包, 视频, 相关搜索	0	0	40	1	https://www.capotastomusic.com/clarinet-sheet-music/christmas/god-rest-ye-merry-gentlemen-easy-clarinet.pdf	3月16日
god rest ye merry gentlemen clarinet sheet music	信息	60	图片包, 视频, 相关搜索	0	0	40	1	https://www.capotastomusic.com/trumpet-sheet-music/christmas/god-rest-ye-merry-gentlemen-easy-trumpet.pdf	3月16日
beginner piano sheet music jingle bells	信息	2	站点子链, 图片, 图片包, 视频, 视频轮播, 相关搜索	5	0.14	70	1	https://www.capotastomusic.com/piano-sheet-music/christmas/jingle-bells-beginner-piano.pdf	1月31日
jingle bells violin sheet music for beginners	信息	27	站点子链, 图片包, 视频, 视频轮播, 相关搜索	0	0	40	1	https://www.capotastomusic.com/violin-sheet-music/christmas/jingle-bells-violin.pdf	3月18日
jingle bells violin sheet music for beginners	信息	38	站点子链, 图片包, 视频, 视频轮播, 相关搜索	0	0	40	1	https://www.capotastomusic.com/violin-sheet-music/christmas/jingle-bells-violin.pdf	3月18日
auld lang syne uke chords	信息	13	视频, 视频轮播, 相关搜索	0	0	110	1	https://www.capotastomusic.com/ukulele-sheet-music/tabs/auld-lang-syne-ukulele-tab.pdf	3月21日
auld lang syne uke chords	信息	37	视频, 视频轮播, 相关搜索	0	0	110	1	https://www.capotastomusic.com/ukulele-sheet-music/songs/auld-lang-syne-ukulele-song.pdf	3月21日
auld lang syne uke chords	信息	40	视频, 视频轮播, 相关搜索	0	0	110	1	https://www.capotastomusic.com/ukulele-sheet-music/songs/auld-lang-syne-ukulele-song.pdf	3月21日
greensleeves sheet music violin	信息	13	图片, 图片包, 视频, 视频轮播, 相关搜索	0	0	50	1	https://www.capotastomusic.com/violin-sheet-music/violin-piano/greensleeves-violin-piano.pdf	3月22日
greensleeves sheet music violin	信息	38	图片, 图片包, 视频, 视频轮播, 相关搜索	0	0	50	1	https://www.capotastomusic.com/violin-sheet-music/easy/greensleeves-violin.pdf	3月22日
amazing grace pdf	信息	65	图片, 图片包, 视频, 相关搜索	0	0	210	1	https://www.capotastomusic.com/piano-sheet-music/beginners/amazing-grace.pdf	2月23日
amazing grace pdf	信息	83	图片, 图片包, 视频, 相关搜索	0	0	210	1	https://www.capotastomusic.com/piano-sheet-music/beginners/amazing-grace.pdf	2月23日
o christmas tree sheet music for violin	信息	21	站点子链, AI 概览, 图片, 视频, 视频轮播, 相关搜索, 热门产品	0	0	40	1	https://www.capotastomusic.com/violin-sheet-music/christmas/o-christmas-tree-violin.pdf	3月19日
o christmas tree sheet music for violin	信息	50	站点子链, AI 概览, 图片, 视频, 视频轮播, 相关搜索, 热门产品	0	0	40	1	https://www.capotastomusic.com/violin-sheet-music/christmas.htm	3月19日"""

def slugify(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"\s+", "-", text)
    return text

def extract_instrument_and_song(keyword):
    # Try to find instrument in keyword
    found_instr = None
    for token, folder in INSTRUMENT_MAPPING.items():
        if f" {token} " in f" {keyword} " or keyword.startswith(f"{token} ") or keyword.endswith(f" {token}"):
            found_instr = folder
            break
            
    # Clean up song name from keyword
    song = keyword
    # Remove markers
    for marker in ['sheet music', 'music sheet', 'score', 'pdf', 'free', 'beginner', 'easy', 'solos', 'for beginners', 'tab', 'chords', 'notes', 'on recorder']:
        song = song.replace(marker, "")
    # Remove instrument
    if found_instr:
        for token in INSTRUMENT_MAPPING.keys():
            song = song.replace(token, "")
            
    song = song.strip()
    return found_instr, song

def main():
    gepu_path = Path("/Users/bizcheers/jan-20-haolingsheng/haolingsheng/gepu")
    
    # 1. Index existing files
    existing_pages = {} # (instrument, song_slug) -> path
    for html_file in gepu_path.rglob("*.html"):
        if html_file.name in ['index.html', 'page-1.html', 'page-2.html', 'page-3.html', 'page-4.html', 'page-5.html', 'page-6.html', 'page-7.html', 'page-8.html', 'page-9.html', 'page-10.html']:
            continue
        rel = html_file.relative_to(gepu_path)
        parts = rel.parts
        if len(parts) == 2:
            instrument = parts[0]
            song_slug = parts[1].replace(".html", "")
            existing_pages[(instrument, song_slug)] = str(rel)
            
    # 2. Process Keywords
    new_opportunities = []
    already_exists = []
    copyright_blocked = []
    
    seen_opps = set()
    
    for line in RAW_KEYWORDS.splitlines():
        if not line.strip(): continue
        parts = line.split("\t")
        keyword = parts[0].strip().lower()
        
        instr, song = extract_instrument_and_song(keyword)
        if not instr or not song:
            continue
            
        song_slug = slugify(song)
        
        # Check copyright
        is_copyright = False
        for restricted in COPYRIGHT_RESTRICTED:
            if restricted in song.lower():
                is_copyright = True
                break
        
        if is_copyright:
            copyright_blocked.append(f"{song} ({instr})")
            continue
            
        # Check existence
        if (instr, song_slug) in existing_pages:
            already_exists.append(f"{song} ({instr}) -> {existing_pages[(instr, song_slug)]}")
        else:
            opp = (song, instr)
            if opp not in seen_opps:
                new_opportunities.append(opp)
                seen_opps.add(opp)
                
    # 3. Output
    print("# ANALYSIS RESULTS")
    print("\n## ✅ New Content Opportunities (Not on Site)")
    for song, instr in sorted(new_opportunities):
        print(f"- {song.title()} ({instr})")
        
    print("\n## 🚫 Already Exists (Skipped)")
    for item in sorted(list(set(already_exists))):
        print(f"- {item}")
        
    print("\n## ⚠️ Copyright Caution (Skipped)")
    for item in sorted(list(set(copyright_blocked))):
        print(f"- {item}")

if __name__ == "__main__":
    main()
