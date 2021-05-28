from github import Github
from pypresence import Presence
import time

RPC = Presence('847761528257642496')
RPC.connect()


g= Github()


def update_presence():
  global g
  global RPC
  repos = g.get_user("KoenvdStroom").get_repos()
  last_updated = ""
  for repo in repos:
    if last_updated == "":
      last_updated = repo
    else:
      if last_updated.updated_at < repo.updated_at:
        last_updated = repo

  RPC.update(state=last_updated.full_name, 
  details="Last updated:", 
  large_image="octocat", 
  large_text="github.com/KoenvdStroom", 
  buttons=[{"label": "Github", "url": "https://github.com/KoenvdStroom"}, {"label": last_updated.full_name, "url": "https://github.com/KoenvdStroom/"+ last_updated.name}]
  )
while True:
  update_presence()
  time.sleep(300)
