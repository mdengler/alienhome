#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

Look up the cantonese phrases / characters for an english word using
the excellent CantoDict at http://www.cantonese.sheik.co.uk/dictionary

Usage examples:

%prog horse
馬 - U+99ac: maa5 / [1] [n] horse [2] a Chinese family name [3] Kangxi radical 187

%prog --all horse

csv output implies --all:
%prog --csv horse
zh_HK,jyutping,english,sound_link,incontextzh_HK,incontextenglish,incontextsound_link,pinyin,codepoint,level,link,radical,stroke_count
鑣,biu1,[1] [n] bit for a horse; bridle [2] said of a horse [3] a dart-like projectile thrown by hand as a weapon,,,,,biao1,U+9463,Level: 3,http://www.cantonese.sheik.co.uk/dictionary/characters/3544/?full=true,Radical:  (#167),Stroke count: 23
驥,kei3 gei3,[1] very fast horse [2] a man of outstanding ability; a great man,,,,,ji4,U+9a65,Level: 3,http://www.cantonese.sheik.co.uk/dictionary/characters/8189/?full=true,Radical:  (#187),Stroke count: 27
驊,waa4,the name of an legendary excellent horse,,,,,hua2,U+9A4A,Level: 3,http://www.cantonese.sheik.co.uk/dictionary/characters/8188/?full=true,Radical:  (#187),Stroke count: 22
馬,maa5,[1] [n] horse [2] a Chinese family name [3] Kangxi radical 187(Classifier(s): 匹,,你就手下留情放佢哋一馬啦。,Show some mercy and let them go.,http://www.cantonese.sheik.co.uk/audio/example722.mp3,ma3,U+99ac,Level: 1,http://www.cantonese.sheik.co.uk/dictionary/characters/157/?full=true,Radical:  (#187),Stroke count: 10
騮,lau4,a legedary fine horse,,,,,liu2,U+9A2E,Level: 3,http://www.cantonese.sheik.co.uk/dictionary/characters/3667/?full=true,Radical:  (#187),Stroke count: 20
駱,lok3,[1] white horse with black mane [2] camel [3] a Chinese family name,,,,,luo4,U+99f1,Level: 2,http://www.cantonese.sheik.co.uk/dictionary/characters/3665/?full=true,Radical:  (#187),Stroke count: 16

"""


import os
import sys

from optparse import OptionParser
from urllib import urlopen
#from xml.etree.ElementTree import parse
from lxml.html import parse

DICT_URL = "http://www.cantonese.sheik.co.uk/dictionary/search/?searchtype=4&text=%s"

tones = {
    1: "high level flat (or falling) - eg: faa1,bing1",
    2: "rising to high level - eg: tou2, hoi2",
    3: "mid level flat - eg: sai3, hei3",
    4: "low level falling - eg: naam4, wu4",
    5: "rising to mid level - eg: ngo5, jyu5",
    6: "low level flat - eg: hai6,din6",
    }


def tones_extract(td, texts_selector, tone_selector="span.tone"):
    texts_raw = td.cssselect(texts_selector)
    texts = []
    for t in texts_raw:
        text = t.text
        if text is not None:
            text = text.strip()
            if text != "":
                texts.append(text)
                texts.extend([t.tail.strip() for t in texts_raw[0]
                              if t.tail is not None and t.tail.strip() != ""])
    tones = [tone.text.strip() for tone in td.cssselect(tone_selector)]
    return zip(texts, tones)


def extract(tr):
    """
    given tr, a tr HtmlElement from DICT_URL, returns its chinese
    (trad) character and a dict of information about it

expects the tr to be the tr like so:

<tr>
<td><a href="http://www.cantonese.sheik.co.uk/dictionary/words/48292/"><img src="http://www.cantonese.sheik.co.uk/images/icons/book.gif" border="0" align="absmiddle" hspace="2" vspace="3" alt="desc">
</a></td>
<td><span class="chinesemed">人見人愛</span></td>
<td valign="top"><span class="listjyutping">jan<span class="tone">4</span> gin<span class="tone">3</span> jan<span class="tone">4</span> oi<span class="tone">3</span></span></td>
<td valign="top"><span class="listpinyin">ren<span class="tone">2</span> jian<span class="tone">4</span> ren<span class="tone">2</span> ai<span class="tone">4</span></span></td>
<td> &nbsp; everyone will love; lovable; likable</td>
</tr>
    """

    if len(tr) != 5:
        print "warning: tr %s with text %s was odd" % (tr, tr.text_content())
        return {}, tr

    link_el, char_el, jp_el, py_el, eng_el = tr

    link = link_el[0].attrib["href"]

    zh_HK = char_el[0].text

    en = eng_el.text.strip().strip(u"\xa0") if eng_el.text is not None else "none?!" # usually for mandarin-only stuff

    jp = tones_extract(jp_el, "span.listjyutping")

    py = tones_extract(py_el, "span.listpingying")

    return zh_HK, {"utf-8": zh_HK,
                   "jyutping": jp,
                   "pinying": py,
                   "english": en,
                   "link": link,
                   }


def cantodict_scrape(link):
    """scrapes cantodict char dict page for details"""

    if not link.endswith("?full=true"):
        link += "?full=true"
    data = urlopen(link)
    html = parse(data).getroot()

    html.make_links_absolute()

    details = {"link": link}

    simple_scrapes = {
        "english": ("td.wordmeaning", "text_content()"),
        "typedesc": ("span.typedesc", "text"),
        "zh_HK": ("td.chinesebigger", "text_content()"),
        "stroke_count": ("div.charstrokecount", "text"),
        "radical": ("div.charradical", "text_content()"),
        "level": ("div.charlevel", "text"),
#        "": ("", "text"),
        }

    for key, (selector, attr) in simple_scrapes.iteritems():
        selection = html.cssselect(selector)
        for el in selection:
            if key not in details:
                details[key] = ""
            details[key] = details[key] + eval("el." + attr).strip()

    #english one is not so simple
    if "english" in details and "Stroke count" in details["english"]:
        english = details["english"]
        interesting_part = ""
        for line in english.split("\n"):
            sc_idx = line.find("Stroke count:")
            interesting_part += line[:sc_idx].strip() + " "
            if sc_idx >= 0:
                break
        details["english"] = interesting_part

    for key in ("jyutping", "pinyin"):
        details[key] = ""
        els = html.cssselect("span.card%s" % key)
        for el in els:
            details[key] += el.text_content().strip()

    details["examples"] = []
    for example_el in html.cssselect("div.example_in_block"):
        if len(example_el) != 6:
            continue
        link_el, sound_el, span_wordexample, ignored, ignored2, meaning_el \
            = example_el
        example = {}
        if "href" in link_el.attrib:
            example["link"] = link_el.attrib["href"]
        if "href" in sound_el.attrib:
            example["sound_link"] = sound_el.attrib["href"]
        example["zh_HK"] = span_wordexample.text_content().strip()
        example["english"] = meaning_el.text_content().strip()
        details["examples"].append(example)

    wdcl = html.cssselect("div.wd_code_links")[0]
    details["codepoint"] = wdcl[-1].text

    return details, link, html


def lookup(word, full=False):
    """uses %s to lookup word""" % DICT_URL
    data = urlopen(DICT_URL % word)
    html = parse(data).getroot()
    chars = html.cssselect("span.chinesemed")

    tables = {}
    for c in chars:
        table = c.getparent().getparent().getparent()
        if table not in tables:
            tables[table] = []
        tables[table].append(c)

    char_table = chars[0].getparent().getparent().getparent()

    extracted_chars = [extract(c.getparent().getparent())
                       for c in tables[char_table]]

    if full:
        for other_table in tables:
            if other_table != char_table:
                extracted_chars.extend([extract(c.getparent().getparent())
                                        for c in tables[other_table]])

    char_details = {}
    for zh_HK, info in extracted_chars:
        link = info.get("link")
        if link is not None:
            char_details[zh_HK] = cantodict_scrape(link)

    return extracted_chars, char_details


def output(word, fd=None, all=False, csv=False):
    if fd is None:
        fd = sys.stdout

    if csv:
        all = True

    extracted_chars, char_details = lookup(word)

    keys = set()
    for zh_HK, (details, link, html) in char_details.iteritems():
        keys.update(details.keys())

    for uninteresting in ("typedesc",):
        if uninteresting in keys:
            keys.discard(uninteresting)

    #handle "examples" key specially
    if "examples" in keys:
        for zh_HK, (details, link, html) in char_details.iteritems():
            examples = details["examples"]
            interesting_keys = ["zh_HK", "english"]
            for example in examples:
                if "sound_link" in example:
                    for k in ["sound_link"] + interesting_keys:
                        details["incontext" + k] = example[k]
                        keys.add("incontext" + k)
                    break
                else:
                    for k in interesting_keys:
                        details["incontext" + k] = example[k]
                        keys.add("incontext" + k)
            del details["examples"]
        keys.discard("examples")

    ordered_keys = [
        "zh_HK",
        "jyutping",
        "english",
        "sound_link",
        "incontextzh_HK",
        "incontextenglish",
        "incontextsound_link",
        "pinyin",
        "codepoint",
        ]

    ordered_keys.extend(sorted(keys.difference(ordered_keys)))

    if csv:
        fd.write(",".join(ordered_keys))
        fd.write(os.linesep)

    if not all:
        extracted_chars = extracted_chars[:1]

    for zh_HK, info in extracted_chars:
        details, link, html = char_details[zh_HK]
        if csv:
            fd.write(",".join([details.get(k, "").strip() for k in ordered_keys]))
        else:
            fd.write("%s - %s: %s / %s" % (zh_HK,
                                           details.get("codepoint", ""),
                                           details.get("jyutping", ""),
                                           details.get("english", "")))
        fd.write(os.linesep)


if __name__ == "__main__":
    # fix for the below fix
    if "LANG" not in os.environ:
        os.environ["LANG"] = "en_GB.utf8"
    # from http://wjd.nu/notes/2009#unicodeencodeerror-python-redirect-pipe
    import codecs, locale
    sys.stdout = codecs.getwriter(locale.getdefaultlocale()[1])(sys.stdout, 'replace')

    parser = OptionParser()
    parser.add_option("--all", action="store_true",
                      help="more than one possible match")
    parser.add_option("--full", action="store_true",
                      help="see --all")
    parser.add_option("--csv", action="store_true",
                      help="results in CSV format, including header; implies --all")
    parser.set_usage(__doc__)

    options, args = parser.parse_args()

    if args == ["-"]:
        args = [line.strip() for line in sys.stdin.readlines()]
    for word in args:
        output(word,
               fd=sys.stdout,
               all=options.full or options.all,
               csv=options.csv)
