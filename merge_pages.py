#!/usr/bin/env python3
import os
import re
from html import escape

www_dir = '/workspace/www'
pages = []

# Get all page files sorted numerically
for i in range(1, 56):
    pages.append(f'page{i}.html')

# Read all article content from all pages
all_articles = []
external_links = set()

for page_file in pages:
    filepath = os.path.join(www_dir, page_file)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract all article blocks
    article_pattern = r'<article>.*?</article>'
    articles = re.findall(article_pattern, content, re.DOTALL)
    all_articles.extend(articles)
    
    # Extract external links for sitemap
    link_pattern = r'<a href="(https?://[^"]+)"'
    links = re.findall(link_pattern, content)
    external_links.update(links)

print(f"Total articles found: {len(all_articles)}")
print(f"Total unique external links: {len(external_links)}")

# Create the merged single page with high SEO optimization
seo_html = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Complete Article Directory - All 5968 Articles in One Place</title>
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="Comprehensive directory of all 5968 curated articles covering technology, health, sports, entertainment, movies, software releases, and more. All external links indexed for easy access.">
<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1">
<meta name="googlebot" content="index,follow">
<meta name="bingbot" content="index,follow">
<link rel="canonical" href="index.html">
<meta name="keywords" content="articles, technology, health news, medical research, sports stories, movie reviews, software releases, gadgets, apps, news newsletter, curated content">
<meta name="author" content="Article Directory">
<meta property="og:title" content="Complete Article Directory - All 5968 Articles">
<meta property="og:description" content="Access all 5968 curated articles in one comprehensive directory covering technology, health, sports, entertainment and more.">
<meta property="og:type" content="website">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Complete Article Directory - All 5968 Articles">
<meta name="twitter:description" content="Access all 5968 curated articles in one comprehensive directory.">
<style>
body{font-family:Arial,sans-serif;line-height:1.6;max-width:1400px;margin:0 auto;padding:20px;background:#fafafa}
h1{color:#333;text-align:center;margin-bottom:10px}
h2{color:#444;border-bottom:2px solid #0066cc;padding-bottom:10px;margin-top:30px}
.intro{background:#fff;padding:25px;margin-bottom:25px;border-radius:8px;box-shadow:0 2px 4px rgba(0,0,0,0.1)}
.stats{display:flex;justify-content:space-around;flex-wrap:wrap;margin:20px 0}
.stat-box{background:#0066cc;color:#fff;padding:15px 25px;border-radius:8px;margin:10px;text-align:center}
.stat-number{font-size:2em;font-weight:bold}
article{margin-bottom:20px;padding:20px;background:#fff;border-radius:8px;box-shadow:0 2px 4px rgba(0,0,0,0.1)}
article h3{margin:0 0 10px;color:#0066cc;font-size:18px}
article p{margin:0 0 15px;color:#555;font-size:14px}
article a{color:#0066cc;font-weight:bold;text-decoration:none;display:inline-block;padding:8px 16px;background:#e6f0ff;border-radius:4px}
article a:hover{background:#0066cc;color:#fff}
.external-links-section{margin-top:40px;padding:25px;background:#fff;border-radius:8px;box-shadow:0 2px 4px rgba(0,0,0,0.1)}
.external-link{display:block;padding:8px 0;border-bottom:1px solid #eee;word-break:break-all}
.external-link:hover{background:#f5f5f5}
nav.toc{background:#fff;padding:20px;margin:20px 0;border-radius:8px;box-shadow:0 2px 4px rgba(0,0,0,0.1)}
nav.toc a{margin-right:10px;margin-bottom:5px;display:inline-block}
footer{margin-top:40px;padding:20px;background:#333;color:#fff;border-radius:8px;text-align:center}
footer a{color:#4da6ff}
@media(max-width:768px){.stats{flex-direction:column}.stat-box{width:100%}}
</style>
</head>
<body>
<header>
<h1>Complete Article Directory</h1>
<div class="intro">
<p>Welcome to our comprehensive article collection featuring <strong>5968 curated articles</strong> all accessible on this single page.</p>
<p>Explore topics including technology gadgets, health news, medical research, sports stories, movie reviews, software releases, and news newsletters.</p>
<p>This page is optimized for search engines and provides direct access to all external resources.</p>
</div>
<div class="stats">
<div class="stat-box"><div class="stat-number">5968</div><div>Total Articles</div></div>
<div class="stat-box"><div class="stat-number">''' + str(len(external_links)) + '''</div><div>External Links</div></div>
<div class="stat-box"><div class="stat-number">55</div><div>Original Pages</div></div>
</div>
</header>

<nav class="toc">
<h2>Quick Navigation</h2>
<p>Jump to sections: '''

# Add navigation anchors for every 100 articles
for i in range(0, len(all_articles), 100):
    section_num = (i // 100) + 1
    seo_html += f'<a href="#section{section_num}">Articles {i+1}-{min(i+100, len(all_articles))}</a> '

seo_html += '''</p>
</nav>

<main>
<h2>All Articles</h2>
'''

# Add all articles with section breaks
section_num = 1
for idx, article in enumerate(all_articles):
    if idx % 100 == 0 and idx > 0:
        section_num += 1
        seo_html += f'</section>\n<section id="section{section_num}">\n<h2>Articles {(section_num-1)*100+1} - {min(section_num*100, len(all_articles))}</h2>\n'
    elif idx == 0:
        seo_html += '<section id="section1">\n'
    
    # Add rel attributes for SEO
    article = re.sub(r'<a href="(https?://[^"]+)"', r'<a href="\1" rel="dofollow noopener noreferrer" target="_blank"', article)
    seo_html += article + '\n'

seo_html += '''</section>

<section class="external-links-section">
<h2>Complete External Links Directory</h2>
<p>Below is a complete list of all external links for search engine crawlers and indexing purposes:</p>
'''

# Add all external links for crawler optimization
for link in sorted(external_links):
    seo_html += f'<a href="{escape(link)}" class="external-link" rel="dofollow noopener noreferrer" target="_blank">{escape(link)}</a>\n'

seo_html += '''</section>
</main>

<footer>
<p><strong>Total Articles:</strong> 5968 | <strong>Total External Links:</strong> ''' + str(len(external_links)) + '''</p>
<p>This page consolidates content from 55 original pages for improved crawlability and user experience.</p>
<p>&copy; 2024 Article Directory. All rights reserved.</p>
</footer>

<!-- Schema.org structured data for SEO -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "CollectionPage",
  "name": "Complete Article Directory",
  "description": "Comprehensive directory of 5968 curated articles covering technology, health, sports, entertainment, and more.",
  "numberOfItems": 5968,
  "itemListElement": [
'''

# Add first few items as sample structured data (limit to avoid huge file)
for idx, article in enumerate(all_articles[:100]):
    title_match = re.search(r'<h3>(.*?)</h3>', article)
    link_match = re.search(r'<a href="(https?://[^"]+)"', article)
    if title_match and link_match:
        if idx > 0:
            seo_html += ',\n'
        seo_html += f'''    {{
      "@type": "ListItem",
      "position": {idx + 1},
      "name": "{escape(title_match.group(1))}",
      "url": "{escape(link_match.group(1))}"
    }}'''

seo_html += '''
  ]
}
</script>
</body>
</html>
'''

# Write the merged file
output_path = os.path.join(www_dir, 'all-articles.html')
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(seo_html)

print(f"Merged page created: {output_path}")
print(f"File size: {os.path.getsize(output_path) / 1024:.2f} KB")
