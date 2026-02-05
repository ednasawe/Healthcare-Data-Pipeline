from etl.extract import extract

def test_extract():
    df = extract()
    assert not df.empty