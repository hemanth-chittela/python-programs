#To delete branches in github
import requests
Owner="<give_the_name_of_the_owner"
Repo="<give_repo_name"
Branch_names=["<give_branch_names_you_want_to_delete>"]
url=f"https://api.github.com/repos/{Owner}/{Repo}/git/refs/heads/{Branch_names}"
url2=f"https://api.github.com/repos/{Owner}/{Repo}/git/refs/heads/{Branch_names}"
key="<Give_API_Key"
#url=requests.get(url)
#print(url)
passing_key={
    "Authorization": f"token {key}",
    "Accept": "application/json"
}
for each_branch in Branch_names:
    url2=f"https://api.github.com/repos/{Owner}/{Repo}/git/refs/heads/{each_branch}"
    deleting_branches=requests.delete(url2,headers=passing_key)
    if deleting_branches.status_code==204:
        print(f"The branch {each_branch} is deleted")
    else:
        print(f"The branch {each_branch} is not yet deleted or already has been deleted")

