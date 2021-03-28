import pyupbit
import rumps
import time



about = """
    비트코인 가격을 알려주는 상태바입니다.
    추가적인 기능을 원한다면 jiungdev@gmail.com 으로 연락주세요.
    """

class CheckPrice(rumps.App):

    @rumps.clicked("About")
    def about(self, _):
        rumps.alert(about)

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
