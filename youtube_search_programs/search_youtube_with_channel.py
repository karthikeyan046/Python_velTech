from youtubesearchpython import VideosSearch

def search_youtube_with_channel(query):
    videos_search = VideosSearch(query, limit=5)
    results = videos_search.result()['result']
    for video in results:
        print(f"Title: {video['title']}")
        print(f"Link: {video['link']}")
        print(f"Channel: {video['channel']['name']}")
        print(f"Channel URL: {video['channel']['url']}")
        print('-' * 50)

search_youtube_with_channel("python tutorial for beginners")
