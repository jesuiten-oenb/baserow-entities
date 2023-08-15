import os
import json
import jinja2

from acdh_tei_pyutils.tei import TeiReader

from config import PROJECT_TITLE


templateLoader = jinja2.FileSystemLoader(searchpath="./templates")
templateEnv = jinja2.Environment(
    loader=templateLoader, trim_blocks=True, lstrip_blocks=True
)
template = templateEnv.get_template("ms_desc.xml")
out_dir = os.path.join("data", "editions")

os.makedirs(out_dir, exist_ok=True)


