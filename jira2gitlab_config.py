################################################################
# Jira options
################################################################

JIRA_URL = 'https://jira.jacoti.com'
JIRA_API = f'{JIRA_URL}/rest/api/2'

# Bitbucket URL, if available, is only used in pattern-matching
# to translate issue references to commits.
BITBUCKET_URL = "https://bitbucket.jacoti.com"

# How many items to request at a time from Jira (usually not more than 1000)
JIRA_PAGINATION_SIZE=100

# the Jira Epic custom field
JIRA_EPIC_FIELD = 'customfield_10303'

# the Jira Sprints custom field
JIRA_SPRINT_FIELD = 'customfield_10300'

# the Jira story points custom field
JIRA_STORY_POINTS_FIELD = 'customfield_10308'

# Custom JIRA fields
JIRA_CUSTOM_FIELDS = {
#    'customfield_14200': 'Metadata 1',
#    'customfield_14201': 'Metadata 2',
}

################################################################
# Gitlab options
################################################################

GITLAB_URL = 'https://gitlab.jacoti.dev'
GITLAB_API = f'{GITLAB_URL}/api/v4'

# Support Gitlab Premium features (e.g. epics and "blocks" issue links)
GITLAB_PREMIUM = False

################################################################
# Import options
################################################################

# set this to false if JIRA / Gitlab is using self-signed certificate.
VERIFY_SSL_CERTIFICATE = False

# PREFIX_LABEL is used with all existing Jira labels
PREFIX_LABEL = ""

# PREFIX_COMPONENT is used with existing Jira components when no match is found in ISSUE_COMPONENT_MAP
# NOTE: better NOT to use a prefix for components, otherwise only 1 component will be imported in Gitlab
PREFIX_COMPONENT = ""

# PREFIX_PRIORITY is used with existing Jira priorities when no match is found in ISSUE_PRIORITY_MAP
PREFIX_PRIORITY = "P::"

# Whether to migrate issue attachments
MIGRATE_ATTACHMENTS = True

# Whether to migrate worklogs as issue comment with /spend quick-action.
MIGRATE_WORLOGS = True

# Jira users are mapped to Gitlab users according to USER_MAP, with the following two exceptios:
# - Jira user 'jira' is mapped to Gitlab user 'root'
# - Jira users that are not in USER_MAP are mapped to Gitlab user 'root'
# If MIGRATE_USERS is True, mapped Gitlab users that don't exist yet in Gitlab will be migrated automatically
# If MIGRATE_USERS is False, all actions performed by a non-existing Gitlab user will be performed by Gitlab user 'root'
MIGRATE_USERS = True

# When MIGRATE_USERS is True, new users can be created in Gitlab.
# This is the *temporary* password they get.
NEW_GITLAB_USERS_PASSWORD = "l29OL72DesOrWsK5"

# If (new or exisiting) Gitlab users are not made admins during the import,
# the original timestamps of all user actions cannot be imported. Instead, the timestamp of the import will be used.
# When this option is enabled, users are made admin and changed back to their original role after the import. 
# If users cannot be changed back to non-admin, this is reported at the end of the import.
# This feature is recommended, but to be used with caution. Check users' status in Gitlab after the import.
MAKE_USERS_TEMPORARILY_ADMINS = True

# Prefix issue titles with "[PROJ-123]" (Jira issue-key)
ADD_JIRA_KEY_TO_TITLE = True

# If REFERECE_BITBUCKET_COMMITS is enabled, tries to translate Jira issue references in Bitbucket to Gitlab issue references
# Disable if the Jira instance does not have an active link to Bitbucket at the moment of the import
# Disable if not needed, to increase performance (more calls are needed for each issue)
# Limitations:
# - Bitbucket repositories need to be imported in Gitlab with the same project name (the group name can change)
# - This feature only works if the issue project and the commit project are in the same Gitlab group
REFERECE_BITBUCKET_COMMITS = True

################################################################
# Import mappings
################################################################

# Jira - Gitlab group/project mapping
# Groups are not created. They must already exist in Gitlab.
PROJECTS = {
#    'SYS': 'migration-sandbox/sysadmin',
    'WEB': 'migration-sandbox/web/jacoti-website',
}

