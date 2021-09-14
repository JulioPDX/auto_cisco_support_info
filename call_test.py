import yaml
from rich import print
from genie.utils import Dq
from tools import manu_year_cisco, product_info, software_release, eox


with open("./credentials.yaml", encoding="utf-8") as file:
    myvars = yaml.safe_load(file)

my_token = myvars["cisco_support_auth_token"]

serial = "SOMESN"
# model = "WS-C3750E-48TD-SD"

# print("*" * 80)
# print(manu_year_cisco(serial))
# print("*" * 80)
# print(product_info(serial, my_token))
# print("*" * 80)
# test = software_release(model, my_token)
# print(test)

test = eox(serial, my_token)
print(test)
