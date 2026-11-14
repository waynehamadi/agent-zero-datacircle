from helpers.tool import Tool, Response

from usr.plugins.datacircle.helpers import datacircle


class DatacircleBestPlans(Tool):
    async def execute(self, **kwargs):
        return Response(message=await datacircle.run(datacircle.best_plans, kwargs), break_loop=False)
