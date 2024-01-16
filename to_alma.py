import os
import json
import pandas as pd

with open(os.path.join("json_dumps", "msdesc.json"), "r") as f:
    data = json.load(f)

result = []
for key, value in data.items():
    result.append([value["signatur"], "ALMA", "data"])
    result.append(["Title", "245", value["title"]])
    result.append(["Date", "264", "date"])
    result.append(
        [
            "Extent, Measures, Foliation",
            "300",
            f"§§a {value['extent']}; $$c {value['height']} × {value['width']}mm; {value['foliation']}.",
        ]
    )
    result.append(["Fragments", "500", f"§§a {value['acc_mat']}"])
    result.append(
        [
            "Organisations/Places",
            "505/8/0",
            f"$$t {', '.join([x['value'] for x in value['mentioned_orgs']])}; {', '.join([x['value'] for x in value['mentioned_places']])}",
        ]
    )

    result.append(["", "", ""])

df = pd.DataFrame(result)
df.to_csv('hansi.csv', index=False)
