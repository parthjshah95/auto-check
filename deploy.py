import os
import datetime
import shutil

now = str(datetime.datetime.now())
dash = "\n-----------------------------\n"
print(dash, "cleaning old build files", dash)
shutil.rmtree('docs', ignore_errors=True)
print("done")
print(dash, "building source", dash)
os.system("npm run build")
print(dash, "deploying to github pages", dash)
os.system("git add docs/")
os.system("git commit -m 'deployed on " + now + "'")
os.system("git push")
print(dash, "completed deployment process", dash)