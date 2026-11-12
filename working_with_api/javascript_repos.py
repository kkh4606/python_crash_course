import json

import requests
import plotly.express as px

url = "https://api.github.com/search/repositories"

url += "?q=language:javascript+sort:stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}

res = requests.get(url, headers=headers)
print(f"Status code: {res.status_code}")


# Convert the response object to dict
res_dict: dict = res.json()


print(f"Total repositories: {res_dict['total_count']}")
print(f"Completed results: {not res_dict['incomplete_results']}")

# Explore information about the repositories.
repo_dicts: list[dict] = res_dict["items"]
print(f"Repositories returned: {len(repo_dicts)}")


print("\nSelected information about each repository: ")


repo_links, stars, hover_texts = [], [], []

for repo_dict in repo_dicts:

    # Turn repo names into active links
    repo_name = repo_dict["name"]
    repo_url = repo_dict["html_url"]
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)

    stars.append(repo_dict["stargazers_count"])

    # Build hover texts.

    owner = repo_dict["owner"]["login"]
    description = repo_dict["description"]
    hover_text = f"{owner}<br />{description}"

    hover_texts.append(hover_text)


title = "Most-Starred repository Javascript"
labels = {"x": "Repository", "y": "Stars"}
fig = px.bar(x=repo_links, y=stars, title=title, labels=labels, hover_name=hover_texts)
fig.update_layout(
    title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20
)


fig.show()
