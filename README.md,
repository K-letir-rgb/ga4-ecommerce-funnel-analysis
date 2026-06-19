# GA4 E-Commerce Funnel Analysis

End-to-end analysis of the [GA4 obfuscated sample e-commerce dataset](https://console.cloud.google.com/marketplace/product/bigquery-public-data/ga4-obfuscated-sample-ecommerce) (Google's public BigQuery dataset), examining user conversion behavior through the purchase funnel for November 2020.

**Tools:** BigQuery (SQL) → Python (pandas) → Tableau Public / Power BI

---

## Business Question

How do users move through the conversion funnel (page_view → view_item → add_to_cart → begin_checkout → purchase), and does cart usage affect purchase likelihood?

---

## Key Finding: The Funnel Isn't Linear

A standard funnel assumes each stage is a strict subset of the one before it. This dataset breaks that assumption:

| Stage | Unique Users (Nov 2020) |
|---|---|
| page_view | 79,181 |
| view_item | 21,440 |
| begin_checkout | 4,219 |
| add_to_cart | 2,060 |
| purchase | 1,532 |

**More users reach `begin_checkout` (4,219) than ever fire `add_to_cart` (2,060).** This isn't a data error — it reflects two distinct paths to checkout: a standard "browse → cart → checkout" flow, and a direct "Buy Now" flow that skips the cart step entirely.

## Cart Usage vs. Purchase Conversion

Splitting checkout-reaching users by whether they used the cart first:

| Path | Users | % of Checkout Reachers | Purchase Rate |
|---|---|---|---|
| Skipped cart (direct checkout) | 3,164 | 75% | 34.3% |
| Added to cart first | 1,055 | 25% | 42.5% |

**Takeaway:** Users who add to cart before checking out convert at a **42.5% rate**, vs. **34.3%** for users who go straight to checkout — an **8.2 percentage point gap** (≈24% relative lift). However, the direct-checkout path is the dominant route to checkout by volume (75% of all checkout-reaching users), not the exception.

**Business implication:** Cart usage correlates with higher purchase intent, even though most users don't use it. This raises a testable question for stakeholders — would nudging direct-checkout users toward the cart (e.g., a "save for later" prompt) increase conversion, or does it just add friction to an already-converting path?

---

## Methodology

1. Queried `bigquery-public-data.ga4_obfuscated_sample_ecommerce.events_*` in BigQuery, filtered to November 2020 (`_TABLE_SUFFIX BETWEEN '20201101' AND '20201130'`)
2. Counted raw event occurrences per funnel stage, then re-ran at the unique-user level (`COUNT(DISTINCT user_pseudo_id)`) — raw counts overstate stage size due to repeat events per user
3. Built a per-user flag table (`MAX(event_name = 'X')` pattern) to classify users by which events they fired, then segmented checkout-reaching users by cart usage and calculated purchase rate per segment
4. [Next] Exported results to Python for further cleaning/visualization, building toward a Tableau/Power BI dashboard

SQL queries are in [`/sql`](./sql).

---

## Status

🔄 In progress — funnel and cart-segment analysis complete in BigQuery. Next: Python cleaning, then dashboard build.
