import datetime
class BankAccount:
    def __init__(self) -> None:
        self.__balance = 0.0
        self.__ownerName = "Defult"
        self.__ownerId = 9860012145857445
        self.__ownerPhoneNumber = "998#########"
        self.__paymentHistory = [{
            "Defult":{
                "to":"defult",
            "when":"defult",
            "summa":"defult"
            }
        }]
    def GetAccountInfo(self):
        return f"""
balance             {self.__balance}
karta egasi         {self.__ownerName}
ownerId             {self.__ownerId}
ownerPhoneNumber    {self.__ownerPhoneNumber}
paymentHistory      {self.__paymentHistory}"""
    def GetPaymentHistory(self):
        return self.__paymentHistory
    def GetOwnerId(self):
        return self.__ownerId
    def GetOwnerName(self):
        return self.__ownerName
    def GetBalance(self):
        return self.__balance
    def SetName(self, newism : str):
        if isinstance(newism, str):
            self.__ownerName = newism
        else:
            raise ValueError("AKA ismni xato kiritdingizov")
    def SetPhoneNumber(self, newphonenumber : str):
        truephones = ["99899", "99898", "99833", "99850", "99895"]
        if newphonenumber[:5] in truephones and len(newphonenumber) == 12:
            self.__ownerPhoneNumber = newphonenumber
        else:
            raise ValueError("AKA nummerni xato kiritdingizov")
    def  AddBalance(self, plusbalance : float):
        if isinstance(plusbalance, (int, float)) and plusbalance > 0:
            self.__balance += plusbalance
        else:
            raise ValueError("AKA pulni xato kiritdingizov")
    def  WithdrawBalance(self, minusbalance: float):
        if isinstance(minusbalance, (int, float)) and self.__balance - minusbalance > 0:
            self.__balance -= minusbalance
            return True
        else:
            return False
    def Transfer(self, qabul_qiluvchi : "BankAccount", summa : float):
        if isinstance(qabul_qiluvchi, BankAccount) and isinstance(summa,(int,float)):
            self.WithdrawBalance(summa)
            qabul_qiluvchi.AddBalance(summa)
            if self.__paymentHistory[0].key == "Defult":
                self.__paymentHistory.remove(self.__paymentHistory[0])
            self.__paymentHistory.append({
                datetime.now() : {
                    "to"    : qabul_qiluvchi.__ownerId,
                    "when"  : datetime.now(),
                    "summa" : summa
                }
            })
Ahror = BankAccount()
print(Ahror.GetAccountInfo())