import time
from utilities.BaseClass import TestBaseClass
from PageObjects.HomePage import HomePage
from PageObjects.CheckOutPage import CardPage
from PageObjects.ConfirmPage import ConfirmPage
from PageObjects.SuccessPage import SuccessPageClass

# @pytest.mark.usefixtures("setup") (we have knowledge of fixture now)
class TestEndToEnd(TestBaseClass):

    def test_EndToEnd(self):

        logs = self.getLogger()

        # Launch the browser
        # Click on shope
        shope_ele = HomePage(self.driver)
        products = shope_ele.shopItems()
        # Get the list of the card elements
        # products = CardPage(self.driver).cardItems() (
        # '''Not required because we already form connection between them
        # list_ele = []
        # for product in products:
        #     print(product.text)
        #     list_ele.append(product.text)
        # print(list_ele)
        # str = ""
        # for i in list_ele:
        #     str += i
        # return str
        logs.info("Print the product list" )
            # logs.info("Product list" + product.text)
        """ Add the mobile in cart to process ahead"""
        add_cart = CardPage(self.driver).addTocardEle()
        add_cart.click()

        """Click on Check Out Button"""
        checkOUT = CardPage(self.driver)
        checkOUT.CheckOutEle()
        # check_button.click()
        # text_box = checkOUT.CheckOutEle()
        # text_box.send_keys("Ind")
        text_box = ConfirmPage(self.driver).CountryEle()
        text_box.send_keys('Ind')
       # checkout_ele = CardPage(self.driver).CheckOutEle()
        # Send_ele = checkout_ele.Confirm_Page().ConfirmEle()
        # Send_ele.send_key("Ind")
        # Confirm_page = checkout_ele.confirm_ele
        # Confirm_page.ConfirmEle.send_keys("ind")
        # # country_ele = confirm_ele
        # country_ele.send_keys("ind")

        # wait = WebDriverWait(self.driver, 10)

        # time.sleep(6)
        # india_ele = ConfirmPage(self.driver).IndiaEle()
        # india_ele.click()
        """Invoke from Base Class"""
        self.VerifyingEle('India')

        checkBox = ConfirmPage(self.driver).CheckBoxEle()
        checkBox.click()

        purchase_ele = ConfirmPage(self.driver).SubmitEle()
        purchase_ele.click()

        successText = SuccessPageClass(self.driver).SuccessTextCapture().text
        logs.info("print cofirm" + successText)
        assert "Success! Thank you!" in successText
        print(self.driver.title)
        # Close the browser
        # driver.close()











