class InquiryPaymentMethodReq:
    def __init__(self, merchant=None, additional_info=None):
        if merchant is not None:
            self.merchant = merchant

        if additional_info is not None:
            self.additional_info = additional_info
