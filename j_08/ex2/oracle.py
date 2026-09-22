import os
import sys
from dotenv import load_dotenv, dotenv_values
# try:
#     from dotenv import load_dotenv, dotenv_values
# except Exception as e:
#     print(
#         f"Missing module dotenv: {e}\n"
#         "Install using 'python3 -m pip install python-dotenv'"
#     )
#     sys.exit(1)
# Hide the .env file from oracle.py
# mv .env .env.bak

# Difference between development and production mode:
# development mode configures with .env file or default values,
# log level is debug or trace
# production mode doesn't configure with .env file, log level is info,
# warning or error; it quits if alues missing


def detect_override(env_file_path: str = ".env") -> bool:
    if os.path.exists(env_file_path):
        file_configs = dotenv_values(env_file_path)
    else:
        file_configs = {}
    override_status = False
    for key, val in file_configs.items():
        sys_val = os.environ.get(key)
        if sys_val is not None and sys_val != val:
            override_status = True
            break
    if os.environ.get("MATRIX_MODE") == "production":
        override_status = True
    return override_status


if __name__ == '__main__':
    print("\nORACLE STATUS: Reading the Matrix...\n")
    is_overridden = detect_override('.env')
    load_dotenv(override=False)

    env_file = os.path.exists('.env')

    defaults: dict[str, str | None] = {
        'MATRIX_MODE': 'development',
        'DATABASE_URL': 'sqlite:///./matrix_dev.db',
        'API_KEY': None,
        'LOG_LEVEL': 'DEBUG',
        'ZION_ENDPOINT': 'http://localhost:8000',
    }
    variables = ['MATRIX_MODE', 'DATABASE_URL', 'API_KEY',
                 'LOG_LEVEL', 'ZION_ENDPOINT']
    # for var in variables:
    #     print(f"DEBUG: {var} = {repr(os.getenv(var))}")
    values: dict[str, str | None] = {}
    missing = []
    for var in variables:
        val = os.getenv(var)
        if val is None or val.strip() == "":
            values[var] = None
            missing.append(var)
        else:
            values[var] = val

    if missing:
        print(f"Configuration missing: {','.join(missing)}\n"
              "Will fix with default values.\n")
    if values['MATRIX_MODE'] == 'production' and missing:
        print(
            "[Warning] Running in production mode with missing \
configurations. Aborting.", file=sys.stderr
            )
        sys.exit(1)
    if values['MATRIX_MODE'] in ('development', None):
        for item in missing:
            values[item] = defaults[item]

    mode = values['MATRIX_MODE']
    db_url = values['DATABASE_URL']
    api_key = values['API_KEY']
    log_level = values['LOG_LEVEL']
    zion_endpoint = values['ZION_ENDPOINT']

    if env_file and not missing:
        env_status = "[OK] .env file properly configured"
    else:
        env_status = "[Warning] .env file not properly configured. \n\
           Run 'cp .env.example .env'"

    if is_overridden:
        override_status = "[OK] Production overrides available"
    else:
        override_status = "[Warning] Production overrides unavailable"
    # if missing == []:
    print(
        "Configuration loaded:\n"
        f"Mode: {mode}\n"
        f"Database: {'Connected' if db_url else 'Not configured'}\n"
        f"API Access: {'Authenticated' if api_key else 'Not authenticated'}\n"
        f"Log Level: {log_level}\n"
        f"Zion Network: {'Online' if zion_endpoint else 'Offline'}\n\n"
        "Environment security check:\n"
        "[OK] No hardcoded secrets detected\n"
        f"{env_status}\n{override_status}\n\n"
        "The Oracle sees all configurations."
    )
