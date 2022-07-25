def counter(keyword: str, paragraph: str) -> int:
    return paragraph.count(keyword)


print(counter("b", "betty bought some butter but the butter was a bit bitter so betty bought some more bitter butter so make the bitter butter better"))
