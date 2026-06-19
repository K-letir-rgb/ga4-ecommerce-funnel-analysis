SELECT
  event_name,
  COUNT(*) AS event_count
FROM
  `bigquery-public-data.ga4_obfuscated_sample_ecommerce.events_*`
WHERE
  _TABLE_SUFFIX BETWEEN '20201101' AND '20201130'
  AND event_name IN ('page_view', 'view_item', 'add_to_cart', 'begin_checkout', 'purchase')
GROUP BY
  event_name
ORDER BY
  event_count DESC