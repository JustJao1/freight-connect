# Freight Connect

A freight marketplace prototype for drivers who need replacement loads and companies with transport requests.

[Live demo](https://portfolio-suite-jv.vercel.app/freight) · [Portfolio](https://jv-software-portfolio.vercel.app/)

**Owner and maintainer:** João Victor da Silva ([JustJao1](https://github.com/JustJao1)).

## What it does

- Search and publish fictional loads using a catalog of 5,571 municipal records across 27 Brazilian federal units.
- Filter by origin, destination, vehicle and capacity; save favorites.
- Estimate trip costs and net revenue; submit and evaluate proposals.
- View geographic endpoints and road routes through Leaflet, OpenStreetMap and OSRM.

## Architecture and limits

HTML, CSS and JavaScript frontend; Python domain operations and temporary SQLite storage. Browser-local snapshots isolate demo data. It is not a production marketplace or a multi-user transport service. Routes use the OSRM car profile, not truck restrictions, and depend on the external service. The municipality dataset is distributed with its original license.

## Local setup

Python 3.11+. Create and activate a virtual environment, then run:

```sh
python -m pip install -r requirements.txt
python run.py
```

Open http://127.0.0.1:8765/. The local server binds only to loopback. Internet access is required for external map assets and route lookup.

Run `python -m unittest discover -s tests -v` to check core operations. GitHub Actions also checks Python compilation and the tests. External service and browser validation are separate.

[Ownership](OWNERSHIP.md) · [Third-party notices](THIRD_PARTY_NOTICES.md)


## Engineering evidence / Evidências de engenharia

[Architecture, decisions and bilingual walkthrough / Arquitetura, decisões e demonstração bilíngue](docs/engineering-quality.md).

Measured snapshot / Registro de 28/11/2026:

PT: 2 testes aprovados; 43% de cobertura (linhas e ramificações no escopo instrumentado); contêiner e health check aprovados.

EN: 2 tests passed; 43% branch-inclusive coverage in the instrumented scope; container and health check passed.

[Actual GitHub Actions run / Execução real de CI](https://github.com/JustJao1/freight-connect/actions/runs/46110650940).

[Portfolio evidence / Evidências no portfólio](https://justjao1.vercel.app/#engineering).
