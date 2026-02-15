source "https://rubygems.org"

# 1. FIXES FOR RUBY 4.0 (Standard library gems now required as external)
gem "csv"
gem "base64"
gem "logger"
gem "bigdecimal"
gem "mutex_m"
gem "erb"
gem "webrick"

# 2. CORE ENGINE (Forced versions to fix the 'tainted?' NoMethodError)
# We use Jekyll 3.10 and Liquid 4.0.4 specifically for Ruby 4.0 compatibility
gem "jekyll", "3.10.0"
gem "liquid", "4.0.4"
gem "kramdown", "~> 2.4"
gem "kramdown-parser-gfm"

# 3. MINIMAL MISTAKES & GITHUB PARITY
# Instead of the 'github-pages' gem, we load the specific plugins usually included
gem "jekyll-remote-theme"
gem "jekyll-include-cache"
gem "jekyll-seo-tag"
gem "jekyll-feed", "~> 0.12"
gem "jekyll-sitemap"
gem "jekyll-paginate"
gem "jekyll-gist"

# 4. THEME
gem "minima", "~> 2.5"

# 5. PLATFORM SUPPORT
platforms :windows, :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo", ">= 1", "< 3"
  gem "tzinfo-data"
  gem "wdm", "~> 0.1"
end

gem "http_parser.rb", "~> 0.8.0"