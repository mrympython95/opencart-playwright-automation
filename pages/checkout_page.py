from playwright.sync_api import Page


class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page

        # Step 2: Billing Details
        self.txt_first_name = page.locator("#input-payment-firstname")
        self.txt_last_name = page.locator("#input-payment-lastname")
        self.txt_address = page.locator("#input-payment-address-1")
        self.txt_city = page.locator("#input-payment-city")
        self.txt_postcode = page.locator("#input-payment-postcode")
        self.drp_country = page.locator("#input-payment-country")
        self.drp_state = page.locator("#input-payment-zone")
        self.btn_continue_billing = page.locator("#button-payment-address")

        # Step 3: Delivery Details
        self.drp_delivery_address = page.locator(
            "select[name='address_id']"
        )
        self.btn_continue_delivery_address = page.locator(
            "#button-shipping-address"
        )

        # Step 4: Delivery Method
        self.radio_shipping_method = page.locator(
            "input[name='shipping_method']"
        )
        self.txt_order_comment = page.locator(
            "textarea[name='comment']"
        )
        self.btn_continue_shipping_method = page.locator(
            "#button-shipping-method"
        )

        # Step 5: Payment Method
        self.radio_payment_method = page.locator(
            "input[name='payment_method']"
        )
        self.txt_payment_comment = page.locator(
            "#collapse-payment-method textarea[name='comment']"
        )
        self.chk_terms = page.locator(
            "input[name='agree']"
        )
        self.btn_continue_payment_method = page.locator(
            "#button-payment-method"
        )

        # Step 6: Confirm Order
        self.lbl_total_price = page.locator(
            "tr", has_text="Total:"
        ).locator("td").last
        self.btn_confirm_order = page.locator(
            "#button-confirm"
        )

    def set_first_name(self, first_name: str):
        self.txt_first_name.fill(first_name)

    def set_last_name(self, last_name: str):
        self.txt_last_name.fill(last_name)

    def set_address(self, address: str):
        self.txt_address.fill(address)

    def set_city(self, city: str):
        self.txt_city.fill(city)

    def set_postcode(self, postcode: str):
        self.txt_postcode.fill(postcode)

    def select_country(self, country: str):
        self.drp_country.select_option(label=country)

    def select_state(self, state: str):
        self.drp_state.select_option(label=state)

    def click_continue(self):
        self.btn_continue_billing.click()


    def click_continue_delivery_address(self):
        self.btn_continue_delivery_address.click()

    def select_shipping_method(self):
        self.radio_shipping_method.check()

    def set_order_comment(self, comment: str):
        self.txt_order_comment.fill(comment)

    def click_continue_shipping_method(self):
        self.btn_continue_shipping_method.click()

    def select_payment_method(self):
        self.radio_payment_method.check()

    def set_payment_comment(self, comment: str):
        self.txt_payment_comment.fill(comment)


    def check_terms(self):
        self.chk_terms.check()

    def click_continue_payment_method(self):
        self.btn_continue_payment_method.click()

    def click_confirm_order(self):
        self.btn_confirm_order.click()