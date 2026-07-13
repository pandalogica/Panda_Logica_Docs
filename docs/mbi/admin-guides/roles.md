# Managing Roles and Permissions in MBI

_Last updated: 2026-07-13_

This guide explains how **groups**, **roles**, and **user assignments** control what people can see and do in MBI. Roles sit on top of your ASR metadata and query definitions: they decide which reports appear for each user, which System Admin actions are allowed, and whether someone can save layouts. Getting roles right is the usual fix when a user can log in but sees an empty menu or no data.

> **Who is this for?** MBI administrators responsible for environments, users, and report access. End users do not manage roles — they receive access from their admin.

## How access works in MBI

MBI separates **who you are** from **what you can open**:

| Layer | What it controls |
|-------|------------------|
| **Group** | Organisational container (for example Sales, Finance, Warehouse). Holds roles and optional group-wide query access. |
| **Role** | Named access profile inside a group (for example Sales Rep, Sales Manager). Users belong to one group/role pair. |
| **User assignment** | Links a user ID to a group and role, plus folders for saved grids, pivots, and dashboards. |
| **Query assignment** | Makes a report visible to a whole group (**All roles**) or to a specific role only. |
| **User rights** | Fine-grained System Admin permissions on a role (for example *Add a File*, *Define Calculated fields*). |

ASR defines tables, fields, and queries. Roles decide **who** those queries are available to. A complete environment needs both — see **[ASR Setup](asr-setup.md)**.

```
Environment + ASR (tables, queries)
        ↓
Groups → Roles → Users
        ↓
Assign queries to group or role
        ↓
User logs in and sees only assigned reports
```

---

## Before you start

- You have **administrator** rights (or rights such as *Add a Group*, *Add a Role*, and *Add a User*).
- An **environment** exists and ASR has at least one working query.
- Users have already activated MBI (or you are ready to assign them after activation) — see **[First Login](../getting-started/first-login.md)**.
- You know which reports each team should see, and whether managers need extra System Admin rights.

---

## 1) Open Groups and Users

1. Launch **MBI** and connect to the environment.
2. Open **System admin** (MQ Setup).
3. Select the **Groups and Users** tab.

You will typically work with:

| Area | Purpose |
|------|---------|
| **Groups** list | Create and select groups |
| **Group details** | Roles, users in each role, and queries assigned to the group or role |
| **User list / add user** | Assign a user from the pool to a group and role |
| **Role rights** | Tick the System Admin activities that role may perform |

> **Tip:** If System Admin opens on Environments or Tables and Fields instead, finish the missing setup first. MBI often steers you to Groups and Users when no groups, roles, or users exist yet.

---

## 2) Create groups and roles

Start with groups that match how your organisation works, then add roles under each group.

### Add a group

1. Click **Add a Group**.
2. Enter a clear group name (for example `SALES` or `FINANCE`).
3. Save / accept the change.

### Add a role

1. Select the group.
2. Click **Add a Role**.
3. Enter a role name (for example `REP`, `MANAGER`, or `READONLY`).
4. Save the role.

Keep role names short and consistent — they appear throughout assignment screens and troubleshooting.

> **Tip:** Prefer a few well-named roles over many near-duplicates. Access differences are easier to manage with query assignments than with dozens of almost-identical roles.

---

## 3) Assign users to a group and role

Every MBI user who should see reports must be placed in a **group** and a **role**.

1. Click **Add a User from the Global Pool** (or edit an existing user row).
2. Select the **user ID**.
3. Choose the **Group** and **Role**.
4. Confirm (or leave default) the folders used for saved **grid**, **pivot**, and **dashboard** layouts.
5. Click **Accept** to write the assignment.

Rules to remember:

- A user must have both a group and a role — MBI will reject incomplete details.
- Changing a user’s group/role changes which queries they inherit.
- Admin users still need a valid group/role if they will run reports as an ordinary user.

---

## 4) Control data visibility with query assignments

Logging in successfully does **not** grant report access. Visibility comes from assigning queries to the group or role.

### Assign at group level (All roles)

Use this when everyone in the group should see the same report:

1. Select the group so **Group details** shows **Group level queries → All roles**.
2. From the available queries list, **drag** the query onto the **All roles** / group-level queries area.
3. Confirm the query appears under group-level queries.

Group-level assignment means every role in that group can open the report.

### Assign at role level

Use this when only some roles should see a report (for example managers only):

1. Select the group and locate the target **role** in Group details.
2. Drag the query onto that role’s **Queries** section (not onto All roles).
3. Confirm it appears under that role only.

You can also use **Assign Query to Groups/Roles** from query maintenance — tick the role (or *All roles*) nodes and apply.