# Bitbucket - Gitlab mapping
# *Not* used to migrate Bitbucket repos (use Gitlab's integration for that)
# Used to map references from issues to commits in Bitbucket repos that are migrated to Gitlab
# Make sure you use the correct casing for Bitbucket: project key is all upper-case, repository is all lower-case
PROJECTS_BITBUCKET = {
  'WEB/jacoti-website': 'migration-sandbox/web/jacoti-website',
}

# Jira - Gitlab username mapping
USER_MAP = {
    'alex'      : 'alex', 
    'amaury'    : 'amaury',
    'baptiste'  : 'baptiste' ,
    'curro'     : 'curro'    ,
    'diego'     : 'diego'    ,
    'etienne'   : 'etienne'  ,
    'gergely'   : 'gergely'  ,
    'gi'        : 'gi'       ,
    'jonatan'   : 'jonatan'  ,
    'jorge'     : 'jorge'    ,
    'julia'     : 'julia'    ,
    'kamil'     : 'kamil'    ,
    'mateo'     : 'mateo'    ,
    'nico'      : 'nico'     ,
    'num'       : 'num'      ,
    'oscar'     : 'oscar'    ,
    'victor'    : 'victor'   ,
    'Ayush.saxena' : 'Ayush.saxena',
    'goretty'   : 'goretty',
    'nikhil.ugale' : 'nikhil.ugale',
}

# Map Jira issue types to Gitlab labels
# Unknown issue types are mapped as generic labels
ISSUE_TYPE_MAP = {
    'Bug': 'T::bug',
    'Improvement': 'T::improvement',
    'New Feature': 'T::new feature',
    'Spike': 'T::spike',
    'Epic': 'T::epic',
    'Story': 'T::story',
    'Task': 'T::task',
    'Sub-task': 'T::task',
    'Concern': 'T::concern',
    'Requirement': 'T:requirement',
}

# Map Jira components to labels
# NOTE: better NOT to use a prefix for components, otherwise only 1 component will be imported in Gitlab
ISSUE_COMPONENT_MAP = {
    'Component1': 'component1',
    'Component2': 'component2'
}

# Map Jira priorities to labels
ISSUE_PRIORITY_MAP = {
    'Trivial': 'P::trivial',
    'Minor': 'P::minor',
    'Major': 'P::normal',
    'Critical': 'P::critical',
    'Blocker': 'P::blocker',
}

# Map Jira resolutions to labels
ISSUE_RESOLUTION_MAP = {
    'Cannot Reproduce': 'S::can\'t reproduce',
    'Duplicate': 'S::duplicate',
    'Incomplete': 'S::incomplete',
    'Won\'t Do': 'S::won\'t do',
    'Won\'t Fix': 'S::won\'t fix',
    'Unresolved': 'S::unresolved',
    'Done': 'S::done',
    'Fixed': 'S::fixed',
}

# Map Jira statuses to labels
ISSUE_STATUS_MAP = {
    'Approved': 'S::approved',
    'Awaiting documentation': 'S::needs doc',
    'In Progress': 'S::in progress',
    'In Review': 'S::in review',
    'Awaiting payment': 'S::awaiting payment' , 
    'Backlog'         : 'S::backlog'         ,
    'Cancelled'       : 'S::cancelled'       ,
    'Closed'          : 'S::closed'          ,
    'Done'            : 'S::done'            ,
    'Open'            : 'S::open'            ,
    'Paid'            : 'S::paid'            ,
    'Rejected'        : 'S::rejected'        ,
    'Reopened'        : 'S::reopened'        ,
    'Resolved'        : 'S::resolved'        ,
    'Selected for Development': 'S::selected for development',
}

# These Jira statuses will cause the corresponding Gitlab issue to be closed
ISSUE_STATUS_CLOSED = {
  'Awaiting documentation',
}

# Set colors for single labels or group of labels
LABEL_COLORS = {
#    'S::in review': '#0000ff'
}
# for key, value in ISSUE_COMPONENT_MAP.items():
#     LABEL_COLORS[value] = '#e6e6fa'
# for key, value in ISSUE_PRIORITY_MAP.items():
#     LABEL_COLORS[value] = '#8fbc8f'
