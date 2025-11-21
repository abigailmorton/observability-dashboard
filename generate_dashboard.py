#!/usr/bin/env python3

from datetime import datetime
from zoneinfo import ZoneInfo
from jinja2 import Environment, FileSystemLoader
from data_sources.markets import fetch_markets
from data_sources.system import get_system_stats

def main():
    # Gather data
    markets = fetch_markets()
    system = get_system_stats()

    # Set up Jinja2 environment (loads templates from current directory)
    env = Environment(loader=FileSystemLoader("."))
    template = env.get_template("template.html")

    # Local time in US Eastern
    local_now = datetime.now(ZoneInfo("America/Chicago"))

    # Render template
    rendered = template.render(
        generated_at=local_now.strftime("%Y-%m-%d %H:%M:%S %Z"),
        markets=markets,
        system=system,
    )

    # Write to file
    output_path = "index.html"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(rendered)

    print(f"Dashboard written to {output_path}")

if __name__ == "__main__":
    main()

