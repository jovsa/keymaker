from report import ReportGenerator
import argparse


parser = argparse.ArgumentParser(
    description='Worker file for repo statistics.')
parser.add_argument('-w', '--watchlist', type=str, default='watchlist.txt', required=False,
                    help='Watchlist input file that lists all the repos that would compute various statistics for. [REQUIRED]')

if __name__ == '__main__':
    args = vars(parser.parse_args())
    report = ReportGenerator()
    with open(args['watchlist'], 'r') as f:
        for repo_name in f.readlines():
            report.add_repo(repo_name)
            report.extract_contributor_stats()
