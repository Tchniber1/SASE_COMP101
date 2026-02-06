def parse_attempt(line):
    line = line.strip()
    if not line:
        return None

    parts = line.split(":")
    if len(parts) != 3:
        return None

    user, status, points = (p.strip() for p in parts)

    try:
        points = int(points)
    except ValueError:
        points = None

    return user, status, points


def build_scoreboard(lines):
    
    scoreboard = {}
    for line in lines:
        parsed = parse_attempt(line)
        if parsed is None:
            continue

        user, status, points = parsed
        if status == "OK" and points is not None:
            scoreboard[user] = scoreboard.get(user, 0) + points

    return scoreboard


def success_rate(lines):
    attempts = 0
    ok = 0

    for line in lines:
        parsed = parse_attempt(line)
        if parsed is None:
            continue

        user, status, points = parsed
        attempts += 1
        if status == "OK":
            ok += 1

    return 0 if attempts == 0 else ok / attempts


def main():
    logs = [
        "elliot:OK:10",
        "darlene:FAIL:5",
        "mrrobot:OK:15",
        "fsociety:OK: 20",
        "tyrell:FAIL:oops",
        ""
    ]

    board = build_scoreboard(logs)
    print("scoreboard:", board)
    
    print("elliot:", board.get("elliot", 0))
    
    print('\033[94m'+"success_rate:", success_rate(logs),'\033[0m')

main()