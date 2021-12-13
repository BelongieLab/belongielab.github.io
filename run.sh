#!/bin/bash
#bundle install

# remove cached site and folders first for a clean rendering
rm -rf Gemfile.lock
rm -rf _site
rm -rf .jekyll-cache

bundle exec jekyll serve