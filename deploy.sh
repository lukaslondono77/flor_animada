#!/bin/bash

# Flor Animada Deployment Script
echo "🌸 Deploying Flor Animada to GitHub Pages..."

# Check if we're in a git repository
if [ ! -d ".git" ]; then
    echo "❌ Not in a git repository. Please initialize git first."
    exit 1
fi

# Add all changes
echo "📝 Adding changes to git..."
git add .

# Commit changes
echo "💾 Committing changes..."
git commit -m "🚀 Deploy optimized Flor Animada to GitHub Pages

- Added modern CSS with high contrast design
- Implemented performance optimizations
- Created static HTML version for GitHub Pages
- Added GitHub Actions workflow for automatic deployment
- Minified CSS for faster loading
- Added responsive design and smooth animations"

# Push to main branch
echo "🚀 Pushing to GitHub..."
git push origin main

echo "✅ Deployment initiated! Check GitHub Actions for deployment status."
echo "🌐 Your app will be available at: https://$(git config --get remote.origin.url | sed 's/.*github.com[:/]\([^/]*\)\/\([^.]*\).*/\1.github.io\/\2/')"
