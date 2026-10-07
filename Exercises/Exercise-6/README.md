# Exercise 6: Real-Time Operations Monitoring and Alerting

This exercise demonstrates monitoring a simulated delivery app with Prometheus and Grafana.

## Steps to Run manually

1. Run the python app locally (or in Docker):
   ```bash
   pip install prometheus-client
   python delivery_metrics.py
   ```

2. Run Prometheus:
   ```bash
   docker run -d --name prometheus --network=host \
     -v $(pwd)/prometheus.yml:/etc/prometheus/prometheus.yml \
     -v $(pwd)/alert_rules.yml:/etc/prometheus/alert_rules.yml \
     prom/prometheus
   ```

3. Run Grafana:
   ```bash
   docker run -d --name grafana -p 3000:3000 grafana/grafana
   ```

4. Configure Grafana at `localhost:3000` to connect to Prometheus at `localhost:9090` (or `host.docker.internal:9090` depending on OS).
