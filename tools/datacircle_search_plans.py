from helpers.tool import Tool, Response

from usr.plugins.datacircle.helpers import datacircle


class DatacircleSearchPlans(Tool):
    async def execute(self, **kwargs):
        return Response(message=await datacircle.run(datacircle.search_plans, kwargs), break_loop=False)
