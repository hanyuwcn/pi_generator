from footer import FooterMaker
import config

class BAGFilterMachineFooterMaker(FooterMaker):
    def make_footer(self, info):
        amount = info[config.QUOTE_TOTAL_AMOUNT]
        deposit_amount = info[config.DEPOSIT_HEADER]

        footer_delivery = self._get_footer_delivery(amount)
        footer_payment = self._get_footer_payment(deposit_amount)
        footer_port = self._get_footer_port()
        footer_producing_time = self._get_footer_producing_time()
        footer_destination = self._get_footer_destination()
        footer_transportation = self._get_footer_transportation()

        return {config.INVOICE_DELIVERY: footer_delivery,
                config.INVOICE_PAYMENT: footer_payment,
                config.INVOICE_PORT: footer_port,
                config.INVOICE_PRODUCING_TIME: footer_producing_time,
                config.INVOICE_DESTINATION: footer_destination,
                config.INVOICE_TRANSPORTATION: footer_transportation}

    @staticmethod
    def _get_footer_delivery(amount):
        return "{delivery_title}: {currency}{amount} FOB {port}".format(delivery_title=config.INVOICE_DELIVERY, currency=config.CURRENCY, amount=amount, port=config.LOADING_PORT)

    @staticmethod
    def _get_footer_payment(deposit_amount):
        return  "{payment_title}: {deposit_amount} {currency} {payment_postfix}".format(payment_title=config.INVOICE_PAYMENT, deposit_amount=deposit_amount, currency=config.CURRENCY, payment_postfix=config.INVOICE_PAYMENT_CONTENT)

    @staticmethod
    def _get_footer_port():
        return "{port_title}: {port}".format(port_title=config.INVOICE_PORT, port=config.LOADING_PORT)

    @staticmethod
    def _get_footer_producing_time():
        return "{producing_time_title}: {producing_time} {producing_time_postfix}".format(producing_time_title=config.INVOICE_PRODUCING_TIME, producing_time=str(config.PRODUCING_TIME), producing_time_postfix=config.INVOICE_PRODUCING_TIME_CONTENT)

    @staticmethod
    def _get_footer_destination():
        return "{destination_port_title}: {port}".format(destination_port_title=config.INVOICE_DESTINATION, port=config.DESTINATION_PORT)

    @staticmethod
    def _get_footer_transportation():
        return "{transportation_title}: {transportation_content}".format(transportation_title=config.INVOICE_TRANSPORTATION, transportation_content=config.INVOICE_TRANSPORTATION_CONTENT)

