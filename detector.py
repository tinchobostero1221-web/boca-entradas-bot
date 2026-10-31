
name: Boca Plateas Detector

on:
  workflow_dispatch:
  schedule:
    - cron: "*/5 * * * *"

jobs:
  revisar:
    runs-on: ubuntu-latest
    steps:
      - name: Descargar repositorio
        uses: actions/checkout@v4

      - name: Preparar Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Instalar dependencias
        run: pip install requests

      - name: Ejecutar detector
        run: python detector.py


