Canonical pages are published on https://pandalogica.com. This copy matches version 2026-11-28.

Version 2026-11-28. This notice is published in English. It describes cookies and similar storage actually used by the Panda Logica website. It is a transparency document, not consent to unrelated processing.

Controller: **Panda Logica Ltd** (PANDA LOGICA LTD, company number 16758509), registered office The Old School, West Street, Southwick, Fareham, Hampshire, PO17 6EA, United Kingdom. Contact: [support@pandalogica.com](mailto:support@pandalogica.com).

Google Analytics is **not** installed. There is no gtag or analytics loader in this website. Older text that named Google Analytics was wrong.

## 1. Cookies and similar storage

| Name | Who sets it | Purpose | How long | Type |
| --- | --- | --- | --- | --- |
| `pandalogica_sid` | Panda Logica | Signed-in session. HttpOnly, Secure, SameSite=Lax. The server also ends the session after 12 hours without a request. A 14-day maximum is configured for permanent sessions, but ordinary sessions are not marked permanent, so that 14-day cap is not what currently expires them | Browser session, and idle limit above | Necessary for sign-in |
| `twofa_trusted` | Panda Logica | Remembers a trusted browser after two-factor sign-in, only if that option is used. HttpOnly, Secure, SameSite=Lax | 30 days | Necessary for the remembered sign-in you chose |
| `pandalogicaCookieConsent` | Panda Logica, in local storage | Stores Accept or Decline | Until you clear site data | Records the banner choice only |
| `pandalogica.theme`, `pl-theme` | Panda Logica, in local storage | Remembers light or dark theme | Until you clear site data | Preference |
| `pandalogica.locale` | Panda Logica, in local storage | Remembers the language you selected | Until you clear site data | Preference |
| `pl_training_progress_v1` | Panda Logica, in local storage | Stores training progress on this browser | Until you clear site data | Preference |

CSRF protection uses the session, not a separate cookie.

## 2. Scripts that are not cookies we operate

- **Google reCAPTCHA** (`www.google.com/recaptcha/api.js`) loads on the registration page and on contact forms when a site key is configured. Google may set its own cookies. The banner does not block or allow this script.
- **YouTube** (`youtube-nocookie.com`) loads only if you start an embedded video. Google may set cookies then. The banner does not control that embed.
- **Stripe Checkout** is Stripe’s hosted payment page. It is not an embedded Stripe.js payment form on our pages. Stripe uses its own cookies on that page under Stripe’s notice.
- **Lucide** and font files are loaded to draw the site. They are not advertising cookies.

## 3. The banner

The banner stores `accepted` or `declined` in local storage and then hides itself. Decline does not stop a script, and Accept does not start one. There is no website analytics cookie for the banner to control.

That means the banner is not a working consent or objection tool for optional analytics. We do not ask you to leave all cookies enabled. You can block cookies in the browser. Blocking `pandalogica_sid` will stop you staying signed in.

ICO guidance does not treat every analytics cookie as either always allowed or always consent-based. A statistics exemption has conditions. We do not rely on that exemption, because we are not running website analytics.

## 4. What still needs to be built

If we later add optional analytics or advertising, we will list the cookie here and we will not load it until a control that actually blocks it is working. reCAPTCHA is a separate gap: it loads with the form, and we have not built a control that stops it before the form is used.

## 5. Contact

[support@pandalogica.com](mailto:support@pandalogica.com). See the [Privacy notice](https://pandalogica.com/help/privacy-policy) for the wider privacy position.
