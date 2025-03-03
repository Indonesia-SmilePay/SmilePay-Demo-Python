class InquiryBalanceReq:
    def __init__(self, accountNo=None, balanceTypes=None, additionalInfo=None):
        if accountNo is not None:
            self.accountNo = accountNo

        if balanceTypes is not None:
            self.balanceTypes = balanceTypes

        if additionalInfo is not None:
            self.additionalInfo = additionalInfo
