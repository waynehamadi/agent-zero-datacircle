from helpers.tool import Tool, Response

from usr.plugins.datacircle.helpers import datacircle


class DatacircleProvider(Tool):
    async def execute(self, **kwargs):
        return Response(message=await datacircle.run(datacircle.provider, kwargs), break_loop=False)
