

import os, shutil

books = ['quick-start','sys-admin','developer','setup']

for book in books:

    path = "./%s" % book


    # copy css
    orig_css = "common/extra.css"
    css = "%s/docs/css" % path
    print("copy css to [%s]" % css)
    shutil.copy(orig_css, css)

    # build each site
    cmd = 'cd %s; mkdocs build' % path
    print("cmd: ", cmd)
    os.system(cmd)

    # move the build site into another site folder
    shutil.move("%s/site" % path, "site/%s" % book)

