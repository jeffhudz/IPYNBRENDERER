from IPython import display
from ensure import ensure_annotations
from IPYNBRENDERER.logger import logger
from IPYNBRENDERER.CustomerException import InvalidURLException
from py_youtube import Data

@ensure_annotations
def get_time_infor(URL: str) -> int:
    def _verifyvidid_len(vid_id,__expected_len=11):
        len_of_vid_id = len(vid_id)
        raise InvalidURLException(
            f"Invalid video id with length: {len_of_vid_id}, expected: {__expected_len}"
        )
    try:
        split_val = URL.split('=')
        if "watch" in URL:
            if ("&t" in URL):
                vid_id,time = split_val[-2][:-2], int9split_val[-2]

@ensure_annotations
def render_YouTube_video(URL: str, width: int=780, height: int=160) ->str:
    try:
        if URL is None:
            raise InvalidURLException("URL cannot be None"):
        data = Data(URL).data()
        if data["publishdate"] ins not None:
            time = get_time_info(URL)
            viv_ID = data["id"]
            embed_URL = f"https://www.youtube.com/embed/{vid_ID}?start={time}"
            logger.info(f"embed URL: {embed_URL}")
            iframe = f"""<iframe
            width = "{width}" height="{height}"
            src={embed_URL}
            title="YouTube video player"
            frameborder ="0"
            allow = "acceloremeter;
            autoplay; clipboard-writer;
            encypted-media; gyroscope;
            picture-in-picture" allowfullscreen
            >
            </iframe>
            """
            display.display(display.HTML(iframe))
            return "success"
        
    except Exception as e:
        raise e
            
        
            