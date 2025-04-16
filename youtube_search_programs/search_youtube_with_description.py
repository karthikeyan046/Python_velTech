from youtubesearchpython import VideosSearch

def search_youtube_with_description(query):
    videos_search = VideosSearch(query, limit=5)
    results = videos_search.result()['result']
    for video in results:
        print(f"Title: {video['title']}")
        print(f"Link: {video['link']}")
        print(f"Description: {video['descriptionSnippet']}")
        print('-' * 50)

search_youtube_with_description("python tutorial for beginners")
