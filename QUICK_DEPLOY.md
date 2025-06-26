# 🚀 Quick Deploy Guide - 100 Gates to Freedom Bot

## Your Bot Token
```
7565894498:AAE35txlRa2uTbZ7lBJWvrM9ExAtGYRtfuI
```

## 📋 Deployment Steps

### 1. Create GitHub Repository
1. Go to https://github.com/new
2. Repository name: `100gates`
3. Make it **PUBLIC** (required for Render free tier)
4. Don't initialize with README
5. Click "Create repository"
6. Copy the repository URL (e.g., `https://github.com/yourusername/100gates.git`)

### 2. Push Code to GitHub
```bash
# Run the deployment script with your repository URL
./deploy.sh https://github.com/yourusername/100gates.git
```

### 3. Deploy to Render
1. Go to https://render.com
2. Sign up/Login with GitHub
3. Click "New +" → "Blueprint"
4. Connect your GitHub repository
5. Click "Apply" to deploy

### 4. Configure Admin Access (Optional)
After deployment, add your Telegram ID to admin access:
1. Go to your Render service dashboard
2. Navigate to "Environment" tab
3. Add variable: `ADMIN_TELEGRAM_IDS` with your Telegram ID

## 🎮 Test Your Bot

1. **Find your bot**: Search for your bot username on Telegram
2. **Start the game**: Send `/start`
3. **Test commands**: Try `/help`, `/status`, `/leaderboard`

## 📱 Bot Features

- **100 Gates**: Answer 100 questions correctly
- **30-second Timer**: Answer within 30 seconds
- **One Strike**: Wrong answer = game over
- **69% Prize**: First winner gets the prize pool
- **Leaderboard**: See top players

## 🔧 Admin Commands

Once deployed, you can use admin tools:
```bash
# View game statistics
python scripts/admin_tools.py stats

# View active players
python scripts/admin_tools.py players

# View leaderboard
python scripts/admin_tools.py leaderboard
```

## 🆘 Troubleshooting

### Bot Not Responding
1. Check Render logs for errors
2. Verify webhook is set correctly
3. Test the health endpoint: `https://your-app.onrender.com/health`

### Database Issues
1. Check if PostgreSQL is provisioned
2. Verify DATABASE_URL is set
3. Check migration logs

### Questions Not Loading
1. Run the seed script manually
2. Check database connection
3. Verify questions table exists

## 📞 Support

If you encounter issues:
1. Check Render service logs
2. Verify all environment variables
3. Test the webhook endpoint manually
4. Check the health endpoint

## 🎯 Next Steps

After successful deployment:
1. **Test the game** with multiple players
2. **Monitor performance** using admin tools
3. **Customize questions** if needed
4. **Set up monitoring** for production use

---

**Your bot will be live at**: `https://100gates-bot.onrender.com`
**Webhook URL**: `https://100gates-bot.onrender.com/webhook` 