import re
from datetime import datetime


def validate_date(input_date: str) -> datetime:
    if len(input_date) < 2:
        return datetime.now()
    return datetime.strptime(input_date, "%Y-%m-%dT%H:%M:%SZ")


def validate_text(text: str) -> str:
    """Validate getting text"""
    return re.sub(
        r"&lt;b&gt;|&lt;/b&gt;|<b>|</b>|&#39;|&amp;#39;|&amp;amp;|&amp;nbsp;|&amp;middot;|&quot;|&nbsp;|&middot;",
        "",
        text,
    )
