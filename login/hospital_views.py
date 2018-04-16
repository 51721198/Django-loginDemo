from django.http import HttpResponse
from django.core import serializers

from login.models import Hospital

import json

from login.service.hospital_service import HosService

hospitalservice = HosService()

class HospitalViews:
    def addHospital(self, request):
        if request.POST:
            hospitalnumber = request.POST['hospitalNumber']
            hospitalname = request.POST['hospitalName']
            hospitalphone = request.POST['hospitalPhone']
            hospitaladdress = request.POST['hospitalAddress']

            if not str.isdigit(hospitalnumber):
                return HttpResponse('医院编号必须为数字')

            code, hos = hospitalservice.getHospitalByNum(int(hospitalnumber))
            if code != 0:
                return HttpResponse('医院已经存在')

            Hospital.objects.create(hostpital_number=hospitalnumber,
                                    hospital_name=hospitalname,
                                    hospital_phone=hospitalphone,
                                    hospital_address=hospitaladdress)

    def getOneHospital(self, request, parm):
        id = int(parm)
        code, hos = hospitalservice.getHospitalByNum(id)
        if code == 0:
            return HttpResponse("无此医院")
        else:
            return HttpResponse(serializers.serialize("json", hos, ensure_ascii=False))

    def getAllHospitals(self, request):
        list = Hospital.objects.all()
        if list:
            return HttpResponse(serializers.serialize("json", list, ensure_ascii=False))
        else:
            return HttpResponse('没有数据')
