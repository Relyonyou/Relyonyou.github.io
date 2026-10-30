# -*- coding: utf-8 -*-
"""把四篇旧文章的内容转换成 Markdown 源文件。

输入：post/blog/*.html（当前线上版本）
输出：post/blog/src/*.md
"""
import base64
import os
import re
from lxml import html as LH

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

IMG_DIR = os.path.join(REPO, 'post/blog/img')
_url_counter = {'n': 0}


def save_data_url(src, slug):
    """把 base64 内联图片落盘，返回站内路径。"""
    m = re.match(r'data:image/(\w+);base64,(.+)', src, re.S)
    if not m:
        return src
    ext = 'jpg' if m.group(1) in ('jpeg', 'jpg') else m.group(1)
    _url_counter['n'] += 1
    name = f'{slug}-{_url_counter["n"]}.{ext}'
    os.makedirs(IMG_DIR, exist_ok=True)
    with open(os.path.join(IMG_DIR, name), 'wb') as f:
        f.write(base64.b64decode(m.group(2)))
    return f'/post/blog/img/{name}'



# ---------------------------------------------------------------- 行内元素
CURRENT_SLUG = ['article']


def inline(node):
    """把行内内容转成 Markdown 文本。"""
    out = [node.text or '']
    for c in node:
        tag = c.tag if isinstance(c.tag, str) else ''
        if tag in ('strong', 'b'):
            out.append('**' + inline(c).strip() + '**')
        elif tag in ('em', 'i'):
            out.append('*' + inline(c).strip() + '*')
        elif tag == 'code':
            out.append('`' + (c.text_content() or '').strip() + '`')
        elif tag == 'a':
            href = (c.get('href') or '').strip()
            text = inline(c).strip()
            out.append(f'[{text}]({href})' if text else '')
        elif tag == 'img':
            src = save_data_url((c.get('src') or '').strip(), CURRENT_SLUG[0])
            alt = (c.get('alt') or '').strip()
            out.append(f'![{alt}]({src})')
        elif tag == 'br':
            out.append('\n')
        else:
            out.append(inline(c))
        out.append(c.tail or '')
    return ''.join(out)


def tidy(text):
    """合并空白，但保留换行。"""
    text = text.replace('\u00a0', ' ')
    lines = [re.sub(r'[ \t]+', ' ', ln).strip() for ln in text.split('\n')]
    return '\n'.join(lines).strip()


# ---------------------------------------------------------------- 块级元素
def block(node, out):
    tag = node.tag if isinstance(node.tag, str) else ''

    if tag in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
        level = 2 if int(tag[1]) <= 2 else 3
        txt = tidy(inline(node))
        if txt:
            out.append('#' * level + ' ' + txt.replace('\n', ' '))
        out.append('')

    elif tag == 'p':
        txt = tidy(inline(node))
        if not txt:
            return
        # 段落内部的换行：拆成多个段落，避免 Markdown 软换行被吞掉
        chunks = [c.strip() for c in txt.split('\n') if c.strip()]
        out.append('  \n'.join(chunks))
        out.append('')

    elif tag in ('ul', 'ol'):
        ordered = tag == 'ol'
        for i, li in enumerate(node.xpath('./li'), 1):
            txt = tidy(inline(li))
            if not txt:
                continue
            prefix = f'{i}. ' if ordered else '- '
            lines = txt.split('\n')
            out.append(prefix + lines[0])
            out.extend('   ' + ln for ln in lines[1:] if ln)
        out.append('')

    elif tag == 'pre':
        # CodeMirror 代码块：按行取，避开行号与隐藏测量元素
        line_nodes = node.xpath('.//pre[contains(@class,"CodeMirror-line")]')
        if line_nodes:
            code = '\n'.join(ln.text_content() for ln in line_nodes)
        else:
            code = node.text_content()
        code = code.rstrip('\n')
        if code.strip():
            out.append('```')
            out.append(code)
            out.append('```')
        out.append('')

    elif tag == 'blockquote':
        inner_md = []
        for c in node:
            block(c, inner_md)
        txt = '\n'.join(inner_md).strip()
        if txt:
            out.extend('> ' + ln if ln else '>' for ln in txt.split('\n'))
            out.append('')

    elif tag == 'hr':
        out.append('---')
        out.append('')

    elif tag in ('div', 'section', 'article', 'main', 'header', 'footer', 'nav', 'body'):
        for c in node:
            block(c, out)

    elif tag == 'img':
        src = save_data_url((node.get('src') or '').strip(), CURRENT_SLUG[0])
        if src:
            out.append(f'![{(node.get("alt") or "").strip()}]({src})')
            out.append('')

    elif tag in ('script', 'style'):
        return

    else:
        for c in node:
            block(c, out)


