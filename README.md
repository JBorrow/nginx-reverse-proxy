nginx Reverse Proxy
===================

A very simple nginx reverse proxy setup.

This setup includes:

- The nginx container, running a reverse proxy to two sub-domains:
  - `/web` backed by a FastAPI service `webservice` running on port `5000`
  - `/api` backed by a FastAPI service `apiservice` running on port `12345`

These three components together allow you to go to:

- `localhost:80/web` to access the `webservice` container.
- `localhost:80/api` to access the `apiservice` container.

License
-------

WTFPL
