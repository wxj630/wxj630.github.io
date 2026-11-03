---
layout: homepage
title: Blog
permalink: /blog/
---

<div class="blog-page">
  <div class="blog-page-heading">
    <div>
      <p class="blog-kicker">Writing</p>
      <h2>Blog</h2>
      <p class="blog-total-metrics">阅读 85.3 万 · 点赞 3,608 · 收藏 8,178 · 分享 2,709</p>
      <p class="blog-lead">文章会在知乎和本博客同步发布。</p>
    </div>
    <a class="blog-back-link" href="{{ "/" | relative_url }}">Back to homepage</a>
  </div>

  <div class="blog-columns">
    {% for column in site.data.blog_columns %}
    <a class="blog-column-link" href="{{ "/blog/" | append: column.key | append: "/" | relative_url }}">
      <strong>{{ column.title }}</strong>
      <span>{{ column.description }}</span>
    </a>
    {% endfor %}
  </div>

  {% assign posts_by_date = site.posts | sort: "date" | reverse %}
  <div class="blog-list">
    {% for post in posts_by_date %}
    <article class="blog-list-item">
      {% if post.cover_image %}
      <a class="blog-list-cover" href="{{ post.url | relative_url }}" aria-label="Read {{ post.title }}">
        <img src="{{ post.cover_image | relative_url }}" alt="">
      </a>
      {% endif %}
      <div class="blog-list-content">
        <div class="blog-post-meta">
          <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%Y-%m-%d" }}</time>
          <span>{{ post.column_title }}</span>
        </div>
        <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
        <p class="blog-excerpt">{{ post.excerpt | strip_html | strip_newlines | truncate: 180 }}</p>
        <a class="blog-read-link" href="{{ post.url | relative_url }}">Read article</a>
      </div>
    </article>
    {% endfor %}
  </div>
</div>
