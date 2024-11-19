import pushbullet
from twilio.rest import Client
from win10toast import ToastNotifier

class Notification:
    def __init__(self):
        self.pb = pushbullet.Pushbullet("YOUR_PUSHBULLET_API_KEY")
        self.account_sid = "YOUR_TWILIO_ACCOUNT_SID"
        self.auth_token = "YOUR_TWILIO_AUTH_TOKEN"
        self.client = Client(self.account_sid, self.auth_token)
        self.toaster = ToastNotifier()

    def trigger_buy_notification(self):
        self.toaster.show_toast("Buy Point Alert!", "Price reached buy level.", duration=10)
        self.pb.push_note("Buy Point Alert!", "Price is at your buy point!")
        self.client.calls.create(url='http://demo.twilio.com/docs/voice.xml', to='YOUR_PHONE_NUMBER', from_='YOUR_TWILIO_NUMBER')

    def trigger_sell_notification(self):
        self.toaster.show_toast("Sell Point Alert!", "Price reached sell level.", duration=10)
        self.pb.push_note("Sell Point Alert!", "Price is at your sell point!")
        self.client.calls.create(url='http://demo.twilio.com/docs/voice.xml', to='YOUR_PHONE_NUMBER', from_='YOUR_TWILIO_NUMBER')
