### datacircle_best_plans
who is best for one GTM API: its plans best first by score out of 100, each with its rank, price per 1,000 and page
use it when the user asks which provider or plan is best for an API (email finder, LinkedIn profile, web scraping...)
args: `slug` (the API's slug from datacircle_list_apis, like "email-finder"), `limit` (optional, 1 to 50, default 10)
usage:
~~~json
{
    "thoughts": ["The user wants the best email finder API"],
    "headline": "Getting the best email finder plans",
    "tool_name": "datacircle_best_plans",
    "tool_args": {
        "slug": "email-finder",
        "limit": 5
    }
}
~~~
