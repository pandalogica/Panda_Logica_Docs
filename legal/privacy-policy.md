Canonical pages are published on https://pandalogica.com. This copy matches version 2026-11-28.

Version 2026-11-28. This notice is published in English. A translation, if one is shown, is for convenience only. The English text governs.

This notice explains how **Panda Logica Ltd** (PANDA LOGICA LTD, company number 16758509) uses personal data. We are the controller for the account, website, billing, licence and diagnostic processing described here. Our registered office is The Old School, West Street, Southwick, Fareham, Hampshire, PO17 6EA, United Kingdom.

Contact for privacy requests: [support@pandalogica.com](mailto:support@pandalogica.com). A separate privacy@ mailbox is not confirmed as monitored.

This notice is a transparency document. It is not consent to all processing, and it is not the contract for MBI. The contract is the [Terms of Service](https://pandalogica.com/help/terms-of-service) and the [MBI EULA](https://pandalogica.com/legal/eula).

## 1. What stays on your systems

MBI is desktop software. In ordinary use it queries your IBM i, SQL Server or other sources that you configure, from your environment. Those query results, and the business records inside your databases, are not uploaded to us as part of licence validation.

We do **not** claim that we never store, access or analyse customer business data in every situation. That older statement was too absolute. What we can say from the product is:

- licence checks send a licence key, product id and Windows device id, not your query results;
- connection settings and the contents of your databases remain on your systems unless you choose to send them to us;
- diagnostic and product-analytics events can be sent to us, and an error message or a short analytics property could include business information if the application or a user puts it there;
- if you email us a spreadsheet, a screenshot or a database extract for support or bespoke work, we then have whatever you sent.

## 2. Personal data we process

| Area | Data | Why |
| --- | --- | --- |
| Account | Company name, user name, email, password hash, role, sign-in timestamps | Create and secure the company account |
| Billing | Email, Stripe customer id, subscription status, trial end, period end, tier, refund amounts | Take payment, run the trial, and set the licence |
| Licence and activation | Licence key, product id, Windows device id, activation counts, expiry, status | Activate MBI and check that the licence is still valid |
| Diagnostics | Application, version, exception type, message, stack trace, a user id if sent, timing and retry fields | Group and fix software faults. Messages are scrubbed for some secrets and local file paths. They are not treated as anonymous |
| Product analytics | Session start and end, screen names, feature names, action names, a user id if it matches the allowed pattern, and short properties | Understand which parts of MBI are used. These records can identify a user. They are not anonymous |
| Website | Sign-in session, security cookies, pages you request, and the IP address used for rate limits | Operate and protect the site |
| Contact and support | Name, email and the message you send, plus anything you attach | Reply to you |
| reCAPTCHA | The check Google runs on registration and contact forms | Reduce automated sign-ups and spam |

We do not sell personal data.

Providing a company name, user name, email and password is necessary to create an account. Payment details are requested by Stripe at checkout because the trial is a subscription checkout, not because we store the card number ourselves. You do not have to send diagnostic or analytics events for the website account to exist. MBI licence validation will not succeed without the licence fields above.

## 3. Purposes and lawful bases

| Purpose | Lawful basis we rely on |
| --- | --- |
| Account, subscription, licence validation, and service messages about those | Contract |
| Taking payment and keeping billing records | Contract, and legal obligation where tax or accounting law requires the record |
| Security, rate limits, fraud prevention, and fault diagnosis | Legitimate interests in keeping the service secure and operable. We have not published a separate legitimate-interests assessment |
| Product analytics of MBI screens and features | Legitimate interests in understanding and fixing the product. You can object. This is not consent-based analytics on the website, and no website analytics tool is installed |
| Replying to contact and support requests | Contract if you are a customer, otherwise legitimate interests in answering the enquiry, or steps you ask us to take before a contract |
| reCAPTCHA on forms | Legitimate interests in blocking automated abuse. The cookie notice explains that the cookie banner does not switch this script on or off |

We do not use personal data for solely automated decisions that produce legal or similarly significant effects of the kind described in UK GDPR Article 22. If a subscription is unpaid, the licence status follows the billing rules in the Terms. That is enforcement of the contract, not profiling.

## 4. Who receives personal data

We use these providers because the product is built that way. We name them so you can see the categories. We do not list a supplier we have not found in the product.

- **Stripe** processes checkout, cards, subscriptions and refunds. We store Stripe ids and subscription state, not the full card number.
- **Postmark** sends email. The configured From address is support@pandalogica.com.
- **Google reCAPTCHA** runs on registration and contact forms when a site key is configured.
- **YouTube** (youtube-nocookie.com) is used only if you play an embedded video.
- The website is configured for **Render** hosting, with a **PostgreSQL** database and **Redis** for rate limits. Hosting and database providers process the data stored in the application.
- Installer files can be stored in **Cloudflare R2**. That store is for software binaries, not for your business database.
- If Linear is configured, diagnostic groups can be sent to **Linear** for staff issue tracking.
- Professional advisers or authorities where the law requires it.

Some of these providers may process personal data outside the United Kingdom. The transfer safeguard for each contract (for example an IDTA or SCCs) is not in this repository, so this notice does not claim that a particular safeguard is in place. That confirmation is an open item before this notice is treated as final.

## 5. How long we keep data

A fixed retention schedule is not defined in the product. Until one is, we keep:

- account and licence records while the account is open, and afterwards for as long as we need them for billing disputes, security, or a legal claim;
- billing and refund records for as long as tax and accounting duties require, which we have not translated into a published number of years;
- diagnostic and analytics events until we delete them under an operational schedule that is not yet published;
- contact messages for as long as we need them to handle the request and any follow-up.

We will not invent a number of months in order to look complete.

## 6. Your rights

If UK GDPR applies, you can ask to access, correct, erase, or restrict personal data, and you can ask for portability where the basis is contract or consent and the processing is automated. You can object to processing based on legitimate interests, including product analytics.

Email [support@pandalogica.com](mailto:support@pandalogica.com). We may need to confirm you are entitled to act for the company account. You can complain to the Information Commissioner’s Office at [https://ico.org.uk](https://ico.org.uk).

We do not run a separate marketing mailing list in this application. Service emails are about the account, security and subscription. If we send a promotional email, you can use the unsubscribe link in that email. Withdrawing from promotional email does not cancel a subscription.

## 7. When we process data for you

Selling and licensing MBI, and validating licences, does not by itself make us a processor of the personal data inside your business databases. Those databases stay in your environment.

If you send us personal data so that we can provide support or write a bespoke query, we are then processing that data for you. A data-processing agreement should be in place before that work. This repository does not contain one. Ask us if you need one.

## 8. Changes

The version date is at the top of this page. If we materially change how we use personal data, we will post the updated notice and, where the change affects a current customer, tell the account email.

## 9. Contact

**Panda Logica Ltd** (PANDA LOGICA LTD, company number 16758509)  
Registered office: The Old School, West Street, Southwick, Fareham, Hampshire, PO17 6EA, United Kingdom  
[support@pandalogica.com](mailto:support@pandalogica.com)
