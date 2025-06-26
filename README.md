# 100 Gates to Freedom Telegram Bot

A high-stakes Telegram game where players must answer 100 consecutive questions correctly to win 69% of the prize pool. One mistake or timeout means starting over from Gate 1.

## 🎮 Game Mechanics

- **100 Gates**: Each question represents a "gate"
- **30-second timer**: Answer within 30 seconds or fail
- **One strike rule**: Wrong answer or timeout = game over
- **Prize pool**: 69% to the first player to reach Gate 100
- **No backtracking**: Can't go back or skip questions

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- PostgreSQL database (Supabase recommended)
- Telegram Bot Token
- Redis (optional, for session management)

### Local Development

1. **Clone and setup**:
```bash
git clone <repository>
cd 100gates
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

2. **Environment variables**:
```bash
cp .env.example .env
# Edit .env with your credentials
```

3. **Database setup**:
```bash
alembic upgrade head
```

4. **Run the bot**:
```bash
uvicorn app.main:app --reload
```

### Environment Variables

Create a `.env` file with:
```env
TELEGRAM_BOT_TOKEN=your_bot_token
DATABASE_URL=postgresql://user:pass@host:port/db
REDIS_URL=redis://localhost:6379
WEBHOOK_URL=https://your-domain.com/webhook
SECRET_KEY=your_secret_key
SENTRY_DSN=your_sentry_dsn
```

## 🏗️ Architecture

- **FastAPI**: Web framework for bot webhook
- **SQLAlchemy**: Database ORM
- **PostgreSQL**: Primary database (Supabase)
- **Redis**: Session management and caching
- **Celery**: Background task processing
- **Alembic**: Database migrations

## 📊 Database Schema

### Players
- `telegram_id`: Unique Telegram user ID
- `username`: Telegram username
- `current_gate`: Current gate progress (1-100)
- `game_state`: Active, eliminated, completed
- `elimination_reason`: Timeout, wrong_answer
- `start_time`: Game start timestamp
- `last_activity`: Last interaction time
- `completed_at`: Completion timestamp (if finished)

### Games
- `id`: Game session ID
- `player_id`: Player reference
- `gate_number`: Current gate
- `question_id`: Question reference
- `start_time`: Gate start time
- `timeout_at`: When gate expires
- `status`: Active, completed, failed

### Questions
- `id`: Question ID
- `gate_number`: Gate number (1-100)
- `question_text`: Question content
- `option_a`, `option_b`, `option_c`, `option_d`: Multiple choice options
- `correct_answer`: Correct option (A, B, C, or D)

## 🚀 Deployment

### Render Deployment

1. **Connect repository** to Render
2. **Create Web Service**:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
3. **Add environment variables**
4. **Set up PostgreSQL** addon
5. **Configure webhook** URL

### Railway Deployment

1. **Connect repository** to Railway
2. **Add PostgreSQL** plugin
3. **Set environment variables**
4. **Deploy automatically**

## 📱 Bot Commands

- `/start` - Begin new game (Gate 1)
- `/restart` - Reset and start from Gate 1
- `/help` - Show game rules and commands
- `/status` - Check current progress
- `/leaderboard` - View top players

## 🔧 Admin Features

- View all active players
- Reset game globally
- Block/unblock players
- Update questions
- Monitor analytics

## 📈 Analytics

- Drop-off heatmap by gate
- Average response times
- Player retention metrics
- Prize pool tracking

## 🛡️ Security Features

- Rate limiting
- Session validation
- Anti-cheating measures
- Unique question ordering
- Time-based validation

## 🤝 Contributing

1. Fork the repository
2. Create feature branch
3. Make changes
4. Add tests
5. Submit pull request

## 📄 License

MIT License - see LICENSE file for details 