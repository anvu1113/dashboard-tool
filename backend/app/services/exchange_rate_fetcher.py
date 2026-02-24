import httpx
import xml.etree.ElementTree as ET
from typing import List, Dict
from datetime import datetime
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession


class ExchangeRateFetcher:
    """Service to fetch and update exchange rates from Vietcombank"""
    
    VIETCOMBANK_API = "https://portal.vietcombank.com.vn/Usercontrols/TVPortal.TyGia/pXML.aspx"
    
    async def fetch_rates(self) -> List[Dict]:
        """Fetch exchange rates from Vietcombank XML API"""
        print(f"[{datetime.now()}] Fetching exchange rates from Vietcombank...")
        
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.get(self.VIETCOMBANK_API)
            response.raise_for_status()
            
            # Parse XML
            root = ET.fromstring(response.text)
            rates = []
            
            for exrate in root.findall('.//Exrate'):
                currency_code = exrate.get('CurrencyCode', '').strip()
                currency_name = exrate.get('CurrencyName', '').strip()
                
                # Clean and parse rates
                buy = exrate.get('Buy', '').replace(',', '').replace('-', '').strip()
                transfer = exrate.get('Transfer', '').replace(',', '').strip()
                sell = exrate.get('Sell', '').replace(',', '').strip()
                
                if currency_code:  # Only add if currency_code exists
                    rates.append({
                        'currency_code': currency_code,
                        'currency_name': currency_name,
                        'buy_rate': float(buy) if buy else None,
                        'transfer_rate': float(transfer) if transfer else None,
                        'sell_rate': float(sell) if sell else None,
                    })
            
            print(f"✓ Fetched {len(rates)} exchange rates")
            return rates
    
    async def update_database(self, session: AsyncSession, rates: List[Dict]):
        """Update or insert rates into database"""
        from app.models.currency_rate import CurrencyRate
        
        updated_count = 0
        created_count = 0
        
        for rate_data in rates:
            # Check if exists
            query = select(CurrencyRate).where(
                CurrencyRate.currency_code == rate_data['currency_code']
            )
            result = await session.exec(query)
            existing = result.first()
            
            if existing:
                # Update existing
                existing.currency_name = rate_data['currency_name']
                existing.buy_rate = rate_data['buy_rate']
                existing.transfer_rate = rate_data['transfer_rate']
                existing.sell_rate = rate_data['sell_rate']
                existing.updated_at = datetime.utcnow()
                session.add(existing)
                updated_count += 1
            else:
                # Insert new
                new_rate = CurrencyRate(**rate_data)
                session.add(new_rate)
                created_count += 1
        
        await session.commit()
        print(f"✓ Database updated: {created_count} created, {updated_count} updated")


# Singleton instance
exchange_rate_fetcher = ExchangeRateFetcher()
