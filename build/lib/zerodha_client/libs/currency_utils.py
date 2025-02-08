class CurrencyUtils:
    @classmethod
    def format_currencies(cls, amount_string: str) -> float:
        current_amount = amount_string.replace(",", "")
        current_amount = current_amount.replace("₹", "")
        return float(current_amount)
