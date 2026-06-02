#!/usr/bin/env python3
"""
PSN Account ID Lookup Script

Retrieves the account ID (and other profile info) from a PSN username.

Prerequisites:
  1. Install the library:  pip install psnawp
  2. Get your NPSSO token:
     - Log into https://store.playstation.com in your browser
     - Visit: https://ca.account.sony.com/api/v1/ssocookie
     - Copy the "npsso" value from the JSON response
     - Set it as an environment variable:  export NPSSO="your_token_here"

Usage:
  python psn_lookup.py                  # uses default username Beqk3101
  python psn_lookup.py SomeOtherUser    # lookup a different username
"""

import base64
import os
import sys

try:
    from psnawp_api import PSNAWP
except ImportError:
    print("Error: psnawp is not installed.")
    print("Install it with:  pip install psnawp")
    sys.exit(1)


def get_psn_account_id(username: str) -> dict:
    """Look up a PSN user's account ID and profile info by username."""
    npsso = os.environ.get("NPSSO")
    if not npsso:
        print("Error: NPSSO token not found.")
        print("Set it as an environment variable:")
        print('  export NPSSO="your_npsso_token_here"')
        print()
        print("How to get your NPSSO token:")
        print("  1. Log into https://store.playstation.com")
        print("  2. Visit https://ca.account.sony.com/api/v1/ssocookie")
        print('  3. Copy the "npsso" value from the JSON response')
        sys.exit(1)

    psnawp = PSNAWP(npsso)
    user = psnawp.user(online_id=username)

    # Extract account info
    account_id_int = int(user.account_id)
    account_id_b64 = base64.b64encode(account_id_int.to_bytes(8, "little")).decode()

    account_info = {
        "online_id": user.online_id,
        "account_id": user.account_id,
        "account_id_base64": account_id_b64,
        "region": getattr(user, "region", "N/A"),
        "avatar_url": getattr(user, "avatar_url", "N/A"),
    }
    return account_info


def main():
    username = sys.argv[1] if len(sys.argv) > 1 else "Beqk3101"

    print(f"Looking up PSN user: {username}")
    print("-" * 40)

    info = get_psn_account_id(username)

    print(f"Online ID:       {info['online_id']}")
    print(f"Account ID:      {info['account_id']}")
    print(f"Account ID (b64): {info['account_id_base64']}")
    print(f"Region:          {info['region']}")
    print(f"Avatar URL:      {info['avatar_url']}")


if __name__ == "__main__":
    main()
