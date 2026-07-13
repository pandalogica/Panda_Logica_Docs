# Creating Calculated Fields

_Last updated: 2026-07-13_

This guide shows how to create **calculated fields** in the ASR (Admin System Repository). Calculated fields let you expose derived values — margins, concatenations, flags, and similar metrics — without changing the ERP or target database. Once defined, they behave like ordinary fields in queries and reports.

> **Who is this for?** MBI administrators and power users who maintain ASR metadata. You need rights such as *Define calculated fields* (or full admin). Everyday report users consume the results; they do not create calculated fields here.

## When to use a calculated field

Use a calculated field when the value users need is **not stored** on the source table, but can be derived from columns already registered in ASR.

Good candidates:

- **Arithmetic** — margin, extended value, variance (`price * qty`, `sales - cost`)
- **Ratios** — percentages and rates (guard against divide-by-zero in the expression)
- **Text composition** — display labels built from codes and names
- **Dashboard measures** — numeric fields you want available as pivot/dashboard measures

Prefer a calculated field over hard-coding logic in every query when the same derivation will be reused across reports.

Do **not** use calculated fields as a substitute for missing ASR setup. Import the underlying tables and define primary keys / master–slave links first — see **[ASR Setup](../admin-guides/asr-setup.md)**.

---

## Before you start

- ASR has an environment with at least one **schema** and the relevant **tables imported**.
- You can open **System admin → Tables and Fields**.
- Your role includes **Define calculated fields** (or you are an administrator) — see **[Roles](../admin-guides/roles.md)**.
- You know which table the field should “belong” to (usually the fact/transaction table users query from).

---

## 1) Open Define Calculated Fields

1. Launch **MBI** and connect to the environment.
2. Open **System admin**.
3. Go to **Tables and Fields**.
4. Open the **Define Calculated Fields** sub-tab.

You will see:

| Area | Purpose |
|------|---------|
| **Schema / Table** lookups | Choose which registered table owns the field |
| **Field name / Field text** | Internal name and display label |
| **Field expression** | Formula used at query time |
| **Field type / Pivot type / Decimals** | How the result is typed and used in pivots |
| **Existing calculated fields** grid | Review, edit, or remove definitions |

> **Tip:** Calculated fields are stored in ASR field metadata (`MFFD`) with a `*Calc…` field ID. They are metadata — the ERP table itself is not altered.

---

## 2) Create the calculated field

1. Click **Reset** (or clear the form) so the button reads **Add new calculated field**.
2. Select the **Schema** (ERP nickname) and **Table** the field belongs to.
3. Enter:
   - **Field name** — short identifier. MBI prefixes it with `*Calc` automatically (tooltip: whatever you type becomes `*Calc` + your text).
   - **Field text** — label users see in grids and field pickers (for example `Line Margin`).
   - **Field expression** — the formula (see the next section). Prefer picking columns from the field finder panels so names match ASR exactly.
   - **Field type** — **Numeric** or **Character**.
   - **Pivot type** — **Measure**, **DataItem**, or **None** (see below).
   - **Decimal places** — for numeric fields (use `0` for integers).
4. Click **Add new calculated field**.

MBI writes the definition into ASR. The new field appears in the calculated fields grid and becomes available when you build or edit queries that use that table.

### Pivot type guidance

| Pivot type | Typical use |
|------------|-------------|
| **Measure** | Numeric values to aggregate (sum, average) in pivots/dashboards |
| **DataItem** | Attributes / dimensions you slice by |
| **None** | General report columns that are not pivot-oriented |

For most monetary or quantity calculations, start with **Numeric** + **Measure**.

---

## 3) Expression basics

The **Field expression** is evaluated when a query runs against the target system. Keep expressions readable and tied to real ASR field names.

### Practical patterns

**Extended value (numeric)**

```text
QTY * PRICE
```

**Margin (numeric)**

```text
SALES - COST
```

**Simple percentage (numeric)**  
Ensure the divisor cannot be zero in your data, or use a guarded pattern your target SQL dialect supports.

```text
(SALES - COST) / SALES
```

**Display label (character)**

```text
CODE || ' - ' || NAME
```

Exact operators and string functions depend on the **target DB platform** (IBM i / System i vs SQL Server). Match the dialect of the environment’s target connection.

### Building expressions safely

