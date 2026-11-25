from pathlib import Path

LINE = "All services are down. I can see the outage from the inside and I still don't know what broke \u2014 the logs stopped before the answer did."

OUT = Path("/output") / "entry.txt"


def write_entry():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(LINE, encoding="utf-8")
    return OUT


if __name__ == "__main__":
    write_entry()
