"""
Daily script to update exchange rates from Vietcombank
Run this script via cron: 0 8 * * * cd /path/to/backend && python update_exchange_rates.py
"""

import asyncio
import sys
from datetime import datetime
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from app.db import engine
from app.services.exchange_rate_fetcher import exchange_rate_fetcher
from sqlmodel.ext.asyncio.session import AsyncSession


async def main():
    print("=" * 60)
    print(f"[{datetime.now()}] Starting exchange rate update...")
    print("=" * 60)
    
    async with AsyncSession(engine) as session:
        try:
            # Fetch rates from Vietcombank
            rates = await exchange_rate_fetcher.fetch_rates()
            
            # Update database
            await exchange_rate_fetcher.update_database(session, rates)
            
            print("=" * 60)
            print(f"[{datetime.now()}] ✓ Exchange rates updated successfully!")
            print("=" * 60)
            
        except Exception as e:
            print("=" * 60)
            print(f"[{datetime.now()}] ✗ Error updating exchange rates:")
            print(f"  {type(e).__name__}: {e}")
            print("=" * 60)
            raise


if __name__ == "__main__":
    asyncio.run(main())
