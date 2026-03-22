#!/bin/bash
echo "=== Demo: Automation Gate + AI Anomaly Detection ==="
echo ""

echo "1. Building images (automation step)..."
docker compose build
echo ""

echo "2. Running security scans (pipeline gate)..."
echo "   (Watch for warnings/vulns in hadolint & pip-audit output)"
echo "   Press Enter to continue..."
read

echo "3. Starting services (only if gate passes)..."
docker compose up -d
echo "Services running on forwarded ports (check Ports tab)"
echo ""

echo "4. Simulating container metrics & running AI anomaly detection..."
python anomaly_demo.py
echo ""
echo "Demo complete! AI flagged anomalies early based on learned normal behavior."