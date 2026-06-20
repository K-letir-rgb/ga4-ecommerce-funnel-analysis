"""
Load and lightly clean the GA4 funnel analysis CSVs exported from BigQuery.
Outputs cleaned versions to data/processed/ for use in the dashboard.
"""

import pandas as pd

# --- Load raw data ---
funnel = pd.read_csv("data/raw/funnel_unique_users_nov2020.csv")
cart_split = pd.read_csv("data/raw/cart_vs_direct_checkout_nov2020.csv")

print("=== Funnel data ===")
print(funnel)
print()
print("=== Cart vs. direct checkout data ===")
print(cart_split)

# --- Light cleaning: funnel ---
# Enforce a logical funnel order (not alphabetical) for clean charting later
funnel_order = ["page_view", "view_item", "add_to_cart", "begin_checkout", "purchase"]
funnel["event_name"] = pd.Categorical(funnel["event_name"], categories=funnel_order, ordered=True)
funnel = funnel.sort_values("event_name").reset_index(drop=True)

# Add a conversion-from-previous-stage column
funnel["pct_of_page_view"] = (funnel["unique_users"] / funnel.loc[funnel["event_name"] == "page_view", "unique_users"].values[0] * 100).round(1)

# --- Light cleaning: cart split ---
# Make the boolean columns readable for charting/labels
cart_split["path"] = cart_split["did_add_to_cart"].map({True: "Added to cart first", False: "Skipped cart (direct checkout)"})
cart_split = cart_split[["path", "user_count", "purchase_rate_pct"]].sort_values("user_count", ascending=False).reset_index(drop=True)

print()
print("=== Cleaned funnel ===")
print(funnel)
print()
print("=== Cleaned cart split ===")
print(cart_split)

# --- Save cleaned outputs ---
funnel.to_csv("data/processed/funnel_cleaned.csv", index=False)
cart_split.to_csv("data/processed/cart_split_cleaned.csv", index=False)