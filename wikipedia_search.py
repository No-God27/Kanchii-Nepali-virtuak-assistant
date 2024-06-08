import wikipediaapi

def get_nepali_wikipedia_intro(word):
    user_agent = 'Kanchi (swapunil27@gmail.com)'  # id ra email bina kaam gardaina noobde le

    wiki_ne = wikipediaapi.Wikipedia(
        language='ne',
        extract_format=wikipediaapi.ExtractFormat.WIKI,
        user_agent=user_agent
    )

    page_ne = wiki_ne.page(word)

    if not page_ne.exists():
        return f"The page for '{word}' does not exist in Nepali Wikipedia."

    title = page_ne.title

    summary = page_ne.summary.split('\n')[0]

    return f"Title: {title}\nFirst line: {summary}"

word = input("Enter a word in Nepali: ")

intro = get_nepali_wikipedia_intro(word)
print(intro)
