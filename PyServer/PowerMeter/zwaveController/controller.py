import logging
import sys

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger('openzwave')

from openzwave.controller import ZWaveController
from openzwave.network import ZWaveNetwork
from openzwave.option import ZWaveOption
import time
import six

if six.PY3:
    from pydispatch import dispatcher
else:
    from louie import dispatcher

device = "/dev/ttyACM0"
log = "None"

# Define some manager options
options = ZWaveOption(device, \
                      config_path="/root/venv3/lib/python3.7/site-packages/python_openzwave/ozw_config", \
                      user_path=".", cmd_line="")
options.set_log_file("OZW_Log.log")
options.set_append_log_file(False)
options.set_console_output(True)
options.set_save_log_level(log)
options.set_logging(True)
options.lock()


def louie_network_started(network):
    print("Hello from network : I'm started : homeid {:08x} - {} nodes were found.".format(network.home_id,
                                                                                           network.nodes_count))


def louie_network_failed(network):
    print("Hello from network : can't load :(.")


def louie_network_ready(network):
    print("Hello from network : I'm ready : {} nodes were found.".format(network.nodes_count))
    print("Hello from network : my controller is : {}".format(network.controller))
    dispatcher.connect(louie_node_update, ZWaveNetwork.SIGNAL_NODE)
    dispatcher.connect(louie_node_event, ZWaveNetwork.SIGNAL_NODE_EVENT)


# dispatcher.connect(louie_value_update, ZWaveNetwork.SIGNAL_VALUE)


def louie_network_awake(network):
    print("Hello from network : I'm awake")


def louie_node_update(network, node):
    print("Hello from node : {}.".format(node))


def louie_value_update(network, node, value):
    print("Hello from value : {}.".format(value))


def louie_node_event(**kwargs):
    print("Hello from node event : {}.".format(kwargs))


# Create a network object
network = ZWaveNetwork(options, autostart=False)

# Connect to the louie dispatcher
dispatcher.connect(louie_network_started, ZWaveNetwork.SIGNAL_NETWORK_STARTED)
dispatcher.connect(louie_network_failed, ZWaveNetwork.SIGNAL_NETWORK_FAILED)
dispatcher.connect(louie_network_ready, ZWaveNetwork.SIGNAL_NETWORK_READY)
dispatcher.connect(louie_network_awake, ZWaveNetwork.SIGNAL_NETWORK_AWAKED)
controller = ZWaveController(1, network)
network.start()
arr = []
for node in network.nodes:
    arr.append(node.id)
print(arr)
# Wait for the network.
print("***** Waiting for network to become ready : ")
for i in range(0, 300):
    if network.state >= network.STATE_READY:
        print("***** Network is ready")
        break
    else:
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(1.0)
