#!/bin/bash

# 100 Gates to Freedom Bot - Deployment Script
echo "🚀 100 Gates to Freedom Bot - Render Deployment"
echo "================================================"

# Check if GitHub repository URL is provided
if [ -z "$1" ]; then
    echo "❌ Please provide your GitHub repository URL"
    echo "Usage: ./deploy.sh https://github.com/yourusername/100gates.git"
    echo ""
    echo "📝 Steps to get your repository URL:"
    echo "1. Go to https://github.com/new"
    echo "2. Create a new repository named '100gates'"
    echo "3. Make it PUBLIC (required for Render free tier)"
    echo "4. Copy the repository URL"
    exit 1
fi

GITHUB_URL=$1

echo "📦 Preparing deployment..."
echo "GitHub Repository: $GITHUB_URL"

# Add GitHub remote
echo "🔗 Adding GitHub remote..."
git remote add origin $GITHUB_URL

# Push to GitHub
echo "⬆️  Pushing code to GitHub..."
git branch -M main
git push -u origin main

if [ $? -eq 0 ]; then
    echo "✅ Code pushed to GitHub successfully!"
    echo ""
    echo "🎯 Next Steps:"
    echo "1. Go to https://render.com"
    echo "2. Sign up/Login with GitHub"
    echo "3. Click 'New +' → 'Blueprint'"
    echo "4. Connect your GitHub repository"
    echo "5. Click 'Apply' to deploy"
    echo ""
    echo "🔧 Environment Variables (already configured in render.yaml):"
    echo "   - TELEGRAM_BOT_TOKEN: ✅ Set"
    echo "   - DATABASE_URL: ✅ Auto-configured"
    echo "   - WEBHOOK_URL: ✅ Auto-configured"
    echo ""
    echo "📱 After deployment, your bot will be available at:"
    echo "   https://100gates-bot.onrender.com"
    echo ""
    echo "🎮 Test your bot by sending /start to your Telegram bot!"
else
    echo "❌ Failed to push to GitHub"
    echo "Please check your repository URL and try again"
    exit 1
fi 