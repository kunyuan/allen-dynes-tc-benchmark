# Minimal Python image for the closed-form Allen-Dynes Tc task.
# No Julia/DFTK/HPC — the workflow is pure arithmetic.
FROM python:3.12-slim

RUN pip install --no-cache-dir numpy==2.1.3

WORKDIR /app

# Public development data (agent-facing). solution/ and tests/ are applied by
# Harbor and are NOT copied here, so the hidden materials and gold never leak.
COPY packet/ /app/packet/

CMD ["/bin/bash"]
