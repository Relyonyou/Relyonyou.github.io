# Cody 的个人主页

<https://relyonyou.github.io/>

个人主页 + 技术笔记存档。纯静态站点，**没有构建步骤**：改完 HTML 直接推送到 `master`，GitHub Pages 会自动发布。

## 目录结构

```
.
├── index.html            首页（关于 / 教育背景 / 动态 / 方向 / 项目 / 写作）
├── 404.html              404 页
├── sitemap.xml           站点地图
├── post/
│   ├── index.html        文章存档列表
│   └── blog/             4 篇旧笔记（Markdown 源 + 生成的 HTML）
│       ├── src/*.md      ← 内容源，改这里
│       ├── img/          文章配图
│       ├── index.html    SQL 语句的分类
│       ├── index1.html   Git 的操作
│       ├── index2.html   Maven 的常用操作
│       └── index3.html   MyBatis
├── img/                  头像、favicon 等
├── tools/                文章构建脚本（见下）
└── css/ js/              旧站点遗留资源（已无页面引用）
```

## 本地预览

页面使用 `/img/...` 这类根路径，**必须通过 HTTP 访问**，直接双击 HTML 会丢样式：

```bash
python3 -m http.server 8000
# 打开 http://localhost:8000
```

## 常见修改

| 要改什么 | 改哪里 |
| --- | --- |
| 首页文字 | `index.html`，搜索 `←改` 注释，共 5 处 |
| 教育背景 | `index.html` 中 `<section id="education">`，中英各一套 |
| 改文章内容 | 编辑 `post/blog/src/<slug>.md`，然后 `python3 tools/build_articles.py` |
| 加一篇文章 | 新建 `post/blog/src/<slug>.md`，在 `tools/build_articles.py` 的 `ARTICLES` 里加一行，跑脚本生成，再在 `post/index.html` 和 `sitemap.xml` 补一条 |
| 换头像 | 覆盖 `img/author-2026.jpg`（512×512，建议正方形） |
| 改配色 | `index.html` 顶部 `:root` 变量；深色模式在 `@media (prefers-color-scheme: dark)` 里 |

## 文章维护

文章内容以 Markdown 维护，HTML 由脚本生成（**只在本地跑，GitHub Pages 侧不需要任何构建**）：

```bash
python3 tools/build_articles.py      # src/*.md  ->  post/blog/index*.html
```

三个脚本，零第三方依赖：

| 脚本 | 作用 |
| --- | --- |
| `tools/build_articles.py` | 入口：读 `src/*.md`，套上页面模板输出 HTML |
| `tools/md2html.py` | 极简 Markdown 渲染器（标题/列表/代码/引用/图片/链接/粗体） |
| `tools/html2md.py` | 一次性迁移工具：把 2020 年的旧 HTML 转成 Markdown，已完成历史使命，留作备查 |

Markdown 支持的语法与 [`tools/md2html.py`](tools/md2html.py) 一致，没有引入表格、脚注等扩展；行尾两个空格表示换行。

## 设计说明

- 首页与文章页共用一套设计语言：760px 单列、无侧栏、细线分隔
- 中英双语：右上角切换，默认跟随浏览器语言，选择存在 `localStorage`
- 深色模式：跟随系统 `prefers-color-scheme`，没有手动开关
- 无外部依赖：不加载 CDN、字体或统计脚本

## 部署

推送到 `master` 即发布：

```bash
git add -A
git commit -m "update"
git push origin master
```

GitHub Pages 通常在 30–60 秒内重建。
