# Source for Ruby gems
source "https://rubygems.org"

# Core Jekyll engine for static site generation
gem "jekyll", "~> 4.4.1"

# GitHub Pages integration (includes Jekyll and supported plugins)
# Uncomment if deploying via GitHub Pages
# gem "github-pages", group: :jekyll_plugins

# Jekyll plugin group
group :jekyll_plugins do
  # Generates sitemap.xml for SEO and search engine indexing
  gem "jekyll-sitemap"
end

# Platform-specific dependencies for Windows and JRuby
platforms :windows, :jruby do
  # Timezone support required by certain gems and environments
  gem "tzinfo", ">= 1", "< 3"
  # Timezone data for Windows platforms
  gem "tzinfo-data"
end

# File system watcher for Windows platforms
gem 'wdm', '~> 0.2.0' if Gem.win_platform? && ENV['CI'].nil?

# HTTP parser for JRuby compatibility
gem "http_parser.rb", "~> 0.6.0", platforms: [:jruby]

# Standard library gems (explicitly listed for compatibility or bundling)
gem "csv"       # CSV parsing and generation
gem "logger"    # Logging utilities
gem "base64"    # Base64 encoding and decoding