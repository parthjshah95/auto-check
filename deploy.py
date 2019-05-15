import os
import datetime
import shutil

domain = "auto-check.ml"
now = str(datetime.datetime.now())
dash = "\n-----------------------------\n"
dots = "..."
print(dash, "cleaning old build files", dots, dash)
shutil.rmtree('docs', ignore_errors=True)
print("done")
print(dash, "building source", dots, dash)
os.system("npm run build")
print(dash, "setting domain name to", domain, dash)
with open("docs/CNAME", "w+") as c:
    c.write(domain)
print("done")
with open("version.txt") as v_file:
    v_string_existing = v_file.read()
    str_list = v_string_existing.split(".")
    incremental_version = int(str_list[2])
    incremental_version += 1
    str_list[2] = str(incremental_version)
    v_string_new = ".".join(str_list)
print("version", v_string_new)
print(dash, "deploying to github pages", dots, dash)
os.system("git add .")
os.system("git commit -m " + v_string_new)
os.system("git push")
print(dash, "completed deployment process", dash)