"""Script used to send data to CSV"""
import csv
import yaml
from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get
from tools import manu_year_cisco, nornir_set_creds, product_info, software_release, eox


with open("./credentials.yaml", encoding="utf-8") as file:
    myvars = yaml.safe_load(file)

my_token = myvars["support_auth_token"]

with open("device_info.csv", mode="w", encoding="utf-8") as csv_file:
    fieldnames = [
        "Name",
        "Platform",
        "Model",
        "Base_PID",
        "Replacement",
        "Serial",
        "EoS",
        "EoSM",
        "LDoS",
        "EoCR",
        "Manufacture Year",
        "Current SW",
        "Recommended SW",
    ]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()


def all_the_things(task):
    """It does all the things"""
    task1_result = task.run(
        name=f"Get facts for {task.host.name}!", task=napalm_get, getters=["get_facts"]
    )

    name = task1_result[0].result["get_facts"]["hostname"]
    model = task1_result[0].result["get_facts"]["model"]
    ver = task1_result[0].result["get_facts"]["os_version"]
    version = ver.split(",")[1]
    serial = task1_result[0].result["get_facts"]["serial_number"]
    platform = task1_result[0].result["get_facts"]["vendor"]
    manu_year = manu_year_cisco(serial)
    base_pid = product_info(serial, my_token)
    upgrade = software_release(base_pid, my_token)
    my_eox = eox(serial, my_token)

    with open("device_info.csv", mode="a", encoding="utf-8") as myfile:
        write = csv.DictWriter(myfile, fieldnames=fieldnames)
        write.writerow(
            {
                "Name": name,
                "Model": model,
                "Current SW": version,
                "Serial": serial,
                "Platform": platform,
                "Manufacture Year": manu_year,
                "Base_PID": base_pid,
                "Recommended SW": upgrade,
                "EoS": my_eox["eos"],
                "EoSM": my_eox["eosm"],
                "LDoS": my_eox["ldos"],
                "EoCR": my_eox["eocr"],
                "Replacement": my_eox["replacement"],
            }
        )


def main():
    """Used to run all the things"""
    norn = InitNornir(config_file="config/config.yaml")
    nornir_set_creds(norn)
    norn.run(task=all_the_things)


if __name__ == "__main__":
    main()
