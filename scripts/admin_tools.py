#!/usr/bin/env python3
"""
Admin tools for 100 Gates to Freedom Bot
Manage players, questions, and game settings
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.database import SessionLocal
from app.crud import get_game_stats, get_active_players, get_leaderboard, eliminate_player
from app.models import Player, Question, GameState, EliminationReason
from app.schemas import QuestionCreate
import argparse
import json

def show_stats():
    """Show game statistics"""
    db = SessionLocal()
    try:
        stats = get_game_stats(db)
        print("\n📊 Game Statistics:")
        print(f"Total Players: {stats['total_players']}")
        print(f"Active Players: {stats['active_players']}")
        print(f"Eliminated Players: {stats['eliminated_players']}")
        print(f"Completed Players: {stats['completed_players']}")
        print(f"Average Gate: {stats['average_gate']:.1f}")
        
        print("\n🏆 Top 10 Drop-off Gates:")
        sorted_dropoff = sorted(stats['dropoff_by_gate'].items(), key=lambda x: x[1], reverse=True)
        for gate, count in sorted_dropoff[:10]:
            if count > 0:
                print(f"Gate {gate}: {count} eliminations")
                
    finally:
        db.close()

def show_active_players():
    """Show all active players"""
    db = SessionLocal()
    try:
        players = get_active_players(db)
        print(f"\n🟢 Active Players ({len(players)}):")
        for player in players:
            username = player.username or f"Player{player.telegram_id}"
            print(f"• @{username} (ID: {player.telegram_id}) - Gate {player.current_gate}/100")
    finally:
        db.close()

def show_leaderboard(limit=20):
    """Show leaderboard"""
    db = SessionLocal()
    try:
        leaderboard = get_leaderboard(db, limit=limit)
        print(f"\n🏆 Top {len(leaderboard)} Players:")
        for i, player in enumerate(leaderboard, 1):
            username = player.username or f"Player{player.telegram_id}"
            status = "🟢" if player.game_state == GameState.ACTIVE else "🔴"
            print(f"{i:2d}. {status} @{username} - Gate {player.current_gate}/100")
    finally:
        db.close()

def eliminate_player_by_id(telegram_id):
    """Eliminate a specific player"""
    db = SessionLocal()
    try:
        player = db.query(Player).filter(Player.telegram_id == telegram_id).first()
        if not player:
            print(f"❌ Player with ID {telegram_id} not found")
            return
        
        eliminate_player(db, telegram_id, EliminationReason.WRONG_ANSWER)
        print(f"✅ Player {telegram_id} has been eliminated")
    finally:
        db.close()

def reset_all_games():
    """Reset all games globally"""
    db = SessionLocal()
    try:
        # Reset all players to eliminated state
        db.execute("UPDATE players SET game_state = 'eliminated', current_gate = 1")
        db.execute("UPDATE games SET status = 'failed'")
        db.commit()
        print("✅ All games have been reset")
    except Exception as e:
        print(f"❌ Error resetting games: {e}")
        db.rollback()
    finally:
        db.close()

def add_question(gate_number, question_text, option_a, option_b, option_c, option_d, correct_answer):
    """Add a new question"""
    db = SessionLocal()
    try:
        from app.crud import create_question
        
        question_data = {
            "gate_number": gate_number,
            "question_text": question_text,
            "option_a": option_a,
            "option_b": option_b,
            "option_c": option_c,
            "option_d": option_d,
            "correct_answer": correct_answer.upper()
        }
        
        question = QuestionCreate(**question_data)
        create_question(db, question)
        print(f"✅ Question for Gate {gate_number} added successfully")
    except Exception as e:
        print(f"❌ Error adding question: {e}")
    finally:
        db.close()

def list_questions():
    """List all questions"""
    db = SessionLocal()
    try:
        questions = db.query(Question).order_by(Question.gate_number).all()
        print(f"\n📝 Questions ({len(questions)} total):")
        for question in questions:
            print(f"Gate {question.gate_number}: {question.question_text[:50]}...")
    finally:
        db.close()

def export_questions(filename="questions_export.json"):
    """Export all questions to JSON file"""
    db = SessionLocal()
    try:
        questions = db.query(Question).order_by(Question.gate_number).all()
        questions_data = []
        
        for question in questions:
            questions_data.append({
                "gate_number": question.gate_number,
                "question_text": question.question_text,
                "option_a": question.option_a,
                "option_b": question.option_b,
                "option_c": question.option_c,
                "option_d": question.option_d,
                "correct_answer": question.correct_answer
            })
        
        with open(filename, 'w') as f:
            json.dump(questions_data, f, indent=2)
        
        print(f"✅ Questions exported to {filename}")
    finally:
        db.close()

def main():
    parser = argparse.ArgumentParser(description="Admin tools for 100 Gates to Freedom Bot")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Stats command
    subparsers.add_parser("stats", help="Show game statistics")
    
    # Players command
    subparsers.add_parser("players", help="Show active players")
    
    # Leaderboard command
    leaderboard_parser = subparsers.add_parser("leaderboard", help="Show leaderboard")
    leaderboard_parser.add_argument("--limit", type=int, default=20, help="Number of players to show")
    
    # Eliminate command
    eliminate_parser = subparsers.add_parser("eliminate", help="Eliminate a player")
    eliminate_parser.add_argument("telegram_id", type=int, help="Telegram ID of player to eliminate")
    
    # Reset command
    subparsers.add_parser("reset", help="Reset all games")
    
    # Questions commands
    subparsers.add_parser("list-questions", help="List all questions")
    subparsers.add_parser("export-questions", help="Export questions to JSON")
    
    # Add question command
    add_question_parser = subparsers.add_parser("add-question", help="Add a new question")
    add_question_parser.add_argument("gate_number", type=int, help="Gate number")
    add_question_parser.add_argument("question_text", help="Question text")
    add_question_parser.add_argument("option_a", help="Option A")
    add_question_parser.add_argument("option_b", help="Option B")
    add_question_parser.add_argument("option_c", help="Option C")
    add_question_parser.add_argument("option_d", help="Option D")
    add_question_parser.add_argument("correct_answer", help="Correct answer (A, B, C, or D)")
    
    args = parser.parse_args()
    
    if args.command == "stats":
        show_stats()
    elif args.command == "players":
        show_active_players()
    elif args.command == "leaderboard":
        show_leaderboard(args.limit)
    elif args.command == "eliminate":
        eliminate_player_by_id(args.telegram_id)
    elif args.command == "reset":
        reset_all_games()
    elif args.command == "list-questions":
        list_questions()
    elif args.command == "export-questions":
        export_questions()
    elif args.command == "add-question":
        add_question(
            args.gate_number,
            args.question_text,
            args.option_a,
            args.option_b,
            args.option_c,
            args.option_d,
            args.correct_answer
        )
    else:
        parser.print_help()

if __name__ == "__main__":
    main() 