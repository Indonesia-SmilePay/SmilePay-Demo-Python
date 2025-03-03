class InquiryAccountReq:
    def __init__(self, merchant=None, paymentMethod=None, accountNo=None, holderName=None, additionalInfo=None):
        if merchant is not None:
            self.merchant = merchant

        if paymentMethod is not None:
            self.paymentMethod = paymentMethod

        if accountNo is not None:
            self.accountNo = accountNo

        if holderName is not None:
            self.holderName = holderName

        if additionalInfo is not None:
            self.additionalInfo = additionalInfo
