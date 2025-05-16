def log_command_usage(command_name: str, user_id: str, user_nickname: str, user_lang: str) -> None:
    print(f"Commande {command_name} appelée par {user_nickname} ({user_id}) [{user_lang}]")
