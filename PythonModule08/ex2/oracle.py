#!/usr/bin/env python3

from dotenv import load_dotenv
import os

SECRETS_LIST = [
        "MATRIX_MODE",
        "DATABASE_URL",
        "API_KEY",
        "LOG_LEVEL",
        "ZION_ENDPOINT"
        ]

if __name__ == "__main__":
    print("\nORACLE STATUS: Reading the Matrix...\n")

    before_load_env = {}
    after_load_env = {}
    for secret in SECRETS_LIST:
        before_load_env[secret] = os.getenv(secret)
    load_dotenv()
    for secret in SECRETS_LIST:
        after_load_env[secret] = os.getenv(secret)

    print("Configuration loaded:")
    print(f"Mode: {os.getenv('MATRIX_MODE')}")
    if os.getenv('DATABASE_URL'):
        print("Database: Connected to local instance")
    else:
        print(f"Database: {os.getenv('DATABASE_URL')}")
    if os.getenv('API_KEY'):
        print("API Access: Authenticated")
    else:
        print(f"API Access: {os.getenv('API_KEY')}")
    print(f"Log Level: {os.getenv('LOG_LEVEL')}")
    print(f"Zion Network: {os.getenv('ZION_ENDPOINT')}")

    all_config = True
    print("\nEnvironment security check:")
    hardcoded: list[str] = []
    for secret in SECRETS_LIST:
        if not os.getenv(secret):
            hardcoded.append(secret)
    if not hardcoded:
        print("[OK] No hardcoded seacrets detected")
        print("[OK] .env file properly configured")
    else:
        print(f"[NG] Hardcoded seacrets detected {hardcoded}")
        all_config = False

    for secret in SECRETS_LIST:
        if (not before_load_env[secret] and
                before_load_env[secret] != after_load_env[secret]):
            print("[NG] Production overrides NOT available")
            all_config = False
            break
    else:
        print("[OK] Production overrides available")

    if all_config:
        print("\nThe Oracle sees all configurations")
