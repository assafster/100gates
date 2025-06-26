# Deployment Guide - 100 Gates to Freedom Bot

This guide will walk you through deploying the 100 Gates to Freedom Telegram Bot on various platforms.

## 🚀 Quick Start (Recommended: Render)

### 1. Prerequisites

- GitHub account
- Telegram Bot Token (get from [@BotFather](https://t.me/botfather))
- PostgreSQL database (provided by Render)

### 2. Deploy to Render

1. **Fork/Clone Repository**
   ```bash
   git clone <your-repo-url>
   cd 100gates
   ```

2. **Connect to Render**
   - Go to [render.com](https://render.com)
   - Sign up/Login with GitHub
   - Click "New +" → "Blueprint"

3. **Deploy with Blueprint**
   - Connect your GitHub repository
   - Render will automatically detect the `render.yaml` configuration
   - Click "Apply"

4. **Configure Environment Variables**
   - Go to your service dashboard
   - Navigate to "Environment" tab
   - Add the following variables:
     ```
     TELEGRAM_BOT_TOKEN=your_bot_token_here
     ADMIN_TELEGRAM_IDS=your_telegram_id,another_admin_id
     ```

5. **Deploy**
   - Click "Deploy" to start the build process
   - Wait for deployment to complete (usually 2-3 minutes)

### 3. Set Webhook

Once deployed, your bot will automatically set its webhook to:
```
https://your-app-name.onrender.com/webhook
```

## 🚂 Alternative: Railway Deployment

### 1. Setup Railway

1. **Install Railway CLI**
   ```bash
   npm install -g @railway/cli
   ```

2. **Login to Railway**
   ```bash
   railway login
   ```

3. **Initialize Project**
   ```bash
   railway init
   ```

### 2. Add Services

1. **Add PostgreSQL**
   ```bash
   railway add
   # Select PostgreSQL
   ```

2. **Deploy Application**
   ```bash
   railway up
   ```

3. **Set Environment Variables**
   ```bash
   railway variables set TELEGRAM_BOT_TOKEN=your_bot_token
   railway variables set WEBHOOK_URL=https://your-app.railway.app
   railway variables set ADMIN_TELEGRAM_IDS=your_telegram_id
   ```

## 🐳 Docker Deployment

### 1. Build Docker Image

```bash
docker build -t 100gates-bot .
```

### 2. Run with Docker Compose

Create `docker-compose.yml`:
```yaml
version: '3.8'
services:
  bot:
    build: .
    ports:
      - "8000:8000"
    environment:
      - TELEGRAM_BOT_TOKEN=${TELEGRAM_BOT_TOKEN}
      - DATABASE_URL=${DATABASE_URL}
      - WEBHOOK_URL=${WEBHOOK_URL}
    depends_on:
      - db
  
  db:
    image: postgres:15
    environment:
      - POSTGRES_DB=100gates
      - POSTGRES_USER=100gates_user
      - POSTGRES_PASSWORD=your_password
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

Run:
```bash
docker-compose up -d
```

## 🏠 Local Development

### 1. Setup Environment

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Create Environment File**
   ```bash
   cp env.example .env
   # Edit .env with your configuration
   ```

3. **Setup Database**
   ```bash
   # Run setup script
   python scripts/setup.py
   
   # Or manually:
   alembic upgrade head
   python scripts/seed_questions.py
   ```

### 2. Run Locally

```bash
uvicorn app.main:app --reload
```

### 3. Set Webhook for Local Development

For local development, you'll need a public URL. Use ngrok:

```bash
# Install ngrok
npm install -g ngrok

# Start tunnel
ngrok http 8000

# Set webhook (replace with your ngrok URL)
curl -X POST "https://api.telegram.org/bot<YOUR_BOT_TOKEN>/setWebhook" \
     -H "Content-Type: application/json" \
     -d '{"url": "https://your-ngrok-url.ngrok.io/webhook"}'
```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `TELEGRAM_BOT_TOKEN` | Your Telegram bot token | ✅ | - |
| `DATABASE_URL` | PostgreSQL connection string | ✅ | - |
| `WEBHOOK_URL` | Public URL for webhook | ✅ | - |
| `SECRET_KEY` | Secret key for security | ❌ | Auto-generated |
| `QUESTION_TIMEOUT` | Seconds per question | ❌ | 30 |
| `TOTAL_GATES` | Number of gates | ❌ | 100 |
| `PRIZE_POOL_PERCENTAGE` | Winner's prize percentage | ❌ | 69 |
| `ADMIN_TELEGRAM_IDS` | Comma-separated admin IDs | ❌ | - |
| `REDIS_URL` | Redis connection (optional) | ❌ | - |
| `SENTRY_DSN` | Sentry error tracking | ❌ | - |

### Database Setup

The bot uses PostgreSQL with the following tables:
- `players` - Player information and progress
- `questions` - Game questions (1-100)
- `games` - Active game sessions

### Questions

The bot comes with 100 pre-seeded questions covering:
- General Knowledge
- Science
- History
- Geography
- Literature
- Math

## 🛠️ Admin Tools

### Command Line Tools

```bash
# Show game statistics
python scripts/admin_tools.py stats

# Show active players
python scripts/admin_tools.py players

# Show leaderboard
python scripts/admin_tools.py leaderboard --limit 20

# Eliminate a player
python scripts/admin_tools.py eliminate 123456789

# Reset all games
python scripts/admin_tools.py reset

# List all questions
python scripts/admin_tools.py list-questions

# Export questions to JSON
python scripts/admin_tools.py export-questions

# Add a new question
python scripts/admin_tools.py add-question 1 "What is 2+2?" "3" "4" "5" "6" "B"
```

### API Endpoints

Admin endpoints (require admin Telegram ID):
- `GET /admin/stats` - Game statistics
- `GET /admin/players` - Active players
- `GET /admin/leaderboard` - Leaderboard
- `POST /admin/reset-game` - Reset all games

## 🔍 Monitoring

### Health Checks

- `GET /` - Basic health check
- `GET /health` - Detailed health status

### Logs

Monitor your application logs:
- **Render**: Service dashboard → Logs
- **Railway**: Project dashboard → Deployments → Logs
- **Local**: Console output

### Error Tracking

Optional Sentry integration:
1. Create account at [sentry.io](https://sentry.io)
2. Add `SENTRY_DSN` to environment variables

## 🚨 Troubleshooting

### Common Issues

1. **Webhook Not Set**
   - Check if your bot token is correct
   - Verify the webhook URL is accessible
   - Check logs for webhook errors

2. **Database Connection**
   - Verify `DATABASE_URL` is correct
   - Check if database is accessible
   - Run migrations: `alembic upgrade head`

3. **Questions Not Loading**
   - Run the seed script: `python scripts/seed_questions.py`
   - Check database for questions table

4. **Bot Not Responding**
   - Check if webhook is set correctly
   - Verify bot token permissions
   - Check application logs

### Debug Mode

Enable debug logging:
```bash
export LOG_LEVEL=DEBUG
uvicorn app.main:app --reload --log-level debug
```

## 🔄 Updates

### Updating the Bot

1. **Pull Latest Changes**
   ```bash
   git pull origin main
   ```

2. **Update Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Migrations**
   ```bash
   alembic upgrade head
   ```

4. **Redeploy**
   - **Render**: Automatic on git push
   - **Railway**: `railway up`
   - **Docker**: `docker-compose up -d --build`

## 📞 Support

If you encounter issues:

1. Check the logs for error messages
2. Verify all environment variables are set
3. Test the webhook endpoint manually
4. Check the [Telegram Bot API documentation](https://core.telegram.org/bots/api)

## 🎯 Next Steps

After deployment:

1. **Test the Bot**
   - Send `/start` to your bot
   - Try answering a few questions
   - Test the timeout mechanism

2. **Customize Questions**
   - Use admin tools to modify questions
   - Add your own questions
   - Export/import question sets

3. **Monitor Performance**
   - Check game statistics
   - Monitor player engagement
   - Track completion rates

4. **Scale Up**
   - Upgrade to paid plans for more resources
   - Add Redis for better performance
   - Implement advanced analytics 