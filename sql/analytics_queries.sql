SELECT 
    a.agent_name,
    COUNT(f.call_id) AS total_calls
FROM fact_calls f
JOIN dim_agent a ON f.agent_id = a.agent_id
GROUP BY a.agent_name
ORDER BY total_calls DESC;

SELECT
    a.agent_name,
    ROUND(
        100.0 * SUM(CASE WHEN f.call_outcome = 'CONVERTED' THEN 1 ELSE 0 END)
        / COUNT(f.call_id),
        2
    ) AS conversion_rate
FROM fact_calls f
JOIN dim_agent a ON f.agent_id = a.agent_id
GROUP BY a.agent_name
ORDER BY conversion_rate DESC;


SELECT
    a.agent_name,
    ROUND(AVG(f.call_duration), 2) AS avg_call_duration
FROM fact_calls f
JOIN dim_agent a ON f.agent_id = a.agent_id
GROUP BY a.agent_name
ORDER BY avg_call_duration DESC;


SELECT
    d.year,
    d.month,
    COUNT(f.call_id) AS total_calls
FROM fact_calls f
JOIN dim_date d ON f.call_date_id = d.date_id
GROUP BY d.year, d.month
ORDER BY d.year, d.month;


SELECT
    l.lead_source,
    COUNT(f.call_id) AS total_calls,
    SUM(CASE WHEN f.call_outcome = 'CONVERTED' THEN 1 ELSE 0 END) AS conversions
FROM fact_calls f
JOIN dim_lead l ON f.lead_id = l.lead_id
GROUP BY l.lead_source
ORDER BY conversions DESC;


