### datacircle_list_apis
every GTM API on Datacircle (datacircle.dev): each API's slug, how many plans and providers it has, its best plan and its pages
use it to find an API's slug for datacircle_best_plans or datacircle_search_plans
args: `query` (optional words of the API's name, like "email finder"), `limit` (optional, default 20)
usage:
~~~json
{
    "thoughts": ["I need the slug of the email finder API"],
    "headline": "Listing Datacircle's APIs",
    "tool_name": "datacircle_list_apis",
    "tool_args": {
        "query": "email finder"
    }
}
~~~
