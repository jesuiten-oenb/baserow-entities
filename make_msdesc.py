import os
import json
import jinja2

from acdh_tei_pyutils.tei import TeiReader

from config import PROJECT_TITLE, JSON_FOLDER


templateLoader = jinja2.FileSystemLoader(searchpath="./templates")
templateEnv = jinja2.Environment(
    loader=templateLoader, trim_blocks=True, lstrip_blocks=True
)
template = templateEnv.get_template("msdesc.xml")
out_dir = os.path.join("data", "editions")

os.makedirs(out_dir, exist_ok=True)

with open(os.path.join(JSON_FOLDER, "msdesc.json"), "r", encoding='utf-8') as f:
    data = json.load(f)

with open(os.path.join(JSON_FOLDER, "ms_item.json"), "r", encoding='utf-8') as f:
    ms_item_data = json.load(f)

ms_item_data = [value for key, value in ms_item_data.items() if value["msdesc"]]


for key, context in data.items():
    if context["xml_id"]:
        save_path = os.path.join(out_dir, f"{context['xml_id']}.xml")
        context["project_title"] = PROJECT_TITLE
        ms_item_list = list(
            filter(
                lambda x: x["msdesc"][0]["value"] == context["signatur"], ms_item_data
            )
        )
        # context["ms_items"] = sorted(ms_item_list, key=lambda x: int(x["order_number"]))
        context["ms_items"] = ms_item_list
        xml_data = template.render(context)
        doc = TeiReader(xml_data)
        doc.tree_to_file(save_path)
