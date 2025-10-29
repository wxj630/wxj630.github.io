## Code Projects

<div class="repo-grid">
  {% for repo in site.data.repositories.pinned_repos %}
  <div class="repo-card">
    <div class="repo-header">
      <h3><a href="{{ repo.url }}" target="_blank">{{ repo.full_name }}</a></h3>
    </div>
    <p class="repo-description">{{ repo.description }}</p>
    <div class="repo-meta">
      <span class="language">{{ repo.language }}</span>
      <span class="stars">⭐ {{ repo.stars }}</span>
      <span class="forks">🍴 {{ repo.forks }}</span>
    </div>
  </div>
  {% endfor %}
</div>

<!-- <div id="github-repos" 
     data-config='{
         "github_username": "wxj630",
         "max_repos": 8,
         "show_forks": false,
         "exclude_repos": []
     }'>
    <!-- Loading repositories... -->
<!-- </div> -->

<!-- <script>
window.manualRepositories = [
    {% for repo in site.data.repositories.pinned_repos %}
    {
        name: "{{ repo.name }}",
        full_name: "{{ repo.full_name }}",
        description: "{{ repo.description }}",
        url: "{{ repo.url }}",
        language: "{{ repo.language }}",
        stars: {{ repo.stars }},
        forks: {{ repo.forks }},
        is_pinned: {{ repo.is_pinned }}
    }{% unless forloop.last %},{% endunless %}
    {% endfor %}
];
</script> -->

<!-- <noscript>
    <div class="repo-grid">
        {% for repo in site.data.repositories.pinned_repos %}
        <div class="repo-card">
            <h3><a href="{{ repo.url }}" target="_blank">{{ repo.full_name }}</a></h3>
            <p>{{ repo.description }}</p>
            <div class="repo-meta">
                <span class="language">{{ repo.language }}</span>
                <span class="stars">⭐ {{ repo.stars }}</span>
                <span class="forks">🍴 {{ repo.forks }}</span>
            </div>
        </div>
        {% endfor %}
    </div>
</noscript> --> -->