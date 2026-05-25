# test
def get_summary(texts) -> tuple[str | tuple[str,tuple[int,int,int]]]:
    ans = []
    for text in texts:
        ans.append(text)
    return tuple(ans)

lines = ["Text thing",
         ("Tuple Thing", (55, 55, 55))]
x = get_summary(lines)
print(x)