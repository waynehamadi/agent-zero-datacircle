# Datacircle for Agent Zero

Find the best GTM APIs. We benchmark all the GTM APIs and we put the results on our website.

Our website: https://datacircle.dev

This Agent Zero plugin gives your agent four tools on Datacircle's open API, https://api.datacircle.dev/v1. You need no key and no account.

| Tool | What the tool gives | Call |
| --- | --- | --- |
| `datacircle_list_apis` | Every GTM API on Datacircle, with the API's slug, number of plans, number of providers and best plan | `GET /apis` |
| `datacircle_best_plans` | One API's plans, sorted by score out of 100, best first. Each plan comes with a rank and a price per 1,000 calls | `GET /apis/{slug}/best` |
| `datacircle_search_plans` | Plans that match a provider or plan name, on all APIs or on one API. Sort by score, provider or price | `GET /plans` |
| `datacircle_provider` | The APIs a provider sells, and the provider's rank on each API | `GET /providers/{slug}` |

## Install

In Agent Zero, open the plugin installer, pick the Git tab and paste this address: `https://github.com/waynehamadi/agent-zero-datacircle`.

Or copy the files of this repository into the folder `usr/plugins/datacircle/` in Agent Zero.

Then ask your agent, for example: "Which email finder API is best for under $5 per 1,000?"

## Network

Each tool call makes one HTTPS GET request to https://api.datacircle.dev/v1 and nothing else. The request holds only the tool's own arguments: no key, no config, nothing from your files or chats. The API takes up to 60 calls a minute from one IP address. The tool waits once, for a minute at most, when the API asks the tool to wait. The tool shows your agent the API's answer. The plugin has no dependencies, stores nothing and runs nothing in the background.

## Remove

Disable the plugin or delete `usr/plugins/datacircle/`. The plugin writes nothing outside that folder.

## Tests

The tests are in `dev/`, outside the plugin's runtime files. Each test calls the real API.

```
pip install -r dev/requirements-dev.txt
pytest -c dev/pytest.ini
```

We tested the plugin on Agent Zero v2.15.

## Links

- Datacircle: https://datacircle.dev
- The API: https://datacircle.dev/api
- The API's spec: https://api.datacircle.dev/v1/openapi.json
- What each key means: https://datacircle.dev/fields

MIT license.
