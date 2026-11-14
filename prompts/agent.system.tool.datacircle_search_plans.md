### datacircle_search_plans
search every plan on Datacircle: all APIs or one, the plans whose provider or plan name holds every word of `query`
use it to find one provider's plans, or an API's cheapest plans with sort "price"
args: `api` (optional, an API's name or slug), `query` (optional words of the provider's or plan's name), `sort` (optional: "score" (default), "provider" or "price"), `limit` (optional, 1 to 50, default 10), `offset` (optional, default 0)
the answer's `total` counts every plan found
usage:
~~~json
{
    "thoughts": ["The user wants the cheapest email finder plans"],
    "headline": "Searching email finder plans by price",
    "tool_name": "datacircle_search_plans",
    "tool_args": {
        "api": "email-finder",
        "sort": "price",
        "limit": 5
    }
}
~~~
