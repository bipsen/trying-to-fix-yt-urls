from yt_converter import convert_to_channel_id

URLS = """https://www.youtube.com/@LofiGirl
https://www.youtube.com/@Jazz_For_Soul
https://www.youtube.com/@DeepMoodRadio.
https://www.youtube.com/@GreenredProductions""".split()

for url in URLS:
    result = convert_to_channel_id(url)
    # result['conversion_message']  har den nye url
    print(result)
