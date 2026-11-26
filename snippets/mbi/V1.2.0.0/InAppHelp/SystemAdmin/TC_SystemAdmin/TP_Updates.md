# Application Updates

Use **Sys Admin → Application Updates** to choose who installs updates for this copy of MBI. Each installation has its own setting.

## Shared PC, RemoteApp or server

Under **Who installs updates?**, choose **System administrator (shared installation)**. This is the default. Enter an **Update contact email** that someone monitors. Select **Send test email** to check delivery using the current environment's outgoing mail settings, then select **Save**.

When Viewer detects a new release, MBI uses that contact for one notification per release for the installation. The administrator can arrange a time to update the shared copy. Users checking from Viewer see the result without an install button. If you leave the address blank, the manual check directs users to their administrator.

## Individual PC

Choose **User (individual PC)** and select **Save**. The person running MBI can accept an update at startup or from **Check for Updates**. Their Windows account needs write access to the installation folder. MBI lists the changed files, verifies the downloads and reopens Viewer after installation.
