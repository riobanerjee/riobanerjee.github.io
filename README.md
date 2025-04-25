# My Portfolio

Personal portfolio website built with Jekyll and Minimal Mistakes theme.

## Local Development

1. Install dependencies:
   ```bash
   bundle install
   ```

2. Run locally:
   ```bash
   bundle exec jekyll serve
   ```

3. Visit http://localhost:4000

## Deployment

The site is automatically deployed to GitHub Pages via GitHub Actions when pushing to the main branch.

## Adding New Projects

1. Create a new markdown file in `_projects/`
2. Add project images to `assets/images/projects/`
3. Follow the template structure
4. Commit and push

## Customization

- Edit `_config.yml` for site settings
- Modify `_data/navigation.yml` for menu items
- Add custom styles to `assets/css/main.scss`