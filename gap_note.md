# Jira documentation lineage gaps

Source: `exports/jira-help-2025-03-07/Jira Cloud Help Docs Markdown Export (7 March 2025).json`. The requested filename `atlassian_jira_cloud_help_docs_export_2025-03-07.json` was not present; this available export contains 40 pages.

`inventory_output.txt` contains the full loader printout: 89 lines (40 page lines, 43 flag lines, and 6 summary lines). Counts below are affected pages per field; a page can have gaps in multiple fields.

## Gap counts

| Field | Gaps |
| --- | ---: |
| source_file | 0 |
| url | 0 |
| last_updated | 3 |
| headings | 40 |

## last_updated

| Page | Exported value | Reason |
| --- | --- | --- |
| What are issue security levels? | `"07/02/2025"` | must be a real ISO date (YYYY-MM-DD) |
| Manage project roles | `null` | empty |
| Add, edit, and delete an issue type | `"14/01/2025"` | must be a real ISO date (YYYY-MM-DD) |

## headings

All 40 pages have a JSON-encoded string in `headings`, rather than a list. The loader flags each as `not a list` and does not coerce it. For the comparisons below only, the string is decoded and the body heading markers are removed using the loader's rules. The original export is unchanged.

| Page | Reasons |
| --- | --- |
| Manage project permissions | `headings` is a JSON-encoded string, not a list; omits body H1: Manage project permissions; decoded section titles match the remaining body headings in order. |
| What are permission schemes? | `headings` is a JSON-encoded string, not a list; omits body H1: What are permission schemes?; decoded section titles match the remaining body headings in order. |
| Grant the Browse projects permission to a group | `headings` is a JSON-encoded string, not a list; omits body H1: Grant the Browse projects permission to a group; decoded section titles match the remaining body headings in order. |
| What are issue security levels? | `headings` is a JSON-encoded string, not a list; omits body H1: What are issue security levels?; decoded section titles match the remaining body headings in order. |
| Manage global permissions | `headings` is a JSON-encoded string, not a list; omits body H1: Manage global permissions; decoded section titles match the remaining body headings in order. |
| Manage project roles | `headings` is a JSON-encoded string, not a list; omits body H1: Manage project roles; decoded section titles match the remaining body headings in order. |
| Create an issue and a subtask | `headings` is a JSON-encoded string, not a list; omits body H1: Create an issue and a subtask; decoded section titles match the remaining body headings in order. |
| Use advanced search with Jira Query Language (JQL) | `headings` is a JSON-encoded string, not a list; omits body H1: Use advanced search with Jira Query Language (JQL); decoded section titles match the remaining body headings in order. |
| Add a transition to a workflow | `headings` is a JSON-encoded string, not a list; omits body H1: Add a transition to a workflow; decoded section titles match the remaining body headings in order. |
| Configure columns on a board | `headings` is a JSON-encoded string, not a list; omits body H1: Configure columns on a board; decoded section titles match the remaining body headings in order. |
| Create and edit Jira automation rules | `headings` is a JSON-encoded string, not a list; omits body H1: Create and edit Jira automation rules; decoded section titles match the remaining body headings in order. |
| Create a notification scheme | `headings` is a JSON-encoded string, not a list; omits body H1: Create a notification scheme; decoded section titles match the remaining body headings in order. |
| Use functions in JQL queries | `headings` is a JSON-encoded string, not a list; omits body H1: Use functions in JQL queries; decoded section titles match the remaining body headings in order. |
| Configure Jira application options | `headings` is a JSON-encoded string, not a list; omits body H1: Configure Jira application options; decoded section titles match the remaining body headings in order. |
| Configure swimlanes on a board | `headings` is a JSON-encoded string, not a list; omits body H1: Configure swimlanes on a board; decoded section titles match the remaining body headings in order. |
| Use smart values in automation rules | `headings` is a JSON-encoded string, not a list; omits body H1: Use smart values in automation rules; decoded section titles match the remaining body headings in order. |
| Manage your personal notification settings | `headings` is a JSON-encoded string, not a list; omits body H1: Manage your personal notification settings; decoded section titles match the remaining body headings in order. |
| Edit multiple issues at the same time | `headings` is a JSON-encoded string, not a list; omits body H1: Edit multiple issues at the same time; decoded section titles match the remaining body headings in order. |
| Add conditions and validators to a workflow transition | `headings` is a JSON-encoded string, not a list; omits body H1: Add conditions and validators to a workflow transition; decoded section titles match the remaining body headings in order. |
| Save your search as a filter | `headings` is a JSON-encoded string, not a list; omits body H1: Save your search as a filter; decoded section titles match the remaining body headings in order. |
| Configure time tracking | `headings` is a JSON-encoded string, not a list; omits body H1: Configure time tracking; decoded section titles match the remaining body headings in order. |
| Link issues to other issues | `headings` is a JSON-encoded string, not a list; omits body H1: Link issues to other issues; decoded section titles match the remaining body headings in order. |
| Use your Scrum backlog | `headings` is a JSON-encoded string, not a list; omits body H1: Use your Scrum backlog; decoded section titles match the remaining body headings in order. |
| Configure outgoing email notifications | `headings` is a JSON-encoded string, not a list; omits body H1: Configure outgoing email notifications; decoded section titles match the remaining body headings in order. |
| Configure workflow schemes | `headings` is a JSON-encoded string, not a list; omits body H1: Configure workflow schemes; decoded section titles match the remaining body headings in order. |
| Create a custom field | `headings` is a JSON-encoded string, not a list; omits body H1: Create a custom field; decoded section titles match the remaining body headings in order. |
| Run automation rules on a schedule | `headings` is a JSON-encoded string, not a list; omits body H1: Run automation rules on a schedule; decoded section titles match the remaining body headings in order. |
| Work with issues in the list view | `headings` is a JSON-encoded string, not a list; omits body H1: Work with issues in the list view; decoded section titles match the remaining body headings in order. |
| Manage webhooks | `headings` is a JSON-encoded string, not a list; omits body H1: Manage webhooks; decoded section titles match the remaining body headings in order. |
| Create a board | `headings` is a JSON-encoded string, not a list; omits body H1: Create a board; decoded section titles match the remaining body headings in order. |
| Plan work in the calendar view | `headings` is a JSON-encoded string, not a list; omits body H1: Plan work in the calendar view; decoded section titles match the remaining body headings in order. |
| Add, edit, and delete an issue type | `headings` is a JSON-encoded string, not a list; omits body H1: Add, edit, and delete an issue type; decoded section titles match the remaining body headings in order. |
| Audit activities in Jira applications | `headings` is a JSON-encoded string, not a list; omits body H1: Audit activities in Jira applications; decoded section titles match the remaining body headings in order. |
| Start a sprint | `headings` is a JSON-encoded string, not a list; omits body H1: Start a sprint; decoded section titles match the remaining body headings in order. |
| Add, edit, and delete resolutions | `headings` is a JSON-encoded string, not a list; omits body H1: Add, edit, and delete resolutions; decoded section titles match the remaining body headings in order. |
| Manage notifications in team-managed projects | `headings` is a JSON-encoded string, not a list; omits body H1: Manage notifications in team-managed projects; decoded section titles match the remaining body headings in order. |
| View the audit log for an automation rule | `headings` is a JSON-encoded string, not a list; omits body H1: View the audit log for an automation rule; decoded section titles match the remaining body headings in order. |
| Customize the look and feel of Jira | `headings` is a JSON-encoded string, not a list; omits body H1: Customize the look and feel of Jira; decoded section titles match the remaining body headings in order. |
| Configure quick filters on a board | `headings` is a JSON-encoded string, not a list; omits body H1: Configure quick filters on a board; decoded section titles match the remaining body headings in order. |
| Track project progress in the summary view | `headings` is a JSON-encoded string, not a list; omits body H1: Track project progress in the summary view; decoded section titles match the remaining body headings in order. |

## Pinecone and embedding configuration

- Index name: `jira-help-docs`
- Dimension: `1536`
- Metric: `cosine`
- Embedding model ID: `text-embedding-3-small`

Index properties were verified through the Pinecone index description API on 2026-10-25. The embedding model ID comes from local configuration; it is not an index property. No credentials are included.
