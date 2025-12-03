import logging
from typing import Dict, List, Optional

def get_logger(name: str) -> logging.Logger:
    """Return a logger instance with a specified name."""
    return logging.getLogger(name)

def validate_payment_data(data: Dict[str, str]) -> bool:
    """Validate payment data."""
    required_fields = ['card_number', 'expiration_date', 'cvv']
    for field in required_fields:
        if field not in data or not data[field]:
            return False
    return True

def calculate_total(subtotal: float, tax_rate: float) -> float:
    """Calculate the total amount including tax."""
    return subtotal + (subtotal * tax_rate / 100)

def get_payment_status(payment_id: int) -> Optional[str]:
    """Get the payment status by its ID."""
    # Simulate a database query
    payment_statuses = {
        1: 'pending',
        2: 'processing',
        3: 'failed',
        4: 'success'
    }
    return payment_statuses.get(payment_id)