import sys
from ansible.parsing.dataloader import DataLoader
from ansible.inventory.manager import InventoryManager
from kazoo.client import KazooClient


def listToString(s):
    # initialize an empty string
    str1 = ""
    # traverse in the string
    for ele in s:
        str1 += ele
    # return string
    return str1


def createZkNode(zk_host, zk_port, host_group, host, serverset_member):
    zk_connection_string = zk_host + ":" + zk_port
    zk = KazooClient(hosts=zk_connection_string)
    zk.start()
    zk.ensure_path("inventory")
    zk_node = "inventory/" + host_group + "/" + host
    zk.ensure_path(zk_node)
    zk.set(zk_node, str(serverset_member).encode())


def uploadExportersEndpoint(
    zk_host, zk_port, inventory_file_name, host_group, exporter_port
):
    data_loader = DataLoader()
    inventory = InventoryManager(loader=data_loader, sources=[inventory_file_name])
    for i in range(len(inventory.get_groups_dict()[host_group])):
        serverset_member = (
            '{"serviceEndpoint":{"host":"',
            inventory.get_groups_dict()[host_group][i],
            '","port":',
            exporter_port,
            '},"additionalEndpoints":{},"status":"ALIVE"}',
        )
        serverset_member = "".join(map(str, serverset_member))
        host = inventory.get_groups_dict()[host_group][i]
        createZkNode(zk_host, zk_port, host_group, host, serverset_member)


def nodeExporter(zk_host, zk_port, inventory_file_name):
    uploadExportersEndpoint(zk_host, zk_port, inventory_file_name, "all", 9100)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("USAGE: python inventory-uploader.py $zookeper_host $inventory-name")
    else:
        args = sys.argv[1:]
        zk_host = listToString(args[0])
        zk_port = str(2181)
        inventory_file_name = listToString(args[1])

        print("Zookeeper Host:", zk_host)
        print("Zookeeper port", zk_port)
        print("Use inventory:", inventory_file_name)

        nodeExporter(zk_host, zk_port, inventory_file_name)
        print("Upload successfully")
