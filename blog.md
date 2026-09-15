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
      <p class="blog-lead">文章会在知乎和本博客同步发布。</p>
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

  {% for column in site.data.blog_columns %}
  {% assign column_posts = site.posts | where: "column_key", column.key | sort: "date" | reverse %}
  <section class="blog-column-archive" id="{{ column.key }}">
    <div class="blog-column-archive-heading">
      <div>
        <p class="blog-kicker">Column</p>
        <h3>{{ column.title }}</h3>
        <p class="blog-column-description">{{ column.description }}</p>
      </div>
      <span class="blog-column-count">{{ column_posts.size }} articles</span>
    </div>

    {% if column_posts.size > 0 %}
    <div class="blog-list">
      {% for post in column_posts %}
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
          <div class="blog-metrics" aria-label="Zhihu interaction snapshot">
            <span>阅读 {% if post.views %}{{ post.views }}{% else %}知乎未公开{% endif %}</span>
            <span>收藏 {% if post.favorites != nil %}{{ post.favorites }}{% else %}知乎未公开{% endif %}</span>
            <span>点赞 {% if post.likes != nil %}{{ post.likes }}{% else %}知乎未公开{% endif %}</span>
          </div>
          <p class="blog-excerpt">{{ post.excerpt | strip_html | strip_newlines | truncate: 180 }}</p>
          <a class="blog-read-link" href="{{ post.url | relative_url }}">Read article</a>
        </div>
      </article>
      {% endfor %}
    </div>
    {% endif %}
  </section>
  {% endfor %}
</div>
