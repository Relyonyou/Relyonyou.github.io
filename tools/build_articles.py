# -*- coding: utf-8 -*-
"""把 post/blog/src/*.md 渲染成站点里的文章页。

用法：python3 tools/build_articles.py
源文件改完重跑即可，不需要其他依赖。
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import md2html  # noqa: E402

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ARTICLES = [
    # 源文件, 输出文件, 标题, 日期, 摘要
    ('sql.md',     'post/blog/index.html',  'SQL 语句的分类',   '2020-03-09', 'SQL 的 DDL / DML / DQL / DCL 语句分类与常用写法。'),
    ('git.md',     'post/blog/index1.html', 'Git 的操作',       '2020-03-11', 'Git 日常操作：本地仓库、远程协作、冲突处理与常用命令。'),
    ('maven.md',   'post/blog/index2.html', 'Maven 的常用操作', '2020-04-02', 'Maven 的概念、下载配置与常用命令。'),
    ('mybatis.md', 'post/blog/index3.html', 'MyBatis',          '2020-04-23', 'MyBatis 入门笔记：配置、映射文件与增删改查。'),
]

CSS = """
  :root{ --bg:#fbfbfa; --fg:#1a1a1c; --body:#3d3d42; --muted:#6f7076;
         --line:#e7e6e3; --accent:#2b5fd9; --tag:#f4f3f0; }
  @media (prefers-color-scheme: dark){
    :root{ --bg:#111113; --fg:#ededf0; --body:#c3c3c9; --muted:#8e8f96;
           --line:#2a2a2f; --accent:#8fb0ff; --tag:#1e1e22; }
  }
  *{box-sizing:border-box}
  html{-webkit-text-size-adjust:100%}
  body{ margin:0; background:var(--bg); color:var(--fg);
        font:16px/1.85 -apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC",
             "Hiragino Sans GB","Microsoft YaHei",sans-serif;
        -webkit-font-smoothing:antialiased }
  a{ color:var(--accent); text-decoration:none; border-bottom:1px solid transparent }
  a:hover{ border-bottom-color:currentColor }
  .topbar{ max-width:720px; margin:0 auto; padding:22px 24px 0;
           display:flex; align-items:center; justify-content:space-between; gap:16px }
  .brand{ font-weight:640; font-size:15px; color:var(--fg) }
  .topbar nav{ display:flex; gap:18px; font-size:14px }
  .topbar nav a{ color:var(--muted) }
  .topbar nav a:hover{ color:var(--accent) }
  main{ max-width:720px; margin:0 auto; padding:40px 24px 56px }
  .kicker{ margin:0 0 8px; font-size:13.5px; color:var(--muted);
           font-variant-numeric:tabular-nums; letter-spacing:.02em }
  h1.title{ margin:0 0 10px; font-size:30px; line-height:1.3; font-weight:640; letter-spacing:-.015em }
  .lead{ margin:0 0 30px; padding-bottom:22px; border-bottom:1px solid var(--line);
         color:var(--muted); font-size:15px }
  footer{ max-width:720px; margin:0 auto; padding:22px 24px 48px;
          border-top:1px solid var(--line); font-size:13px; color:var(--muted) }

  /* ---------- 正文 ---------- */
  .article{ font-size:16px; color:var(--body) }
  .article p{ margin:0 0 16px }
  .article h1,.article h2,.article h3,.article h4,.article h5,.article h6{
    color:var(--fg); line-height:1.4; font-weight:620; margin:36px 0 14px }
  .article h2{ font-size:20px; padding-bottom:6px; border-bottom:1px solid var(--line) }
  .article h3{ font-size:17.5px }
  .article h4,.article h5,.article h6{ font-size:16px }
  .article ul,.article ol{ padding-left:24px; margin:0 0 16px }
  .article li{ margin:5px 0 }
  .article li>ul,.article li>ol{ margin:6px 0 2px }
  .article strong{ color:var(--fg); font-weight:620 }
  .article img{ max-width:100%; height:auto; border:1px solid var(--line);
                border-radius:5px; margin:10px 0; display:block }
  .article hr{ border:0; border-top:1px solid var(--line); margin:32px 0 }
  .article blockquote{ margin:18px 0; padding:2px 0 2px 16px;
                       border-left:2px solid var(--line); color:var(--muted) }
  .article blockquote p:last-child{ margin-bottom:0 }
  .article pre{ background:var(--tag); border:1px solid var(--line); border-radius:6px;
                padding:14px 16px; overflow-x:auto; margin:0 0 18px;
                font-size:13.5px; line-height:1.65 }
  .article code{ font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace; font-size:13.5px }
  .article :not(pre)>code{ background:var(--tag); border:1px solid var(--line);
                           border-radius:4px; padding:1px 5px }
  .article table{ border-collapse:collapse; display:block; overflow-x:auto; margin:0 0 18px; font-size:15px }
  .article th,.article td{ border:1px solid var(--line); padding:6px 11px; text-align:left }
  .article th{ background:var(--tag) }
  @media (max-width:600px){
    .topbar{padding:16px 20px 0}
    main{padding:28px 20px 40px}
    h1.title{font-size:24px}
  }
"""

SHELL = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · Cody</title>
<meta name="description" content="{desc}">
<meta property="og:type" content="article">
<meta property="og:title" content="{title} · Cody">
<meta property="og:description" content="{desc}">
<meta name="theme-color" content="#fbfbfa">
<link rel="icon" href="/img/favicon.ico">
<style>{css}</style>
</head>
<body>
<div class="topbar">
  <a class="brand" href="/">Cody</a>
  <nav><a href="/">首页</a><a href="/post/">文章存档</a></nav>
</div>
<main>
  <p class="kicker">2020 年的笔记 · {date}</p>
  <h1 class="title">{title}</h1>
  <p class="lead">{desc}</p>
  <div class="article">
{body}
  </div>
</main>
<footer>© 2026 Cody · <a href="/post/">返回文章存档</a></footer>
</body>
</html>
"""


def strip_front(md):
    """去掉源文件里的标题行与日期行（页面壳已经渲染）。"""
    md = md.lstrip('\n')
    md = re.sub(r'^# .*\n', '', md, count=1)
    md = re.sub(r'^\s*- 日期：.*\n', '', md, count=1)
    return md.lstrip('\n')


def main():
    for src, out, title, date, desc in ARTICLES:
        path = os.path.join(REPO, 'post/blog/src', src)
        md = open(path, encoding='utf-8').read()
        body = md2html.render(strip_front(md))
        body = '\n'.join('    ' + ln for ln in body.splitlines())
        html = SHELL.format(title=title, date=date, desc=desc, css=CSS, body=body)
        open(os.path.join(REPO, out), 'w', encoding='utf-8').write(html)
        print(f'{src:12s} -> {out:24s} {len(html):>8,} 字节')


if __name__ == '__main__':
    main()
