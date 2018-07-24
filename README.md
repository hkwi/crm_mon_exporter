prometheus exporter for pacemaker `crm_mon`.

Start the daemon like this:

```
FLASK_APP=crm_mon_exporter FLASK_RUN_HOST=0.0.0.0 FLASK_RUN_PORT=9099 flask run
```

Metrics
----

`crm_mon_current_dc` will be exported with nodes in the group in metric labels. 
This is suitable for table format, which was [added in grafana 4.3](http://docs.grafana.org/guides/whats-new-in-v4-3/#prometheus-table-data-column-per-label).
