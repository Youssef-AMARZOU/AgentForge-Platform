#!/usr/bin/env python
"""
Example: Run Streamlit Dashboard
Run with: streamlit run examples/dashboard_demo.py
Or: python examples/dashboard_demo.py
"""

import subprocess
import sys
from pathlib import Path


def main():
    """Launch the Streamlit dashboard."""
    dashboard_path = Path(__file__).parent.parent / "dashboard" / "app.py"

    if not dashboard_path.exists():
        print(f"Dashboard not found at: {dashboard_path}")
        return

    print("=" * 60)
    print("LAUNCHING STREAMLIT DASHBOARD")
    print("=" * 60)
    print(f"Dashboard: {dashboard_path}")
    print("\nThe dashboard will open in your browser at http://localhost:8501")
    print("Press Ctrl+C to stop the server\n")

    try:
        subprocess.run([
            sys.executable, "-m", "streamlit", "run",
            str(dashboard_path),
            "--server.headless", "false",
            "--browser.gatherUsageStats", "false"
        ])
    except KeyboardInterrupt:
        print("\nDashboard stopped.")
    except Exception as e:
        print(f"Error launching dashboard: {e}")
        print("\nAlternatively, run directly:")
        print(f"  streamlit run {dashboard_path}")


if __name__ == "__main__":
    main()