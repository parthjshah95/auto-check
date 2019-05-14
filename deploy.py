import os
import datetime
import shutil

now = str(datetime.datetime.now())
dash = "\n-----------------------------\n"
dots = "..."
print(dash, "cleaning old build files", dots, dash)
shutil.rmtree('docs', ignore_errors=True)
print("done")
print(dash, "building source", dots, dash)
os.system("npm run build")
print(dash, "deploying to github pages", dots, dash)
os.system("git commit -a -m 'deployed on " + now + "'")
os.system("git push")
print(dash, "completed deployment process", dash)