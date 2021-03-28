import pyupbit
import rumps
import time


class CheckPrice(rumps.App):

    @rumps.clicked("About")
    def about(self, _):
        rumps.alert("hello")

    """
    this function find that price is now market price.
    then, return price
    """
    @rumps.clicked("balance")
    def money(self, _):
    # 비공개 코드 

    @rumps.timer(30)
    def NowPrice(self, _):
         
        HumPrice = pyupbit.get_current_price("KRW-HUM")
        MedPrice = pyupbit.get_current_price("KRW-BTC")

        self.title = f"BTC KRW - {MedPrice}"



if __name__ == "__main__":

    HumAndMed = CheckPrice("...")
    HumAndMed.run()
