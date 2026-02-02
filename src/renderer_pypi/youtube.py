from renderer_pypi.custom_exception import InvalidURLException
from renderer_pypi.logger import logger
import re
from IPython.display import HTML, display

def render_youtube_video(url: str, width: int = 780, height: int = 315):
    try:
        # pass
        regex = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
        match = re.search(regex, url)
        if not match:
            raise InvalidURLException("The provided YouTube URL is invalid.")
        video_id = match.group(1)

        embed_url = f"https://www.youtube-nocookie.com/embed/{video_id}"

        iframe = f"""
        <iframe width="{width}" height="{height}"
        src="{embed_url}" frameborder="0"
        title="YouTube video player"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen></iframe>
        """
        display(HTML(iframe))
        logger.info(f"Successfully rendered YouTube video for URL: {url}")
        return "success"
    
    except Exception as e:
        raise e