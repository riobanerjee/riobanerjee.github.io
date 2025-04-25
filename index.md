---
layout: home
author_profile: true
---

# Welcome to My Portfolio

I'm a data scientist and machine learning engineer with a passion for building intelligent systems that solve real-world problems. This portfolio showcases my recent projects in machine learning, data processing, and AI applications.

## Featured Projects

{% for project in site.projects limit:2 %}
<div class="archive__item">
  <h2 class="archive__item-title">
    <a href="{{ project.url | relative_url }}">{{ project.title }}</a>
  </h2>
  <p class="archive__item-excerpt">{{ project.excerpt }}</p>
</div>
{% endfor %}

[View All Projects](/projects/){: .btn .btn--primary}