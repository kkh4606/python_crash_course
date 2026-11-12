from operator import itemgetter

import requests

# Make an API call, and check the response
res = requests.get(url="https://hacker-news.firebaseio.com/v0/topstories.json")
print(f"Status code: {res.status_code}")


# Process information about each submission.
res_ids = res.json()
submission_dicts = []

for submission_id in res_ids:

    # Make a new API call for each submission.

    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    res = requests.get(url=url)
    print(f"id: {submission_id}\tstatus_code: {res.status_code}")
    res_dict = res.json()

    # Build a dictionary for each article.

    try:

        submission_dict = {
            "title": res_dict["title"],
            "hn_link": f"https://hacker-news.firebaseio.com/v0/item/{submission_id}",
            "comments": res_dict["descendants"],
        }

    except KeyError:
        pass

    else:

        submission_dicts.append(submission_dict)


submission_dicts = sorted(submission_dicts, key=itemgetter("comments"), reverse=True)

for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion Link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")
