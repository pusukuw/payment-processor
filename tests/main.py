import logging
import os
from payment_processor.config import Config
from payment_processor.payment_gateway import PaymentGateway
from payment_processor.transaction import Transaction

class PaymentProcessor:
    def __init__(self, config: Config):
        self.config = config
        self.payment_gateway = PaymentGateway(self.config.payment_gateway_url)

    def process_transaction(self, transaction: Transaction):
        try:
            self.payment_gateway.charge_card(transaction.card_number, transaction.amount)
            transaction.status = "success"
            logging.info(f"Transaction {transaction.id} processed successfully")
            return transaction
        except Exception as e:
            transaction.status = "failed"
            logging.error(f"Error processing transaction {transaction.id}: {str(e)}")
            return transaction

def main():
    logging.basicConfig(level=logging.INFO)
    config = Config(os.environ["CONFIG_FILE"])
    payment_processor = PaymentProcessor(config)
    transaction = Transaction(1, "1234-5678-9012-3456", 10.99)
    processed_transaction = payment_processor.process_transaction(transaction)
    print(processed_transaction.__dict__)

if __name__ == "__main__":
    main()