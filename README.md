# Standup SaaS – Public Demo

## Overview
This is a **public demo version** of a Slack-based standup automation system.

The original project was built as a SaaS-style backend for freelance use and
contains sensitive credentials and client-specific logic.
Those parts are intentionally excluded here.

This demo focuses on **architecture, security thinking, and workflow design**.

---

## What This Demonstrates
- Secure webhook handling using HMAC-SHA256 (Slack-style)
- State-machine driven user flows
- Multi-tenant aware design (team_id isolation)
- Cron-style automation endpoints
- Backend-first SaaS thinking

---

## Original System Capabilities (Production)
- Slack Events API integration
- PostgreSQL with connection pooling
- Timezone-safe standup tracking (India time fix)
- Secure cron triggers
- Team-level summary reports

---

## Why This Repo Exists
To demonstrate **how I design and think about AI-enabled backend systems**,
without exposing production secrets or freelance client data.
