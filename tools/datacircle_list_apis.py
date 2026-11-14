from helpers.tool import Tool, Response

from usr.plugins.datacircle.helpers import datacircle


class DatacircleListApis(Tool):
    async def execute(self, **kwargs):
        return Response(message=await datacircle.run(datacircle.list_apis, kwargs), break_loop=False)
