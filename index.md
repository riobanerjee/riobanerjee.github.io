---
layout: splash
author_profile: false
---

<div class="profile-container">
  <div class="profile-image">
    <img src="/assets/images/profile/avatar.jpg" alt="Profile">
  </div>
  
  <div class="profile-content">
    <h1>Agnibha Banerjee</h1>
    <p class="subtitle">Astrophysicist | Data Scientist</p>
    <p class="description">
      I'm an astrophysicist and data scientist exploring exoplanet atmospheres at The Open University. Passionate about applying machine learning to solve real-world problems.
    </p>
    <div class="profile-buttons">
      <a href="/projects/" class="btn btn--primary">Projects</a>
      <a href="/about/" class="btn btn--inverse">About</a>
    </div>
  </div>
</div>

<style>
.profile-container {
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 4em 1em;
  gap: 3em;
  flex-wrap: wrap;
}

.profile-image img {
  width: 220px;
  height: 220px;
  border-radius: 50%;
  box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}

.profile-content {
  max-width: 500px;
}

.profile-content h1 {
  font-size: 2.2em;
  margin-bottom: 0.3em;
}

.subtitle {
  font-size: 1.2em;
  color: #666;
  margin-bottom: 1em;
}

.description {
  font-size: 1em;
  color: #888;
  margin-bottom: 2em;
  line-height: 1.6;
}

.profile-buttons {
  display: flex;
  gap: 1em;
}

@media (max-width: 768px) {
  .profile-container {
    flex-direction: column;
    text-align: center;
    margin: 2em 1em;
    gap: 1.5em;
  }
  
  .profile-image img {
    width: 180px;
    height: 180px;
  }
  
  .profile-content h1 {
    font-size: 1.8em;
  }
  
  .subtitle {
    font-size: 1em;
  }
  
  .description {
    font-size: 0.9em;
    margin-bottom: 1.5em;
  }
}
</style>