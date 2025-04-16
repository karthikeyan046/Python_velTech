from youtubesearchpython import VideosSearch

def search_youtube_by_views(query):
    videos_search = VideosSearch(query, limit=10)
    results = videos_search.result()['result']
    
    # Sort by view count in descending order
    sorted_results = sorted(results, key=lambda x: int(x['viewCount']['text'].replace(',', '')), reverse=True)
    
    for video in sorted_results[:5]:  # Limit to top 5
        print(f"Title: {video['title']}")
        print(f"Link: {video['link']}")
        print(f"View Count: {video['viewCount']['text']}")
        print('-' * 50)

search_youtube_by_views("python tutorial for beginners")
