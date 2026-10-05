import sys
import anyio

from mcp import Client, StdioServerParameters


server = StdioServerParameters(
    command=r"D:\Python\Py-Projects\first_mcp_project\.venv\Scripts\python.exe",
    args=["server_test.py"],
)


async def main():
    async with Client(server) as client:

        tools = await client.list_tools()

        print([tool.name for tool in tools.tools])

        tool = sys.argv[1]
        a = int(sys.argv[2])
        b = int(sys.argv[3])

        result = await client.call_tool(
            tool,
            {"a": a, "b": b}
        )

        print(result)


if __name__ == "__main__":
    anyio.run(main)