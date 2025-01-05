# Pull Request [descriptive helpful title name] Description

Please include a summary of the change and outline main fixes/additions. Please also include relevant motivation and context. List any dependencies that are required for this change. Lastly, please make a clear note of which branch the PR is set to merge into.

## JIRA Ticket

For implementing xyz - [PRIME-xxxx](https://jira.target.com/browse/PRIME-xxxx)

## Type of change

*Consistent with [Keep a Changelog](https://keepachangelog.com/en/1.0.0/#how) categories.* 

- [ ] `Added` components
- [ ] `Changed` components 
- [ ] `Deprecated` components
- [ ] `Removed` components
- [ ] `Migration` components
- [ ] `Fixed` bug
- [ ] `Security` resolution
  <br><br>
- [ ] **This is a breaking change!**

## Checklist

### Compatibility

- [ ] Ensure backward compatibility.
    - [ ] Include pre-release script (if necessary).
    - [ ] Communicate changes (if necessary).
    - [ ] Create Jira ticket to update other scripts (if necessary). Link to Jira ticket:
- [ ] Update start and end times of coordinator (stg/prod) if applicable.

### PLUM Communication
- [ ] If change to main or stage branch, does change need to be communicated with PLUM?

### Workflow Execution

- [ ] Run Workflow on an edge node (if necessary). Link to successful Oozie workflow run: add-link-here
- [ ] Verify the coverage report (if necessary). Explain any major changes in the Additional Notes.
- [ ] All necessary property files have been updated.

### Docs

- [ ] Add comments to appropriate headers in changelog.md.
- [ ] Update the relevant README.md (if necessary).

### Vela file
- [ ] Vela file reset for others to use.

### Releases
- [ ] Will need to tag/deploy a release on stage or main branch.
- [ ] Add Stage or Production release details in the appropriate Release log - [Releases](https://confluence.target.com/pages/viewpage.action?spaceKey=digi&title=Releases)

## Additional Notes

Anything else to add?