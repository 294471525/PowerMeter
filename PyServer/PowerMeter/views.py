import csv
import time
from collections import Iterable

from django.core import serializers
from django.http import HttpResponse
from django.http import JsonResponse

from PowerMeter import models
from PowerMeter.zwaveController.PowerData import PowerData

ONE_UNDEAD_THREAD_FLAG = False
network = object
zwcontroller = object


def enable_thread(request):
    import threading
    from PowerMeter.zwaveController import controller
    global network
    global zwcontroller
    network = controller.network
    zwcontroller = controller.controller
    threading.Thread(target=record_data(network.nodes), daemon=True).start()
    return HttpResponse("it works")


def record_data(nodes):
    while True:
        for i in nodes:
            if i >= 2:
                powers = nodes[i].get_values(label='Power')
                voltages = nodes[i].get_values(label='Voltage')
                currents = nodes[i].get_values(label='Current')
                powerdata = PowerData(None, None, None, None)
                for power in powers.values():
                    powerdata.power = power.data
                for voltage in voltages.values():
                    powerdata.voltage = voltage.data
                for current in currents.values():
                    powerdata.current = current.data
                    current.refresh()
                print(powerdata.voltage)
                models.data.objects.create(nodeId=i, power=powerdata.power, voltage=powerdata.voltage,
                                           current=powerdata.current)
            time.sleep(1.0)


def get_data(request):
    if request.method == "GET":
        id = request.GET.get("id")
        if id is None:
            result = models.data.objects.last()
        else:
            result = models.data.objects.filter(nodeId=id).last()
        if not isinstance(result, Iterable):
            result = [result, ]
        result = serializers.serialize("json", result)
        return JsonResponse({"data": result})


def add_node(request):
    if request.method == "GET":
        size = len(network.nodes)
        list = models.nodes.objects.values_list('nodeId', flat='true')
        if zwcontroller.add_node():
            for i in range(0, 30):
                if len(network.nodes) > size:
                    for node in network.nodes:
                        if node not in list:
                            models.nodes.objects.create(nodeId=node.id, name="NONE")
                            return HttpResponse("Success")
                time.sleep(1)
        return HttpResponse("Add node fail")


def deleteNode(request):
    if request.method == "GET":
        size = len(network.nodes)
        arr = []
        for node in network.nodes:
            arr.append(node)
        if zwcontroller.remove_node():
            for i in range(0, 30):
                if len(network.nodes) < size:
                    for id in arr:
                        if id not in network.nodes:
                            models.nodes.objects.get(nodeId=id).delete()
                            return HttpResponse("Success")
            time.sleep(30)
        return HttpResponse("Remove node fail")


def edit_node(request):
    if request.method == "GET":
        nodeId = request.GET.get('nodeId')
        name = request.GET.get('name')
        models.nodes.objects.filter(nodeId=nodeId).update(name=name)
        return HttpResponse("Success")


def nodelist(request):
    if request.method == "GET":
        result = models.nodes.objects.all()
        if not isinstance(result, Iterable):
            result = [result, ]
        result = serializers.serialize("json", result)
        return JsonResponse({"nodeList": result})


def download(request):
    if request.method == "GET":
        startTime = request.GET.get("startTime")
        endTime = request.GET.get("endTime")
        nodeId = request.GET.get("id")
        nodeData = HttpResponse(content_type='text/csv')
        nodeData['Content-Disposition'] = 'attachment; filename="powerData.csv"'
        createCSV(startTime, endTime, nodeId, nodeData)
        return nodeData


def createCSV(startTime, endTime, nodeId, nodeData):
    writer = csv.writer(nodeData)
    writer.writerow(['nodeID', 'power', 'current', 'vlotage', 'dateTime'])
    data = models.data.objects.filter(dateTime__range=(startTime, endTime)).filter(nodeId=nodeId)
    for d in data:
        writer.writerow([d.nodeId, d.power, d.current, d.voltage, d.dateTime])
