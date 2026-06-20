import pytest
from thumbzilla_api import Client


@pytest.mark.asyncio
async def test_search():
    client = Client()
    idx = 0

    async for video in client.search(query="nancy a"):
        idx += 1
        assert isinstance(video.title, str) and len(video.title) > 0

        if idx >= 3:
            break