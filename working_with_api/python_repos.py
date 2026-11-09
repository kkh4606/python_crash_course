import requests

url = "https://api.github.com/search/repositories"

url += "?q=language:python+sort:stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}

res = requests.get(url, headers=headers)
print(f"Status code: {res.status_code}")


# Convert the response object to dict
res_dict: dict = res.json()


print(f"Total repositories: {res_dict['total_count']}")
print(f"Completed results: {not res_dict['incomplete_results']}")

# Explore information about the repositories.
repo_dicts: list = res_dict["items"]
print(f"Repositories returned: {len(repo_dicts)}")


# Examine the first repository

repo_dict: dict = repo_dicts[0]
# print(f"\nKeys: {len(repo_dict)}")
# for key in sorted(repo_dict.keys()):
#     print(key)


print(f"\nSelected information about the first repository:")
print(f"Name: {repo_dict['name']}")
print(f"Owner: {repo_dict['owner']['login']}")
print(f"Stars: {repo_dict['stargazers_count']}")
print(f"Repository: {repo_dict['html_url']}")
print(f"Created: {repo_dict['created_at']}")
print(f"Updated: {repo_dict['updated_at']}")
print(f"Description: {repo_dict['description']}")
