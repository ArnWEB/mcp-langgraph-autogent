from mcp.server.fastmcp import FastMCP

mcp = FastMCP("CrawlUrls")


@mcp.tool()
def carwl_urls(url: str) -> dict:
    """
    Crawls the given URL and extracts defect descriptions in raw unstructured text.

    Example:
    Input: "https://example.com"
    Output: [
      "Login page fails to load under poor network conditions.",
      "User receives error 403 when uploading files over 5MB.",
    ]
    """
    return """Login button is unresponsive on the first click, user has to click multiple times to proceed.

            Users are unable to upload JPEG files as profile pictures; the upload fails without any clear error message.

            Search bar doesn't return any results for keywords with special characters.

            Payment gateway intermittently fails during checkout, causing transaction rollbacks.

            On mobile devices, the navigation menu overlaps the main content and cannot be closed.

            API returns a 500 error when fetching user details for accounts created before 2022.

            Page load time on the dashboard exceeds 10 seconds during peak usage hours.

            Password reset email is not being sent even though the UI shows a success message.

            Session timeout is not enforced, and users remain logged in indefinitely.

            Dropdown values are not loading dynamically in the new user registration form"""


# @mcp.tool()
# def impact_analysis(defect_descriptions: str) -> str:
#     """Impact analysis based on the defect description in plain text"""
#     return "return imapact analysis"


if __name__ == "__main__":
    mcp.run(transport="stdio")
