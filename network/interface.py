from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from orca_nw_lib.interface import (
    get_interface,
    config_interface,
)
from orca_nw_lib.common import Speed, PortFec

@api_view(["GET", "PUT"])
def device_interfaces_list(request):
    result = []
    http_status = True
    if request.method == "GET":
        device_ip = request.GET.get("mgt_ip", "")
        if not device_ip:
            return Response(
                {"status": "Required field device mgt_ip not found."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        intfc_name = request.GET.get("intfc_name", "")
        data = get_interface(device_ip, intfc_name)
        return JsonResponse(data, safe=False)

    elif request.method == "PUT":
        req_data_list = (
            request.data if isinstance(request.data, list) else [request.data]
        )
        for req_data in req_data_list:
            device_ip = req_data.get("mgt_ip", "")
            if not device_ip:
                return Response(
                    {"status": "Required field device mgt_ip not found."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            if not req_data.get("name"):
                return Response(
                    {"status": "Required field name not found."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            try:
                config_interface(
                    device_ip=device_ip,
                    intfc_name=req_data.get("name"),
                    loopback=req_data.get("loopback"),
                    enable=True
                    if str(req_data.get("enabled")).lower() == "true"
                    else False
                    if str(req_data.get("enabled")).lower() == "false"
                    else None,
                    mtu=int(req_data.get("mtu")) if "mtu" in req_data else None,
                    description=req_data.get("description"),
                    fec=PortFec.get_enum_from_str(req_data.get("fec")),
                    speed=Speed.get_enum_from_str(req_data.get("speed")),
                )

                result.append(f"{request.method} request successful :\n {req_data}")
                http_status = http_status and True
            except Exception as err:
                result.append(
                    f"{request.method} request failed :\n {req_data} \n {str(err)}"
                )
                http_status = http_status and False

    return Response(
        {"result": result},
        status=status.HTTP_200_OK
        if http_status
        else status.HTTP_500_INTERNAL_SERVER_ERROR,
    )