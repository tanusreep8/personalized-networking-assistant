import wikipediaapi

wiki = wikipediaapi.Wikipedia(
    language='en',
    user_agent='PersonalizedNetworkingAssistant/1.0'
)

def fact_check(topic):

    page = wiki.page(topic)

    if page.exists():
        return page.summary[:500]

    return "No information found."


# Test
if __name__ == "__main__":

    topic = "Blockchain"

    result = fact_check(topic)

    print("\nFact Check Result:\n")
    print(result)