from login.models import Hospital


# hospital的service
class HosService:
    def getHospitalByNum(self, num):
        res = Hospital.objects.filter(hostpital_number=num)
        if not res:
            return 0, ""
        else:
            return 1, res
