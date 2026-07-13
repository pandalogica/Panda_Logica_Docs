# Troubleshooting Common Issues

_Last updated: 2026-07-13_

Use this page when something in MBI is not behaving as expected. Start with the symptom that matches your situation, then follow the related guide if you need deeper setup help.

> **Who is this for?** All MBI users and administrators. Support teams can use these checks before escalating.

## Before you start

- Note the **exact error message**, if any.
- Confirm which **environment** you are connected to.
- Know whether you are an **end user** or an **administrator**.

---

## 1) I can log in but see no data or an empty menu

1. Ask an administrator to confirm your **role** includes the reports you need.
2. Confirm you selected the correct **environment** at connect time.
3. See **[Managing Roles and Permissions](../admin-guides/roles.md)**.

---

## 2) Activation or license failed

1. Recheck the **admin email** and **product key** from your welcome message.
2. Confirm the workstation can reach the licensing / activation endpoint.
3. If it still fails, contact [support@pandalogica.com](mailto:support@pandalogica.com) with the error text.

See also **[First Login](../getting-started/first-login.md)**.

---

## 3) Connection to the database fails

1. Verify network/VPN access to the database host.
2. Confirm credentials and that the account is not locked.
3. Administrators should re-test the TSR connection in System Admin.

See **[TSR Setup](../admin-guides/tsr-setup.md)** and the Data Connection Setup Guide (PDF) from training.

---

## 4) A report opens but returns no rows

1. Widen the **date range**.
2. Clear personal filters that may be too narrow.
3. Confirm your role can access that query’s data.

See **[Setting Up a Report](../user-guides/setting-up-a-report.md)**.

---

## 5) Layout changes do not save

1. Confirm you used **Save Layout** and gave the layout a name.
2. Check whether your role allows saving personal layouts.
3. Re-open the report and look under **Personal** layouts.

---

## 6) Still stuck?

1. Capture screenshots of the error and the environment name.
2. Contact support via the website contact form (subject: Support) or email support@pandalogica.com.
3. Include whether the issue affects one user or everyone.

---

## Related guides

- **[First Login](../getting-started/first-login.md)**
- **[Roles](../admin-guides/roles.md)**
- **[ASR Setup](../admin-guides/asr-setup.md)**
- **[Setting Up a Report](../user-guides/setting-up-a-report.md)**
- **[MBI FAQ](faq.md)**