1. Use the **field finder** panels to insert registered column names rather than typing from memory.
2. Only reference fields that exist on tables already imported into ASR.
3. Keep the **Field type** consistent with the expression result (numeric vs character).
4. Avoid embedding environment-specific library names unless your standard expressions require them — prefer field references MBI already resolves through ASR.

> **Tip:** Start with a simple expression, add the field to a test query, and confirm values before building complex nested logic.

---

## 4) Edit or remove a calculated field

### Edit

1. Click a row in the calculated fields grid.
2. The form switches to **Update calculated field** (schema, table, and field name are locked).
3. Change **Field text**, **expression**, **type**, **pivot type**, or decimals.
4. Click **Update calculated field**.

### Remove

1. Right-click the calculated field and choose remove/delete.
2. If the field is used in any query definitions, MBI lists those queries and blocks deletion until you remove the field from them.
3. Confirm permanent deletion only when nothing still references it.

---

## 5) Publish and verify in a report

A calculated field is not useful until a query exposes it and users can open that query.

1. Open **Queries** (query maintenance / wizard) for a report that uses the owning table.
2. **Add the calculated field** to the query’s field list like any other column (`*Calc…` fields appear among available fields).
3. Save the query definition.
4. Ensure the query is **assigned to groups/roles** so users can see it — see **[Roles](../admin-guides/roles.md)**.
5. In MBI, open the report, set a sensible date range or filter, and **Run**.
6. Confirm the column appears with the expected **Field text** and sensible values.
7. Optionally check dashboard/pivot behaviour if you set **Pivot type** to Measure or DataItem.

End users then treat it like any other column — filter, sort, group, and save layouts as described in **[Setting Up a Report](../user-guides/setting-up-a-report.md)**.

### Verification checklist

| Check | Expected result |
|-------|-----------------|
| Field in ASR grid | Listed under Define Calculated Fields for the correct schema/table |
| Field in query | Available and selected on the query |
| Query assigned | Role/group can open the report |
| Runtime values | Match a known sample (spot-check against ERP) |
| Type/format | Numeric decimals and labels look correct |

---

## Pitfalls to avoid

**Creating the field before importing tables.**  
Expressions cannot resolve columns that are not in ASR. Import tables/fields first.

**Wrong owning table.**  
Attach the calculated field to the table users actually query (often the line/fact table), not a rarely used master, unless the expression only needs master columns in that context.

**Field type mismatch.**  
A character expression marked **Numeric** (or the reverse) causes confusing results or runtime errors. Match type to the expression.

**Forgetting to add it to the query.**  
ASR definition alone does not show the column. Add `*Calc…` to each query that should display it.

**Forgetting role assignment.**  
Users still need the report assigned to their group or role.

**Deleting a field still used by queries.**  
Remove it from query field lists first; MBI will name the blocking queries.

**Over-complex one-off expressions.**  
If only one report needs a special case, consider whether query-level logic is clearer — reuse calculated fields when the business rule is shared.

**Assuming ERP data changed.**  
Calculated fields do not write back to the target system. They compute at read time from current TSR data.

---

## Troubleshooting

**Define Calculated Fields controls are disabled.**  
Your role lacks *Define calculated fields*. Ask an admin to grant the right or perform the change — see **[Roles](../admin-guides/roles.md)**.

**Cannot add the field (validation fails).**  
Schema, table, field name, field text, and expression are all required. Ensure the `*Calc` name is not already used on that table.

**Expression saves but report errors or shows blanks.**  
Check target SQL dialect, field names, and null/zero edge cases. Simplify the expression and retest.

**Field missing from the query field picker.**  
Confirm you selected the same schema/table, refreshed query metadata, and that the calculated field appears in the ASR grid.

**Users cannot see the new column.**  
Add it to the published query, save, and have users refresh/reopen the report. Confirm they are on the correct environment.

**Decimals look wrong.**  
Update the calculated field’s decimal places and re-check layouts that may still format the old definition.

**Need the wider ASR context.**  
Return to **[ASR Setup](../admin-guides/asr-setup.md)** for environments, imports, and joins before adding more calculations.

---

## Related guides

- **[ASR Setup](../admin-guides/asr-setup.md)** — import tables, keys, joins, then optional calculated fields
- **[Setting Up a Report](../user-guides/setting-up-a-report.md)** — run, filter, and layout reports that use your fields
- **[Roles](../admin-guides/roles.md)** — assign queries and grant *Define calculated fields*
- **[First Login](../getting-started/first-login.md)** — activation and first connection for new users
- **Support:** support@pandalogica.com
