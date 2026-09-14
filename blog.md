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
      <p class="blog-lead">从知乎专栏迁移的文章，保留原始发布日期、正文、图片和互动数据快照。</p>
    </div>
    <a class="blog-back-link" href="{{ "/" | relative_url }}">Back to homepage</a>
  </div>

  <div class="blog-columns">
    {% for column in site.data.blog_columns %}
    <a class="blog-column-link" href="#{{ column.key }}">
      <strong>{{ column.title }}</strong>
      <span>{{ column.description }}</span>
    </a>
    {% endfor %}
  </div>

  {% assign posts_by_date = site.posts | sort: "date" | reverse %}
  {% assign seen_columns = "|" %}
  <div class="blog-list">
    {% for post in posts_by_date %}
    {% assign column_marker = post.column_key | append: "|" %}
    <article class="blog-list-item"{% unless seen_columns contains column_marker %} id="{{ post.column_key }}"{% endunless %}>
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
        <div class="blog-metrics" aria-label="Zhihu interaction snapshot">
          <span>阅读 {% if post.views %}{{ post.views }}{% else %}知乎未公开{% endif %}</span>
          <span>收藏 {% if post.favorites != nil %}{{ post.favorites }}{% else %}知乎未公开{% endif %}</span>
          <span>点赞 {% if post.likes != nil %}{{ post.likes }}{% else %}知乎未公开{% endif %}</span>
        </div>
        <p class="blog-excerpt">{{ post.excerpt | strip_html | strip_newlines | truncate: 180 }}</p>
        <a class="blog-read-link" href="{{ post.url | relative_url }}">Read article</a>
      </div>
    </article>
    {% assign seen_columns = seen_columns | append: column_marker %}
    {% endfor %}
  </div>
</div>
