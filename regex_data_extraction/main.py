from extract_emails import extract_emails
from extract_urls import extract_urls
from extract_phone_numbers import extract_phone_numbers
from extract_credit_cards import extract_credit_cards
from extract_time import extract_time
from extract_html_tags import extract_html_tags
from extract_hashtags import extract_hashtags
from extract_currency import extract_currency

if __name__ == "__main__":
    text = """
    Here are some emails: user@example.com, test@mail.co.uk.
    Visit: https://example.com.
    Call: (123) 456-7890 or 123.456.7890.
    Credit Card: 1234-5678-9012-3456.
    Meeting time: 14:30 or 2:30 PM.
    HTML: <div>Sample div</div> <img src="image.jpg" alt="description"/>.
    Hashtags: #example #ThisIsAHashtag.
    Prices: $19.99, $1,234.56.
    """

    print("Emails:", extract_emails(text))
    print("URLs:", extract_urls(text))
    print("Phone Numbers:", extract_phone_numbers(text))
    print("Credit Cards:", extract_credit_cards(text))

    times_24, times_12 = extract_time(text)
    print("24-hour Time:", times_24)
    print("12-hour Time:", times_12)

    print("HTML Tags:", extract_html_tags(text))
    print("Hashtags:", extract_hashtags(text))
    print("Currency Amounts:", extract_currency(text))
