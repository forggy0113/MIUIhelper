import json
from AutoWeb import internalTest

with open("Test/data/accounts.json", "r", encoding="utf-8") as r:accounts = json.load(r)

for Account in accounts:
    internalTest(account=Account["account"], password=Account["password"],tasks=Account["tasks"])
print("结束!")