### Optional: allow saving layouts

Query assignments can include a save flag. If users need to keep personal grid/dashboard layouts for that report, enable save on the assignment; otherwise leave it read-only as your policy requires.

---

## 5) Set role permissions (System Admin rights)

Roles also control **what administrators and power users can change** in System Admin — separate from which reports they can run.

Typical rights groups include:

| Category | Examples |
|----------|----------|
| **Files & fields** | *Add a File*, *Remove a File*, *Define Master/Slave fields*, *Define calculated fields* |
| **Query definitions** | *Create a Query*, *Delete a Query*, *Add Query Fields*, *Remove Query Fields* |
| **Groups and users** | *Add a Group*, *Add a Role*, *Add a User*, *Remove a Group* |

1. Select the role whose rights you want to edit.
2. Tick only the activities that role should perform.
3. Save changes.

End-user roles usually need **no** System Admin rights — only query assignments. Reserve *Add a File*, *Define Master/Slave fields*, and *Define calculated fields* for trusted admins.

---

## 6) Verify access

Before telling users the environment is ready, walk this checklist:

| Check | How to verify |
|-------|----------------|
| Group exists | Group appears in **Groups and Users** |
| Role exists | Role appears under the group |
| User assigned | User row shows correct group and role |
| Query assigned | Query listed under **All roles** or the user’s role |
| Rights appropriate | Role has admin ticks only if intended |
| User test | Sign in as the user (or ask them to) and confirm the report appears |

Also confirm ASR is healthy: tables imported, joins accepted, and a test query returns rows — see **[ASR Setup](asr-setup.md)**. Empty results with a visible report is usually filters or data, not roles; a missing report is almost always assignment.

---

## Common scenario: “I can log in but see no data”

This is the most frequent access issue after first login.

**What the user sees**

- Activation and environment connection succeed.
- Home screen or left menu shows few or no reports.
- Running anything returns nothing useful, or there is nothing to open.

**Likely causes (in order)**

1. **User has no group/role** — assignment missing or incomplete.
2. **User has a role, but no queries** — nothing assigned to that role or to the group’s All roles.
3. **Wrong group/role** — user assigned to a setup role that has no operational reports.
4. **Query exists only in Designer / ASR** — created but never assigned to groups/roles.
5. **Wrong environment** — user connected to a different environment than the one you configured.

**Fix**

1. In **Groups and Users**, find the user and note their group and role.
2. Open that group’s details and confirm at least one query is assigned to **All roles** or that specific role.
3. If missing, drag the intended starter report onto the correct node and save.
4. Ask the user to reconnect (or restart MBI) and open the report again.
5. Point them to **[First Login](../getting-started/first-login.md)** for the UI tour once reports appear, and **[Setting Up a Report](../user-guides/setting-up-a-report.md)** for filters and layouts.

> **Tip:** Keep one “smoke test” query assigned at **group / All roles** level for every live group. It makes first-login checks fast and reduces false “no data” tickets.

---

## Troubleshooting

**Add a Group / Add a Role / Add a User is disabled.**  
Your account lacks the matching user right, or you are not an admin. Sign in with an administrator, or ask one to grant *Add a Group*, *Add a Role*, or *Add a User*.

**“This user already exists” when adding.**  
The user is already in the environment’s user list. Edit the existing row instead of adding again.

**“A Group has not been selected” / “A Role has not been selected”.**  
Both fields are required. Create the group and role first, then assign the user.

**Query already exists at group level.**  
It is already assigned via **All roles**. You do not need a duplicate role-level assignment unless you intentionally want role-only access — in that case remove the group-level entry first if your process requires it.

**Managers see reports that reps should not.**  
Move those queries from **All roles** to the manager role only.

**User sees the report but System Admin options are missing.**  
Expected for end-user roles. Grant specific rights (for example *Define calculated fields*) only when that person should configure ASR.

**Access looks correct but results are empty.**  
Roles control visibility of the report, not row content from the target database. Check date filters, TSR connectivity, and whether the query’s tables have data. See **[Setting Up a Report](../user-guides/setting-up-a-report.md)** and **[ASR Setup](asr-setup.md)**.

---

## Related guides

- **[First Login](../getting-started/first-login.md)** — activation, first connection, and UI tour
- **[ASR Setup](asr-setup.md)** — environments, tables, fields, and query foundations
- **[Setting Up a Report](../user-guides/setting-up-a-report.md)** — filters, layouts, and grids for end users
- **[Calculated Fields](../advanced/calculated-fields.md)** — derived metrics in ASR Tables and Fields
- **Support:** support@pandalogica.com
