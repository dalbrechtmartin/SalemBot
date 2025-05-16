from datetime import datetime

def log_command_usage(command_name: str, user_id: str, user_nickname: str, user_lang: str) -> None:
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{current_time}] Commande {command_name} appelée par {user_nickname} ({user_id}) [{user_lang}]")