def to_markdown(node):
    out = []
    block(node, out)
    md = '\n'.join(out)
    md = re.sub(r'\n{3,}', '\n\n', md)
    return md.strip() + '\n'


# ---------------------------------------------------------------- 各篇入口
def load(path):
    doc = LH.parse(os.path.join(REPO, path), parser=LH.HTMLParser(encoding='utf-8'))
    for tag in ('script', 'style'):
        for e in doc.xpath(f'//{tag}'):
            e.getparent().remove(e)
    return doc


def article_body(doc):
    node = doc.xpath('//div[contains(@class,"article")]')
    if node:
        return node[0]
    node = doc.xpath('//div[@id="write"]')
    if node:
        return node[0]
    return doc.find('body')


def demote_headings(md, base=2):
    """正文里的 h2 变成 h3，避免与页面标题抢层级。"""
    def fix(m):
        level = len(m.group(1))
        return '#' * min(6, level + (base - 2)) + ' '
    return re.sub(r'^(#{1,6}) ', fix, md, flags=re.M)


def main():
    jobs = [
        ('post/blog/index.html',  'sql',     'SQL 语句的分类',   '2020-03-09', '向'),
        ('post/blog/index1.html', 'git',     'Git 的操作',       '2020-03-11', '向'),
        ('post/blog/index2.html', 'maven',   'Maven 的常用操作', '2020-04-02', '向'),
        ('post/blog/index3.html', 'mybatis', 'MyBatis',          '2020-04-23', '向'),
    ]
    outdir = os.path.join(REPO, 'post/blog/src')
    os.makedirs(outdir, exist_ok=True)

    for path, slug, title, date, _ in jobs:
        CURRENT_SLUG[0] = slug
        _url_counter['n'] = 0
        doc = load(path)
        md = to_markdown(article_body(doc))
        md = demote_headings(md, base=2)

        # 去掉与页面标题重复的首个标题
        md = re.sub(r'^#{2,3} ' + re.escape(title) + r'\s*$', '', md, count=1, flags=re.M).lstrip('\n')
        # 去掉小书匠导出残留前缀
        md = md.replace('mark text##', '## ').replace('mark text', '')
        # 去掉上一轮注入的返回导航
        md = re.sub(r'^\[← 返回 Cody 的主页\]\(/\) · \[文章存档\]\(/post/\)\s*$', '', md, flags=re.M)
        # 标题里重复的 ## 前缀
        md = re.sub(r'^(#{2,3}) #+\s*', r'\1 ', md, flags=re.M)
        # 正文行首漏掉空格的 ## 标题
        md = re.sub(r'^##(?=\S)', '## ', md, flags=re.M)
        md = re.sub(r'^#{1,6}\s*$', '', md, flags=re.M)
        # 有序列表缺少空格：1.xxx -> 1. xxx
        md = re.sub(r'^(\d+)\.(?=\S)', r'\1. ', md, flags=re.M)
        # 标题紧邻的分隔线没有意义，去掉
        md = re.sub(r'\n---\n\n(#{2,3} )', r'\n\n\1', md)
        md = re.sub(r'(#{2,3} [^\n]*)\n\n---\n', r'\1\n', md)
        md = re.sub(r'\n{3,}', '\n\n', md)
        # 单独的 ----- 分隔线统一成 ---
        md = re.sub(r'^-{5,}$', '---', md, flags=re.M)
        md = re.sub(r'\n{3,}', '\n\n', md)

        front = f'# {title}\n\n- 日期：{date}\n\n'
        open(os.path.join(outdir, slug + '.md'), 'w', encoding='utf-8').write(front + md)
        print(f'{slug:8s} {len(md):>7,} 字符 -> post/blog/src/{slug}.md')


if __name__ == '__main__':
    main()
