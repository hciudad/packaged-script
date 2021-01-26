#! /usr/local/bin/python
import json
import os
import pkgutil
import shutil
import sqlite3
import sys
import tempfile

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
os.environ.setdefault("CLOUDBOLT_DIR", "/opt/cloudbolt")

sys.path.insert(0, os.environ["CLOUDBOLT_DIR"])

import django
django.setup()

from django.conf import settings

def main():
    temp_dir = tempfile.mkdtemp()

    try:
        print(f"Django DB settings: {json.dumps(settings.DATABASES, indent=4)}\n\n")

        src_version = os.path.join(temp_dir, "db1")
        dest_version = os.path.join(temp_dir, "db2")

        # Save sqlite DBs to temp location
        with open(src_version, "wb") as f:
            f.write(pkgutil.get_data("data", "v9.2.1.db"))

        with open(dest_version, "wb") as f:
            f.write(pkgutil.get_data("data", "v9.3.1.db"))
             
        conn = sqlite3.connect(src_version)
        print("sqlite3 query results:")
        print(conn.execute("select * from item").fetchall())
        conn.close()
    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)

if __name__ == "__main__":
    main()
    sys.exit(0)
