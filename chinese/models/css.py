# Copyright 2012-2014 Thomas Tempe <thomas.tempe@alysse.org>
# Copyright 2012 Roland Sieker <ospalh@gmail.com>
# Copyright 2025 Nicolas Corrieri <corrieripro@gmail.com>


"""
CSS used by the different Chinese models.
"""

style = u'''\
.card { word-wrap: break-word; }
.win .chinese { font-family: "MS Mincho", "ＭＳ 明朝"; }
.mac .chinese { }
.linux .chinese { font-family: "Kochi Mincho", "東風明朝"; }
.mobile .chinese { font-family: "Hiragino Mincho ProN"; }
.chinese { font-size: 30px; padding-bottom: 5pt;}
.english { padding-bottom: 10pt; }
.reading { font-size: 16px;}
.comment {font-size: 15px; color:grey;}
.tags {color:gray;text-align:right;font-size:10pt;}
.note {color:gray;font-size:12pt;margin-top:20pt;}
.hint {font-size:12pt;}
.answer { background-color:#efefef;border:dotted;border-width:1px; padding:10pt;}
.stroke { margin:20pt 0; height:100px }
.tone1 {color: #c82829;}
.tone2 {color: #eab700;}
.tone3 {color: #718c00;}
.tone4 {color: #4271ae;}
.tone5 {color: #8e908c;}

.nightMode .answer {background-color: #1d1f21;}
.nightMode .tone1 {color: #cc6666;}
.nightMode .tone2 {color: #f0c674;}
.nightMode .tone3 {color: #b5bd68;}
.nightMode .tone4 {color: #81a2be;}
.nightMode .tone5 {color: #969896;}
'''
