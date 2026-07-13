# TSR Setup

_Last updated: 2026-07-13_

This guide explains how to configure the **TSR (Target System Repository)** connection — the live operational database MBI reads when users run reports. TSR holds your ERP or business data. ASR holds the metadata that describes that data.

> **Who is this for?** MBI administrators and IT staff who create or maintain environments. End users do not configure TSR.

## Before you start

- You have **administrator** rights in MBI System Admin.
- You know the target platform (for example **IBM i / System i** or **SQL Server**).
- You have a **read-focused** service account (preferred) and network access from the MBI workstation to the database server.
- You understand which libraries/catalogs the business will query.

> **Tip:** Configure a working TSR connection before importing large numbers of tables into ASR. See **[ASR Setup](asr-setup.md)** after the connection succeeds.

---

## 1) Open the environment settings

1. Launch **MBI** and open **System Admin**.
2. Go to the **Environments** tab.
3. Select an existing environment, or create a new one.

Confirm:

- **Environment name** is clear to users.
- **ASR DB platform** and location are set (metadata store).
- **Target DB platform** matches your operational system.

---

## 2) Enter the target connection

On the environment details:

1. Choose **Target DB platform** (IBM i or SQL Server are the common options).
2. Enter the **server / IP**, port if required, and authentication details for the service account.
3. Specify the default **catalog**, **library**, or schema users should work with first.
4. Save with **Accept changes**.

> **Important:** Prefer a dedicated read-only (or least-privilege) account for reporting. Avoid day-to-day personal admin passwords in shared environments.

---

## 3) Test connectivity

1. Use the environment’s connection test / connect action (wording varies by version).
2. Confirm MBI can list schemas or libraries.
3. If the test fails, check network/firewall, credentials, and that the database allows the MBI host.

Only continue to ASR table import when the connection test succeeds.

---

## 4) Register schemas for reporting

1. With the environment selected, add **schema** nicknames that map to real libraries/catalogs (for example `IBM_ERP` → `MYLIB`).
2. Save changes.
3. Proceed to **[ASR Setup](asr-setup.md)** to import tables and define keys/joins.

---

## 5) Verify with a simple query

1. After ASR has at least one table and a simple query, run that query as a test user.
2. Confirm rows return for an expected date range.
3. If activation works but menus are empty, check **[Roles](roles.md)**.

---

## Troubleshooting

**Connection test fails immediately.**  
Verify host, port, VPN/firewall, and that the account is not locked.

**Connected but no schemas appear.**  
Confirm the account can list libraries/catalogs and that schema nicknames were saved on the environment.

**Reports time out or return no rows.**  
Widen filters first; then review query definition and TSR performance with your DBA.

**Users see the wrong company data.**  
Confirm they are connected to the correct environment and role assignments match that environment’s queries.

---

## Related guides

- **[ASR Setup](asr-setup.md)** — import tables, keys, joins, and calculated fields
- **[Roles](roles.md)** — who can see which reports
- **[First Login](../getting-started/first-login.md)** — end-user activation and first query
- **[Creating Calculated Fields](../advanced/calculated-fields.md)** — derived metrics in ASR
