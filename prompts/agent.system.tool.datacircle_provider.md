### datacircle_provider
one provider on Datacircle: each API it sells, its rank on each and its best plan there
use it when the user asks about a provider, like Apollo or Bright Data
args: `slug` (the provider's slug or name, like "bright-data" or "Bright Data")
usage:
~~~json
{
    "thoughts": ["The user asks what Apollo sells and how it ranks"],
    "headline": "Getting Apollo's ranks on Datacircle",
    "tool_name": "datacircle_provider",
    "tool_args": {
        "slug": "apollo"
    }
}
~~~
