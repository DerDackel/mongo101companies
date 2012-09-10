import pymongo as pm

conn = pm.Connection()
db = conn["meganalysis"]

employees = db["employees"]
depts = db["depts"]

modded = []

for dept in depts.find():
    if dept.get("ancestors") != None:
        for anc_id in dept["ancestors"]:
            anc = depts.find_one({"_id" : anc_id})
            if anc.get("super") and not anc["super"] in dept["ancestors"]:
                dept["ancestors"].append(anc["super"])
    modded.append(dept)
