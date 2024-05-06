# Generated by Django 3.2.12 on 2022-04-08 10:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("history", "0058_alter_webhook_url"),
    ]

    operations = [
        migrations.RenameField(
            model_name="webhook",
            old_name="new_executed_outgoing_transaction",
            new_name="new_executed_multisig_transaction",
        ),
        migrations.RenameField(
            model_name="webhook",
            old_name="pending_outgoing_transaction",
            new_name="pending_multisig_transaction",
        ),
        migrations.AlterField(
            model_name="webhook",
            name="new_executed_multisig_transaction",
            field=models.BooleanField(
                default=True, help_text="New mined multisig transaction"
            ),
        ),
        migrations.AlterField(
            model_name="webhook",
            name="pending_multisig_transaction",
            field=models.BooleanField(
                default=True, help_text="New pending multisig transaction"
            ),
        ),
        migrations.AlterField(
            model_name="webhook",
            name="new_confirmation",
            field=models.BooleanField(default=True, help_text="New confirmation"),
        ),
        migrations.AlterField(
            model_name="webhook",
            name="new_incoming_transaction",
            field=models.BooleanField(
                default=True, help_text="New incoming transaction of eth/token"
            ),
        ),
        migrations.AlterField(
            model_name="webhook",
            name="new_module_transaction",
            field=models.BooleanField(
                default=True, help_text="New mined module transaction"
            ),
        ),
        migrations.AlterField(
            model_name="webhook",
            name="new_outgoing_transaction",
            field=models.BooleanField(
                default=True, help_text="New outgoing transaction of eth/token"
            ),
        ),
        migrations.AlterField(
            model_name="webhook",
            name="new_safe",
            field=models.BooleanField(default=True, help_text="New Safe created"),
        ),
    ]