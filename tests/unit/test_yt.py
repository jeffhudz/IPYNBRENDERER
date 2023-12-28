import pytest
from IPYNBRENDERER.youtube import get_time_info
from IPYNBRENDERER.CustomerException import InvalidURLException

good_URL_data =[
    ("https://www.youtube.com/IATUT2qzDmU",0),
    ("https://www.youtube.com/watch?v=IATUT2qzDmU",0),
    ("https://www.youtube.com/watch?v=IATUT2qzDmU&t=42s",42)]

URL_id_bad_data =[
    ("https://www.youtube.com/watch?v==IATUT2qzDmU",),
    ("https://www.youtube.com/watch?v=IATUT2qzDmU==22"),
    ("https://www.youtube.com/watch?v==IATUT2qzDmUy&t=42s")]

@pytest.mark.parametrize("URL,response",good_URL_data)
def test_get_time_info(URL,response):
    assert get_time_info(URL)== response
    
@pytest.mark.parametrize("URL",URL_id_bad_data)
def test_get_time_info(URL):
    with pytest.raises(InvalidURLException):
        get_time_info(URL)