# DESIGN.md

# Overview
A simple REST API: GET /convert?lbs=<number> → returns JSON with:
- lbs: original input
- kg: result (rounded to 3 decimals)
- formula: conversion string

Errors:
- 400 if lbs missing or not a number
- 422 if negative or non-finite (NaN/Inf)

# Architecture & Rationale
- Flask: chosen for speed and simplicity.
- Gunicorn: WSGI server: production-grade, concurrency support.
- systemd: keeps service running, restarts on reboot.
- NGINX: reverse proxy on port 80 → forwards to Gunicorn on 8080.

# Flow
Client → NGINX (80) → Gunicorn (127.0.0.1:8080) → Flask (convert.py:app).

# Error Handling
- Missing or non-numeric → 400 Bad Request.
- Negative or non-finite (NaN/Inf) → 422 Unprocessable Entity.
- Conversion formula applied with rounding to 3 decimals.

# Security Hygiene
- Security Group rules:
  - SSH (22) restricted to my IP.
  - HTTP (80) open for testing.
- Service runs as non-root (ec2-user).
- Logs handled by journald; optional cap via etc/systemd/journald.conf.

# Log Rotation
The service logs are captured by systemd via journald. To prevent unlimited growth, log size can be capped in /etc/systemd/journald.conf:
[Journal]
SystemMaxUse=100
After updating, run sudo systemctl restart systemd-journald


# Reliability
- Managed by systemd: auto-restarts, survives reboot.
- systemctl enable ensures startup at boot.
- NGINX provides a stable, standard HTTP interface.

# Alternative
Node/Express was suggested; Python/Flask chosen for familiarity and rapid development.

---

