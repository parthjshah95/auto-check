import os
import datetime
import shutil

now = str(datetime.datetime.now())
shutil.rmtree('docs', ignore_errors=True)
os.system("npm run build")

os.system("git add docs/")
os.system("git commit -m 'deployed on " + now + "'")
os.system("git push")