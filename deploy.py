import os
import datetime
import shutil

now = str(datetime.datetime.now())
os.system("npm run build")
shutil.rmtree('docs', ignore_errors=True)
os.rename('dist', 'docs')

os.system("git add docs/")
os.system("git commit -m 'deployed on " + now + "'")
os.system("git push")