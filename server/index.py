#! /usr/bin/python
import indexers
import autocomplete
import time
from datetime import datetime
import indexers.github_helpers as helpers

helpers.create_index('history')
helpers.create_index('search')
helpers.create_index('autocomplete')


if __name__ == '__main__':
    start = time.mktime(datetime.now().timetuple())

    gh_repos, ghe_repos, jira_users, jira_projs = indexers.index()
    autocomplete.index(gh_repos, ghe_repos, jira_users, jira_projs)
    end = time.mktime(datetime.now().timetuple())
    print 'Completed: (%s secs)' % (end-start)
