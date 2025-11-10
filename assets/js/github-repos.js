class GitHubRepos {
    constructor() {
        this.config = {};
        this.manualRepos = [];
        this.apiRepos = [];
        this.init();
    }

    async init() {
        await this.loadConfig();
        await this.loadFromGitHub();
        this.renderRepos();
        this.setupErrorHandling();
    }

    async loadConfig() {
        try {
            const container = document.getElementById('github-repos');
            if (container && container.dataset.config) {
                this.config = JSON.parse(container.dataset.config);
            }
            
            if (window.manualRepositories) {
                this.manualRepos = window.manualRepositories;
            }
        } catch (error) {
            console.warn('Failed to load config, using defaults:', error);
            this.setDefaultConfig();
        }
    }

    setDefaultConfig() {
        this.config = {
            max_repos: 6,
            show_forks: false,
            exclude_repos: []
        };
    }

    async loadFromGitHub() {
        try {
            const username = this.config.github_username || 'wxj630';
            const response = await fetch(
                `https://api.github.com/users/${username}/repos?sort=updated&per_page=${this.config.max_repos || 6}`
            );
            
            if (!response.ok) throw new Error(`GitHub API error: ${response.status}`);
            
            const repos = await response.json();
            
            this.apiRepos = repos.filter(repo => {
                if (!this.config.show_forks && repo.fork) return false;
                if (this.config.exclude_repos.includes(repo.name)) return false;
                return true;
            }).map(repo => this.transformRepoData(repo));
            
        } catch (error) {
            console.error('Failed to load from GitHub:', error);
            this.showFallbackMessage();
        }
    }

    transformRepoData(repo) {
        return {
            name: repo.name,
            full_name: repo.full_name,
            description: repo.description || 'No description available',
            url: repo.html_url,
            language: repo.language || 'Unknown',
            stars: repo.stargazers_count,
            forks: repo.forks_count,
            updated_at: repo.updated_at,
            is_pinned: false,
            from_api: true
        };
    }

    // getMergedRepositories() {
    //     const allRepos = [...this.manualRepos];
        
    //     this.apiRepos.forEach(apiRepo => {
    //         const exists = allRepos.some(manualRepo => 
    //             manualRepo.full_name === apiRepo.full_name
    //         );
    //         if (!exists) allRepos.push(apiRepo);
    //     });

    //     return allRepos.sort((a, b) => {
    //         if (a.is_pinned && !b.is_pinned) return -1;
    //         if (!a.is_pinned && b.is_pinned) return 1;
    //         return (b.stars || 0) - (a.stars || 0);
    //     }).slice(0, this.config.max_repos || 8);
    // }

    getMergedRepositories() {
        const allRepos = [...this.manualRepos];
        
        this.apiRepos.forEach(apiRepo => {
            const existingIndex = allRepos.findIndex(manualRepo => 
                manualRepo.full_name === apiRepo.full_name
            );
            
            if (existingIndex !== -1) {
                // 如果仓库已存在，更新关键信息
                allRepos[existingIndex] = {
                    ...allRepos[existingIndex],  // 保留原有属性
                    stars: apiRepo.stars,        // 更新星数
                    forks: apiRepo.forks,        // 更新fork数
                    description: apiRepo.description,  // 更新描述
                    updated_at: apiRepo.updated_at,     // 更新最后更新时间
                    // 可以添加其他需要更新的字段
                };
            } else {
                // 如果仓库不存在，添加新仓库
                allRepos.push(apiRepo);
            }
        });

        return allRepos.sort((a, b) => {
            if (a.is_pinned && !b.is_pinned) return -1;
            if (!a.is_pinned && b.is_pinned) return 1;
            return (b.stars || 0) - (a.stars || 0);
        }).slice(0, this.config.max_repos || 8);
    }



    renderRepos() {
        const container = document.getElementById('github-repos');
        if (!container) return;

        const repos = this.getMergedRepositories();
        
        if (repos.length === 0) {
            container.innerHTML = this.getEmptyMessage();
            return;
        }

        container.innerHTML = `
            <div class="repo-stats">
                <span class="last-updated">Last updated: ${new Date().toLocaleDateString()}</span>
                <span class="repo-count">Showing ${repos.length} repositories</span>
            </div>
            <div class="repo-grid">
                ${repos.map(repo => this.renderRepoCard(repo)).join('')}
            </div>
            <div class="repo-footer">
                <a href="https://github.com/${this.config.github_username || 'wxj630'}" 
                   target="_blank" class="view-all-btn">
                   View all repositories on GitHub →
                </a>
            </div>
        `;
    }

    renderRepoCard(repo) {
        const isPinned = repo.is_pinned ? '<span class="pinned-badge" title="Pinned Repository">📌</span>' : '';
        const apiIndicator = repo.from_api ? '<span class="api-indicator" title="Live from GitHub">🔄</span>' : '';
        
        return `
            <div class="repo-card ${repo.is_pinned ? 'pinned' : ''}">
                <div class="repo-header">
                    <h3>
                        <a href="${repo.url}" target="_blank" rel="noopener">
                            ${repo.full_name}
                        </a>
                    </h3>
                    <div class="repo-badges">
                        ${isPinned}
                        ${apiIndicator}
                    </div>
                </div>
                <p class="repo-description">${repo.description}</p>
                <div class="repo-meta">
                    <span class="language" data-language="${repo.language}">
                        <span class="language-color"></span>
                        ${repo.language}
                    </span>
                    <span class="stars" title="${repo.stars} stars">
                        ⭐ ${this.formatNumber(repo.stars)}
                    </span>
                    <span class="forks" title="${repo.forks} forks">
                        🍴 ${this.formatNumber(repo.forks)}
                    </span>
                </div>
                ${repo.updated_at ? `
                    <div class="repo-updated">
                        Updated ${this.formatDate(repo.updated_at)}
                    </div>
                ` : ''}
            </div>
        `;
    }

    formatNumber(num) {
        if (num >= 1000) return (num / 1000).toFixed(1) + 'k';
        return num.toString();
    }

    formatDate(dateString) {
        const date = new Date(dateString);
        const now = new Date();
        const diffDays = Math.ceil(Math.abs(now - date) / (1000 * 60 * 60 * 24));
        
        if (diffDays === 1) return 'today';
        if (diffDays < 7) return `${diffDays} days ago`;
        if (diffDays < 30) return `${Math.ceil(diffDays / 7)} weeks ago`;
        return date.toLocaleDateString();
    }

    getEmptyMessage() {
        return `
            <div class="repos-empty">
                <p>No repositories found.</p>
                <p>Check my <a href="https://github.com/${this.config.github_username || 'wxj630'}" target="_blank">GitHub profile</a> for more projects.</p>
            </div>
        `;
    }

    showFallbackMessage() {
        const container = document.getElementById('github-repos');
        if (container && this.manualRepos.length > 0) {
            container.innerHTML += `
                <div class="api-fallback">
                    <p>Showing manually configured repositories (GitHub API unavailable)</p>
                </div>
            `;
        }
    }

    setupErrorHandling() {
        window.addEventListener('error', (e) => {
            console.error('Error in GitHubRepos:', e.error);
        });
    }
}

document.addEventListener('DOMContentLoaded', () => {
    if (window.manualRepositories) {
        new GitHubRepos();
    }
});