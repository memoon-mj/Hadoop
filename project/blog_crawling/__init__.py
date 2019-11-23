import blog_crawler

keyword = "데이트"

blog = blog_crawler.call_and_print(keyword, 1)
for i in blog:
    print(i)

