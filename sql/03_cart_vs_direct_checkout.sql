WITH user_events AS (
  SELECT
    user_pseudo_id,
    MAX(event_name = 'add_to_cart') AS did_add_to_cart,
    MAX(event_name = 'begin_checkout') AS did_checkout,
    MAX(event_name = 'purchase') AS did_purchase
  FROM
    `bigquery-public-data.ga4_obfuscated_sample_ecommerce.events_*`
  WHERE
    _TABLE_SUFFIX BETWEEN '20201101' AND '20201130'
    AND event_name IN ('add_to_cart', 'begin_checkout', 'purchase')
  GROUP BY
    user_pseudo_id
)
SELECT
  did_add_to_cart,
  did_checkout,
  COUNT(*) AS user_count,
  ROUND(100 * COUNTIF(did_purchase) / COUNT(*), 1) AS purchase_rate_pct
FROM
  user_events
WHERE
  did_checkout = TRUE
GROUP BY
  did_add_to_cart, did_checkout