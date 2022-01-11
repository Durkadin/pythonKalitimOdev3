
class WebPush:
  def __init__(self, Platform, optin, global_frequency_capping, start_date, end_date, language, push_type):
    self.Platform=Platform
    self.optin=bool(optin)
    self.global_frequency_capping=global_frequency_capping
    self.start_date=start_date
    self.end_date=end_date
    self.language=language
    self.push_type=push_type

    def send_push(self):
      print("Push Gönderildi!!!!")


    send_push()



class TriggerPush(WebPush):
        def __init__(self,trigger_page):
          self.trigger_page=trigger_page
          self.push_type=TriggerPush



        def send_push(self):
             print(" push type:"+self.push_type+" Gönderildi!!")


class BulkPush(WebPush):
        def __init__(self,send_date):
          self.send_date=int(send_date)
          self.push_type=BulkPush

        def send_push(self):
             print(" push type:"+self.push_type+" Gönderildi!!")



class SegmentPush(WebPush):
        def __init__(self,segment_name):
          self.segment_name=segment_name
          self.push_type=SegmentPush

        def send_push(self):
             print(" push type:"+self.push_type+" Gönderildi!!")


class PriceAlertPush(WebPush):
        def __init__(self,price_info, discount_rate):
          self.price_info=int(price_info)
          self.discount_rate=float(discount_rate)
          self.push_type=PriceAlertPush

        def send_push(self):
             print(" push type:"+self.push_type+" Gönderildi!!")

        def discountPrice(self):
          indirim = float(self.price_info*self.discount_rate)

          return indirim

class InstockPush(WebPush):
        def __init__(self,stock_info):
          self.stock_info=bool(False)
          self.push_type="InStockPush"

        def send_push(self):
             print(" push type:"+self.push_type+" Gönderildi!!")

        def stockUpdate(self):
            if self.stock_info == False:

                stock_info=True

                return stock_info

            if self.stock_info == True:

                stock_info=False

                return stock_info

