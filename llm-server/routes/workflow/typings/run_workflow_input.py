from typing import Optional
from werkzeug.datastructures import Headers


# This is the api payload and doesnot represent workflow schema, use WorkflowDataType from opencopilot types for that
class WorkflowData:
    def __init__(
        self,
        text: str,
        headers: Headers,
        server_base_url: str,
        swagger_url: Optional[str],
        app: Optional[str],
    ) -> None:
        self.text = text
        self.headers = headers
        self.server_base_url = server_base_url
        self.swagger_url = swagger_url
        self.app = app  # example trello
