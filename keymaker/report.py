from pydriller.metrics.process.change_set import ChangeSet


class ReportGenerator:
    def __init__(self):
      self.watchlist = []
      self.stats = {}

    def add_repo(self, repo_name):
      self.watchlist.append(repo_name.strip())
      print(f"Added {repo_name} to watchlist.")

    def extract_contributor_stats(self):
      pass

    def extract_repo_statistics(self):
      pass

    def generate_report(self):
      pass
