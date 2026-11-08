# MBI Setup Overview

This document explains, in plain language, how MBI is configured so it can connect to your business database and show dashboards and reports.

[Open the diagram](./images/MBI%20Overview.jpg)

---

## 1) What MBI is (at a high level)

MBI has two main “sides”:

1. **System Admin** (used by administrators)  
   Where you define how MBI connects to your databases and what business data means (for example: what a “Customer”, “Sales Order”, “Item”, etc. are).

2. **MBI UI** (used by end users)  
   Where users view dashboards, lists, and drill-down screens. This is the main MBI application people interact with day to day.

---

## 2) The two engines behind MBI

MBI works by combining two internal engines:

### A) The “Query Runner” (TSR)
Think of this as the part that:
- Takes a request like “show Sales Orders for this customer”
- Builds the required database query
- Runs it against the **target business database**
- Collects the results and passes them to **MBI UI** to display

In simple terms: **TSR fetches the data.**

### B) The “Definition & Security Manager” (ASR)
Think of this as the part that stores and manages the “rules and meanings” MBI needs, such as:
- What tables and fields exist in your business database (e.g., Customers, Items, Sales Orders)
- How those business areas link together (e.g., Customer → Sales Orders → Sales Order Lines)
- Users, groups, roles, and permissions (who can see/do what)
- How screens should look in MBI UI (which fields to show, friendly names, ordering, header/detail layouts)
- Saved “query definitions” (the building blocks that tell MBI which business areas to use, how they connect, and which fields to return)

In simple terms: **ASR defines the structure, security, and how data should be presented.**

---

## 3) Why MBI talks about “platforms” (IBM i, SQL Server, etc.)

Different database platforms require different connection methods and slightly different database query handling.

MBI supports multiple platforms (for example **IBM i** and **SQL Server**) by selecting:
- A compatible **ASR** for that platform
- A compatible **TSR** for that platform

This is how MBI stays “database-agnostic” (it can work with different database technologies without changing the MBI UI).

---

## 4) Environments: the key idea in System Admin

In **System Admin**, you create one or more **Environments**.

An **Environment** is a named setup that tells MBI:
- Which **ASR** to use (and how to connect to it)
- Which **TSR** to use (and how to connect to the target business database)

You can think of an Environment like a “connection profile”, for example:
- “Production”
- “Test”
- “Training”
- “Customer ABC – Live”

Each Environment always pairs:
- **One ASR connection** (where definitions/security live)
- **One TSR connection** (where the business data is fetched from)

---

## 5) The small internal database (used by MBI itself)

MBI keeps a small internal database that stores:
- The list of Environments
- For each Environment: the selected database platform(s) and connection details

This internal database is not your business data.  
It exists so MBI can remember “how to connect and which route to use” when the user selects an Environment.

---

## 6) What you do in System Admin (typical setup tasks)

### Step 1: Create an Environment
You will:
- Give the Environment a name (e.g., “Production”)
- Choose the database platform for:
  - ASR (definitions/security storage)
  - TSR (target business database access)
- Enter the required connection details for each

### Step 2: Define business structure and relationships (ASR side)
You define:
- The main business areas (Customers, Vendors, Items, Sales Orders, Purchase Orders, Inventory, etc.)
- How they connect together (so MBI can drill down correctly)

### Step 3: Configure users and permissions (ASR side)
You define:
- Users and groups
- Roles/permissions (who can access which areas, dashboards, actions)

### Step 4: Configure how data appears in MBI UI (ASR side)
You define:
- Friendly field names (so users see “Customer Name” instead of a database field name)
- Which fields appear by default
- Header/detail layouts (summary row + detail lines)
- Sorting and display order

### Step 5: Define reusable queries (ASR side)
You define reusable query “templates” that tell MBI:
- Which business areas to use
- How they connect
- Which fields to return

These query definitions are what TSR uses later to build and run the actual database queries.

---

## 7) What happens when an end user uses MBI UI

When a user opens MBI UI and selects an Environment:

1. MBI reads the Environment settings from the internal database
2. MBI routes requests through the correct **ASR** and **TSR** for that Environment
3. When the user opens a dashboard or list:
   - ASR provides the definitions (what to show, what it means, permissions)
   - TSR runs the required database queries and returns the results
4. MBI UI displays the results and allows drill-down based on the relationships you defined

---

## 8) Practical example (in plain terms)

If a user clicks:
**Customer → View Sales Orders → View Order Lines**

- **ASR** knows:
  - What “Customer”, “Sales Order”, and “Order Line” mean
  - How they link together
  - Which fields should be shown
  - Whether this user is allowed to view them

- **TSR** does the work of:
  - Running the database queries needed for each screen
  - Returning the data to MBI UI for display

---

## 9) Key takeaways

- **System Admin** is where you configure Environments, definitions, permissions, and screen layouts.
- **MBI UI** is what end users interact with (dashboards and drill-down views).
- **ASR** = definitions + relationships + security + display rules + saved query templates.
- **TSR** = runs queries against the target database and returns results to MBI UI.
- An **Environment** always pairs one ASR + one TSR, with platform choices and connection details.

---
