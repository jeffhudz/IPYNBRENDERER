import pytest
from IPYNBRENDERER.youtube import render_YouTube_video
from IPYNBRENDERER.custom_exception import InvalidURLException

class TestYTvideoRenderer:
    
    URL_test_success_data =[
        ("https://www.youtube.com/watch?v=IATUT2qzDmU","success"),
        ("https://www.youtube.com/watch?v=IATUT2qzDmU&t=42s","success")]

    URL_test_bad_data =[
        ("https://www.youtube.com/watch?v=IATUT2qzDmUtyty"),
        ("https://www.youtube.com/watch?v=IATUT2qzDmU00"),
        ("https://www.youtube.com/watch?v==IATUT2qzDmU"),
        ("https://www.youtube.com/watch?v==IATUT2qzDmU&t")
        ]

    @pytest.mark.parametrize("URL,response",URL_test_success_data)
    def test_render_YT_success(self,URL,response):
        assert render_YouTube_video(URL)== response
    
    @pytest.mark.parametrize("URL",URL_test_bad_data)
    def test_render_YT_failed(self, URL):
        with pytest.raises(InvalidURLException):
            render_YouTube_video(URL)










