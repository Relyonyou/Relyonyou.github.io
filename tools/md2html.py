# -*- coding: utf-8 -*-
"""极简 Markdown 渲染器：只覆盖本站文章用到的语法，无第三方依赖。

支持：标题 / 段落（行尾两空格硬换行）/ 围栏代码块 / 有序与无序列表 /
引用 / 分隔线 / 图片 / 链接 / 粗体 / 斜体 / 行内代码。
"""
import re
from html import escape


def _inline(text):
    """行内元素。先占位再转义，避免二次处理。"""
    slots = []

    def hold(html):
        slots.append(html)
        return f'\x00{len(slots)-1}\x00'

    text = re.sub(r'`([^`]+)`', lambda m: hold('<code>' + escape(m.group(1)) + '</code>'), text)
    text = re.sub(r'!\[([^\]]*)\]\(([^)\s]+)\)',
                  lambda m: hold(f'<img src="{escape(m.group(2))}" alt="{escape(m.group(1))}" loading="lazy">'), text)
    text = re.sub(r'\[([^\]]+)\]\(([^)\s]+)\)',
                  lambda m: hold(f'<a href="{escape(m.group(2))}">{escape(m.group(1))}</a>'), text)

    text = escape(text)
    text = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'(?<![*\w])\*([^*\n]+)\*(?!\*)', r'<em>\1</em>', text)

    # 还原占位符
    for i, html in enumerate(slots):
        text = text.replace(f'\x00{i}\x00', html)
    return text


def render(md):
    lines = md.replace('\r\n', '\n').split('\n')
    out, i = [], 0
    while i < len(lines):
        line = lines[i]

        # 围栏代码块
        if line.startswith('```'):
            lang = line[3:].strip()
            i += 1
            buf = []
            while i < len(lines) and not lines[i].startswith('```'):
                buf.append(lines[i])
                i += 1
            i += 1
            cls = f' class="language-{escape(lang)}"' if lang else ''
            out.append(f'<pre><code{cls}>' + escape('\n'.join(buf)) + '</code></pre>')
            continue

        # 标题
        m = re.match(r'^(#{1,6})\s+(.*)$', line)
        if m:
            level = len(m.group(1))
            out.append(f'<h{level}>{_inline(m.group(2).strip())}</h{level}>')
            i += 1
            continue

        # 分隔线
        if re.match(r'^-{3,}\s*$', line):
            out.append('<hr>')
            i += 1
            continue

        # 引用
        if line.startswith('>'):
            buf = []
            while i < len(lines) and lines[i].startswith('>'):
                buf.append(re.sub(r'^>\s?', '', lines[i]))
                i += 1
            body = render('\n'.join(buf))
            out.append('<blockquote>' + body + '</blockquote>')
            continue

        # 列表
        if re.match(r'^\s*([-*]|\d+\.)\s+', line):
            ordered = bool(re.match(r'^\s*\d+\.\s+', line))
            tag = 'ol' if ordered else 'ul'
            items = []
            while i < len(lines):
                m2 = re.match(r'^\s*([-*]|\d+\.)\s+(.*)$', lines[i])
                if m2:
                    items.append(m2.group(2))
                    i += 1
                elif (items and lines[i].strip()
                      and not re.match(r'^(#{1,6}\s|```|>|-{3,}\s*$)', lines[i])
                      and not re.match(r'^\s*([-*]|\d+\.)\s+', lines[i])):
                    # 懒续行：列表项之间夹着普通说明行，并入上一项，避免编号重置
                    items[-1] += '  \n' + lines[i].strip()
                    i += 1
                else:
                    break
            body = ''.join(
                '<li>' + '<br>'.join(_inline(x.strip()) for x in t.split('  \n')) + '</li>'
                for t in items)
            out.append(f'<{tag}>{body}</{tag}>')
            continue

        # 空行
        if not line.strip():
            i += 1
            continue

        # 段落：累积到空行，行尾两空格 = 硬换行
        buf = []
        while i < len(lines) and lines[i].strip() and not re.match(
                r'^(#{1,6}\s|```|>|\s*([-*]|\d+\.)\s+|-{3,}\s*$)', lines[i]):
            buf.append(lines[i])
            i += 1
        html, parts = [], []
        for t in buf:
            hard = t.endswith('  ')
            parts.append(_inline(t.strip()) + ('<br>' if hard else ''))
        html = '<p>' + '\n'.join(parts).replace('<br>\n', '<br>') + '</p>'
        out.append(html)

    return '\n'.join(out)
