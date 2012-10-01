def Crawl_Web(seed):
	tocrawl = [seed]
	crawled = []
	index = []
	while tocrawl :
		page = tocrawl.pop()
		if page not in crawled:
			content = get_page(page)
			add_page_to_index(index,page,content)
			union(tocrawl,get_all_links(get_page(page)))
			crawled.append(page)

	return index