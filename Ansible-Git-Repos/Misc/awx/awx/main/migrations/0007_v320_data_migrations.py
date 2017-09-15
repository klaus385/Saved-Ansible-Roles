# -*- coding: utf-8 -*-
# Python
from __future__ import unicode_literals

# Django
from django.db import migrations, models

# AWX
from awx.main.migrations import _inventory_source as invsrc
from awx.main.migrations import _migration_utils as migration_utils
from awx.main.migrations import _reencrypt as reencrypt
from awx.main.migrations import _scan_jobs as scan_jobs
from awx.main.migrations import _credentialtypes as credentialtypes
import awx.main.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_v320_release'),
    ]

    operations = [
        # Inventory Refresh
        migrations.RunPython(migration_utils.set_current_apps_for_migrations),
        migrations.RunPython(invsrc.remove_rax_inventory_sources),
        migrations.RunPython(invsrc.remove_inventory_source_with_no_inventory_link),
        migrations.RunPython(invsrc.rename_inventory_sources),
        migrations.RunPython(reencrypt.replace_aesecb_fernet),
        migrations.RunPython(scan_jobs.migrate_scan_job_templates),

        migrations.RunPython(credentialtypes.migrate_to_v2_credentials),
        migrations.RunPython(credentialtypes.migrate_job_credentials),
    ]
