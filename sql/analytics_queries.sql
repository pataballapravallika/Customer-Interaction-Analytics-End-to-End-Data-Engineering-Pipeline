SELECT 
    a.agent_name,
    COUNT(f.call_id) AS total_calls
FROM fact_calls f
JOIN dim_agent a ON f.agent_id = a.agent_id
GROUP BY a.agent_name
ORDER BY total_calls DESC;
