import os
import datetime

now = str(datetime.datetime.now())
os.rename('dist', 'docs')

os.system("git add docs/")
os.system("git commit -m 'deployed on " + now + "'")
os.system("git push")