class InquiryStatusReq:
    def __init__(self, tradeType=None, orderNo=None, tradeNo=None):
        if tradeType is not None:
            self.tradeType = tradeType

        if orderNo is not None:
            self.orderNo = orderNo

        if tradeNo is not None:
            self.tradeNo = tradeNo
