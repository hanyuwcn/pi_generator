from footer import FooterMaker
import config
from utils import writer_tools
from system import logger
import traceback

class SpicesFooterMaker(FooterMaker):
    def make_footer(self, info):
        try:
            logger.info("Start making footer...")

            amount = info[config.QUOTE_TOTAL_AMOUNT]
            deposit_amount = info[config.DEPOSIT_HEADER]

            footer_total_price = self._get_footer_total_price(amount)
            footer_deposit = self._get_footer_deposit(amount)
            footer_packing = self._get_packing()
            footer_payment = self._get_footer_payment(deposit_amount)
            footer_port = self._get_footer_port()
            footer_delivery_time = self._get_footer_delivery_time()
            footer_destination = self._get_footer_destination()
            footer_insurance = self._get_insurance()
            footer_transportation = self._get_footer_transportation()

            logger.info("Footer successfully made.")

            footer = {config.INVOICE_TOTAL_PRICE_TITLE: footer_total_price,
                    config.DEPOSIT_HEADER: footer_deposit,
                    config.INVOICE_PACKING_TITLE: footer_packing,
                    config.INVOICE_PAYMENT_TITLE: footer_payment,
                    config.INVOICE_PORT_TITLE: footer_port,
                    config.INVOICE_DELIVERY_TIME_TITLE: footer_delivery_time,
                    config.INVOICE_DESTINATION_TITLE: footer_destination,
                    config.INVOICE_INSURANCE_TITLE: footer_insurance,
                    config.INVOICE_TRANSPORTATION_TITLE: footer_transportation}
            ## (TODO) set this dictionary static into configurations

            return footer
        except Exception as e:
            logger.error("Application collapse when making the footer!")
            logger.error(f"{e.__class__}, occur_error: {traceback.format_exc()}")

    @staticmethod
    def _get_footer_total_price(amount):
        return "{total_price_title}: {currency}{amount} FOB {port}".format(
            total_price_title=config.INVOICE_TOTAL_PRICE_TITLE,
            currency=config.CURRENCY,
            amount=amount,
            port=config.LOADING_PORT)

    @staticmethod
    def _get_footer_deposit(amount):
        return "{deposit_percentage} deposit={deposit_amount} {currency}".format(
            deposit_percentage=str(config.DEPOSIT_PERCENTAGE*100) + "%",
            deposit_amount=writer_tools.get_deposit(amount, rounding=False),
            currency=config.CURRENCY)

    @staticmethod
    def _get_packing():
        return "{packing_title}: {packing_term}".format(
            packing_title=config.INVOICE_PACKING_TITLE,
            packing_term=config.INVOICE_PACKING_TERM)


    @staticmethod
    def _get_footer_payment(deposit_amount):
        return  "{payment_title}: {payment_rule}".format(
            payment_title=config.INVOICE_PAYMENT_TITLE,
            payment_rule=config.INVOICE_PAYMENT_RULE)

    @staticmethod
    def _get_footer_port():
        return "{port_title}: {port}".format(port_title=config.INVOICE_PORT_TITLE,
                                             port=config.LOADING_PORT)

    @staticmethod
    def _get_footer_delivery_time():
        return "{delivery_time_title}: Within {delivery_time} {delivery_time_postfix}".format(
            delivery_time_title=config.INVOICE_DELIVERY_TIME_TITLE,
            delivery_time=str(config.DELIVERY_TIME),
            delivery_time_postfix=config.INVOICE_DELIVERY_TIME_CONTENT)

    @staticmethod
    def _get_footer_destination():
        return "{destination_port_title}: {port}".format(
            destination_port_title=config.INVOICE_DESTINATION_TITLE,
            port=config.DESTINATION_PORT)

    @staticmethod
    def _get_insurance():
        return "{insurance_title}: {insurance_term}".format(
            insurance_title=config.INVOICE_INSURANCE_TITLE,
            insurance_term=config.INVOICE_INSURANCE_TERM)

    @staticmethod
    def _get_footer_transportation():
        return "{transportation_title}: {transportation_content}".format(
            transportation_title=config.INVOICE_TRANSPORTATION_TITLE,
            transportation_content=config.INVOICE_TRANSPORTATION_CONTENT)

